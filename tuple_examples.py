"""
tuple_examples.py
파이썬 튜플(Tuple) 예제와 설명을 포함한 스크립트입니다.

실행: python tuple_examples.py
"""

import sys

def show_header(title):
    print('\n' + '=' * 60)
    print(title)
    print('=' * 60)


def basic_tuple_examples():
    show_header('1) 튜플 생성과 기본 접근')
    # 튜플 생성
    t = (1, 2, 3)
    print('튜플 t =', t)

    # 인덱싱
    print('t[0] =', t[0])
    print('t[-1] =', t[-1])

    # 슬라이싱 (튜플도 시퀀스이므로 슬라이싱 가능)
    print('t[0:2] =', t[0:2])


def immutability_example():
    show_header('2) 불변성(immutability)')
    t = (10, 20, 30)
    print('원본 튜플 t =', t)
    try:
        # 아래 행은 예외를 발생시킵니다: 'tuple' object does not support item assignment
        t[0] = 100
    except TypeError as e:
        print('튜플의 요소를 변경하려고 하면 TypeError가 발생합니다 ->', repr(e))

    # 하지만 튜플이 가리키는 객체가 가변(mutable)이면 그 내부는 변경 가능
    t2 = ([1, 2], 3)
    print('가변 요소를 포함하는 튜플 t2 =', t2)
    t2[0].append(99)
    print('t2 내부 리스트를 수정한 후 =', t2)


def unpacking_examples():
    show_header('3) 언패킹(Unpacking)')
    # 기본 언패킹
    t = ('Alice', 30)
    name, age = t
    print('이름:', name, ', 나이:', age)

    # 별표 표현을 사용한 확장 언패킹
    vals = (1, 2, 3, 4, 5)
    a, *middle, e = vals
    print('a =', a, ', middle =', middle, ', e =', e)


def nesting_and_methods():
    show_header('4) 중첩 튜플과 관련 연산')
    nested = (1, (2, 3), (4, 5, 6))
    print('중첩 튜플 =', nested)

    # len, count, index 사용
    sample = (1, 2, 2, 3, 2)
    print('sample.count(2) =', sample.count(2))
    print('sample.index(3) =', sample.index(3))


def use_cases_and_advice():
    show_header('5) 사용 사례 & 권장사항')
    print('- 불변성이 필요한 데이터(변경 불가)를 표현할 때 사용')
    print('- dict의 키로 사용 가능 (해시 가능한 경우)')
    print('- 리스트보다 메모리 효율이 좋을 때가 있음')


def demo_small_tasks():
    show_header('6) 작은 실습 문제들 (빠른 데모)')
    # 예제 1: 두 튜플 이어붙이기
    t1 = (1, 2)
    t2 = (3, 4)
    print('t1 + t2 =', t1 + t2)

    # 예제 2: 튜플 반복
    print('t1 * 3 =', t1 * 3)

    # 예제 3: 튜플을 리스트로 변환 후 조작
    t = (5, 6, 7)
    lst = list(t)
    lst.append(8)
    t_new = tuple(lst)
    print('튜플을 리스트로 바꿔서 수정한 후 다시 튜플로:', t_new)


def student_program_interactive():
    """튜플과 변수만 사용해 학생 성적 입력, 석차 계산, 정렬을 수행합니다."""
    students = ()  # ((name, score), ...)

    # 학생 수 입력
    while True:
        try:
            n_s = input('학생 수를 입력하세요 (정수): ').strip()
            n = int(n_s)
            if n <= 0:
                print('양수를 입력하세요.')
                continue
            break
        except Exception:
            print('정수를 입력하세요.')

    i = 0
    while i < n:
        name = input(f'{i+1}번 학생 이름: ').strip()
        if name == '':
            print('이름을 비워둘 수 없습니다.')
            continue
        while True:
            try:
                s = input(f'{name}의 점수 (정수): ').strip()
                score = int(s)
                break
            except Exception:
                print('정수를 입력하세요.')

        students = students + ((name, score),)
        i += 1

    student_program_process_and_print(students)


def student_program_demo():
    students = (('홍길동', 88), ('김영희', 95), ('이철수', 88), ('박민수', 72))
    print('=== 학생 프로그램 데모 데이터 ===')
    student_program_process_and_print(students)


def student_program_process_and_print(students):
    # students: ((name, score), ...)
    # 석차 계산
    with_ranks = ()  # ((name, score, rank), ...)

    idx = 0
    while idx < len(students):
        name = students[idx][0]
        score = students[idx][1]

        # rank: score보다 큰 점수 개수 + 1
        rank = 1
        j = 0
        while j < len(students):
            other = students[j][1]
            if other > score:
                rank += 1
            j += 1

        with_ranks = with_ranks + ((name, score, rank),)
        idx += 1

    print('\n원본 입력 (석차 포함):')
    k = 0
    while k < len(with_ranks):
        rec = with_ranks[k]
        print(f'{k+1}. 이름: {rec[0]}, 점수: {rec[1]}, 석차: {rec[2]}')
        k += 1

    # 점수 내림차순 정렬 (선택 방식, 튜플만 사용)
    remaining = with_ranks
    sorted_students = ()

    while len(remaining) > 0:
        max_idx = 0
        m = 1
        while m < len(remaining):
            if remaining[m][1] > remaining[max_idx][1]:
                max_idx = m
            m += 1

        sorted_students = sorted_students + (remaining[max_idx],)

        # remaining에서 제거
        if max_idx == 0:
            remaining = remaining[1:]
        elif max_idx == len(remaining) - 1:
            remaining = remaining[:max_idx]
        else:
            remaining = remaining[:max_idx] + remaining[max_idx+1:]

    print('\n정렬 결과 (점수 내림차순):')
    t = 0
    while t < len(sorted_students):
        rec = sorted_students[t]
        print(f'{t+1}. 이름: {rec[0]}, 점수: {rec[1]}, 석차: {rec[2]}')
        t += 1


def main():
    basic_tuple_examples()
    immutability_example()
    unpacking_examples()
    nesting_and_methods()
    use_cases_and_advice()
    demo_small_tasks()

if __name__ == '__main__':
    main()
#석차순으로 정렬
