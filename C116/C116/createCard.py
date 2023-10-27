import cv2

img = cv2.imread("poster.jpg")

rocket = img[120:360,400:500]

img[0:240,500:600]=rocket

text_to_show = "I love coding at BYJU'S"

cv2.putText (
    img,
    text_to_show,
    (20,200),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(0,255,0)
)
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.imwrite("greeting.jpg",img)