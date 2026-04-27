import sys
import os
os.system('pip3 install Pillow numpy --quiet')
from PIL import Image
import numpy as np

img = Image.open('/Users/abhivish/.gemini/antigravity/brain/d9bf9420-c279-4e0d-913b-126bada1651f/media__1777279471879.png').convert('RGB')
arr = np.array(img)
mask = np.any(arr < 240, axis=-1)
if mask.any():
    coords = np.argwhere(mask)
    y0, x0 = coords.min(axis=0)
    y1, x1 = coords.max(axis=0)
    pad = 30
    y0 = max(0, y0 - pad)
    y1 = min(arr.shape[0], y1 + pad)
    x0 = max(0, x0 - pad)
    x1 = min(arr.shape[1], x1 + pad)
    cropped = img.crop((x0, y0, x1, y1))
else:
    cropped = img
cropped.save('assets/hero-phone-final.png')
print("Cropped successfully")
