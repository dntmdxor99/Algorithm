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


int main(){    

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, k;

    cin >> n >> k >> MAX;       // 인자 받음

    k = min(k, n-k);        // k를 좀 더 작은 애로 집어 넣음

    int arr[100000] = {0,};
    // int arr[k+1] = {0,};     // 이러면 동적으로 받아서 배열이 아닌 벡터로 되는듯 ..

    if (k > 0)
        cout << bio(arr, n ,k) << "\n";
    else
        cout << 1 << "\n";

    return 0;
}
