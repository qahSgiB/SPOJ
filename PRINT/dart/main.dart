import 'dart:io';
import 'dart:math';



void main()
{
    int testsCount = int.parse(stdin.readLineSync());

    int max = 1000000000;
    int erMax = sqrt(max).ceil();

    List<bool> erSieve = List.filled(erMax-2, true);
    List<int> erPrimes = [];

    for (int n = 2; n < erMax; n++)
    {
        if (erSieve[n-2])
        {
            erPrimes.add(n);

            for (int nPrime = n*2; nPrime < erMax; nPrime += n) erSieve[nPrime-2] = false;
        }
    }

    for (int test = 0; test < testsCount; test++)
    {
        List<int> input = stdin.readLineSync().split(' ').map(int.parse).toList();
        int start = input[0];
        int end = input[1];
        if (start == 1) start = 2;

        List<bool> primes = List.filled(end-start+1, true);
        int testMax = sqrt(end).ceil();

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
            if (primes[n-start]) stdout.writeln(n);
        }

        stdout.writeln();
    }
}