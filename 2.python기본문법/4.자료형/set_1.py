# set(집합)의 기본 사용법과 예제
# 특징:
# 1. 중복을 허용하지 않는다
# 2. 순서를 보장하지 않는다
# 3. 집합연산 가능 (교집합, 합집합, 차집합)
# 4. 서로 다른 자료형끼리 전환이 가능하다 (리스트 <--> 튜플)

def print_section(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

# 1. 중복 허용하지 않음 예제
print_section("1. 중복 제거 특성")
numbers = {1, 2, 2, 3, 3, 4, 5, 5}
print(f"중복된 값을 포함해 생성: {numbers}")
print("→ 자동으로 중복이 제거됨")

# 2. 순서를 보장하지 않음
print_section("2. 순서 미보장 특성")
fruits = {'apple', 'banana', 'cherry', 'date'}
print(f"초기 set: {fruits}")
print("→ 출력할 때마다 순서가 달라질 수 있음")

# 3. 집합 연산
print_section("3. 집합 연산")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"A = {A}")
print(f"B = {B}")

# 교집합
intersection = A & B  # A.intersection(B)도 가능
print(f"교집합 (A & B): {intersection}")

# 합집합
union = A | B  # A.union(B)도 가능
print(f"합집합 (A | B): {union}")

# 차집합
difference = A - B  # A.difference(B)도 가능
print(f"차집합 (A - B): {difference}")

# 대칭차집합 (합집합 - 교집합)
symmetric_difference = A ^ B  # A.symmetric_difference(B)도 가능
print(f"대칭차집합 (A ^ B): {symmetric_difference}")

# 4. 자료형 변환
print_section("4. 자료형 변환")

# 리스트를 집합으로 변환
my_list = [1, 2, 2, 3, 3, 4]
set_from_list = set(my_list)
print(f"리스트: {my_list}")
print(f"리스트에서 변환된 집합: {set_from_list}")

# 튜플을 집합으로 변환
my_tuple = (1, 2, 2, 3, 3, 4)
set_from_tuple = set(my_tuple)
print(f"튜플: {my_tuple}")
print(f"튜플에서 변환된 집합: {set_from_tuple}")

# 집합을 리스트로 변환
list_from_set = list(set_from_tuple)
print(f"집합을 리스트로 변환: {list_from_set}")

# 집합을 튜플로 변환
tuple_from_set = tuple(set_from_tuple)
print(f"집합을 튜플로 변환: {tuple_from_set}")

# 추가 유용한 메서드들
print_section("5. 유용한 메서드들")

# add(): 요소 추가
fruits = {'apple', 'banana'}
fruits.add('cherry')
print(f"add() 후: {fruits}")

# remove(): 요소 제거 (없으면 에러)
fruits.remove('banana')
print(f"remove('banana') 후: {fruits}")

# discard(): 요소 제거 (없어도 에러 없음)
fruits.discard('not_exists')
print(f"discard('not_exists') 후: {fruits}")

# pop(): 임의의 요소 제거 및 반환
popped = fruits.pop()
print(f"pop()으로 제거된 요소: {popped}")
print(f"pop() 후: {fruits}")

# clear(): 모든 요소 제거
fruits.clear()
print(f"clear() 후: {fruits}")

# 실행 시 주의사항:
# - 출력 결과의 순서는 실행할 때마다 다를 수 있습니다 (순서 미보장 특성)
# - pop()은 임의의 요소를 반환하므로, 실행할 때마다 다른 결과가 나올 수 있습니다


list_1.append(list_2)
print(
    list_1=',list_1) #리스트 연결' \
    'pringt(list_1 * 3 =', list_1 * 3)

#문자열
str_1 = 'Hello'
str_2 = 'World'
print('str_1 + str_2 =', str_1 + str_2

print('str_1 * 3 =', str_1 * 3
      

#set
# 중복허용 안함
set_1 = {1, 2, 3, 4, 5, 6, 7}
print
print(set_1[0])
# set에서 특정 위치에 단일 값에 접근하려면
print('set_1 + set_2 =', set_1 + set_2
print('set_1.intersection(set_2) =', set_1.intersection(set_2))
#합집합
print('set_1.union(set_2) =', set_1.union(set_2))
#차집합
print('set_1.difference(set_2) =', set_1.difference(set_2))