import os
import sys
import linecache
import cv2
import random
# img = cv2.imread('IMG_2012-09-28T09-00-05.jpg')
# # cv2.namedWindow("image")
# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# str1='KL01_AS371'
# str2= str1.find('KL01')
# print('KL01')

filename = '../number.txt'
# IMG= cv2.imread("..//crop//69.jpg")
# size=IMG.size

if os.path.exists(filename):
	os.remove(filename)
if __name__ == '__main__':
    fliename = '../BIRD_v200_3.txt'
    # fi=open("number.txt","a")
    f = open(fliename)
    j = 0
    imgdir = 'C:\\birds_3\\crop\\'

    while True:  # 循环读取文本里面的内容
        fi = open(filename, "a")
        line = f.readline()  # 一行一行的读
        if not line:  # 如果没有内容，则退出循环
            break
        if line.find('.jpg')>=0:
            Name=line.rstrip()
            img = cv2.imread(line.rstrip())
        if line.find(',')>=0:
            list = []
            for i in range(len(line.split(','))):  # \t即tab健分隔
                list.append(line.split(',')[i])
            # font = cv2.FONT_HERSHEY_DUPLEX
            # cv2.putText(img,list[4].rstrip(),(int(list[0])-10, int(list[1])-10),font,2,(255,0,0),1)
            y=int(list[1])
            h=int(list[3])
            x=int(list[0])
            w=int(list[2])
            if(x<0 or y<0):
                continue
            # elif (x>0 and x<=300) or (y>0 and y<=300):
            #     a = random.randint(0, min(x,y))
            #     b = random.randint(0, min(x,y))
            #     cropImg = img[(y-b):(y-b + 600), (x-a):(x-a + 600)]
            #     st = list[4].rstrip() + ' ' + '00000' + str(j) + '.jpg' + ' ' + str(a) + ' ' + str(b) + ' ' + list[2] + ' ' + list[3]
            #     fi.writelines(st)
            #     fi.write('\n')
            #     cv2.imwrite(imgdir + '00000' + str(j) + '.jpg', cropImg)

            elif (x>300 and y>300) :
                a=random.randint(0,300)
                b=random.randint(0,300)
                cropImg = img[(y-b):(y-b + 600), (x-a):(x-a + 600)]
                st = list[4].rstrip() + ' ' +'00000' + str(j) + '.jpg' + ' ' + str(a) + ' ' + str(b) + ' ' + list[2] + ' ' + list[3]
                fi.writelines(st)
                fi.write('\n')
                cv2.imwrite(imgdir + '00000' + str(j) + '.jpg', cropImg)

            # cv2.imwrite(imgdir + '0000' + str(j) + '.jpg', cropImg)
            # st= list[4].rstrip() +' '+str(j)+'.jpg'+' '+list[0]+' '+list[1]+' '+list[2]+' '+list[3]
            # fi.writelines(st)
            # fi.write('\n')

            j+=1
            # cv2.rectangle(img, (int(list[0]), int(list[1])), (int(list[0])+int(list[2]), int(list[1])+int(list[3])), (0, 0, 255), 4)
            # cv2.imwrite(Name,img)
    f.close()



