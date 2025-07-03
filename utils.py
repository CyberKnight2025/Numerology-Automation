import hashlib
from datetime import datetime

def calculate_life_path_number(birthdate):
    digits = [int(ch) for ch in birthdate if ch.isdigit()]
    total = sum(digits)
    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(d) for d in str(total))
    return total

def calculate_expression_number(name):
    name = name.upper()
    letter_values = {ch: i+1 for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    total = sum(letter_values.get(ch, 0) for ch in name)
    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(d) for d in str(total))
    return total

def calculate_soul_urge_number(name):
    vowels = "AEIOU"
    name = name.upper()
    letter_values = {ch: i+1 for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    total = sum(letter_values.get(ch, 0) for ch in name if ch in vowels)
    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(d) for d in str(total))
    return total

def calculate_personality_number(name):
    vowels = "AEIOU"
    name = name.upper()
    letter_values = {ch: i+1 for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    total = sum(letter_values.get(ch, 0) for ch in name if ch not in vowels and ch.isalpha())
    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(d) for d in str(total))
    return total

def calculate_destiny_number(name):
    return calculate_expression_number(name)

def generate_fingerprint(name, birthdate, *args):
    fingerprint_input = f"{name}-{birthdate}-{'-'.join(str(a) for a in args)}"
    return hashlib.sha256(fingerprint_input.encode('utf-8')).hexdigest()

def calculate_pinnacles(birthdate):
    month, day, year = map(int, birthdate.split('-'))
    def reduce(n): 
        while n > 9 and n not in [11, 22, 33]: 
            n = sum(int(x) for x in str(n))
        return n
    lp = calculate_life_path_number(birthdate)
    pinnacle_1 = reduce(month + day)
    pinnacle_2 = reduce(day + year)
    pinnacle_3 = reduce(pinnacle_1 + pinnacle_2)
    pinnacle_4 = reduce(month + year)
    return pinnacle_1, pinnacle_2, pinnacle_3, pinnacle_4

def calculate_personal_cycles(birthdate):
    now = datetime.now()
    birth_month, birth_day = map(int, birthdate.split('-')[1:])
    year_digits = [int(d) for d in str(now.year)]
    personal_year = sum(year_digits) + int(birth_month) + int(birth_day)
    while personal_year > 9 and personal_year not in [11, 22, 33]:
        personal_year = sum(int(d) for d in str(personal_year))
    personal_month = (personal_year + now.month) % 9 or 9
    personal_day = (personal_month + now.day) % 9 or 9
    return personal_year, personal_month, personal_day
