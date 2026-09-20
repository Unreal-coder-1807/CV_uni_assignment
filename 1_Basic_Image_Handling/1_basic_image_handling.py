import os
import cv2
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(BASE_DIR, "assignment_1_cv.jpg")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Q1 & Q2: Read image and verify it loaded
img = cv2.imread(IMG_PATH)
if img is None:
    print(f"Error: could not load image at '{IMG_PATH}'. Check the path/filename.")
    exit()
print("Q1/Q2: Image loaded successfully.")
cv2.imwrite(os.path.join(OUTPUT_DIR, "q1_original.jpg"), img)

# Q3: Height, width, channels
h, w, c = img.shape
print(f"Q3: Height={h}, Width={w}, Channels={c}")

# Q4: Total number of pixels
print(f"Q4: Total number of pixels = {h * w} (img.shape[0]*img.shape[1])")

# Q5: dtype
print(f"Q5: Data type of image matrix = {img.dtype}")

# Q6: Save with a different filename
cv2.imwrite(os.path.join(OUTPUT_DIR, "assignment_1_cv_copy.jpg"), img)
print("Q6: Image saved as 'output/assignment_1_cv_copy.jpg'")

# Q7: Read directly in grayscale mode
gray_direct = cv2.imread(IMG_PATH, cv2.IMREAD_GRAYSCALE)
cv2.imwrite(os.path.join(OUTPUT_DIR, "q7_grayscale_direct.jpg"), gray_direct)

# Q8: Convert color image to grayscale using cvtColor
gray_converted = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(os.path.join(OUTPUT_DIR, "q8_grayscale_cvtcolor.jpg"), gray_converted)

# Q9: Display using Matplotlib, hide axis
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # matplotlib expects RGB
plt.imshow(img_rgb)
plt.axis("off")
plt.title("Q9 - Matplotlib Display (no axis)")
plt.savefig(os.path.join(OUTPUT_DIR, "q9_matplotlib_display.png"), bbox_inches="tight")
plt.close()

# Q10: Resize to 50% of original width and height
resized = cv2.resize(img, (w // 2, h // 2))
print(f"Q10: Resized from ({w}x{h}) to ({w // 2}x{h // 2})")
cv2.imwrite(os.path.join(OUTPUT_DIR, "q10_resized_50pct.jpg"), resized)
