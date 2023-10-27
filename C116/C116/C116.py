import cv2


img = cv2.imread("butterfly.jpg")
grey_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
print(grey_img)
cv2.imshow("Display image",grey_img)

cv2.waitKey(0)

