<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>n by m 체스보드에서 기사의 여행 문제를 해결하는 백트래킹 알고리즘을 구현하시오.</p><p><br></p><p><span style="color: rgb(51, 51, 51);">Knight's Tour 문제는 해밀턴 경로(path)와 해밀턴 회로(circuit, cycle)를 찾는 문제로 구분할 수 있다.</span><br></p><p><span style="color: rgb(51, 51, 51);">해밀턴 회로는 출발 정점과 무관하게 회로의 수를 구할 수 있고,</span></p><p>해밀턴 경로는 출발 정점에 따라 가능한 경로의 수가 달라짐에 유의하시오.</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 번째 줄에 체스보드의 크기 n(행의 크기)과 m(열의 크기)이 주어진다.</p><p>두 번째 줄에 출발정점의 개수 T가 주어진다.</p><p>이후로 T개의 출발정점이 i(row), j(col) 의 쌍으로 주어진다.</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 번째 줄에 해밀턴 회로의 개수를 출력한다.</p><p>두 번째 줄부터 입력에서 주어진 출발정점 각각에 대해 해밀턴 경로의 수를 한 줄에 하나씩 출력한다.</p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">3 4
3
0 0
0 1
1 0</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">0
2
0
4
</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 2
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">3 10
2
0 0
1 1</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 2</p> <pre data-v-6e5e6c6e="">32
448
416</pre></div></div></div> <!----> <!----></div></div></div>
