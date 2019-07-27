#include <iostream>
#include <string>
#include <math.h>
#include <stdlib.h>

using namespace std;



const long long maxExchangeDpMax = 100000000;
long long maxExchangeDp[maxExchangeDpMax];



long long maxExchange(long long n) {
	long long maxN;

	if (n < maxExchangeDpMax) maxN = maxExchangeDp[n];
    else
    {
        long long n2 = floor(n/2);
        long long n3 = floor(n/3);
        long long n4 = floor(n/4);

        maxN = maxExchange(n2)+maxExchange(n3)+maxExchange(n4);
    }

    return maxN;
}



int main()
{
    maxExchangeDp[0] = 0;
    maxExchangeDp[1] = 1;
    maxExchangeDp[2] = 2;
    maxExchangeDp[3] = 3;

    for (long long n = 4; n < maxExchangeDpMax; n++)
    {
        long long n2 = floor(n/2);
        long long n3 = floor(n/3);
        long long n4 = floor(n/4);
        long long nSum = maxExchangeDp[n2]+maxExchangeDp[n3]+maxExchangeDp[n4];

        if (nSum > n) maxExchangeDp[n] = nSum;
        else maxExchangeDp[n] = n;
    }

    string newLine;
    while (getline(cin, newLine)) {
        long long n = atol(newLine.c_str());

        cout << maxExchange(n) << "\n";
    }

    return 0;
}