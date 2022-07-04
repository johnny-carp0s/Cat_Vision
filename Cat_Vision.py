import cv2

print(cv2.__version__)

img = cv2.imread("discord pfp.jpg", 1)
img = cv2.resize(img, (0,0), fx=2,fy=2)
img = cv2.rotate(img, cv2.ROTATE_180)
cv2.imwrite('newimg.jpg', img)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()