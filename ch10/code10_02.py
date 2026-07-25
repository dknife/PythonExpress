# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제10장 파이썬의 응용
# 코드 10.2: 비정형 데이터 정리 자동화

import csv

INPUT_FILE = 'members_raw.txt'
OUTPUT_FILE = 'members.csv'

def unify_separator(line):
    """Replace / and, with | as a single separator."""
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
    """Normalize phone number to 010-XXXX-XXXX format."""
    digits = ''
    for ch in phone:
        if ch.isdigit():
            digits += ch
    if len(digits) != 11:
        return None
    return f'{digits[:3]}-{digits[3:7]}-{digits[7:]}'

def clean_data(input_file, output_file):
    """Read raw text, clean it, and write to CSV."""
    cleaned = []
    errors = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            unified = unify_separator(line)
            if unified is None:
                errors.append((line_num, 'Cannot parse'))
                continue

            parts = unified.split('|')
            parts = [p.strip() for p in parts]

            if len(parts) != 4:
                errors.append((line_num, 'Field count error'))
                continue

            name, phone, email, city = parts
            phone = normalize_phone(phone)
            if phone is None:
                errors.append((line_num, 'Invalid phone'))
                continue

            cleaned.append({
                'name': name, 'phone': phone,
                'email': email, 'city': city
            })

    # CSV 파일로 저장
    fields = ['name', 'phone', 'email', 'city']
    with open(output_file, 'w', newline='',
            encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(cleaned)

    print(f'Completed: {len(cleaned)} records saved '
        f'to {output_file}')
    if errors:
        print(f'Warnings ({len(errors)} lines skipped):')
        for num, msg in errors:
            print(f'  Line {num}: {msg}')

if __name__ == '__main__':
    clean_data(INPUT_FILE, OUTPUT_FILE)
