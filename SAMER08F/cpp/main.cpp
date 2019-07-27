#include <iostream>

using namespace std;



int main()
{
    int n = -1;

    while (n != 0)
    {
        cin >> n;

        if (n != 0)
        {
            int count = (n*(n+1)*(2*n+1))/6;
            cout << count << "\n";
        }
    }

    return 0;
}