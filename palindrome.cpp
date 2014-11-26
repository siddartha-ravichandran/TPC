#include <iostream>
#include <string>
using namespace std;

#define ZERO 48
#define NINE 57
 
string findNextPalin(string number)
{
	string palindrome = number;

	int len = palindrome.size() - 1;

	int mid = palindrome.size()/2;

	for (int i = 0;i < mid; ++i)
	{
		palindrome[len - i] = palindrome[i];
	}

	

	while(palindrome <= number)
    {
     
			int i = ((palindrome.size() % 2 == 0) ? (mid - 1): mid);
			int j = mid;

            while(i >= 0 && j < palindrome.size() && palindrome[i] == NINE )
            {
                palindrome[i] = palindrome[j] = ZERO;
                i--;
                j++;
            }

			// Case : when all 9s in palindrome
            if(i < 0)
            {
                
				palindrome = "1" + palindrome;
                palindrome[palindrome.size() - 1]++;

				return palindrome;
            } else {

				palindrome[i]++;
				
				palindrome[j] = palindrome[i];
            
			}
 
    }

	return palindrome;

}

int main()
{
    int numCases;

    cin >> numCases;

    for(int i = 0; i < numCases ; i++)
    {
        string number,palindrome;

        cin >> number;

		cout << findNextPalin (number) << endl;

	}
}
