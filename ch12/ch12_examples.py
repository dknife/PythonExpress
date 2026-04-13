"""
제12장: 데이터 과학과 파이썬
으뜸 파이썬 Express — 예제 코드
"""

# ============================================================
# 데이터 과학이란
# ============================================================

# install individually
# $ pip install numpy pandas matplotlib scikit-learn

# ============================================================
# 판다스로 데이터 다루기
# ============================================================

import pandas as pd

# Series: 1D data with index
s = pd.Series([85, 92, 78, 88],
              index=['Korean', 'English', 'Math', 'Science'])
print(s)
print(f'\nKorean score: {s["Korean"]}')
print(f'Mean: {s.mean():.1f}')

# DataFrame: 2D tabular data
data = {
    'name': ['Hong Gildong', 'Kim Cheolsu',
             'Lee Younghee', 'Park Jimin'],
    'Korean': [85, 92, 78, 95],
    'English': [90, 88, 82, 91],
    'Math': [78, 95, 88, 87]
}
df = pd.DataFrame(data)
print(df)

# save DataFrame to CSV file
df.to_csv('scores.csv', index=False, encoding='utf-8-sig')

# read CSV file into DataFrame
df2 = pd.read_csv('scores.csv')
print(df2)

print(df.head(2))       # first 2 rows
print(df.tail(2))       # last 2 rows
print(df.shape)         # (num rows, num cols)
print(df.info())        # column types and missing values
print(df.describe())    # statistical summary of numeric columns

# select columns
print(df['name'])              # single column -> Series
print(df[['name', 'Korean']])  # multiple columns -> DataFrame

# select rows
print(df.loc[0])              # row at label index 0
print(df.iloc[0:2])           # rows by position (0~1)

# conditional filtering
print(df[df['Korean'] >= 90]) # students with Korean >= 90

# ============================================================
# 데이터 정리와 가공
# ============================================================

import pandas as pd
import numpy as np

data = {
    'name': ['Hong Gildong', 'Kim Cheolsu', 'Lee Younghee',
             'Park Jimin', 'Choi Suhyun'],
    'year': [1, 2, 1, 3, 2],
    'Korean': [85, 92, np.nan, 95, 78],
    'English': [90, np.nan, 82, 91, 88],
    'Math': [78, 95, 88, np.nan, 92]
}
df = pd.DataFrame(data)
print(df)

# check missing values
print(df.isnull().sum())   # count of missing values per column

df_dropped = df.dropna()
print('dropna result:')
print(df_dropped)

# fill with 0
df_filled = df.fillna(0)
print('fillna(0) result:')
print(df_filled)

# fill with column mean (more reasonable)
df_mean = df.copy()
df_mean['Korean'] = df_mean['Korean'].fillna(
    df_mean['Korean'].mean())
df_mean['English'] = df_mean['English'].fillna(
    df_mean['English'].mean())
df_mean['Math'] = df_mean['Math'].fillna(
    df_mean['Math'].mean())
print('\nfillna(mean) result:')
print(df_mean)

# sort by Korean score in descending order
df_sorted = df.sort_values('Korean', ascending=False)
print(df_sorted)

# add new column: calculate average score
df['average'] = df[['Korean', 'English', 'Math']].mean(axis=1)
print(df[['name', 'average']])

# average Korean score by year
print(df.groupby('year')['Korean'].mean())

# average of all numeric columns by year
print(df.groupby('year')[['Korean', 'English', 'Math']].mean())

# ============================================================
# 데이터 시각화
# ============================================================

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

months = ['1월', '2월', '3월', '4월', '5월', '6월']
sales = [120, 135, 148, 162, 155, 178]

plt.figure(figsize=(7, 4))
plt.plot(months, sales, marker='o', color='\#2196F3',
         linewidth=2, label='매출')
plt.title('월별 매출 추이', fontsize=14)
plt.xlabel('월')
plt.ylabel('매출 (만 원)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# generate 200 random scores: mean 70, std 10
scores = np.random.normal(70, 10, 200)

plt.figure(figsize=(7, 4))
plt.hist(scores, bins=15, color='\#4CAF50', edgecolor='white',
         alpha=0.8)
plt.title('시험 점수 분포', fontsize=14)
plt.xlabel('점수')
plt.ylabel('학생 수')
plt.axvline(scores.mean(), color='red', linestyle='--',
            label=f'평균: {scores.mean():.1f}')
plt.legend()
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
study_hours = np.random.uniform(1, 10, 30)
scores = study_hours * 8 + np.random.normal(0, 5, 30) + 20

plt.figure(figsize=(7, 4))
plt.scatter(study_hours, scores, color='\#FF5722', alpha=0.7,
            edgecolors='black', linewidth=0.5)
plt.title('공부 시간과 성적의 관계', fontsize=14)
plt.xlabel('공부 시간')
plt.ylabel('점수')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

categories = ['식비', '교통비', '문화', '통신비', '저축']
amounts = [35, 15, 20, 10, 20]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1',
          '#96CEB4', '#FFEAA7']

plt.figure(figsize=(6, 6))
plt.pie(amounts, labels=categories, colors=colors,
        autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('월 지출 비율', fontsize=14)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame({
    'name': ['Hong', 'Kim', 'Lee', 'Park'],
    'Korean': [85, 92, 78, 95],
    'English': [90, 88, 82, 91],
    'Math': [78, 95, 88, 87]
})
df.set_index('name')[['Korean', 'English', 'Math']].plot.bar(
    figsize=(7, 4), rot=0, edgecolor='white')
plt.title('Student Scores by Subject', fontsize=14)
plt.ylabel('Score')
plt.ylim(0, 100)
plt.legend(loc='lower right')
plt.tight_layout()
plt.show()

# ============================================================
# 머신러닝 맛보기
# ============================================================

# --- scatter\_plot.py \{ ---
import numpy as np
import matplotlib.pyplot as plt

# study hours and exam scores (10 students)
hours = np.array([1, 2, 3, 3.5, 4, 5, 6, 7, 8, 9])
scores = np.array([32, 41, 52, 48, 58, 65, 73, 80, 88, 93])

plt.scatter(hours, scores, color='steelblue', s=80,
            edgecolors='navy', zorder=3)
plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.title('Study Hours vs Score')
plt.grid(True, alpha=0.3)
plt.show()

# --- linear\_regression.py \{ ---
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# data
hours = np.array([1, 2, 3, 3.5, 4, 5, 6, 7, 8, 9])
scores = np.array([32, 41, 52, 48, 58, 65, 73, 80, 88, 93])

# reshape: sklearn requires 2D array for features
X = hours.reshape(-1, 1)   # (10, 1) column vector
y = scores

# train model
model = LinearRegression()
model.fit(X, y)

# model parameters
a = model.coef_[0]         # slope
b = model.intercept_       # intercept
print(f'Regression line: y = {a:.2f}x + {b:.2f}')

# --- predict\_and\_plot.py \{ ---
# predict for new study hours
new_hours = np.array([[4.5], [6.5], [10]])
predictions = model.predict(new_hours)

print('Predictions:')
for h, s in zip(new_hours.flatten(), predictions):
    print(f'  Study {h:.1f} hours -> {s:.1f} points')

# plot: scatter + regression line
plt.figure(figsize=(8, 5))

# original data (scatter)
plt.scatter(hours, scores, color='steelblue', s=80,
            edgecolors='navy', label='Actual data', zorder=3)

# regression line
line_x = np.linspace(0, 10, 100).reshape(-1, 1)
line_y = model.predict(line_x)
plt.plot(line_x, line_y, color='red', linewidth=2,
         label=f'Fit line: y={a:.2f}x+{b:.2f}')

# predicted points
plt.scatter(new_hours, predictions, color='red', s=120,
            marker='*', zorder=4, label='Predicted')

plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.title('Linear Regression: Study Hours vs Score')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 11)
plt.ylim(20, 105)
plt.show()

r2 = model.score(X, y)
print(f'R-squared: {r2:.4f}')
