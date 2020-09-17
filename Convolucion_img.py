import cv2
import numpy as np

img = "perro.png"
im = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
a = [ [ -1.0, 0.0, 1.0 ],
      [ -1.0, 0.0, 1.0 ],
      [ -1.0, 0.0, 1.0 ] ]
kernel = np.asarray(a)
dst = cv2.filter2D(im, -1, kernel)
norm = cv2.normalize(dst, None, 0, 255, cv2.NORM_MINMAX)
from IPython.display import Image
Image(filename='perro.png')
cv2.imwrite("norm.png", norm)
Image(filename="norm.png")