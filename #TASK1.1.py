#TASK1

def min_coins(coins, amount):
    """
    Finds the minimum number of coins needed to make up a given amount using dynamic pragramming
    
    Parameters:
    coins(list of int) : A list of coin denominations available for making change.
    amount(int) : The target amount for which we need to find minimum number of coins.

    Returns:
    int : the minimum number of coins required to make the given amount.
            if it is not possible, returns -1.
    """
    #initialize the dp array with a large value representing infinity
    dp = [float('inf')] * (amount+1)
    dp[0] = 0 #no coins is needed to make amount 0

    #build the dynamic programmming array
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)

    return dp[amount] if dp[amount] != float('inf') else -1

#testing the function
coins = [1,2,5]
amount = 11
result = min_coins(coins, amount)
print(f"Minimun number of coins to make {amount}: {result}")

#TASK2

def longest_common_sequences(s1, s2):
    """
    Finds the length of the longest common subsequence (LCS) of two strings using dynamic programming.

    Parameters:
    s1 (str): The first string.
    s2 (str): The second string.

    Returns:
    int: The length of the LCS of s1 and s2.
    """
    # Lengths of the input strings
    x, y = len(s1), len(s2)

    # Create two rows for dynamic programming
    prev = [0] * (y + 1)  # Previous row
    curr = [0] * (y + 1)  # Current row

    # Build the table using rolling rows
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if s1[i - 1] == s2[j - 1]:  # If the characters match
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])

        # Move to the next row and make the current row the previous row
        prev, curr = curr, prev

    # The length of the LCS is in the last row
    return prev[y]


# Testing the function
s1 = "abcde"
s2 = "ace"
result = longest_common_sequences(s1, s2)
print("The length of the LCS:", result)

#TASK3

def knapsack(weights, values, capacity):
    """\
        Solves the 0/1 knapsack problem using dynamic programming

        Parameters:
        weights(list of int) : the weights of the items
        values(list of int) : the values of the items
        capacity(int) : the maximum weight capacity of the knapsack

        Returns:
        int : the maximum value that can be achieved within the given capacity.
    """
    n = len(weights) #number of items

    #create a dp table with dimensions
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    #build the dp table
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w: #if item can fit in the knapsack
                dp[i][w] = max(dp[i-1][w], values[i-1]+dp[i-1][w-weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    #the maximun value is in dp[n][capacity]
    return dp[n][capacity]

#testing the function
weights = [1,3,4,5]
values = [1,4,5,7]
capacity = 7
result = knapsack(weights, values, capacity)
print(f"the maximum value that can be achieved is : {result}")