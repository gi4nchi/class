from matplotlib import pylab as plt

series1=[]
series2=[]
series3=[]

for i in range(0, 30):
    series1.append(i)
    series2+=[i*i]
    series3+=[i**3]

plt.figure('first')
plt.plot(list(range(0, 30)), series1, 'g:', label="linear")
plt.plot(list(range(0, 30)), series2, 'b+', label='quafric')
plt.legend(loc='upper left')
plt.title('Try')
plt.ylim(0,1000)
plt.xlabel('Series')
plt.ylabel('Linear Progression')


plt.figure('second')
plt.plot(list(range(0, 30)), series2)
plt.title('Quadric')
plt.ylim(0,1000)
plt.xlabel('Series')
plt.ylabel('Linear Progression')

plt.figure('third')
plt.plot(list(range(0, 30)), series3)
plt.title('Cubic')
plt.ylim(0,1000)
plt.xlabel('Series')
plt.ylabel('Linear Progression')
plt.show()