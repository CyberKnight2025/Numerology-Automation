from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def home():
	return "Welcome to the Numerology Backend!"

# Sample numerology calculation endpoint
@app.route('/calculate', methods=['POST'])
def calculate_numerology():
	data = request.json
	name = data.get("name", "")
	birthdate = data.get("birthdate", "")
	result = f"Numerology report for {name}, born on {birthdate}"
	return jsonify({"report": result})

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)
