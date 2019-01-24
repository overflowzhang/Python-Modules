#直方图

mean, sigma = 0, 1
x = mean + sigma * np.random.randn(10000)
plt.hist(x,50)
plt.show()