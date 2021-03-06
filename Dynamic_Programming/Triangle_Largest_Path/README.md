2022-1 알고리즘 5주차 3번

삼각형 위의 최대 경로

Description

파스칼의 삼각형처럼 생긴 삼각형에서 경로 위의 숫자들의 합이 최대인 경로를 찾고자 한다.

예를 들어, 아래와 같이 높이가 4인 삼각형을 생각해 보자.

3

7 4

2 4 6

8 5 9 3

이 삼각형에서 경로는 바로 아래로 이동하거나 바로 아래의 오른쪽으로만 이동 가능한다.

위의 예에서라면 숫자 합이 최대인 경로는 [3 7 4 9]이고 경로 합은 23이다.

경로 합의 최대 크기를 출력하고 해당 경로를 한 줄로 출력하라.

단, 최대 크기를 가진 경로가 여러 개일 경우에는 제일 오른쪽으로 치우친 경로를 출력한다.

예를 들어,

1

2 2

3 2 3

4 2 2 5

5 2 2 2 4

이처럼 두 개의 최대 경로 [1 2 3 4 5] 와 [1 2 3 5 4] 가 존재할 경우

[1 2 3 5 4]를 출력하면 된다.



문제에 대한 해설과 파이썬 참조 구현 코드는 아래 영상을 참고할 수 있다.

(단, 가급적 먼저 문제를 스스로 충분히 풀어보고 난 후에 영상을 참고할 것을 강력히 권장한다.)

https://youtu.be/ycwnAwRHQxM


Input
첫 번째 줄에는 삼각형의 높이 n이 주어진다.

두 번째 줄부터 n개의 줄에 각각 삼각형의 숫자들이 주어진다.


Output
첫 번째 줄에 최대 경로의 합을 출력한다.

두 번째 줄에 최대 경로를 출력한다.

단, 최대 경로가 여러 개일 경우에는 가장 오른쪽으로 치우친 경로를 출력한다.


Sample Input 1 

4
3
7 4
2 4 6
8 5 9 3
Sample Output 1

23
3 7 4 9
Sample Input 2 

5
1
2 2
3 2 3 
4 2 2 5
5 2 2 2 4
Sample Output 2

15
1 2 3 5 4



</br>

좀 더 최적화가 필요</br>
더 좋은 알고리즘이 있을 듯?
