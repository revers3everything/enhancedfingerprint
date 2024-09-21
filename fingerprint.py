import fingerprint_enhancer								# Load the library
import cv2

img = cv2.imread('F:\Documents\Researchs\Fingerprinthacking\image1.png', 0)						# read input image
out = fingerprint_enhancer.enhance_Fingerprint(img)		# enhance the fingerprint image
cv2.imshow('enhanced_image', out);						# display the result
cv2.imwrite('F:\\Documents\\Researchs\\Fingerprinthacking\\enhanced_image1.png', out)
cv2.waitKey(0)										# hold the display window
