# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제7장 모듈 활용
# 코드 7.24: search, findall, sub로 전화번호 처리

import re

text = 'My phone is 010-1234-5678 and home is 02-555-7777.'

m = re.search(r'\d{2,3}-\d{3,4}-\d{4}', text)
print(m.group()) # 처음 일치한 부분 문자열

nums = re.findall(r'\d{2,3}-\d{3,4}-\d{4}', text)
print(nums) # 일치한 모든 부분의 리스트

cleaned = re.sub(r'\d', '*', text) # 모든 숫자를 *로 치환
print(cleaned)
