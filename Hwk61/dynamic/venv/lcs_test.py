# Dynamic Programming implementation of LCS problem
def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

                # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
# end of function lcs

# A Dynamic Programming based Python program for edit
# distance problem
def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

                # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]
#end def editDistDP(str1, str2, m, n):


# Driver program to test the above function
def lcs_test():
    pool = ['goose', 'cat', 'danger', 'panic']
    word = input("please enter a word from the list:\n{0}\n".format(pool))
    #dictionary comprehesion of reuslts
    results = {w:lcs(w, word) for w in pool}
    #sort the dictionary on values.
    #reverse = True means sort in reverse order
    results = {k: v for k, v in sorted(results.items(),
                                       key=lambda item: item[1], reverse=True)}
    commonality = list(results.items())[0][1]
    if(commonality > len(word)/2):  #if common letters are fewer than half the entry
        print("I think you meant", list (results.keys())[0])
    else:
        print("I have no idea what you meant.")
#end def lcs_test():

def main():
    pool = ['goose', 'cat', 'danger', 'panic']
    word = input("please enter a word from the list:\n{0}\n".format(pool))
    word = word.lower() #convert word to lowercase

    for w in pool:
        print(w, editDistDP(word, w, len(word), len(w)))

#end def main():

if __name__ == '__main__':
    main()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)