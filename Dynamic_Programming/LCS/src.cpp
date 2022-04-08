#include <iostream>
#include <cstring>

using namespace std;
int m = 0;


string get_lsc(int i, int j, int path[][1000], string sub) {  
  // cout << i << " " << j << endl;
   if ((i == 0) || (j == 0))
      return "";
   else {
      if (path[i][j] == 1)
         return get_lsc(i - 1, j - 1, path, sub) += sub[i];
      else if (path[i][j] == 2)
         return get_lsc(i, j - 1, path, sub);
      else
         return get_lsc(i - 1, j, path, sub);
   }
}


void lsc(string str1, string str2) {
   int str1_len = str1.length();
   int str2_len = str2.length();

   m = max(str1_len, str2_len);

   int data[1000][1000];
   int path[1000][1000];


   memset(data, 0, sizeof(data));
   memset(path, 0, sizeof(path));

   for (int i = 1; i < str1_len; i++) {
      for (int j = 1; j < str2_len; j++) {
         if (str1[i] == str2[j]) {
            data[i][j] = data[i - 1][j - 1] + 1;
            path[i][j] = 1;
         }
         else {
            data[i][j] = max(data[i - 1][j], data[i][j - 1]);
            if (data[i][j-1] > data[i-1][j])
               path[i][j] = 2;
            else
               path[i][j] = 3;
         }
      }
   }

   // for (int i = 1; i < str1_len; i++){
   //     for (int j = 1; j < str2_len; j++){
   //         cout << data[i][j] << " ";
   //     }
   //     cout << '\n';
   // }

 //  cout << '\n';

   // for (int i = 1; i < str1_len; i++){
   //     for (int j = 1; j < str2_len; j++){
   //         cout << path[i][j] << " ";
   //     }
   //     cout << '\n';
   // }
   // cout << '\n';


   string sub = get_lsc(str1_len-1, str2_len-1, path, str1);

  cout << sub.length() << endl;
   cout << sub << endl;
}


int main() {
   string str1, str2;

   cin >> str1;
   cin >> str2;


   str1.insert(0, " ");
   str2.insert(0, " ");


   lsc(str1, str2);


   return 0;
}
