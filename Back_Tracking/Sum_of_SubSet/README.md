<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>교재와 강의자료를 참고하여 Sum-of-Subsets 문제를 푸는 Algorithm 5.4의 구현을 완성하시오.</p><p><br></p><p>n개의 원소를 가진 정수의 집합 S가 주어지고,</p><p>임의의 정수 W가 주어졌을 때,</p><p>합이 W가 되는 부분집합의 개수와 각 부분집합을 출력하도록 하시오.</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 줄에 원소의 개수 n과 임의의 정수 W가 주어진다.</p><p>둘째 줄에 n개의 정수가 주어진다.</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 줄에 원소의 합이 W가 되는 부분집합의 개수를 출력한다.</p><p>둘째 줄부터 원소의 합이 W가 되는 모든 부분집합을 한 줄에 하나씩 출력한다.</p><p><span style="color: rgb(51, 51, 51);">단, 부분집합에서의 원소 출력 순서는 주어진 S의 원소 순서와 동일해야 한다. (백트래킹 순서대로)</span><br></p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">4 13
3 4 5 6</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">1
3 4 6</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 2
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">3 10
1 2 3</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 2</p> <pre data-v-6e5e6c6e="">0
</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 3
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">20 20
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 3</p> <pre data-v-6e5e6c6e="">64
1 2 3 4 10
1 2 3 5 9
1 2 3 6 8
1 2 3 14
1 2 4 5 8
1 2 4 6 7
1 2 4 13
1 2 5 12
1 2 6 11
1 2 7 10
1 2 8 9
1 2 17
1 3 4 5 7
1 3 4 12
1 3 5 11
1 3 6 10
1 3 7 9
1 3 16
1 4 5 10
1 4 6 9
1 4 7 8
1 4 15
1 5 6 8
1 5 14
1 6 13
1 7 12
1 8 11
1 9 10
1 19
2 3 4 5 6
2 3 4 11
2 3 5 10
2 3 6 9
2 3 7 8
2 3 15
2 4 5 9
2 4 6 8
2 4 14
2 5 6 7
2 5 13
2 6 12
2 7 11
2 8 10
2 18
3 4 5 8
3 4 6 7
3 4 13
3 5 12
3 6 11
3 7 10
3 8 9
3 17
4 5 11
4 6 10
4 7 9
4 16
5 6 9
5 7 8
5 15
6 14
7 13
8 12
9 11
20
</pre></div></div></div> <!----> <!----></div></div></div>
