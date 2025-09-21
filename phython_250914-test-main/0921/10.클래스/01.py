class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def __str__(self):
        return f'이름: {self.name}, 나이: {self.age}, 점수: {self.scores}'

    def get_total(self):
        return sum(self.scores)

    def get_avg(self):
        return self.get_total() / len(self.scores)

if __name__ == '__main__':
    # 테스트 코드
    s1 = Student('홍길동', 20, [95, 98, 88])
    s2 = Student('이순신', 30, [100, 98, 98])

    # 기본 정보 출력
    print(s1)
    print(s2)
    
    # 총점과 평균 출력
    print(f'{s1.name}의 총점: {s1.get_total()}, 평균: {s1.get_avg():.2f}')
    print(f'{s2.name}의 총점: {s2.get_total()}, 평균: {s2.get_avg():.2f}')

    print(students[0],name)
    students[0],name = '강감찬'

    for s in studebts:
        print(s)
        