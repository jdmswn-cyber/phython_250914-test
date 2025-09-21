# tuple, list, set
# tuple : 순서가 있고, 중복을 허용한다, 수정이 불가능하다 (immutable)
tuple_1 = (1, 2, 3, 4, 5, 1, 2, 3
tuple_2 = (10,20)
print('tuple_1 =', tuple_1)
print('tuple_2 =', tuple_2) #튜플 생성
print('tuple_1[0] =', tuple_1[0]) #인덱싱
print('tuple_1[1:4] =', tuple_1[1:4]) #슬라이싱
print('len(tuple_1) =', len(tuple_1)) #길이 확인
print('tuple_1 + tuple_2 =', tuple_1 + tuple_2) #튜플 연결
print('tuple_1 * 3 =', tuple_1 * 3) #튜플 반복
print("tuple[0]=",tuple_1[0]) #인덱싱
print("tuple[1:4]=",tuple_1[1:4]) #슬라이싱
print("tuple[1:4]=",tuple_1[1:4]) #슬라이싱
print('튜플의 개수=',len(tuple_1)) #튜플의 개수
print("마지막 튜플의 값=",tuple_1[-1]) #음수 인덱스
#튜플의 데이터중에서 마지막 3개를 출력
print("마지막 3개의 값=",tuple_1[-3:]) #음수 인덱스
#튜플의 데이터중에서 처음 3개를 출력
print("처음 3개의 값=",tuple_1[:3]) #음수 인덱스
#튜플의 데이터중에서 처음 3개를 출력
#역방향으로 출력
print("역방향으로 출력=",tuple_1[::-1]) #음수 인덱스
#튜플의 데이터중에서 처음 3개를 출력

