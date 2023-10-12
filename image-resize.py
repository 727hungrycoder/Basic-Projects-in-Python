# pdf  merger

# install opencv-python module for cv2

import cv2

# configurable Parameters

source = "SPACE.JPG"
destination = "RESIZED ASTRANAUT.png"

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("astranaut",src)
# cv2.waitKey(0)
# waitkey will wait untill a key is pressed


# Percent by which the image is resized

scale_percent = 50

# calculate 50 percent of original dimensions

width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# desired size
d_size = (width,height)

# resize image

output = cv2.resize(src,d_size)

cv2.imwrite(destination,output)
cv2.waitKey(5)

