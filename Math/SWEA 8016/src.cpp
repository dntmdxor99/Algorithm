#include <iostream>

using namespace std;

int main() {
  unsigned long long int test, i;
  cin >> test;

  for (int j = 1; j <= test; j++){
    cin >> i;
    if (i == 1){
      cout << '#' << j << " " <<  1 << " " << 1 << endl;
    }
    else{
      unsigned long long int left = 2 * (i - 1) * (i - 1) + 1;
      unsigned long long int right = 2 * i * i - 1;
      cout << '#' << j << " " <<  left << " " << right << endl;
    }
  }
  
  return 0;
}
