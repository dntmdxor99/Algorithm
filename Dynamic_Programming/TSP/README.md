<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>교재와 강의자료를 참고하여 TSP 문제를 동적계획법으로 해결하는 Algorithm 3.11의 구현을 완성하시오.</p><p>단, 출력값은 알고리즘에서 계산한 D 테이블에서 최적값이 무한대가 아닌 값들을 출력해야 함에 주의하시오.</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 줄에 그래프의 정점 개수 n과 그래프의 간선 개수 m이 주어진다.</p><p>둘째 줄부터 m개의 간선이 u, v, w의 형태로 주어진다.</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 줄에 순회 경로의 최적 경로값 minlength를 출력한다.</p><p>둘째 줄에 1번 정점에서 시작하여 1번 정점으로 되돌아 오는 최적 경로를 출력한다.</p><p>(최적 경로가 여러 개 있을 수 있으므로, 교재와 강의자료에서 구현한 알고리즘의 출력 경로를 출력하도록 유의할 것)</p><p>셋째 줄부터 D 테이블을 참조하여 D[i][j]가 무한대가 아닌 항목을 아래와 같이 출력한다.</p><p>i j D[i][j]</p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
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
</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">21
1 3 4 2 1
1 7 21
2 0 1
2 4 10
2 6 20
3 1 8
3 4 14
3 5 12
4 0 6
4 1 4
</pre></div></div></div> <!----> <!----></div></div></div>
