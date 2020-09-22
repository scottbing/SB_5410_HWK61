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

# Driver program to test the above function
def main():
    pool = ['goose', 'cat', 'danger', 'panic']
    word = input("please enter a word from the list:\n".format(pool))
    #dictionary comprehesion of reuslts
    results = {w:lcs(w, word) for w in pool}
    #sort the dictionary on values.
    #reverse = True means sort in reverse order
    results = {k: v for k, v in sorted(results.items(),
                                       key=lambda item: item[1], reverse=True)}
    print("I think you meant", list (results.keys())[0])
    print("you typed: ", word)

#end def main():

if __name__ == '__main__':
    main()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)