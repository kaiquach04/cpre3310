# 3310 Lab 02
# Part 01
# 2/3/26 - Rauer

# Depending upon the number of arguments on the command line this program
# conduct frequency analysis or help test a potential key (alphabet).
# If there are only 2 arguments, the program will conduct a frequency analysis 
# of the ciphertext characters.  If there are 3 arguments, the program will
# use the mapping.txt file to substitute characters to provide a potential 
# solution for the decryption.  Most likely you will need to run this multiple times
# to find the final solution of the plaintext. 
#
# The mapping file should be constructed in the format of cipherChar:plainChar on an individual
# line.

# SYNTAX:   python3 part01_skel.py ciphertext.txt [mapping.txt]
#           python3 part01_skel.py <ciphertext_file> [<mapping_file>]

import sys

# readIn:
#   Reads in a file and returns its contents as a single string.
def readIn(filename: str) -> str:
    with open(filename, 'r') as file:
        lines = [line.rstrip().upper() for line in file]
    return ''.join(lines)
    
# countChars:
#   Counts the total number of characters in the ciphertext. 
def countChars(cipherText: str) -> int:
    return sum(1 for char in cipherText if char.isalpha())

# frequency:
#   Counts the occurrences of each character in the ciphertext.
#   Returns a dictionary with characters as the keys and num of occurences as the values.
def frequency(cipherText: str) -> dict:
    freq = {} 
    # TODO:
    # Loop through the ciphertext.
    # Learning about .get() will be helpful for this next part.
    #   Add the character to the freq dictionary if it isn't in there yet.
    #   Increase the value of the character every time it occurs.
    for char in cipherText:
	if freq.get(char) == None:
	  freq[char] = 1
	else:
	  print(f"{char} already present")
	  freq[char] += 1
	  
    return freq
    
# freqAnalysis:
#   Performs frequency analysis and returns a sorted list of characters with their counts and percentages.
#   The key=lambda x: x[2] specifies that the sorting should be based on the third element (x[2], 
#   the percentage) of each inner list. 
#   The reverse=True sorts the list in descending order.
#   Note: Normal distribution of characters in the English language (descending order):
#         "E, T, A, O, I, N, S, H, R, D, L, C, U, M, W, F, G, Y, P, B, V, K, J, X, Q, Z"
#   Returns a list of lists, where the inner lists have format: [character, number, percentage]
def freqAnalysis(cipherText: str) -> list:
    totalChars = countChars(cipherText)     # This is counting the total number of characters
    freq = frequency(cipherText)            # This is getting the number of occurences of each character
    # TODO:
    # Add logic to calculate a character's percentage of the total in the ciphertext
    # This should go after count in the square brackets below
    # freqList will be a list of lists, where each inner list is for a character
    # Each character should have a list with format: [character, number, percentage]
    
    freqList = freqList = [[char, count, ] for char, count in freq.items()]
    freqList.sort(key=lambda x: x[2], reverse=True) # This sorts the list
    return freqList
    
# printFreqAnalysis:
#   Prints a formatted frequency analysis chart.
def printFreqAnalysis(freqList: list) -> None:
    print("Character\tCount\tPercentage")
    for char, count, percentage in freqList:
        print(f"{char}\t\t{count}\t{percentage:.2f}%")
        
# decryptWithMapping:
#   Decrypts the ciphertext using a substitution mapping.
def decryptWithMapping(cipherText: str, mapping: dict) -> str:
    plainText = []
    for char in cipherText:
        if char in mapping:
            plainText.append(mapping[char])
        else:
            plainText.append(char)
    return ''.join(plainText)

# loadMapping:
#   Loads mapping values from the file mapping.txt with the format cipherChar:plainChar.
#   You have been provided with the layout of the normal distribution characters in 
#   the file mapping.txt.  Based upon the frequencies you have found, you should modify the file.
#   The best way to start is with the highest frequency cipherChar being mapped to E.
#   This would look like 
#   X:E
#   where X is the cipherChar and E is the plainChar
#   Note: Just another reminder that the normal distribution of characters 
#   in the English language (descending order) are:
#         "E, T, A, O, I, N, S, H, R, D, L, C, U, M, W, F, G, Y, P, B, V, K, J, X, Q, Z"
def loadMapping(mappingFile: str) -> dict:
    mapping = {}
    with open(mappingFile, 'r') as file:
        for line in file:
            line = line.strip()
            if ':' in line:
                cipherChar, plainChar = line.split(':')
                mapping[cipherChar.upper()] = plainChar.upper()
    return mapping


def main() -> None:
  
    cipherText = readIn(sys.argv[1])

    if len(sys.argv) == 3:
        mappingFile = sys.argv[2]
        mapping = loadMapping(mappingFile)
        decryptedText = decryptWithMapping(cipherText, mapping)
        print("Decrypted Text:")
        print(decryptedText)
    elif len(sys.argv) == 2:
        print("Frequency Analysis:")
        freqList = freqAnalysis(cipherText)
        printFreqAnalysis(freqList)
    else:
        print("Usage: python3 part01_skel.py <ciphertext_file> [<mapping_file>]")
        return
        

if __name__ == "__main__":
    main()
