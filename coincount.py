#Recursive function which takes in the amount and the index of the coin denomination
#that is broken into sub-problems :
# 1. Considering the same coin again with deduction in amount
# 2. Considering the remaining coins without deducting the amount
def coincount(amount,index):
	if amount == 0:
		return 1
	elif amount < 0:
		return 0
	else:
			
		withoutsamecoin = coincount (amount,index+1) if index < (len(coins) - 1) else 0
			
		withsamecoin = coincount (amount - coins[index],index)
		
		return withoutsamecoin + withsamecoin
		
# Initialize the coins list
coins = [1,2,5,10,20,50,100]
		
# print the no. of outcomes
print coincount (100,0)
