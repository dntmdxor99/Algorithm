<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>교재의 내용과 강의자료를 참고하여 0-1 배낭문제를 해결하는 알고리즘의 구현을 완성하시오.</p><p>강의자료에서 knapsack2() 또는 knapsack3()를 참조할 것.</p><p><br></p><p>단, 입력값은 단위 무게당 이익의 순서로 정렬되어 있지 않음에 유의하시오.</p><p>또한,알고리즘 실행 결과의 출력은 알고리즘의 실행과정에서결과 테이블 P에 저장한</p><p><span style="color: rgb(51, 51, 51);">무게(i) 또는 이익(j)이 0이 아닌</span>모든 항목 P[i][j]를 (i, j)의 오름차순으로 모두 출력한다는 것에 주의하시오.</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 번째 줄에 아이템의 개수 n이 주어진다.</p><p>두 번째 줄에 n개의 무게 w[i]가 주어진다.</p><p>세 번째 줄에 n개의 이익 p[i]가 주어진다.</p><p>네 번째 줄에 배낭 무게의 개수 T가 주어진다.</p><p>이후로 T개의 줄에 한 줄에 하나씩 배낭 무게 W가 주어진다.</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>주어진 배낭 무게 W 각각에 대해 다음과 같이 출력한다.<br></p><p>첫 줄에 최대 이익 maxprofit을 출력한다.</p><p>이후로 알고리즘의 실행과정에서 결과 테이블 P에 저장한</p><p><span style="color: rgb(51, 51, 51);"><span style="color: rgb(51, 51, 51);">무게(i) 또는 이익(j)이 0이 아닌</span>모든 항목 P[i][j]를 (i, j)의 오름차순으</span>로 모두 출력한다</p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">3
5 10 20
50 60 140
1
30</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">200
1 10 50
1 20 50
1 30 50
2 20 140
2 30 190
3 30 200</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 2
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">4
2 5 10 5
40 30 50 10
4
8
16
20
25</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 2</p> <pre data-v-6e5e6c6e="">70
1 3 40
1 8 40
2 3 40
2 8 70
3 3 40
3 8 70
4 8 70
90
1 1 0
1 6 40
1 11 40
1 16 40
2 1 0
2 6 40
2 11 70
2 16 70
3 11 70
3 16 90
4 16 90
120
1 5 40
1 10 40
1 15 40
1 20 40
2 5 40
2 10 70
2 15 70
2 20 70
3 15 90
3 20 120
4 20 120
130
1 5 40
1 10 40
1 15 40
1 20 40
1 25 40
2 10 70
2 15 70
2 20 70
2 25 70
3 20 120
3 25 120
4 25 130
</pre></div></div></div> <!----> <!----></div></div></div>
