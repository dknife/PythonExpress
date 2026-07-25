# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제10장 파이썬의 응용
# 코드 10.1: 단어장 앱 전체 코드  —  WordApp 클래스

import json
import random
from pathlib import Path


class WordApp:
    """A simple vocabulary application."""

    def __init__(self, filename='my_words.json'):
        self.filename = Path(filename)
        self.words = {}
        self.load()

    def load(self):
        """Load vocabulary from file into self.words."""
        if self.filename.exists():
            with self.filename.open('r', encoding='utf-8') as f:
                self.words = json.load(f)
        else:
            self.words = {}

    def save(self):
        """Save self.words to the file."""
        with self.filename.open('w', encoding='utf-8') as f:
            json.dump(self.words, f, ensure_ascii=False, indent=2)

    def add(self):
        """Add a new word."""
        eng = input('English word : ').strip().lower()
        if eng in self.words:
            print(f' "{eng}" is already registered.')
            return
        meaning = input('Meaning : ').strip()
        self.words[eng] = meaning
        print(f' "{eng}: {meaning}" added!')

    def show(self):
        """Display all words."""
        if not self.words:
            print(' No words registered.')
            return
        print(f' --- Total {len(self.words)} words ---')
        for eng, meaning in self.words.items():
            print(f' {eng:20s} : {meaning}')

    def search(self):
        """Search for a word."""
        eng = input('Word to search : ').strip().lower()
        if eng in self.words:
            print(f' {eng} : {self.words[eng]}')
        else:
            print(f' "{eng}" not found.')

    def quiz(self):
        """Quiz mode: randomly ask up to 5 questions."""
        if len(self.words) < 2:
            print(' Need at least 2 words for a quiz.')
            return
        items = list(self.words.items())
        random.shuffle(items)
        count = min(5, len(items))
        score = 0
        print(f'\n === Quiz Start ({count} questions) ===')
        for i, (eng, meaning) in enumerate(items[:count], 1):
            answer = input(f' Q{i}. What does "{eng}" mean? ')
            if answer.strip() == meaning:
                print(' Correct!')
                score += 1
            else:
                print(f' Wrong! The answer is "{meaning}".')
        print(f'\n Result: {score} out of {count} correct')

    def run(self):
        """Main menu loop."""
        print('=== My Vocabulary App ===')
        while True:
            print('\n1.Add 2.List 3.Search 4.Quiz 5.Save 6.Quit')
            choice = input('Choice : ').strip()
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
                print(' Saved!')
            elif choice == '6':
                self.save()
                print(' Vocabulary saved. Goodbye!')
                break
            else:
                print(' Invalid input.')


if __name__ == '__main__':
    app = WordApp()
    app.run()
