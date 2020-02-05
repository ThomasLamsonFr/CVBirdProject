import cv2
import numpy as np
import time
import os
import matplotlib.pyplot as plt

from detector.detector import *


base_path = '../data/photos'
images = os.listdir(base_path)

while True:
	try:
		print("Pictures in " + base_path + ":")
		for i, n in enumerate(images):
			print("- [{}] ".format(i) + n)
		ans = int(input("Select a picture: "))
		assert 0 <= ans < len(images)
		break
	except (ValueError, AssertionError):
		pass

src_img = cv2.imread(base_path + '/' + images[ans])
src_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
bin_mats, elapsed = detect_markers(src_img,
						  max_dim=800,
						  draw_preprocessed=False,
						  draw_corner=True,
						  draw_quads=True)
print("Elapsed time: %.3fs" % elapsed)

for mat in bin_mats:
	plt.figure(figsize=(5, 5))
	plt.imshow(mat, cmap='gray')
	plt.show()

