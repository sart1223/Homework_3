from matplotlib import pylab as plt
import pandas as pd

df1 = pd.read_csv("AMD.csv")
print(df1.head())

df2 = pd.read_csv("UA.csv")
print(df2.head())

mean1 = df1["Close"].mean()
mean2 = df2["Close"].mean()

plt.figure("AMD Stock")
plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=0.6, label="AMD Stock price, mean="+str(mean1))
# or the same can be:
plt.figure(("Under Armour Stock"))
plt.plot("Date", "Close", 'r-', linewidth=0.6, label="UA Stock price, mean="+str(mean2), data=df2)


plt.show()

plt.scatter(df1["Date"], df1["Close"], color="k")
plt.scatter(df2["Date"], df2["Close"], color="g")
plt.show()