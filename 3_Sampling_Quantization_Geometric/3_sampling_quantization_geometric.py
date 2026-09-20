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

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h, w = gray.shape

# Q21: 8-bit -> 4-bit quantization (16 levels)
levels_4bit = 16
quantized_4bit = (gray // (256 // levels_4bit)) * (256 // levels_4bit)
quantized_4bit = quantized_4bit.astype(np.uint8)
cv2.imwrite(os.path.join(OUTPUT_DIR, "q21_quantized_4bit.jpg"), quantized_4bit)

# Q22: 8-bit -> 2-bit quantization (4 levels)
levels_2bit = 4
quantized_2bit = (gray // (256 // levels_2bit)) * (256 // levels_2bit)
quantized_2bit = quantized_2bit.astype(np.uint8)
cv2.imwrite(os.path.join(OUTPUT_DIR, "q22_quantized_2bit.jpg"), quantized_2bit)

# Q23: Downsample by factor of 2
downsampled = cv2.resize(img, (w // 2, h // 2), interpolation=cv2.INTER_NEAREST)
print(f"Q23: Original resolution = {w}x{h}, New resolution = {w // 2}x{h // 2}")
cv2.imwrite(os.path.join(OUTPUT_DIR, "q23_downsampled.jpg"), downsampled)

# Q24: Crop a rectangular ROI using user-provided coordinates
x1, y1, x2, y2 = w // 4, h // 4, 3 * w // 4, 3 * h // 4  # example ROI
roi = img[y1:y2, x1:x2]
cv2.imwrite(os.path.join(OUTPUT_DIR, "q24_cropped_roi.jpg"), roi)

# Q25: Rotate image by 90 degrees and save
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite(os.path.join(OUTPUT_DIR, "q25_rotated.jpg"), rotated)
print("Q25: Rotated image saved as 'output/q25_rotated.jpg'")
