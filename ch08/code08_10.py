# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.10: raise로 입력값 검증하기

def get_ans(ans):
    if ans in ['yes', 'no']:
        print('Valid input.')
    else:
        raise ValueError('Please enter yes or no.')

while True:
    try:
        ans = input('Enter yes or no: ')
        get_ans(ans)
        break
    except Exception as e:
        print('error:', e)
