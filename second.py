import cv2
import numpy as np

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

def empty(a):
    pass
def tracks():
    cv2.namedWindow("HSV")
    cv2.resizeWindow("HSV",640,300)
    cv2.createTrackbar("Hue Min","HSV",150,179,empty)
    cv2.createTrackbar("Hue Max","HSV",179,179,empty)
    cv2.createTrackbar("Sat Min","HSV",78,255,empty)
    cv2.createTrackbar("Sat Max","HSV",255,255,empty)
    cv2.createTrackbar("Val Min","HSV",112,255,empty)
    cv2.createTrackbar("Val Max","HSV",255,255,empty)
def colordetect(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("Hue Min","HSV")
    h_max = cv2.getTrackbarPos("Hue Max", "HSV")
    s_min = cv2.getTrackbarPos("Sat Min", "HSV")
    s_max = cv2.getTrackbarPos("Sat Max", "HSV")
    v_min = cv2.getTrackbarPos("Val Min", "HSV")
    v_max = cv2.getTrackbarPos("Val Max", "HSV")
    #print(type(h_min))
    #print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    return imgHSV,mask,imgResult


tracks()
while True:
    img = cv2.imread('D:\playpython\\di.png')#yuankuai,fangkuaiD:\playpython
    img=cv2.resize(img,(640,480),interpolation=cv2.INTER_AREA )
    img = cv2.GaussianBlur(img, (7, 7), 1)
    #初始化
    imgHSV,mask,imgResult = colordetect(img)
    imgStack = stackImages(0.5,([img,imgHSV],[mask,imgResult]))
    cv2.imshow("result",imgStack)
    key = cv2.waitKey(40) & 0xFF
    if key == ord('q'):
        break
    
cv2.destroyAllWindows()




#红色管道数据150，179,78,255,112,255
# url = 0#"E:\OpenCV\opencv\sources\samples\data\my\wandao.mp4"
# camera = cv2.VideoCapture(url)
# tracks()
# while (True):
#     ret,frame = camera.read()
#     img = cv2.GaussianBlur(frame, (7, 7), 1)
#     imgHSV,mask,imgResult = colordetect(frame)
#     # cv2.imshow("img",img)
#     # cv2.imshow("imgHSV",imgHSV)
#     # cv2.imshow("mask",mask)
#     # cv2.imshow("result",imgResult)
#     imgStack = stackImages(0.5,([frame,imgHSV],[mask,imgResult]))
#     cv2.imshow("result",imgStack)
#     key = cv2.waitKey(40) & 0xFF
#     if key == ord('q'):
#         break
    
# camera.release()
# cv2.destroyAllWindows()
