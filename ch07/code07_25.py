# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제7장 모듈 활용
# 코드 7.25: 이메일 주소 추출과 형식 검증

import re

text = 'Contact: alice@example.com, bob.smith@univ.ac.kr, not_an_email@'
emails = re.findall(r'[\w.]+@[\w.]+\.[a-zA-Z]+', text)
print(emails)

def is_valid_email(s):
    pattern = r'^[\w.]+@[\w.]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, s) is not None

print(is_valid_email('alice@example.com'))
print(is_valid_email('not_an_email@'))
