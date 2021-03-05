import os
from PIL import Image
import numpy as np 
img_parts=[]
img_parts_avgdat=[]
faces_avgdat=[]
ready_image=[]
face_width=20
face_height=20
img = Image.open("mom3.jpg")
img=img.resize((2000,2000))
imglist = os.listdir("Dataset/faces")
faces_obj=[Image.open("Dataset/faces/"+str(i)).resize((face_width,face_height)) for i in imglist[0:10000]]#face data array
faces= [np.array(i) for i in faces_obj]#face array with pixel data
sum =0
sum2=0
for j in range((int)(img.height/face_height)):
	for i in range((int)(img.width/face_width)):
		img_parts.append(img.crop((i*face_width,face_height*j,face_width*(1+i),face_height*(1+j))))
img_parts_data = [np.array(i) for i in img_parts]
for i in range((int)((img.height/face_height)*(img.width/face_width))):
	sumR = 0
	sum2R=0
	sumB = 0
	sum2B=0
	sumG = 0
	sum2G=0
	for j in range(face_width):
		for k in range(face_height):
			sumR = sumR + (img_parts_data[i][j,k,0])
			sumB = sumB + (img_parts_data[i][j,k,1])
			sumG = sumG + (img_parts_data[i][j,k,2])
			sum2R = sum2R + (faces[i][j,k,0])
			sum2B = sum2B + (faces[i][j,k,1])
			sum2G = sum2G + (faces[i][j,k,2])
	img_parts_avgdat.append(np.array([(int)(sumR/(face_width*face_height)),(int)(sumB/(face_width*face_height)),(int)(sumG/(face_width*face_height))]))
	faces_avgdat.append(np.array([(int)(sum2R/(face_width*face_height)),(int)(sum2B/(face_width*face_height)),(int)(sum2G/(face_width*face_height))]))

for i in img_parts_avgdat:
	minval=9999999999	
	for j in range((int)((img.height/face_height)*(img.width/face_width))):
		if((abs(i[0]-faces_avgdat[j][0])+abs(i[1]-faces_avgdat[j][1])+abs(i[2]-faces_avgdat[j][2]))/3<minval):
			index = j
			minval=(abs(i[0]-faces_avgdat[j][0])+abs(i[1]-faces_avgdat[j][1])+abs(i[2]-faces_avgdat[j][2]))/3		
	ready_image.append(faces[index])
canvas = Image.new('RGB',(2000,2000))
for i in range((int)(img.height/face_height)):
	for j in range((int)(img.width/face_width)):
		canvas.paste(Image.fromarray(ready_image[(int)(img.width/face_width)*i+j]),(face_width*j,face_height*i))
canvas.show()
canvas.save("result.jpg")


