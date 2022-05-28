<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>교재와 강의자료를 참고하여 외판원 순회 문제를 분기한정법으로 해결하는 Algorithm 6.3의 구현을 완성하시오.</p><p>분기한정을 위한 Best FS의 방문순서대로 노드의 상태를 출력해야 함에 유의하시오.</p><p><span style="color: rgb(51, 51, 51);">또, 방향 그래프에서는 bound 값이 무한대일 경우에 INF라고 출력하도록 해야 함에 유의하시오!!!</span><br></p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 줄에 정점의 개수 n과 간선의 개수 m이 주어진다.</p><p>둘째 줄부터 m개의 간선이 u, v, w의 형태로 주어진다.</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫째 줄부터 분기한정법으로 방문하는 노드의 상태를 아래와 같이 출력한다.</p><p>level bound path[0] path[1] ...... path[k]</p><p>(마지막에 공백이 출력되지 않도록 유의할 것)</p><p>노드의 상태 출력이 모두 끝나면 다음 줄에 최적값 minlength를 출력한다.</p><p>다음 줄에는 1번 정점을 출발점으로 하는 최적 순회 경로를 출력한다.</p><p>(최적 순회 경로는 여러 개가 있을 수 있으나, 교재와 강의자료에서 선택하는 순회 경로를 출력하도록 유의할 것)</p><p>또한, 방향 그래프에서는 bound 값이 무한대일 경우에는 INF라고 출력하도록 해야 함에 유의하시오!!!</p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">5 20
1 2 8
1 3 13
1 4 18
1 5 20
2 1 3
2 3 7
2 4 8
2 5 10
3 1 4
3 2 11
3 4 10
3 5 7
4 1 6
4 2 6
4 3 7
4 5 11
5 1 10
5 2 6
5 3 2
5 4 1</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">0 22 1
1 26 1 2
1 30 1 3
1 33 1 4
1 34 1 5
2 29 1 2 3
2 29 1 2 4
2 29 1 2 5
3 46 1 2 3 4 5 1
3 29 1 2 3 5 4 1
29
1 2 3 5 4 1
</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 2
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">4 9
1 2 2
1 3 9
2 1 1
2 3 6
2 4 4
3 2 7
3 4 8
4 1 6
4 2 3
</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 2</p> <pre data-v-6e5e6c6e="">0 13 1
1 20 1 2
1 20 1 3
1 INF 1 4
2 22 1 2 3 4 1
2 INF 1 2 4 3 1
2 26 1 3 2 4 1
2 21 1 3 4 2 1
21
1 3 4 2 1
</pre></div></div></div> <!----> <!----></div></div></div>
