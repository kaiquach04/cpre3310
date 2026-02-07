# 3310 Lab 02
# Part 02
# 12/13/24 - Rursch

# This program will generate the key with the specified dimensions.
# This key is random bits that need to be the exact same size as the image
# that you want to encrypt.  In our specific case this will be a 500x500 image,
# but this could be parameterized and used for different image sizes.
#
# Students will not alter this program for lab.
# 
# SYNTAX:   python3 generate_pad.py 500 500 random_pad.png
#           python3 generate_pad.py <image_width> <image_height> <output_pad.png>

import numpy as np
from PIL import Image
import sys

# generatePad:
#   This will generate the key with the dimensions provided on the command line
#   The random bits are 0 or 1.
#   The binary bits (0 or 1) then need to be converted to an image (0 - 255)and saved
def generatePad(width: int, height: int, output_pad: str) -> None:
    random_bits = np.random.randint(0, 2, size=(height, width)).astype(np.uint8)  
    random_bits_image = Image.fromarray(random_bits * 255)  
    random_bits_image.save(output_pad)

    print(f"Random pad saved as '{output_pad}'.")

def main() -> None:
    if len(sys.argv) < 4:
        print("Usage: python3 generate_pad.py <image_width> <image_height> <output_pad.png>")
        sys.exit(1)

    width = int(sys.argv[1])
    height = int(sys.argv[2])
    output_pad = sys.argv[3]

    generatePad(width, height, output_pad)

if __name__ == "__main__":
    main()

