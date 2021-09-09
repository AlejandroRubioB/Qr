import cv2
import qrcode
cap = cv2.VideoCapture(0)#Abrir la web cam de mi computadora
detector = cv2.QRCodeDetector()
while True:
    success, img = cap.read()
    data, _ , _ =detector.detectAndDecode(img)
    #Si se encuntra algun dato en el código  Qr mostrarlo
    if data != '':
        print (data)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0XFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
