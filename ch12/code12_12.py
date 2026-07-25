# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.12: 월별 매출 추이를 선 그래프로

import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [120, 135, 148, 162, 155, 178]

plt.figure(figsize=(7, 4))
plt.plot(months, sales, marker='o', color='#2196F3',
    linewidth=2, label='Sales')
plt.title('Monthly Sales Trend', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Sales (10K KRW)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
