import random   # 이 줄을 맨 위에 추가!

# 현실적으로 가장 많이 사용되는 패턴
# 매개변수가 많을때
# 첫번째나 두번째 혹은 많은 3번째 까지는 positional
# 나머지는 전부 default parameter

# 학생들의 정보는 리스트로 받고 옵션을 줘서 다양하게 값을 리턴
import random

def students_info(scores, max_val=None, min_val=None, avg=False):
    if max_val is True:
        return max(scores)
    elif min_val is True:
        return min(scores)
    elif avg is True:
        return sum(scores) / len(scores)
    else:
        return scores


# 함수 전달하는 매개변수가 가변적일대
# temp(1)
# temp[(1,2)
# temp([1,2,3])

def temp(params):
    for i in params:
        pass # 적절한 로직

    parmas = [10]
    temp( [1,2,4])

    #가변 매개변수
    def temp(params): #packing
        print(type(params)) # tuple
        for i in params:
            print(i)

            temp(1,2,4)

    v1,v2 = (100,10)
    print(f'v1 : {vl}')

    def Test(*args,name):
        pass
    Test(1.2,3)
    test(1,2,3,name='홍길동')

    #positional, defualt, 가변
    #def test(*args,data): test(1,2,3,4) X
    #def test(data,*args): test(1,2,3,4) O
    




git config --global user.name "jdmswn-cyber"
git config --global user.email jdmswn@gmail.com"

ㅊㅊㅇ