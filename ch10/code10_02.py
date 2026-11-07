# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제10장 파이썬의 응용
# 코드 10.2: 비정형 데이터 정리 자동화

import csv

INPUT_FILE = 'members_raw.txt'
OUTPUT_FILE = 'members.csv'

def unify_separator(line):
    """구분자 /와 ,를 |로 통일한다."""
    line = line.replace('/', '|')
    line = line.replace(',', '|')
    if '|' not in line:
        # /나 ,가 없는 경우: 공백으로 분리
        parts = line.split()
        # 재조합: 이름은 두 단어일 수 있음
        # @가 포함된 이메일을 찾아 필드 위치 파악
        for i, p in enumerate(parts):
            if '@' in p:
                email_idx = i
                break
        else:
            return None
        name = ' '.join(parts[:email_idx - 1])
        phone = parts[email_idx - 1]
        email = parts[email_idx]
        city = ' '.join(parts[email_idx + 1:])
        return f'{name}|{phone}|{email}|{city}'
    return line

def normalize_phone(phone):
    """전화번호를 010-XXXX-XXXX 형식으로 통일한다."""
    digits = ''
    for ch in phone:
        if ch.isdigit():
            digits += ch
    if len(digits) != 11:
        return None
    return f'{digits[:3]}-{digits[3:7]}-{digits[7:]}'

def clean_data(input_file, output_file):
    """원본 텍스트를 읽어 정리한 뒤 CSV로 저장한다."""
    cleaned = []
    errors = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            unified = unify_separator(line)
            if unified is None:
                errors.append((line_num, '분석할 수 없음'))
                continue

            parts = unified.split('|')
            parts = [p.strip() for p in parts]

            if len(parts) != 4:
                errors.append((line_num, '필드 개수 오류'))
                continue

            name, phone, email, city = parts
            phone = normalize_phone(phone)
            if phone is None:
                errors.append((line_num, '잘못된 전화번호'))
                continue

            cleaned.append({
                '이름': name, '전화번호': phone,
                '이메일': email, '도시': city
            })

    # CSV 파일로 저장
    fields = ['이름', '전화번호', '이메일', '도시']
    with open(output_file, 'w', newline='',
            encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(cleaned)

    print(f'완료: {len(cleaned)}건을 '
        f'{output_file}에 저장했습니다.')
    if errors:
        print(f'경고 ({len(errors)}줄 건너뜀):')
        for num, msg in errors:
            print(f'  {num}번째 줄: {msg}')

if __name__ == '__main__':
    clean_data(INPUT_FILE, OUTPUT_FILE)
