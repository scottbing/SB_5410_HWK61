# Dynamic Programming implementation of LCS problem
from PIL import Image, ImageDraw

HOMER1 = 'homer01'
HOMER2 = 'homer02'
NED = 'ned'

def storePixels(im):
    width = int(im.size[0])
    height = int(im.size[1])

    # store ppixels inout double tuple format.
    pixel_array = []

    for i in range(width):  # for loop for x position
        for j in range(height):  # for loop for y position
            # get r and g and b values of pixel at position
            r, g, b = im.getpixel((i, j))
            pixel_array.append([(r, g, b), (i, j)])
        # end for j
    # end for i
    return pixel_array
# end def storePixels(im):

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
    # load image piixels
    with Image.open(HOMER1 + '.jpg') as im1:
        h1_pixels = storePixels(im1)
    with Image.open(HOMER2 + '.jpg') as im2:
        h2_pixels = storePixels(im2)
    with Image.open(NED + '.jpg') as im3:
        nd_pixels = storePixels(im3)
        print("stored")

    # comparison between Homer #1 and Homer #2
    X = h1_pixels
    Y = h2_pixels
    print("Length of LCS between Homer1 and Homer2 is ", lcs(X, Y))

    # comparison between Homer #1 and Ned
    X = h1_pixels
    Y = nd_pixels
    print("Length of LCS between Homer1 and Ned is ", lcs(X, Y))

    # comparison between Homer #2 and Ned
    X = h2_pixels
    Y = nd_pixels
    print("Length of LCS between Homer2 and Ned is ", lcs(X, Y))

    print(("\nThe high number that results from the comparison of the two"))
    print(("Homer images is indicative of the fact that they have a high"))
    print(("degree of similarity between them.\n"))

    print(("The very low numbers that resulted from the comparison of the "))
    print(("each of the Homer images to the Ned Flanders image is indicative of the"))
    print(("the fact that there is very little similarity between each of these images."))

#end def main():

if __name__ == '__main__':
    main()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)