import re

five_digit_zip = '98101'
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'

five_digit_pattern = r'\d{5}'

print(re.search(five_digit_pattern, five_digit_zip))
print(re.search(five_digit_pattern, nine_digit_zip))
print(re.search(five_digit_pattern, phone_number))