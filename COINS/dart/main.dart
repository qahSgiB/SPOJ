import 'dart:io';



int maxExchange(int n) {
	int maxN;

	if (n < 12) maxN = n;
	else maxN = maxExchange((n/2).floor())+maxExchange((n/3).floor())+maxExchange((n/4).floor());

	return maxN;
}



void main() async
{
	while (true)
	{
		int n = int.parse(stdin.readLineSync());

		stdout.writeln(maxExchange(n));
	}
}