https://www.acmicpc.net/problem/16563


시간 초과가 오지게 나서 당황했는데, 문제를 곰곰히 생각해보니까 최적화 할 수 있는 부분이 너무 많았다.  
  
  
  
배열의 크기를 5,000,000으로 잡을 필요가 없다.  
최대 수를 찾아야 하는데, 그냥 변수에 저장하면 되는 일이었다.  
최대 수까지 에라토스테네스의 수를 계산할 필요가 없이, 최대 수의 제곱근까지만 계산해도 된다.  
마지막으로 제일 작은 소수로 초기화 하면 logN 시간에 풀 수 있었다....  
