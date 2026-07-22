"""
제1장: 파이썬 소개와 개발 환경
알짜 파이썬 — 예제 코드 (원고에서 자동 추출)
"""

# ============================================================
# 파이썬 설치와 개발 환경
# ============================================================

print('Hello Python')

from google.colab import drive
drive.mount('/content/drive')

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread('./drive/MyDrive/myData.png')
plt.imshow(img)

# ============================================================
# 첫 번째 파이썬 프로그램
# ============================================================

print('Hello World!')

print("Hello World!")

print('Hello World!")

10 + 20
3 * 5
100 / 4
2 ** 10

# --- 첫 번째 파이썬 스크립트 ---
# 첫 번째 파이썬 프로그램
print('Hello Python!')
print('Let us start programming!')

# ============================================================
# 실습을 통한 1장 개념 정리
# ============================================================

print('Name:', 'Hong Gildong')
print('Age:', 20)
print('Hobby:', 'Reading')

  print('Hello')

print(type(10))
print(type(3.14))
print(type('hello'))

print('=' * 40)
print('Welcome to Python programming!')
print('Start your coding journey today.')
print('Every expert was once a beginner.')
print('=' * 40)
