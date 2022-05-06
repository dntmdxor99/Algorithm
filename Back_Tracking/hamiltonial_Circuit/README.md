<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>교재와 강의자료를 참고하여 해밀턴 회로 문제를 해결하는 Algorithm 5.6의 구현을 완성하시오.</p><p><br></p><p>주어진 무방항 무가중치 그래프 G = (V, E) 에서</p><p>해밀턴 회로의 개수를 출력하시오.</p><p><br></p><p>Algorithm 5.6을 구현할 때, 출발정점은 1로 간주한다는 것을 주의하시오.</p><p>vindex[0] = 1;</p><p>hamiltonian(0);</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫째 줄에 정점의 개수 n과 간선의 개수 m이 주어진다.</p><p>둘째 줄부터 m개의 간선이 주어진다.</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫째 줄에 해밀턴 회로의 개수를 출력한다.</p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">8 13
1 2
1 3
1 7
1 8
2 3
2 7
2 8
3 4
3 6
4 5
5 6
6 7
7 8</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">8
</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 2
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">5 6
1 2
1 5
2 3
2 4
2 5
3 4</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 2</p> <pre data-v-6e5e6c6e="">0
</pre></div></div></div> <!----> <!----></div></div></div>
