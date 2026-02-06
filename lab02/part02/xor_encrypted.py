# 3310 Lab 02
# Part 02
# 12/13/24 - Rursch

# This program will XOR two encrypted images to demonstrate information leakage when
# reusing the same one time pad.
#
# SYNTAX:   python3 xor_encrypted.py encrypted_cat_500.png encrypted_yin_yang_500.png leaked_info.png
#           python3 xor_encrypted.py <encrypted_image1.png> <encrypted_image2.png> <output_leak.png>



import numpy as np
from PIL import Image
import sys

# xorEncryptedImages:
#   The function loads both encrypted images, converts them to NumPY arrays,
#   XORs the two encrypted images together, converts the array data to uint8,
#   finally converts the result back to an image.
def xorEncryptedImages(image1Path: str, image2Path: str, outputLeak: str) -> None:
    # Load the encrypted images to 1-bit mode (binary)
    encryptedImage1 = Image.open(image1Path).convert('1')  
    encryptedImage2 = Image.open(image2Path).convert('1')  #

    # Convert both images to NumPy arrays
    encryptedArray1 = np.array(encryptedImage1)
    encryptedArray2 = np.array(encryptedImage2)

    # XOR the two encrypted images together to demonstrate the problem when reusing a one time pad.
    leakedInfoArray = np.bitwise_xor(encryptedArray1, encryptedArray2)

    # Ensure the leakedInfoArray is in the correct data type (uint8)
    leakedInfoArray = leakedInfoArray.astype(np.uint8)  

    # Convert the result from binary (0 or 1) to an image (0-255) and save
    leakedInfoImage = Image.fromarray(leakedInfoArray * 255)  
    leakedInfoImage.save(outputLeak)

    print(f"Leaked information saved as '{outputLeak}'.")

def main() -> None:
    if len(sys.argv) < 4:
        print("Usage: python xor_encrypted.py <encrypted_image1.png> <encrypted_image2.png> <output_leak.png>")
        sys.exit(1)

    encryptedImage1Path = sys.argv[1]
    encryptedImage2Path = sys.argv[2]
    outputLeak = sys.argv[3]

    xorEncryptedImages(encryptedImage1Path, encryptedImage2Path, outputLeak)

if __name__ == "__main__":
    main()
