<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>교재와 강의자료를 참고하여 0-1 배낭문제를 해결하는 Algorithm 5.7을 완성하시오.</p><p><br></p><p>단, 문제의 입력은 단위무게당 이익순으로 정렬되어 있지 않음에 유의하시오.</p><p>또한, 알고리즘의 출력은 알고리즘의 실행 단계별로</p><p>상태공간트리의 각 노드에서의 상태를 출력해야 함에 주의하시오.</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫번째 줄에 아이템의 개수 n과 배낭의 무게 W가 주어진다.</p><p>두번째 줄에 n개의 아이템 무게 w[i]가 주어진다.</p><p>세번째 줄에 n개의 아이템 이익 p[i]가 주어진다.</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 번째 줄부터 한 줄에 하나씩 상태공간트리를 방문하는 노드의 상태를 출력하시오.</p><p>노드 상태는 다음과 같은 순서로 출력한다.</p><p>i weight profit bound maxprofit</p><p>상태를 출력하는 순서는 Algorithm 5.7의 노드 실행 순서이다. (즉, DFS with Pruning의 노드 순회 순서임)</p><p>노드의 상태 출력이 끝나는 다음 줄에 최대이익을 출력한다.</p><p>이후로 배낭에 담은 아이템을 한 줄에 하나씩 무게와 이익 순서로 출력한다.</p><p>아이템을 출력하는 순서는 처음에 단위무게당 이익으로 정렬한 순서대로 출력함에 주의할 것.</p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">4 16
2 5 10 5
40 30 50 10
</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">0 0 0 115 0
1 2 40 115 40
2 7 70 115 70
3 17 120 115 70
3 7 70 80 70
4 12 80 80 80
4 7 70 70 80
2 2 40 98 80
3 12 90 98 90
4 17 100 98 90
4 12 90 90 90
3 2 40 50 90
1 0 0 82 90
90
2 40
10 50</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 2
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">4 16
5 2 5 10
30 40 10 50
</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 2</p> <pre data-v-6e5e6c6e="">0 0 0 115 0
1 2 40 115 40
2 7 70 115 70
3 17 120 115 70
3 7 70 80 70
4 12 80 80 80
4 7 70 70 80
2 2 40 98 80
3 12 90 98 90
4 17 100 98 90
4 12 90 90 90
3 2 40 50 90
1 0 0 82 90
90
2 40
10 50
</pre></div></div></div> <!----> <!----></div></div></div>
