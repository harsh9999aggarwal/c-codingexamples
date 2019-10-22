from matplotlib import pyplot as plt
ages=[10,10,45,88,99,10,19,1]
#ages=[2,5,60,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40]
range=(0,100)
bins=10
#ages2=[12,15,40,30,30,45,50,45,43,40,44,60,71,33,51,18,9,77,32,21,20,100]
bins2=5
plt.hist(ages,bins,range,color='red',histtype='bar',rwidth=0.3)
#plt.hist(ages2,bins2,range,color='blue',histtype='bar',rwidth=0.1)
plt.xlabel('age')
plt.ylabel('no of people')
plt.title('myhistogram')
plt.show()
