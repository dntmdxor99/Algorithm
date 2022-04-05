# src.py는 과제 제출 소스 코드
# src_study.py는 공부 소스 코드

<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>교재와 강의자료를 참고하여 Algorithm 2.8 쉬트라센 행렬 곱셈 알고리즘을 구현하시오.</p><p>n, threshold의 값이 주어지고, n * n 정방행렬 두 개와 입력으로 주어질 때,</p><p>Algorithm 2.8을 적용하여 strassen() 함수의 호출 횟수와 두 정방행렬의 곱 A*B 행렬을 출력하시오.</p><p><br></p><p>단, n의 값이 2의 거듭제곱 수가 아닐 때는 다음과 같이</p><p>n보다 큰 거듭제곱 수를 n으로 재정의한다.</p><p><span style="color: rgb(199, 146, 234);">int</span>k<span style="color: rgb(199, 146, 234);">=</span><span style="color: rgb(247, 140, 108);">1</span>;</p><p><span style="color: rgb(199, 146, 234);">while</span>(k<span style="color: rgb(199, 146, 234);">&lt;</span>n) {</p><p>k<span style="color: rgb(199, 146, 234);">*=</span><span style="color: rgb(247, 140, 108);">2</span>;</p><p>}</p><p>주의할 점은 입력값은 n * n으로 주어지므로,</p><p>행렬의 크기는 k * k로 만들고(원소는 0으로 초기화할 것),</p><p>입력을 받을 때는 n * n으로 입력을 받아야 함에 주의해야 한다.</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 번째 줄에 n과 threshold의 값이 주어진다.</p><p>두 번째 줄부터 n * n 행렬 두 개의 값이 주어진다.</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 번째 줄에 strassen() 함수의 호출 횟수를 출력한다.</p><p>두 번째 줄부터 두 행렬 A와 B를 곱한 행렬의 값을 출력한다.</p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">2 1
2 3
4 1
5 7
6 8</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">8
28 38
26 36</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 2
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">2 2
2 3
4 1
5 7
6 8</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 2</p> <pre data-v-6e5e6c6e="">1
28 38
26 36</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 3
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">5 2
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 3</p> <pre data-v-6e5e6c6e="">57
5 5 5 5 5
5 5 5 5 5
5 5 5 5 5
5 5 5 5 5
5 5 5 5 5</pre></div></div></div> <!----> <!----></div></div></div>
