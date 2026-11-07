# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.9: 학생 정보를 관리하는 Student 클래스

class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

    def info(self):
        avg = self.average()
        print(f'{self.name}({self.student_id}) - {self.major}, 평균: {avg:.1f}')

# 학생 객체를 생성하고 사용
s1 = Student('홍길동', '2026001', '컴퓨터공학')
s1.add_score(85)
s1.add_score(92)
s1.add_score(78)
s1.info() # 홍길동(2026001) - 컴퓨터공학, 평균: 85.0

s2 = Student('김영희', '2026002', '경영학')
s2.add_score(95)
s2.add_score(88)
s2.info() # 김영희(2026002) - 경영학, 평균: 91.5
