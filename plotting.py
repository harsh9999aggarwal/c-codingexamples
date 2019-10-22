from matplotlib import pyplot as plt
x1=[1,2,3]
y1=[2,4,1]
plt.plot(x1,y1,label='line 1',color='red',linestyle='dotted',linewidth=5,marker='o',markerfacecolor='blue',markersize=10)

y2=[1,5,6,7]
x2=[1,2,4,6]
plt.plot(x2,y2,label='line 2',color='green',linewidth=5,marker='s',markerfacecolor='orange',markersize=10)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('my first graph')
plt.legend()
plt.show()
