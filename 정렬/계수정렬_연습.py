array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]


arr = [0] * (max(array) + 1)

# O(N)
for i in range(len(array)):
    arr[array[i]] += 1

# O(N + K)
for i in range(len(arr)): # len(arr)은 원소 중 가장 큰 값을 의미하는 K이다. K만큼 반복
    for j in range(arr[i]): # 안쪽 for문은 총 N만큼 반복
        print(i, end=' ')

'''
계수정렬의 시간 복잡도와 공간 복잡도는 모두 O(N+K)입니다.
N: 데이터의 개수
K: 데이터 중 가장 큰 값

때에 따라서 심각한 비효율성을 보일 수 있음
ex. 데이터의 개수는 2개인데 값이 0과 999,999,999인 경우(데이터의 범위가 너무 큰 경우)

그래서 데이터의 범위가 작으면서 동일한 값을 가지는 데이터가 여러개 존재하는 경우 효율적이다.
ex. 성적과 같이 0~100점 사이에 여러 값이 중복될 수 있는 경우
'''
