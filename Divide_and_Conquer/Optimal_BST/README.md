<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>교재와 강의자료를 참고하여 Algorithm 3.9/3.10의 구현을 완성하시오.</p><p><br></p><p>원소의 개수 n, 키의 값 K, 원소의 탐색 빈도값의 배열 p가 주어질 때</p><p>A, R 행렬의 값을 구해서 출력하고,</p><p>R 행렬을 이용하여 구축할 수 있는 이진탐색트리의</p><p>preorder, inorder 순회 탐색 결과를 출력하시오.</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 번째 줄에 key의 개수 n이 주어진다.</p><p>두 번째 줄에 n 개의 key 값이 주어진다. (key 값은 정렬되어 있다고 가정해도 된다.)</p><p>세 번째 줄에 n 개의 빈도값 p가 주어진다. (p[i] 값은 양의 정수값으로 주어진다.)</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>먼저 행렬 A의 윗 부분 삼각형을 출력한다. (0을 포함)</p><p>다음으로 행렬 R의 윗 부분 삼각형을 출력한다. (0을 포함)</p><p>A와 R을 출력한 후에 최적 이진탐색트리에서 평균검색시간의 최적값을 출력한다.</p><p>다음 줄에 최적 이진탐색트리의 preorder 순회 탐색 결과를 출력한다.</p><p>다음 줄에 최적 이진탐색트릴의 inorder 순회 탐색 결과를 출력한다.</p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">4
10 20 30 40
3 3 1 1</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">0 3 9 11 14
0 3 5 8
0 1 3
0 1
0
0 1 1 2 2
0 2 2 2
0 3 3
0 4
0
14
20 10 30 40
10 20 30 40</pre></div></div></div> <!----> <!----></div></div></div>
