### 주의점)  

입력되는 이진 코드가 정확한 이진 코드가 아닐 수도 있다.  

마지막에 0이 남을 수도 있음 -> 재귀가 아닌 반복문으로 해결  

heapq에서 빈도수 기준으로 노드를 정렬하려면 리스트 형태로 넣으면 된다.  

리스트의 앞 부분을 기준으로 정렬함    
  <br>
  <br>
<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>교재와 강의자료를 참고하여 허프만 코드 트리를 생성하는 허프만 알고리즘의 구현을 완성하시오.</p><p>허프만 트리의 리프 노드가 아닌 internal 노드들에는 심볼값으로 '+' 문자를 입력해 두도록 한다.</p><p><br></p><p>위 알고리즘을 통해 허프만 트리를 만들었다면, 문자열을 허프만 코드로 인코딩, 디코딩하는 알고리즘을 구현하시오.</p><p><br></p><p>허프만 코드 문제에서 preorder, inorder 출력시 마지막에 공백 문자를 출력하지 않도록 하는 것이불필요하게 어렵습니다.</p><p>따라서, 이 경우에 한해서만, preorder, inorder 출력시에만 마지막에 공백 문자를 추가해서 출력하시기 바랍니다.</p><p>첫 두 줄 preorder, inorder 출력시에만 공백문자 추가할 것. 이후에는 공백 문자 없음.</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫째 줄에 문자의 개수 n이 주어진다.</p><p>둘째 줄에 n개의 문자가 주어진다.</p><p>문자는 알파벳 대문자, 또는 소문자로만 입력된다고 가정한다.</p><p>셋째 줄에 n개의 빈도값이 주어진다.</p><p>빈도값은 모두 양의 정수라고 가정한다.</p><p>다음 줄에 문자열의 개수 T1이 주어진다.</p><p>이후 T1개의 줄에 한 줄에 하나씩 텍스트 문자열이 주어진다.</p><p>다음 줄에 문자열의 개수 T2가 주어진다.</p><p>이후 T2개의 줄에 한 줄에 하나씩 허프만 코드 문자열이 주어진다.</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫째 줄에 허프만 트리의 preorder traversal 결과를 쓴다. (출력 포맷은 아래 출력 사례를 참조한다.)</p><p>둘째 줄에 허프만 트리의 inorder traversal 결과를 쓴다.<span style="color: rgb(51, 51, 51);">(출력 포맷은 아래 출력 사례를 참조한다.)</span></p><p>셋째 줄 이후로 T1개의 문자열을 인코딩한 허프만 코드를 한 줄에 하나씩 출력한다.</p><p>이후로 T2개의 허프만 코드를 디코딩한 텍스트 문자열을 한 줄에 하나씩 출력한다.</p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">6
b e c a d f
5 10 12 16 17 25
5
cab
dec
fad
becadf
fdaceb
5
110001110
011111110
100001
11101111110000110
10010011011111110</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">+:85 +:33 a:16 d:17 +:52 f:25 +:27 c:12 +:15 b:5 e:10 
a:16 +:33 d:17 +:85 f:25 +:52 c:12 +:27 b:5 +:15 e:10 
110001110
011111110
100001
11101111110000110
10010011011111110
cab
dec
fad
becadf
fdaceb
</pre></div></div></div> <!----> <!----></div></div></div>
