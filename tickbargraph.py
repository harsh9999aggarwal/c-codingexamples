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
