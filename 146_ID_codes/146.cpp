#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    // try to get input
    try {
        string jeebus;
        string temp;
        // while getting input to jeebus
        while (cin >> jeebus) {
            // if end character, break out
            if(jeebus == "#") break;
            // put it into temp
            temp = jeebus;
            bool isGay = false;
            bool isSuperGay = false;

            do {
                // if second
                if(isGay){
                    // put bool to true to mark that there was a successor
                    isSuperGay = true;
                    // output it and break
                    cout << temp << endl;
                    break;
                }
                // if is same, aka first loop, put bool to true
                if(jeebus == temp) {
                    isGay = true;
                }

            }
            // get next permutation for temp
            while (next_permutation(temp.begin(),temp.end()));
            // if there was no successor, print it
            if (!isSuperGay) cout << "No Successor" << endl;
        }
    }
    // if can't read input, print newline
    catch (const exception& e) {
        cout << endl;
    }
}