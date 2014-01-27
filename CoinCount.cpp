#include <iostream>
#include <string>
#include <fstream>
using namespace std;

//The final amount that is to be made
int finalamount = 100;

//Array of the denominations available to us
int coins[] = {1,2,5,10,20,50,100};

// Size of the above array
int size;

// File where are the outcomes are available
ofstream myfile;

// Function which takes in an amount and the index of the coin denomination that has to be taken
// to start with.

// Also takes the path of the denominations that been visited yet.
int CoinCount (int amount,int index, string path)
{
	char buffer[30];

	// If the amount is '0' then write the outcome to the file and return 1 (as this a possible outcome)
	if (amount == 0) {

		myfile << path << endl;

		return 1;
	// If the amount is negative, then return '0' as this is not a possible outcome
	} else if (amount < 0)
		return 0;
	else {

		// Move Forward with the next index that is without considering the coin at the same 'index'
		int withoutsamecoin = (index < (size - 1)) ? CoinCount (amount, index + 1,path) : 0;

		// update the path with the appropriate coin denomination
		path.append ( itoa(coins[index],buffer,10) );
		path.append ( " " );

		// Now use the coin at the specified index to deduct the amount
		// The remaining amount is to be counted (considering the same coin again)
		int withsamecoin = CoinCount (amount - coins[index], index, path);

		// Sum of the 2 gives use the total no. of outcomes.
		return withoutsamecoin + withsamecoin;
	}		
}



int main()
{
	// Initialize the Path 
	string path("");

	// Specify the size
	size = sizeof (coins) / sizeof (coins[0]);

	cout << "Amount : " << finalamount << endl;
	
	cout << "Denominations Available: ";
	
	for (int i = 0; i <= size; ++i)
	{
		cout << coins[i] << " ";
	}

	// Open the file
	myfile.open ("outcomes.txt");

	// Display the total no. of outcomes
	cout << endl << "No. of Outcomes:" << CoinCount (finalamount,0,path) << endl;

	// Close the file
	myfile.close();

	cin.get();

}
