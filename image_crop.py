import cv2

img = cv2.imread("league.png")
crop_img = img[640:640+57, 1290:1290+233]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)