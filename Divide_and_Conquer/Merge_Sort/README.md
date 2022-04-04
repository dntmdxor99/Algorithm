합병 정렬

1번은 in-place하지 않은 정렬</br>
2번은 in-place한 정렬</br>

while i <= mid and j <= high:</br>
    U.append((S[i], i := i + 1)[0] if S[i] < S[j] else (S[j], j := j + 1)[0])</br>

삼항 연산자처럼 쓰는 법

