class customer:
    def__init__(self, name, email,age =18):
    self.name = name
    self.email = email
    self.age = age
    self.loyalty_points = 0
#인스턴스 생성
customer1 = customer('홍길동', 'hong@gmail.com',25)
customer2 = customer('이순신', 'lee@gmail.com')
#속성에 접근해서 출력
print(customer1.name, customer1.email, customer1.loyalty_point))
print(customer2.name, customer2.email, customer2.age)

