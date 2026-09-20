import os
import cv2
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(BASE_DIR, "assignment_1_cv.jpg")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

img = cv2.imread(IMG_PATH)
if img is None:
    print(f"Error: could not load image at '{IMG_PATH}'.")
    exit()

h, w, _ = img.shape

# Q11: Access and print pixel value at a user-provided (x, y)
x, y = w // 2, h // 2  # example coordinate (center of image)
pixel = img[y, x]
print(f"Q11: Pixel value at ({x}, {y}) = {pixel}")

# Q12: Modify a selected pixel's value and save
modified = img.copy()
modified[y, x] = [0, 0, 255]  # set to red (BGR)
cv2.imwrite(os.path.join(OUTPUT_DIR, "q12_modified_pixel.jpg"), modified)
print(f"Q12: Pixel at ({x}, {y}) modified to [0,0,255] and saved.")

# Q13: Print B, G, R values of a selected pixel
b, g, r = img[y, x]
print(f"Q13: At ({x}, {y}) -> B={b}, G={g}, R={r}")

# Q14: Split into B, G, R channels and save each
b_ch, g_ch, r_ch = cv2.split(img)
cv2.imwrite(os.path.join(OUTPUT_DIR, "q14_blue_channel.jpg"), b_ch)
cv2.imwrite(os.path.join(OUTPUT_DIR, "q14_green_channel.jpg"), g_ch)
cv2.imwrite(os.path.join(OUTPUT_DIR, "q14_red_channel.jpg"), r_ch)

# Q15: Merge channels back into a single color image
merged = cv2.merge((b_ch, g_ch, r_ch))
cv2.imwrite(os.path.join(OUTPUT_DIR, "q15_merged_image.jpg"), merged)

# Q16: Min and max intensity of grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
min_val, max_val = gray.min(), gray.max()
print(f"Q16: Min intensity = {min_val}, Max intensity = {max_val}")

# Q17: Mean intensity of grayscale image
mean_val = gray.mean()
print(f"Q17: Mean intensity = {mean_val:.2f}")

# Q18: Mean and standard deviation using NumPy
mean_np = np.mean(gray)
std_np = np.std(gray)
print(f"Q18: Mean = {mean_np:.2f}, Std Dev = {std_np:.2f}")

# Q19: Create a 256x256 grayscale image with every pixel = 128
flat_img = np.full((256, 256), 128, dtype=np.uint8)
cv2.imwrite(os.path.join(OUTPUT_DIR, "q19_flat_gray_128.jpg"), flat_img)

# Q20: Grayscale intensity ramp from 0 to 255
ramp_row = np.linspace(0, 255, 256, dtype=np.uint8)
ramp_img = np.tile(ramp_row, (256, 1))
cv2.imwrite(os.path.join(OUTPUT_DIR, "q20_intensity_ramp.jpg"), ramp_img)
