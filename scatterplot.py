import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10,11]
y=[2,4,6,3,1,7,9,5,5,7,4]
bins=11
plt.scatter(x,y,bins,color='blue',label='star',marker='*')
plt.legend()
plt.show()

