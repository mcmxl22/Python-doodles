import datetime
import time
import random
import string


DATE = datetime.datetime.now()
DAY = DATE.day

def set_expiration():
    expires = f"{DAY + 1}"
    return expires


def set_letter_code():
    letters = string.ascii_uppercase
    code_1 = random.choice(letters)
    code_2 = random.choice(letters)
    day_code = f"{code_1}{code_2}"
    return day_code


def write_code():
    tomorrow = set_expiration()
    today = DAY

    with open("code.txt", "r+") as file:
        code = "".join(file.readlines())
        file_code = file.write(set_letter_code())

        if not code:
            file_code
        else:
            return code

        if today in tomorrow:
            with open("code.txt", "w") as file:
                file_code
        else:
            return code


print(set_letter_code())
print(set_expiration())
