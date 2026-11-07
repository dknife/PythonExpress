# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.10: raise로 입력값 검증하기

def get_ans(ans):
    if ans in ['예', '아니오']:
        print('정상적인 입력입니다.')
    else:
        raise ValueError('예/아니오를 입력하세요.')

while True:
    try:
        ans = input('예 또는 아니오를 입력하세요: ')
        get_ans(ans)
        break
    except Exception as e:
        print('오류:', e)
