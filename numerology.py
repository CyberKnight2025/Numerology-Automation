
import datetime


def calculate_life_path_number(birthdate):
	digits = [int(digit) for digit in birthdate.replace("-", "")]
	while len(digits) > 1:
	    digits = [int(digit) for digit in str(sum(digits))]
	return digits[0]


if __name__ == "__main__":
	birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
	life_path_number = calculate_life_path_number(birthdate)
	print(f"Your Life Path Number is: {life_path_number}")
