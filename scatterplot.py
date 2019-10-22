import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9]
y=[2,4,6,3,1,7,9,5,5]
bins=10
plt.scatter(x,y,bins,color='red',label='star',marker='*')
plt.legend()
plt.show()

