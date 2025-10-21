import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# Load Image
image_path = r"C:\Users\sanja\Downloads\aerial-footage-of-a-scenic-road-surrounded-by-towering-pine-trees-and-large-trees-captured-by-a-drone-showcasing-a-serene-natural-landscape-from-above-video.jpg"
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError(f"Image at path {image_path} not found.")

# Convert image to HSV for color segmentation
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define red color range for masking in HSV (red wraps at hue 0/180)
lower_red1 = np.array([0, 50, 50])     # Lower saturation and value thresholds to tolerate lighting
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])

# Create masks for red color
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)

# Morphological operations to clean the mask using smaller kernel for preserving small blobs
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))  
red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)

# Find contours from mask
contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Circularity calculation helper
def circularity(contour):
    perimeter = cv2.arcLength(contour, True)
    area = cv2.contourArea(contour)
    if perimeter == 0:
        return 0
    return 4 * math.pi * area / (perimeter * perimeter)

# Filter contours based on area and circularity thresholds suitable for very small bullseyes
min_area = 10         # Lowered to detect smaller blobs
circularity_threshold = 0.5  # More relaxed circularity threshold

filtered_contours = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    circ = circularity(cnt)
    print(f"Contour area: {area:.2f}, circularity: {circ:.2f}")  # Debug output
    if area >= min_area and circ >= circularity_threshold:
        filtered_contours.append(cnt)

# Draw all contours in blue for debugging
result = image.copy()
cv2.drawContours(result, contours, -1, (255, 0, 0), 1)  # All contours in blue

# Draw filtered contours in green
cv2.drawContours(result, filtered_contours, -1, (0, 255, 0), 2)  # Filtered contours in green

# Show results
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Red Mask after Morph")
plt.imshow(red_mask, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("All contours (blue) and Filtered contours (green)")
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
