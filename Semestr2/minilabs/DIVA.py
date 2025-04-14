import matplotlib
import math
y=lambda x:math.exp(-(x**2))+x**2
y1=lambda x:-2*x*math.exp(-(x**2))+2*x
x0=3
speed=0.01
epochs=100
def gradiendDescend(func,diffFunc,x0,speed,epochs):
    xlst=[x0]
    ylst=[]
    ylst.append(func(x0))
    for i in range(epochs):
        x_new=xlst[i]-speed*diffFunc(xlst[i])
        xlst.append(x_new)
        y_new=func(xlst[i+1])
        ylst.append(y_new)
    return xlst,ylst
print(gradiendDescend(y,y1,x0,speed,epochs))
x = np.linspace(-10, 10, 50)
y = math.exp(-(x**2))+x**2
fig,ax=plt.subplots()
ax.plot(x,y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('y=math.exp(-(x**2))+x**2')
plt.show()
