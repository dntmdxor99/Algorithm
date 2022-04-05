# 이것보다 더 좋은 알고리즘이 있음
# 추가 예정
  
<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>우리 교재의 Chapter 2, Exercise 42번 (p. 94)을 풀어보자.</p><p>이 문제는 분할정복의 대표적인 문제로, 트로미노 타일링 문제로 널리 알려져있다.</p><p>단, 이 실습과제에서 트로미노 타일의 번호는 트로미노를 놓는 순서로 정한다.</p><p>예를 들어, 다음과 같은 트로미노 퍼즐은 아래와 같은 순서로 트로미노를 놓는다.</p><p><br></p><br></p><p><br></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 번째 줄에 n, row, col이 주어진다.</p><p>n은 n*n 트로미노 퍼즐 보드의 크기이다. (2의 거듭제곱 수라고 가정해도 된다.)</p><p>row, col은 구멍의 행과 열이다. 0 &lt;= row, col &lt;= (n - 1)</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>트로미노를 놓는 순서대로 타일에 번호를 부여한 보드를 출력한다.</p><p>구멍 타일의 번호는 0으로 한다.</p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">2 0 0</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">0 1
1 1
</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 2
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">4 0 0</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 2</p> <pre data-v-6e5e6c6e="">0 2 3 3
2 2 1 3
4 1 1 5
4 4 5 5</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 3
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">8 1 2</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 3</p> <pre data-v-6e5e6c6e="">3 3 4 4 8 8 9 9
3 2 0 4 8 7 7 9
5 2 2 6 10 10 7 11
5 5 6 6 1 10 11 11
13 13 14 1 1 18 19 19
13 12 14 14 18 18 17 19
15 12 12 16 20 17 17 21
15 15 16 16 20 20 21 21</pre></div></div></div> <!----> <!----></div></div></div>

