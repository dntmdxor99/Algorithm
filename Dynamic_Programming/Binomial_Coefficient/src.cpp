#include <iostream>
#include <typeinfo>

using namespace std;

int MAX;

int bio(int arr[], int n, int k){
    int temp1, temp2;
    for (int i = 0; i < n; i++){       // arr이 i = 1부터 n까지 계속 갱신됨, n이 최종적으로 nC?가 되는 꼴
        for (int j = 0; j <= min(i, k); j++)        // j는 nC?에서 ?에 해당하는 값임 0~k까지만 있으면 됨
        {
            if (j == 0 || j == n){       // nC0, nCn = 1
                arr[j] = 1;
                temp2 = 1;
            }
            else{
                temp1 = arr[j];     // 변환되기 전 arr[j]를 미리 temp1에 집어 넣음
                arr[j] = (arr[j] + temp2) % MAX;       // nCj = n-1Cj-1 + n-1Cj임, 이때 arr[j-1]은 미리 어디에 저장해놔야할듯??
                temp2 = temp1;      // 변환되기 전 arr[j]를 가지고, 다음번에 실행할때 써먹음
            }
        }
        // for (int t = 0; t <= k; t++)
        //         cout << arr[t] << " ";
        //     cout << endl;
    }
    
    return (arr[k-1] + arr[k]) % MAX;
}


int bin_recursion(int n, int k){
    if ((k == 0) || (k == n)){
        return 1;
    }
    else{
        return bin_recursion(n-1, k-1) + bin_recursion(n-1, k);
    }
}


int arr[100][100] = {0,};
void bin_memoization(int i, int j){
    if ((j == 0) || (j == i)){
        arr[i][j] = 1;
    }
    else{
        bin_memoization(i-1, j-1);
        bin_memoization(i-1, j);
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j];
    }
}


int bin_DP(int n, int k){
    for (int i = 0; i <= n; i++){
        for (int j = 0; j <= min(k, i); j++){
            if ((j == 0) || (j == i)){
                arr[i][j] = 1;
            }
            else{
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j];
            }
        }
    }
    return arr[n][k];
}


int optimal_bin(int n, int k, int MAX){
    int B[100000] = {0,};       // 배열에 이항 계수를 저장함
    k = min(k, n-k);        // k를 좀 더 작은 애로 집어 넣음

    int temp, temp2;       // B[j-1]을 저장하는 원소

    for (int i = 0; i <= n; i++){
        for (int j = 0; j <= min(k, i); j++){
            if ((j == 0) || (j == n)){     //j == 0 혹은 j == n과 같다면 1을 저장함
                B[j] = 1;
                temp = 1;
            }
            else{
                // B[j] = B[j] + B[j-1];       // 이러면 B[j-1]은 이미 업데이트 된 상태이므로 기존의 B[j-1]을 저장한 무언가를 넣어줘야함
                temp2 = B[j];       // 변환되기 전의 B[j]를 넣음
                B[j] = (B[j] + temp) % MAX;
                temp = temp2;        // 변환되기 전의 B[j]를 넣음, temp는 다음 반복문, 즉 j+1으로 가서 기존의 B[j]의 역할을 수행함
            }
        }
        // for (int idx = 0; idx <= k; idx++){      // 과정을 출력함
        //         cout << B[idx] << " ";
        //     }
        //     cout << endl;
    }
    return B[k];
}


int main(){    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, k;

    cin >> n >> k >> MAX;       // 인자 받음

    

    if (k > 0)
        cout << optimal_bin(n ,k, MAX) << "\n";
    else
        cout << 1 << "\n";

    return 0;
}
