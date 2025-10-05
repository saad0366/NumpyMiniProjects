import numpy as np

print("🖼️ MINI PROJECT 2: IMAGE PROCESSING WITH NUMPY 🖼️")

# Step 1: Generate a random grayscale image (10x10)
# Each pixel value = brightness (0–255)
image = np.random.randint(0, 256, size=(10, 10), dtype=np.uint8)

print("\n🎨 Original Image (Pixel Values 0–255):")
print(image)

# Step 2: Invert Colors
# Inversion = 255 - pixel_value
inverted_image = 255 - image

print("\n🌑 Inverted Image:")
print(inverted_image)

# Step 3: Increase Brightness by 50
# Use np.clip to prevent values from going above 255
bright_image = np.clip(image + 50, 0, 255)

print("\n💡 Brightened Image (+50):")
print(bright_image)

# Step 4: Apply Threshold
# If pixel > 128 → 255 (white), else 0 (black)
threshold_image = np.where(image > 128, 255, 0)

print("\n⚫ Threshold Image (Binary - 0 or 255):")
print(threshold_image)
#no knowledge of matplotlib but due to curiosity i asked gpt to do this
import matplotlib.pyplot as plt

plt.subplot(1, 4, 1); plt.imshow(image, cmap='gray'); plt.title('Original')
plt.subplot(1, 4, 2); plt.imshow(inverted_image, cmap='gray'); plt.title('Inverted')
plt.subplot(1, 4, 3); plt.imshow(bright_image, cmap='gray'); plt.title('Brightened')
plt.subplot(1, 4, 4); plt.imshow(threshold_image, cmap='gray'); plt.title('Threshold')
plt.show()
