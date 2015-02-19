#include <iostream>
#include <vector>
using namespace std;

class TaroJiroDividing {
    int a, b;
public:
    int getNumber(int a, int b) {
        int count_a = 0;
        int count_b = 0;
        vector<int> store_a;
        vector<int> store_b;

        if(a % 2 == 0 && b % 2 != 0)
            return 0;
        if(a % 2 != 0 && b % 2 == 0)
            return 0;

        while(a % 2 == 0) {
            store_a.push_back(a);
            a /= 2;
            count_a++;
        }

        if(a % 2 != 0) {
            store_a.push_back(a);
            count_a++;
        }

        while(b % 2 == 0) {
            store_b.push_back(b);
            b /= 2;
            count_b++;
        }

        if(b % 2 != 0) {
            store_b.push_back(b);
            count_b++;
        }

        if(count_a > count_b) {
            cout << count_b << endl;
            return count_b;
        }

        else {
            cout << count_a << endl;
            return count_a;
        }
    }
};

int main() {
    TaroJiroDividing number;
    number.getNumber(4, 7);

    return 0;
}
