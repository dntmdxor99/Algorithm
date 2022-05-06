<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>교재와 강의자료를 참고하여 m-Coloring 문제를 해결하는 Algorithm 5.5의 구현은 완성하시오.</p><p><br></p><p>주어진 평면 그래프 G = (V, E)에 대해서</p><p>인접한 지역을 서로 다른 색으로 색칠하기 위해 필요한 최소 색의 수 m의 값과</p><p>해당하는 m의 값으로 색칠할 수 있는 경우의 수를 출력하시오.</p><p><br></p><p>단,<span style="color: rgb(51, 51, 51);">그래프의 입력은 간선의 집합으로 주어지고,</span>주어진 그래프는 평면 그래프라고 가정해도 된다.</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 줄에 정점의 수 n과 간선의 수 k가 주어진다.</p><p>둘째 줄부터 k개의 간선이 주어진다.</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫째 줄에 색칠 가능한 최소의 m값을 출력한다.</p><p>둘째 줄에 해당 m값으로 색칠할 수 있는 경우의 수를 출력한다.</p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">4 5
1 2
1 3
1 4
2 3
3 4</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">3
6</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 2
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">4 6
1 2
1 3
1 4
2 3
2 4
3 4</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 2</p> <pre data-v-6e5e6c6e="">4
24</pre></div></div></div> <!----> <!----></div></div></div>
