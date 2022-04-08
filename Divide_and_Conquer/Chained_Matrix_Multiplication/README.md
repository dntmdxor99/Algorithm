<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>교재와 강의자료를 참고하여, Algorithm 3.6/3.7 연쇄 행렬 곱셈 알고리즘의 구현을 완성하라.</p><p><br></p><p>행렬의 개수 n과 각 행렬의 크기 값의 배열 d를 입력으로 받고</p><p>M, P 행렬의 값을 구해서 출력하고,</p><p>단위 곱셈의 최적 횟수 및 괄호로 묶은 행렬 곱셈의 순서를 출력하라.</p><p><br></p><p>단, 최적 횟수의 최대값은 999999를 넘지 않는다.</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 번째 줄에 행렬의 개수 n이 주어진다.</p><p>두 번째 줄부터 행렬의 크기 값의 배열 d가 주어진다.</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>먼저 행렬 M의 윗 부분 삼각형을 출력한다. (0을 포함)</p><p>다음으로 행렬 P의 윗 부분 삼각형을 출력한다. (0을 포함)</p><p>M과 P를 출력한 후에 최적값을 출력한다.</p><p>다음 줄에 행렬 곱셈의 순서를 괄호로 묶어 출력한다.</p><p>모든 단위 행렬에도 괄호가 포함되어야 하고,</p><p>행렬 이름은 A1, A2, .... , An 으로 표기한다.</p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">6
5 2 3 4 6 7 8</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">0 30 64 132 226 348
0 24 72 156 268
0 72 198 366
0 168 392
0 336
0
0 1 1 1 1 1
0 2 3 4 5
0 3 4 5
0 4 5
0 5
0
348
((A1)(((((A2)(A3))(A4))(A5))(A6)))</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 2
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">1
3 5</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 2</p> <pre data-v-6e5e6c6e="">0
0
0
(A1)</pre></div></div></div> <!----> <!----></div></div></div>
