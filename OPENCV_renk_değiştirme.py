import cv2

img = cv2.imread("kaynaks4/shapes.png")
h,w,ch = img.shape
print("h,w,ch",h,w,ch)

for row in range(h):
   
   for col in range(w):
      b,g,r = img[row,col]
      b = 255 - b
      g = 255 - g
      r = 255 - r
      img[row,col] = [b, g, r]
      
cv2.imshow("Original",img)
cv2.waitKey(0)

#resimleri yan yana getirme söyle yapilir:
#horizontal = np.hstack((img1,img2))
#cv2.imshow("birlestirilmis resimler",horizontal)

