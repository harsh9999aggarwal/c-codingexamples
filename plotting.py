from matplotlib import pyplot as plt
x1=[1,2,3,4]
y1=[2,4,1,3]
plt.plot(x1,y1,label='line 1',color='green',linestyle='dotted',linewidth=5,marker='o',markerfacecolor='orange',markersize=10)

y2=[1,5,6,7,9]
x2=[1,2,4,6,7]
plt.plot(x2,y2,label='line 2',color='blue',linewidth=5,marker='s',markerfacecolor='red',markersize=10)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('see my first graph')
plt.legend()
plt.show()
