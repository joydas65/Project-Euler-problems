#include <bits/stdc++.h>
#include <malloc.h>
using namespace std;
bool isPrime(int n) {
  // Corner cases
  if (n <= 1)
    return false;
  if (n <= 3)
    return true;

  if (n % 2 == 0 || n % 3 == 0)
    return false;

  for (int i = 5; i * i <= n; i = i + 6)
    if (n % i == 0 || n % (i + 2) == 0)
      return false;

  return true;
}
int main() {
  int n, i, ind = -1;
  int primes[150000];
  for (i = 2; i <= 1000000; i++) {
    if (isPrime(i)) {
      primes[++ind] = i;
    }
  }
  long *prefixarr;

  prefixarr = (long *)malloc(ind * sizeof(long));

  long k = 0;

  for (i = 0; i <= ind; i++) {
    prefixarr[i] = k + primes[i];
    k += primes[i];
  }

  int t = 0;

  cin >> t;

  for (i = 0; i < t; i++) {
    cin >> n;
    int first = 0, flag = 0;
    int last = ind;
    int middle = (first + last) / 2;

    while (first <= last) {
      if (primes[middle] < n)
        first = middle + 1;
      else if (primes[middle] == n) {
        flag = 1;
        break;
      } else
        last = middle - 1;

      middle = (first + last) / 2;
    }
    if (flag == 1) {
      cout << prefixarr[middle] << endl;
    } else {
      cout << prefixarr[last] << endl;
    }
  }

  return 0;
}
