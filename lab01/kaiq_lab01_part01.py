# lab01_part01.py by Kai Quach
# 01/29/26

def modify(sentence: list[str], shift: int) -> str:
    result = []
    for char in sentence:
        upperCase = char.upper()
        ascii = ord(upperCase)
        indexVal = ascii - 65
        newPos = (indexVal + shift) % 26 # The wording threw me off but im assuming technically the shift value should be pos mathematically but result in negative (go left)
        shiftedChar = chr(newPos + 65)
        result.append(shiftedChar)
    return ''.join(result)

def main() -> None:
    sentence: list[str] = list(input("Write a sentence without spaces: "))
    shift: int = int(input("Enter the shift value (positive for mathematically shifting to the right, negative shift to left: "))
    result: str = modify(sentence, shift)
    print(f"Encrypted sentence: {result}")

if __name__ == "__main__":
    main()
