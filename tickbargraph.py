import matplotlib.pyplot as plt
import csv
with open('tec.csv')as csvfile:
    readcsv=csv.reader(csvfile,delimeter=',')
    for row in readcsv:
        print(row)
        
x=[1,2,3,4,5,6,7,8,9,11]
y=[2,4,5,7,11,6,9,12,2,4]
tick_label=['one','two','three','our','five','six','seven','two','three','our']
plt.bar(x,y,tick_label=tick_label,width=0.2,color=['red','green'])
plt.show()
import matplotlib.pyplot as plt
img1 = image.load_img(img_path,target_size=(100,100))

x = image.img_to_array(img1)/255.0
plt.axis("off")
plt.imshow(x)
plt.show()
print(x.shape)
x =x.reshape((1,100,100,3))
datagen = image.ImageDataGenerator(
                                      rotation_range=30,
                                      width_shift_range=0.2,
                                      height_shift_range=0.2,
                                      shear_range =0.2,
                                       zoom_range =0.2,
                                     horizontal_flip = True,
                                       fill_mode ="nearest"
)
