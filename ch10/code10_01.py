# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제10장 파이썬의 응용
# 코드 10.1: 단어장 앱 전체 코드  —  WordApp 클래스

import json
import random
from pathlib import Path


class WordApp:
    """간단한 단어장 앱."""

    def __init__(self, filename='my_words.json'):
        self.filename = Path(filename)
        self.words = {}
        self.load()

    def load(self):
        """파일에서 단어장을 읽어 self.words에 저장한다."""
        if self.filename.exists():
            with self.filename.open('r', encoding='utf-8') as f:
                self.words = json.load(f)
        else:
            self.words = {}

    def save(self):
        """self.words를 파일에 저장한다."""
        with self.filename.open('w', encoding='utf-8') as f:
            json.dump(self.words, f, ensure_ascii=False, indent=2)

    def add(self):
        """새 단어를 추가한다."""
        eng = input('영어 단어를 입력하세요: ').strip().lower()
        if eng in self.words:
            print(f' 이미 등록된 단어입니다: "{eng}"')
            return
        meaning = input('뜻을 입력하세요: ').strip()
        self.words[eng] = meaning
        print(f' 추가했습니다: "{eng}: {meaning}"')

    def show(self):
        """모든 단어를 출력한다."""
        if not self.words:
            print(' 등록된 단어가 없습니다.')
            return
        print(f' --- 단어 {len(self.words)}개 ---')
        for eng, meaning in self.words.items():
            print(f' {eng:20s} : {meaning}')

    def search(self):
        """단어를 검색한다."""
        eng = input('검색할 단어를 입력하세요: ').strip().lower()
        if eng in self.words:
            print(f' {eng} : {self.words[eng]}')
        else:
            print(f' 찾을 수 없는 단어입니다: "{eng}"')

    def quiz(self):
        """퀴즈 모드: 무작위로 최대 5문제를 출제한다."""
        if len(self.words) < 2:
            print(' 퀴즈를 내려면 단어가 2개 이상 필요합니다.')
            return
        items = list(self.words.items())
        random.shuffle(items)
        count = min(5, len(items))
        score = 0
        print(f'\n === 퀴즈 시작 ({count}문제) ===')
        for i, (eng, meaning) in enumerate(items[:count], 1):
            answer = input(f' Q{i}. "{eng}"의 뜻을 입력하세요: ')
            if answer.strip() == meaning:
                print(' 정답입니다!')
                score += 1
            else:
                print(f' 틀렸습니다! 정답은 "{meaning}"입니다.')
        print(f'\n 결과: {count}문제 중 {score}문제 정답')

    def run(self):
        """메인 메뉴 루프."""
        print('=== 나만의 단어장 앱 ===')
        while True:
            print('\n1.추가 2.목록 3.검색 4.퀴즈 5.저장 6.종료')
            choice = input('메뉴 번호를 입력하세요: ').strip()
            if choice == '1':
                self.add()
            elif choice == '2':
                self.show()
            elif choice == '3':
                self.search()
            elif choice == '4':
                self.quiz()
            elif choice == '5':
                self.save()
                print(' 저장했습니다!')
            elif choice == '6':
                self.save()
                print(' 단어장을 저장했습니다. 안녕히 가세요!')
                break
            else:
                print(' 잘못된 입력입니다.')


if __name__ == '__main__':
    app = WordApp()
    app.run()
