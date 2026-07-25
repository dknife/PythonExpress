# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.15: 지출 비율을 원형 그래프로

import matplotlib.pyplot as plt

categories = ['Food', 'Transport', 'Culture', 'Phone', 'Savings']
amounts = [35, 15, 20, 10, 20]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1',
    '#96CEB4', '#FFEAA7']

plt.figure(figsize=(6, 6))
plt.pie(amounts, labels=categories, colors=colors,
    autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Monthly Expense Ratio', fontsize=14)
plt.show()
