
import cv2

filename = "octocat.png"
img = cv2.imread(filename)
imageName = filename.split('.')[0]
size = 100

def pixelate(img, h, w):
    height, width = img.shape[:2]

    temp = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)

    needed = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    cv2.imshow("pixelated " + imageName, needed)
    cv2.imwrite("pixelated_"+filename, needed)
    return temp


pixelate(img, size, size)
k = cv2.waitKey(0)