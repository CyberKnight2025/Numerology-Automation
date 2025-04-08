def reduce_to_single_digit(num):
    while num > 9 and num not in [11, 22, 33]:
        num = sum(int(digit) for digit in str(num))
    return num

def calculate_life_path(birth_date):
    digits = [int(char) for char in birth_date if char.isdigit()]
    return reduce_to_single)digit(sum(digits))

@app.route('/calculate', methods=['POST'])
def calculate_numerology():
    data = request.json
    name = data.get("name", "")

    if not birthdate:
        return jsonify({"error": "Birthdate is required"}), 400

    life_path_number = calculate_life_path(birthdate)
    report = f"Numerology report for {name}, born on {birthdate}: Your Life Path Number is {life_path_number}"

    return jsonify({"report": report})
