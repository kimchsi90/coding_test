# 소수 판별 함수(2 이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어 떨어진다면
        if x % 2 == 0:
            return False # 소수가 아님
    return True # 소수임


# 소수의 성질을 이용한 개선된 알고리즘
import math

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, math.sqrt(x) + 1):
        if x % i == 0:
            return True
    return False
