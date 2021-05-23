import re
def verify(username):
    rollregex = re.compile(r'1901220(\d{2})(\d+)')
    if username.startswith('1901220'):
        rollregex = re.compile(r'1901220(\d{2})(\d+)')
    elif username.startswith('2001220'):
        rollregex = re.compile(r'2001220(\d{2})9(\d+)')
    x = rollregex.findall(username)
    return x[0]