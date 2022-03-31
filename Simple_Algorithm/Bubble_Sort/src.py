n = int(input())
data = list(map(int, input().split()))


def bubble_sort(n):     # 오름차순으로 정렬
    for i in range(0, n):
        for j in range(i + 1, n):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]


bubble_sort(n)
print(*data)
