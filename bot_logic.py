import random

def gen_pass(pass_length):
    elements = "1234567890QqWwEeRrTtYyUuIiOoPp{[}]AaSsDdFfGgHhJjKk:;ZzXxCcVvBbNnMm+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_nick(pass_length):
    elements = "QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"
    nick = ""
    for i in range(pass_length):
        nick += random.choice(elements)
    return nick
