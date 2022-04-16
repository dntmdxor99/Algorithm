<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>교재와 강의자료를 참고하여 Algorithm 4.2 크루스칼 알고리즘의 구현을 완성하시오.</p><p>그래프의 입력은 간선의 집합으로 주어지며,</p><p>출력값은 크루스칼 알고리즘의 각 단계별로</p><p>F 집합에 추가되는 간선을 순서대로 출력한다.</p><p>단, 가중치는 unique하며, 동일한 가중치를 가진 간선은 없다고 가정해도 된다.</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 줄에 정점의 개수 n, 간선의 개수 m이 주어진다.</p><p>두 번째 줄부터 다음과 같은 형태로 m 개의 간선이 주어진다.</p><p>u v w</p><p>u와 v는 정점의 번호이고, 1부터 n까지의 자연수로 표시한다.</p><p>w는 간선 &lt;u, v&gt;의 가중치이며, 양의 정수 값으로 주어진다.</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>크루스칼 알고리즘의 초기 단계부터 종료 단계까지<span style="color: rgb(51, 51, 51);">(n-1 times)</span></p><p>F 집합에 포함되는 간선을 순서대로 출력한다.<br></p><p><span style="color: rgb(51, 51, 51);">u v w</span></p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">5 7
1 2 1
1 3 3
2 3 7
2 4 6
3 4 4
3 5 2
4 5 5</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">1 2 1
3 5 2
1 3 3
3 4 4
</pre></div></div></div> <!----> <!----></div></div></div>
