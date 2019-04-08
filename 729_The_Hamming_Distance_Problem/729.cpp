#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int number_of_testcases, n, k, i;
    char a[20];
    // get number of testcases
    cin >> number_of_testcases;
    // for each testcase (get number, then substract)
    while (number_of_testcases--) {
        // get the length and the hamming distance
        cin >> n >> k;
        // create first string by adding n-k zeroes and k ones
        for (i = 0; i < n - k; i++) a[i] = '0';
        for (i = n - k; i < n; i++) a[i] = '1';
        // also the null byte to mark end
        a[n] = '\0';

        do {
        // write out the string
            puts(a);
            // while there is a next permutations which is written into a
            // first is start of permutation, for a it just takes first letter
            // second is end of permutation, a + n targets null byte in a
            // a + n is non inclusive
        } while (next_permutation(a, a + n));
        // if there are more testcases, print new line
        if (number_of_testcases) cout << endl;
    }
}
