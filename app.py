import os
import psycopg2
import hashlib
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from utils import (
    calculate_life_path_number,
    calculate_expression_number,
    calculate_soul_urge_number,
    calculate_personality_number,
    calculate_destiny_number,
    generate_fingerprint,
    calculate_pinnacles,
    calculate_personal_cycles,
)

load_dotenv()

# Load from environment
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

app = Flask(__name__)

def get_or_create_location(cursor, country, state, city):
    cursor.execute("SELECT id FROM countries WHERE name = %s", (country,))
    country_row = cursor.fetchone()
    if country_row:
        country_id = country_row[0]
    else:
        cursor.execute("INSERT INTO countries (name) VALUES (%s) RETURNING id", (country,))
        country_id = cursor.fetchone()[0]

    cursor.execute("SELECT id FROM states WHERE name = %s AND country_id = %s", (state, country_id))
    state_row = cursor.fetchone()
    if state_row:
        state_id = state_row[0]
    else:
        cursor.execute("INSERT INTO states (name, country_id) VALUES (%s, %s) RETURNING id", (state, country_id))
        state_id = cursor.fetchone()[0]

    cursor.execute("SELECT id FROM cities WHERE name = %s AND state_id = %s", (city, state_id))
    city_row = cursor.fetchone()
    if city_row:
        city_id = city_row[0]
    else:
        cursor.execute("INSERT INTO cities (name, state_id) VALUES (%s, %s) RETURNING id", (city, state_id))
        city_id = cursor.fetchone()[0]

    return country_id, state_id, city_id

@app.route('/')
def home():
    return jsonify({"message": "Flask backend is running!"})

@app.route('/reports', methods=['POST'])
def create_report():
    try:
        data = request.get_json()
        name = data.get("name", "")
        birthdate = data.get("birthdate", "")
        country = data.get("country", "")
        state = data.get("state", "")
        city = data.get("city", "")

        if not all([name, birthdate, country, state, city]):
            return jsonify({"error": "Name, birthdate, and full location (country/state/city) are required"}), 400

        life_path = calculate_life_path_number(birthdate)
        expression = calculate_expression_number(name)
        soul_urge = calculate_soul_urge_number(name)
        personality = calculate_personality_number(name)
        destiny = calculate_destiny_number(name)
        fingerprint = generate_fingerprint(name, birthdate, life_path, expression, soul_urge, personality, destiny)
        pinnacle_1, pinnacle_2, pinnacle_3, pinnacle_4 = calculate_pinnacles(birthdate)
        personal_year, personal_month, personal_day = calculate_personal_cycles(birthdate)

        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()

        # Prevent duplicates
        cursor.execute("SELECT id FROM reports WHERE fingerprint = %s", (fingerprint,))
        if cursor.fetchone():
            return jsonify({"error": "Duplicate report already exists."}), 409

        # Insert location and get location IDs
        country_id, state_id, city_id = get_or_create_location(cursor, country, state, city)

        # Insert into reports
        cursor.execute("""
            INSERT INTO reports (
                name, birthdate, life_path, expression_number, soul_urge,
                personality, destiny_number, fingerprint,
                pinnacle_1, pinnacle_2, pinnacle_3, pinnacle_4,
                personal_year, personal_month, personal_day,
                country_id, state_id, city_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            name, birthdate, life_path, expression, soul_urge, personality, destiny, fingerprint,
            pinnacle_1, pinnacle_2, pinnacle_3, pinnacle_4,
            personal_year, personal_month, personal_day,
            country_id, state_id, city_id
        ))

        conn.commit()
        return jsonify({"report": {
            "name": name,
            "birthdate": birthdate,
            "location": {"country": country, "state": state, "city": city},
            "life_path": life_path,
            "expression_number": expression,
            "soul_urge": soul_urge,
            "personality": personality,
            "destiny_number": destiny,
            "pinnacle_1": pinnacle_1,
            "pinnacle_2": pinnacle_2,
            "pinnacle_3": pinnacle_3,
            "pinnacle_4": pinnacle_4,
            "personal_year": personal_year,
            "personal_month": personal_month,
            "personal_day": personal_day
        }}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

@app.route('/reports', methods=['GET'])
def get_reports():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute("""
            SELECT r.id, r.name, r.birthdate, r.life_path, r.expression_number, r.soul_urge,
                r.personality, r.destiny_number, r.created_at,
                r.pinnacle_1, r.pinnacle_2, r.pinnacle_3, r.pinnacle_4,
                r.personal_year, r.personal_month, r.personal_day,
                c.name AS country, s.name AS state, ci.name AS city
            FROM reports r
            LEFT JOIN countries c ON r.country_id = c.id
            LEFT JOIN states s ON r.state_id = s.id
            LEFT JOIN cities ci ON r.city_id = ci.id
        """)
        rows = cursor.fetchall()
        reports = []
        for row in rows:
            reports.append({
                "id": row[0],
                "name": row[1],
                "birthdate": str(row[2]),
                "life_path": row[3],
                "expression_number": row[4],
                "soul_urge": row[5],
                "personality": row[6],
                "destiny_number": row[7],
                "created_at": str(row[8]),
                "pinnacle_1": row[9],
                "pinnacle_2": row[10],
                "pinnacle_3": row[11],
                "pinnacle_4": row[12],
                "personal_year": row[13],
                "personal_month": row[14],
                "personal_day": row[15],
                "country": row[16],
                "state": row[17],
                "city": row[18]
            })
        return jsonify({"reports": reports})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

