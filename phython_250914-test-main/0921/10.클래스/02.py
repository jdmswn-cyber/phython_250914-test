class teacher:
    def __init__(self): # 생성자
        print('생성자')

    pass
#객체 생성
print('객체 생성전')
t = teacher() # 객체를 생성할때는 반드시 내부의 생성자가 호출 __init_(self)가 호출
t2 = teacher('이순신')
print('객체 생성후')
print(type(t))

t.age = 10
print(t.age)
print(t2.age)
