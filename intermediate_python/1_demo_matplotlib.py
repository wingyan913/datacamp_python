# BASIC PLOTS WITH MATPLOTLIB
# Data visualization
# explore data, report insight

# subpackage: pyplot
import matplotlib.pyplot as plt

year = [2010, 2011, 2012, 2013]
weight = [50.0, 52.0, 54.0, 56.0]
plt.plot(year, weight) #line
# 1st arg: horizontal axis
# 2nd arg: vertical axis
plt.show() # display plot


plt.scatter(year, weight) # dot only, no line
plt.show()

#______________________________________________________________________________
# HISTOGRAM
# explore dataset, see distribution

import matplotlib.pyplot as plt

values = [0.1, 0.2, 0.5, 1, 2, 5, 10]
plt.hist(values, 3)
# x: a list of value to build a histogram
# bin: how many bins, the data should be divided (default: 10 bins)

plt.show()

#______________________________________________________________________________
#CUSTOMIZATION
yrs = [2010,2011,2012]
sal = [10, 20, 30]
yrs = [2008, 2009] + yrs
sal = [0, 5] + sal
plt.plot(yrs, sal)
plt.xlabel("Year")
plt.ylabel("Salary")
plt.title("Unknown")
plt.xticks([2008, 2009, 2010, 2011, 2012])
plt.yticks([0, 10, 20, 30])
plt.show()