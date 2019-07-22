#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>

using namespace std;



int main()
{
    int testsCount;
    scanf("%i", &testsCount);

    int max = 2147483647;
    // int max = 10000;
    int erMax = ceil(sqrt(max));

    bool erSieve[erMax-2];
    fill_n(erSieve, erMax-2, true);
    vector<int> erPrimes;

    for (int n = 2; n < erMax; n++)
    {
        if (erSieve[n-2])
        {
            erPrimes.push_back(n);

            for (int nPrime = n*2; nPrime < erMax; nPrime += n) erSieve[nPrime-2] = false;
        }
    }

    for (int test = 0; test < testsCount; test++) {
        int start;
        int end;
        scanf("%i %i", &start, &end);
        if (start == 1) start = 2;

        bool primes[end-start+1];
        fill_n(primes, end-start+1, true);
        int testMax = ceil(sqrt(end));

        for (int n = 2; n <= testMax; n++)
        {
            if (erSieve[n-2])
            {
                int nStart = start%n == 0 ? start : start+n-(start%n);
                if (nStart == n) nStart += n;

                for (int nPrime = nStart; nPrime <= end; nPrime += n) primes[nPrime-start] = false;
            }
        }

        for (int n = start; n <= end; n++)
        {
            if (primes[n-start])
            {
                printf("%i", n);
                printf("\n");
            }
        }

        // printf("\n");
    }

    return 0;
}