import re
def verify(username):
    rollregex = re.compile(r'1901220(\d{2})(\d+)')
    x = rollregex.findall(username)
    return x[0]