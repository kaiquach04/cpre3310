# 3310 Lab 02
# Part 02
# 12/13/24 - Rursch

# This program will encrypt an image using a one time pad and saves the encrypted output.
# The image will converted to NumPy arrays, then XOR'ed with the random pad previously 
# created.  Then, converted from binary (0 or 1) to an image (0-255) and then saved as a png.
#
# You will need to run this for each file:  cat_500 and yin_yang_500.png
#
# SYNTAX:   python3 encrypt_image.py cat_500.png random_pad.png encrypted_cat_500.png
#           python3 encrypt_image.py <image.png> <pad.png> <output_encrypted.png>

import numpy as np
from PIL import Image
import sys

# encryptImage:
#   The images will be converted to binary, then to NumPy arrays which are easier to work with
#   The NumPy image array will be XOR'ed with the random pad previously generated.
#   The data is converted to uint8 and then saved back out as an image.
def encryptImage(imagePath: str, padPath: str, outputEncrypted: str) -> None:
    # Convert image and pad to 1-bit mode (binary)
    image = Image.open(imagePath).convert('1')  
    pad = Image.open(padPath).convert('1')  

    # Convert both to NumPy arrays
    imageArray = np.array(image)
    padArray = np.array(pad)

    # XOR the image with the pad
    encryptedArray = np.bitwise_xor(imageArray, padArray)

    # Ensure the encryptedArray is in the correct data type (uint8)
    encryptedArray = encryptedArray.astype(np.uint8)  

    # Convert the result back to an image and save
    encryptedImage = Image.fromarray(encryptedArray * 255)  
    encryptedImage.save(outputEncrypted)

    print(f"Encrypted image saved as '{outputEncrypted}'.")

def main() -> None:
    if len(sys.argv) < 4:
        print("Usage: python3 encrypt_image.py <image.png> <pad.png> <output_encrypted.png>")
        sys.exit(1)

    imagePath = sys.argv[1]
    padPath = sys.argv[2]
    outputEncrypted = sys.argv[3]

    encryptImage(imagePath, padPath, outputEncrypted)

if __name__ == "__main__":
    main()
