#include <iostream>
#include <vector>


using namespace std;


int ver_num, edge_num, cnt, m;
vector<vector<int>> W;
vector<int> vcolor;


bool promising(int i){
    int j = 1;
    while (j < i){
        if (W[i][j] && (vcolor[i] == vcolor[j]))
            return false;
        j++;
    }
    return true;
}


void m_coloring(int i){
    if (promising(i)){
        if (i == ver_num)
            cnt++;
        else{
            for(int color = 1; color <= m; color++){
                vcolor[i + 1] = color;
                m_coloring(i + 1);
            }
        }
    }
}


int main(){
    cin >> ver_num >> edge_num;

    W.resize(ver_num + 1, vector<int>(ver_num + 1, 0));

    int i, j;
    for(int k = 0; k < edge_num; k++){
        cin >> i >> j;
        W[i][j] = 1;
        W[j][i] = 1;
    }

    vcolor.resize(ver_num + 1, 0);

    for(m = 1; m <= ver_num; m++){
        cnt = 0;
        m_coloring(0);
        if (cnt)
            break;
    }

    cout << m << '\n' << cnt << '\n';

    return 0;
}
