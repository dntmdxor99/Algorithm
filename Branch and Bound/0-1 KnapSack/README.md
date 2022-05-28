<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>교재와 강의자료를 참고하여 0-1 배낭문제를 분기한정법으로 해결하는 Algorithm 6.2 의 구현을 완성하시오.</p><p>단, 입력값은 단위 무게당 이익의 내림차순으로 정렬되어 있지 않음에 주의하시오.</p><p>출력은 Best FS로 노드를 방문할 때 해당 노드의 상태를 아래와 같이 출력해야 한다.</p><p>level weight profit bound</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 줄에 아이템의 개수 n과 배낭 무게 W가 주어진다.</p><p>둘째 줄에 n개의 아이템 무게 w가 주어진다.</p><p>셋째 줄에 n개의 아이템 이익 p가 주어진다.</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 줄부터 Best FS로 방문하는 모든 노드의 상태를 출력한다.</p><p>각 상태를 출력하는 순서는 다음과 같다.</p><p><span style="color: rgb(51, 51, 51);">level weight profit bound</span><br></p><p><span style="color: rgb(51, 51, 51);">상태의 출력이 모두 끝나고 다음 줄에 최대 이익 maxprofit을 출력한다.</span></p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">4 16
2 5 10 5
40 30 50 10</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">0 0 0 115
1 2 40 115
1 0 0 82
2 7 70 115
2 2 40 98
3 17 120 0
3 7 70 80
3 12 90 98
3 2 40 50
4 17 100 0
4 12 90 90
90
</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 2
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">4 16
5 2 10 5
30 40 50 10 </pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 2</p> <pre data-v-6e5e6c6e="">0 0 0 115
1 2 40 115
1 0 0 82
2 7 70 115
2 2 40 98
3 17 120 0
3 7 70 80
3 12 90 98
3 2 40 50
4 17 100 0
4 12 90 90
90
</pre></div></div></div> <!----> <!----></div></div></div>
