#include <iostream>
using namespace std;

int main()
{
	int * store;
	int j;
	int temp2,temp3;
	int N,K,size;

	bool breakout = false;

	while (true) {

		if (!(cin>> N))
			break;
		cin>> K;

		
		if (N <= 0) 
			break;

		if (K == 0) {
			cout << (((N-1) > 1234567890) ? 1234567891 : N-1) <<endl;
			continue;
		}


		if (K > 10000)
			size = 10000;
		else 
			size = K+1;

		store = new int[size];
		breakout = false;
		
		for (j = 0; j<N; ++j) {
			for (int k = 0; ((j-k)%size) >= 0 && k <= K; ++k) {
				if (k == 0)
					store [j%size] = j;
				else 
					store [j%size] += store [(j-k)%size];
				
			}

			if (store[j%size] > 1234567890) {
				j++;
				break;
			}

		}

		cout<< store [(j-1)%size] << endl;

		delete store;
		
	}
	
	return 0;

}


