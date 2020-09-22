# A Dynamic Programming based Python3 program to
# find minimum of coins to make a given change V
import sys


# m is size of coins array (number of
# different coins)
def minCoins(coins, m, V):
    # table[i] will be storing the minimum
    # number of coins required for i value.
    # So table[V] will have result
    table = [[sys.maxsize, []] for i in range(V + 1)]
    #print("table: ", table)

    # Base case (If given value V is 0)
    table[0] = [0, [None]]

    # # Initialize all table values as Infinite
    # for i in range(1, V + 1):
    #     table[i] = sys.maxsize
    #     #print("table: ", table)

        # Compute minimum coins required
    # for all values from 1 to V
    for i in range(1, V + 1):

        # Go through all coins smaller than i
        for j in range(m):
            if (coins[j] <= i):

                sub_res = table[i - coins[j]]
                if (sub_res[0] != sys.maxsize and
                    sub_res[0] + 1 < table[i][0]):
                    table[i][0] = sub_res[0] + 1
                    #if there is no subres,make new res the curr coin
                    if sub_res[1][0] == None:
                        table[i][1] = [coins[j]]
                    else:
                        #concatenate sub resuul and curr coin
                        table[i][1] = sub_res[1] + [coins[j]]
                    #print("table: ", table)
    return table[V]


# Driver Code
if __name__ == "__main__":
    coins = [25, 10, 5, 1]
    m = len(coins)
    V = 17
    print("Minimum coins required is ",
          minCoins(coins, m, V))

# This code is contributed by ita_c
