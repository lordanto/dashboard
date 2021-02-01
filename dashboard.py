
#line plotting
from matplotlib import pyplot as plt

x = [5, 2, 9, 4, 7]

y = [10, 5, 8, 4, 2]

plt.plot(x, y)

plt.show()

# Bar plotting
from matplotlib import pyplot as plt

x = [5, 2, 9, 4, 7]

y = [10, 5, 8, 4, 2]

plt.bar(x, y)

plt.show()

#Histogram Plotting
from matplotlib import pyplot as plt

y = [13, 1, 2, 6, 4]

plt.hist(y)

plt.show()

#Scanner Plotting
from matplotlib import pyplot as plt

plt.plot([1, 2, 3, 4],
         [1, 4, 9, 16], 'ro')
#ro to make red circles
plt.axis([0, 6, 0, 20])
plt.show()
