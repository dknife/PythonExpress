"""
제12장: 데이터 과학과 파이썬
알짜 파이썬 — 예제 코드 (원고에서 자동 추출)
"""

# ============================================================
# 판다스로 데이터 다루기
# ============================================================

import pandas as pd

# Series: 인덱스가 있는 1차원 데이터
s = pd.Series([85, 92, 78, 88],
    index=['Korean', 'English', 'Math', 'Science'])
print(s)
print(f'\nKorean score: {s["Korean"]}')
print(f'Mean: {s.mean():.1f}')

# DataFrame: 2차원 표 형태 데이터
data = {
    'name': ['Hong Gildong', 'Kim Cheolsu',
             'Lee Younghee', 'Park Jimin'],
    'Korean': [85, 92, 78, 95],
    'English': [90, 88, 82, 91],
    'Math': [78, 95, 88, 87]
}
df = pd.DataFrame(data)
print(df)

# --- CSV 파일 읽기와 쓰기 ---
# DataFrame을 CSV 파일로 저장
df.to_csv('scores.csv', index=False, encoding='utf-8-sig')

# CSV 파일을 읽어 DataFrame 생성
df2 = pd.read_csv('scores.csv')
print(df2)

print(df.head(2)) # 처음 2행
print(df.tail(2)) # 마지막 2행
print(df.shape) # (행 수, 열 수)
print(df.info()) # 열의 타입과 결측값 정보
print(df.describe()) # 수치형 열의 통계 요약

# 열 선택
print(df['name']) # 열 하나 -> Series
print(df[['name', 'Korean']]) # 열 여러 개 -> DataFrame

# 행 선택
print(df.loc[0]) # 레이블 인덱스 0의 행
print(df.iloc[0:2]) # 위치 기반 행 선택 (0~1)

# 조건 필터링
print(df[df['Korean'] >= 90]) # 국어 점수 90 이상인 학생

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

# 결측값 확인
print(df.isnull().sum()) # 열별 결측값 개수

df_dropped = df.dropna()
print('dropna result:')
print(df_dropped)

# 0으로 채우기
df_filled = df.fillna(0)
print('fillna(0) result:')
print(df_filled)

# 열 평균으로 채우기 (더 합리적)
df_mean = df.copy()
df_mean['Korean'] = df_mean['Korean'].fillna(
    df_mean['Korean'].mean())
df_mean['English'] = df_mean['English'].fillna(
    df_mean['English'].mean())
df_mean['Math'] = df_mean['Math'].fillna(
    df_mean['Math'].mean())
print('\nfillna(mean) result:')
print(df_mean)

# 국어 점수 기준 내림차순 정렬
df_sorted = df.sort_values('Korean', ascending=False)
print(df_sorted)

# 새 열 추가: 평균 점수 계산
df['average'] = df[['Korean', 'English', 'Math']].mean(axis=1)
print(df[['name', 'average']])

# 학년별 국어 점수 평균
print(df.groupby('year')['Korean'].mean())

# 학년별 모든 수치형 열의 평균
print(df.groupby('year')[['Korean', 'English', 'Math']].mean())

# ============================================================
# 데이터 시각화
# ============================================================

# --- 월별 매출 추이를 선 그래프로 ---
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [120, 135, 148, 162, 155, 178]

plt.figure(figsize=(7, 4))
plt.plot(months, sales, marker='o', color='\#2196F3',
    linewidth=2, label='Sales')
plt.title('Monthly Sales Trend', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Sales (10K KRW)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# --- 시험 점수 분포 히스토그램 ---
import numpy as np
import matplotlib.pyplot as plt

# 평균 70, 표준편차 10인 난수 점수 200개 생성
scores = np.random.normal(70, 10, 200)

plt.figure(figsize=(7, 4))
plt.hist(scores, bins=15, color='\#4CAF50', edgecolor='white',
    alpha=0.8)
plt.title('Exam Score Distribution', fontsize=14)
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.axvline(scores.mean(), color='red', linestyle='--',
    label=f'Mean: {scores.mean():.1f}')
plt.legend()
plt.tight_layout()
plt.show()

# --- 공부 시간과 점수의 산점도 ---
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
study_hours = np.random.uniform(1, 10, 30)
scores = study_hours * 8 + np.random.normal(0, 5, 30) + 20

plt.figure(figsize=(7, 4))
plt.scatter(study_hours, scores, color='\#FF5722', alpha=0.7,
    edgecolors='black', linewidth=0.5)
plt.title('Study Hours and Score Relation', fontsize=14)
plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# --- 지출 비율을 원형 그래프로 ---
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

# --- DataFrame에서 직접 막대 그래프 그리기 ---
import pandas as pd
import matplotlib.pyplot as plt

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

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 코드 12.14에서 사용한 데이터
np.random.seed(42)
study_hours = np.random.uniform(1, 10, 30)
scores = study_hours * 8 + np.random.normal(0, 5, 30) + 20

# reshape: 사이킷런의 특성 데이터는 2차원 배열이어야 함
X = study_hours.reshape(-1, 1) # (30, 1) 열 벡터
y = scores

# 모델 학습
model = LinearRegression()
model.fit(X, y)

# 모델 파라미터
a = model.coef_[0] # 기울기
b = model.intercept_ # 절편
print(f'Regression line: y = {a:.2f}x + {b:.2f}')

# 새로운 공부 시간에 대한 점수 예측
new_hours = np.array([[4.5], [6.5], [10]])
predictions = model.predict(new_hours)

print('Predictions:')
for h, s in zip(new_hours.flatten(), predictions):
    print(f' Study {h:.1f} hours -> {s:.1f} points')

# 그래프: 산점도 + 회귀선
plt.figure(figsize=(8, 5))

# 원본 데이터 (산점도)
plt.scatter(study_hours, scores, color='steelblue', s=80,
    edgecolors='navy', label='Actual data', zorder=3)

# 회귀선
line_x = np.linspace(0, 10, 100).reshape(-1, 1)
line_y = model.predict(line_x)
plt.plot(line_x, line_y, color='red', linewidth=2,
    label=f'Fit line: y={a:.2f}x+{b:.2f}')

# 예측된 점
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

# ============================================================
# 실습을 통한 12장 개념 정리
# ============================================================

import pandas as pd

data = {
    'name': ['Hong', 'Kim', 'Lee', 'Park', 'Choi'],
    'kor' : [85, 90, 78, 92, 88],
    'eng' : [80, 95, 82, 70, 88],
    'math': [90, 85, 88, 95, 92],
}
df = pd.DataFrame(data)
print(df.head())
print(df.describe())

df['total'] = df['kor'] + df['eng'] + df['math']
df['avg']   = df['total'] / 3
print(df.sort_values('avg', ascending=False))

import matplotlib.pyplot as plt

x = list(range(10))
y = [v * v for v in x]

plt.plot(x, y, marker='o')
plt.title('y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

plt.scatter(df['kor'], df['eng'])
for i, name in enumerate(df['name']):
    plt.annotate(name, (df['kor'][i] + 0.5, df['eng'][i] + 0.5))
plt.xlabel('Korean'); plt.ylabel('English')
plt.title('Korean vs English scores')
plt.grid(True)
plt.show()

import numpy as np
from sklearn.linear_model import LinearRegression

hours  = np.array([1, 2, 3, 4, 6, 7, 8]).reshape(-1, 1)
scores = np.array([52, 58, 65, 70, 82, 87, 92])

model = LinearRegression().fit(hours, scores)
print(f'Slope     : {model.coef_[0]:.2f}')
print(f'Intercept : {model.intercept_:.2f}')

pred = model.predict([[5]])
print(f'5 hours -> {pred[0]:.1f} points')

from sklearn.metrics import classification_report

y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1]

print(classification_report(y_true, y_pred, 
                                        target_names=['Negative', 'Positive']))
