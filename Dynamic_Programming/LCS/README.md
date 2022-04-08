<div class="ivu-card-body" style="padding: 40px;">  <div class="panel-body"> <div data-v-6e5e6c6e="" id="problem-content" class="markdown-body"><p data-v-6e5e6c6e="" class="title">Description</p> <p data-v-6e5e6c6e="" class="content"><p>두 개의 문자열이 주어질 때, 최장공통부분서열(LCS, Longest Common Subsequence)을 찾아라.</p><p>예를 들어, 두 개의 문자열 X = "ABCBDAB", Y = "BDCABA"에 대해서</p><p>공통부분서열의 최대값은 4이고, 해당하는 부분서열은 BCBA이다.</p><p><br></p><p>최장공통부분서열 문제는 대표적인 동적계획법 알고리즘으로,</p><p>다음과 같은 파이썬 코드로 구현된 알고리즘을 참조할 수 있다.</p><pre><code>def lcs(x, y):
&nbsp; &nbsp; x, y = [' '] + x, [' '] + y
&nbsp; &nbsp; m, n = len(x), len(y)
&nbsp; &nbsp; c = [[0 for _ in range(n)] for _ in range(m)]
&nbsp; &nbsp; b = [[0 for _ in range(n)] for _ in range(m)]
&nbsp; &nbsp; for i in range(1, m):
&nbsp; &nbsp; &nbsp; &nbsp; for j in range(1, n):
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if x[i] == y[j]:
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; c[i][j] = c[i - 1][j - 1] + 1
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; b[i][j] = 1
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else:
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; c[i][j] = max(c[i][j - 1], c[i - 1][j])
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; b[i][j] = 2 if (c[i][j - 1] &gt; c[i - 1][j]) else 3
&nbsp; &nbsp; return c, b<br></code></pre><p><br></p><p>공통부분서열의 재구축은 다음과 같은 파이썬 코드로 구현된 알고리즘을 참조할 수 있다.</p><pre><code>def get_lcs(i, j, b, x):
&nbsp; &nbsp; if i == 0 or j == 0:
&nbsp; &nbsp; &nbsp; &nbsp; return ""
&nbsp; &nbsp; else:
&nbsp; &nbsp; &nbsp; &nbsp; if b[i][j] == 1:
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return get_lcs(i - 1, j - 1, b, x) + x[i]
&nbsp; &nbsp; &nbsp; &nbsp; elif b[i][j] == 2:
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return get_lcs(i, j - 1, b, x)
&nbsp; &nbsp; &nbsp; &nbsp; elif b[i][j] == 3:
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return get_lcs(i - 1, j, b, x)
<br></code></pre><p>위 파이썬 참조 구현에 대한 해설은 유튜브 동영상을 참고할 수 있다.</p><p><a href="https://youtu.be/z8KVLz9BFIo" rel="nofollow" target="_blank">https://youtu.be/z8KVLz9BFIo</a><br></p><p>단, 파이썬 참조 구현이 제공되므로, 이 과제에서는 파이썬 언어는 선택할 수 없음에 유의하라.</p></p> <p data-v-6e5e6c6e="" class="title">Input <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 번째 줄에 문자열 X가 주어진다.</p><p>두 번째 줄에 문자열 Y가 주어진다.</p><p>X, Y 문자열에는 영문 알파벳 대문자만 포함되어 있다. (A..Z)</p></p> <p data-v-6e5e6c6e="" class="title">Output <!----></p> <p data-v-6e5e6c6e="" class="content"><p>첫 번째 줄에 최장공통부분서열의 길이를 출력한다.</p><p>두 번째 줄에 위 파이썬 참조 코드에서 사용한 방법대로 적용했을 때의 최장공통부분서열을 출력한다.</p><p>단, 공통부분서열이 없으면 두 번째 줄은 출력하지 않는다.</p></p>  <div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 1
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">ABCBDAB
BDCABA</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 1</p> <pre data-v-6e5e6c6e="">4
BCBA</pre></div></div></div><div data-v-6e5e6c6e=""><div data-v-6e5e6c6e="" class="flex-container sample"><div data-v-6e5e6c6e="" class="sample-input"><p data-v-6e5e6c6e="" class="title">Sample Input 2
                <a data-v-6e5e6c6e="" class="copy"><i data-v-6e5e6c6e="" class="ivu-icon ivu-icon-clipboard"></i></a></p> <pre data-v-6e5e6c6e="">AAAA
BBB</pre></div> <div data-v-6e5e6c6e="" class="sample-output"><p data-v-6e5e6c6e="" class="title">Sample Output 2</p> <pre data-v-6e5e6c6e="">0</pre></div></div></div> <!----> <!----></div></div></div>
