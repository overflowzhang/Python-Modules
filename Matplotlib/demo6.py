#子图

# figsize绘图对象的宽度和高度，单位为英寸，dpi绘图对象的分辨率，即每英寸多少个像素，缺省值为80
plt.figure(figsize=(8,6),dpi=100)

# subplot(numRows, numCols, plotNum)
# 一个Figure对象可以包含多个子图Axes，subplot将整个绘图区域等分为numRows行*numCols列个子区域，按照从左到右，从上到下的顺序对每个子区域进行编号
# subplot在plotNum指定的区域中创建一个子图Axes
A = plt.subplot(2,2,1)
plt.plot([0,1],[0,1], color="red")

plt.subplot(2,2,2)
plt.title("B")
plt.plot([0,1],[0,1], color="green")

plt.subplot(2,1,2)
plt.title("C")
plt.plot(np.arange(10), np.random.rand(10), color="orange")

# 选择子图A
plt.sca(A)
plt.title("A")

plt.show()