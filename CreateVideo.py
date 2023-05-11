import os
import cv2
path = "Images/"
images = []
for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    if ext in ['111.jpg', '112.jpg','113.jpg','114.jpg','115.jpg','116.jpg','117.jpg','118.jpg','119.jpg','120.jpg']:
        cv_2 = path+ "/"+cv_2
        print(cv_2)
        images.append(cv_2)
count = len(images)

frame = cv2.imread(images[0])
height, width, layers = frame.shape
size = (width, height)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range (0,count):
    print(images[i])
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("done")
    