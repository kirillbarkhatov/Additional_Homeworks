import re

psw_1 = "ff9022BB"
psw_2 = "test1"
psw_3 = "QWERTYasdf"



# pattern = re.compile(r'([a-zA-Z0-9]){8,}')
# pattern_d = re.compile(r'')


def check(psw):
    pattern = re.compile(r'([a-zA-Z0-9]){8,}')
    if pattern.match(psw) is None:
        print(f'{psw} не соответствует сложности')
        return False

    psw_check_dig = False
    psw_check_let = False
    psw_check_big_let = False

    for i in pattern.match(psw).group():
        if re.match(re.compile(r'[a-z]'), i) is not None:
            psw_check_let = True
        if re.match(re.compile(r'[A-Z]'), i) is not None:
            psw_check_big_let = True
        if re.match(re.compile(r'[0-9]'), i) is not None:
            psw_check_dig = True
    if psw_check_dig & psw_check_let & psw_check_big_let:
        return print(f'{psw} соответствует сложности')
    else:
        print(f'{psw} не соответствует сложности')

check(psw_1)
check(psw_2)
check(psw_3)


ptr = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}'

print(re.match(ptr, psw_1))
print(re.match(ptr, psw_2))
print(re.match(ptr, psw_3))

