import sys
import os

import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import color, exposure, io

ImageDirectory = 'imgs/train/'
listofallcheckingimages = [
			'img_5107.jpg', 'img_7061.jpg', 'img_6867.jpg', 'img_10277.jpg',
			'img_14881.jpg', 'img_16831.jpg', 'img_19191.jpg', 'img_21198.jpg', 
			'img_22992.jpg', 'img_24701.jpg'
			]

typeofcheckedClasses = [ 'safe driving', 
			'texting - right', 
			'talking on the phone - right', 
			'texting - left', 
			'talking on the phone - left ',
			'operating the radio',
			'drinking',
			'reaching behind', 
			'hair and makeup',
			'talking to passenger'
			]


fig, ax = plt.subplots(10, 2, figsize=(8, 24), sharex=True, sharey=True)

for i, image in enumerate(listofallcheckingimages):
	label = 'c' + 'i'
	path_of_image = os.path.join(ImageDirectory, label, image)
	print ("Analyzing %s" % path_of_image)
	try:
		image = color.rgb2gray(io.imread(path_of_image))


	# fd: 1d flattened array
		fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
		                    cells_per_block=(1, 1), visualise=True)
		print(("Feature vector length: %d" % len(fd)))

		fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), sharex=True, sharey=True)

		ax[i][0].axis('off')
		ax[i][0].set_title(typeofcheckedClasses[i])
		ax[i][0].imshow(image, aspect='auto', cmap=plt.cm.gray)

		# Rescale histogram for better display
		hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))

		ax[i][1].axis('off')
		ax[i][1].set_title('%s hog' % typeofcheckedClasses[i])
		ax[i][1].imshow(hog_image_rescaled, aspect='auto', cmap=plt.cm.gray)
	except:
		pass

fig.subplots_adjust(wspace=0.1, hspace=0.3)
plt.savefig('output/hog_listofallcheckingimages.png', bbox_inches='tight')