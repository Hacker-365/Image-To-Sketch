import cv2

image = cv2.imread("C:\\Users\\91720\\Downloads\\goku.jpeg")
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)

blur_img = cv2.GaussianBlur(invert, (21, 21), 0)
inverted_blur = cv2.bitwise_not(blur_img)

sketch = cv2.divide(grey_img, inverted_blur, scale = 256.0)

cv2.imwrite("sketch.png", sketch)