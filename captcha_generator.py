import random
import string
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import cv2

# Generate a random CAPTCHA text
def generate_captcha_text(length=5):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))

# Create a CAPTCHA image
def generate_captcha_image(captcha_text, width=200, height=80):
    # Create an image with white background
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 40)  # You can change the font
    except:
        font = ImageFont.load_default()

    # Add text to the image
    text_x = (width - len(captcha_text) * 20) // 2
    text_y = (height - 40) // 2
    draw.text((text_x, text_y), captcha_text, font=font, fill='black')

    # Add noise
    for _ in range(500):
        x, y = random.randint(0, width), random.randint(0, height)
        draw.point((x, y), fill='black')

    # Convert to OpenCV format
    captcha_np = np.array(image)
    return captcha_np

# Display the CAPTCHA image
def show_captcha():
    captcha_text = generate_captcha_text()
    captcha_image = generate_captcha_image(captcha_text)

    print(f"Generated CAPTCHA: {captcha_text}")
    
    # Show the image using OpenCV
    cv2.imshow("CAPTCHA", captcha_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_captcha()
