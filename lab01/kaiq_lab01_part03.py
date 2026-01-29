# lab01_part03.py by Kai Quach
# 01/29/26

import sys

def readFile(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()
    
def analyze(ciphertext: str) -> None:
    upperCase = ciphertext.upper()

    for shift in range(26):
        result = []

        for char in upperCase:
            if "A" <= char <= "Z":
                index = ord(char) - 65
                new_idx = (index - shift) % 26
                result.append(chr(new_idx + 65))
            else:
                result.append(char)

        testCipherStr = ''.join(result)
        print(f"Testing shift by {shift}:\n{testCipherStr}\n")
   


def main() -> None:
    if len(sys.argv) < 2:
        print("Not enough values")
        print("Usage: python3_part03_skel.py ciphertext.txt")
        return
    
    ciphertext=readFile(sys.argv[1])
    analyze(ciphertext)




if __name__ == "__main__":
    main()