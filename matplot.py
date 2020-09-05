import matplotlib.pyplot as plt

IBM_Mon = ['Jan', 'April', 'July', 'Oct', 'Dec']
IBM_Inc = [500, 400, 1000, 800, 750]
Info_Inc = [600, 800, 500, 400, 1200]
plt.plot(IBM_Mon, IBM_Inc, 'yd-', label='IBM')
plt.plot(IBM_Mon, Info_Inc, 'gs-', label='INFOSYS')
plt.title('Quart Income')
plt.xlabel("(Month's)")
plt.ylabel("Rupee\n(In Lakhs)")
plt.legend()
plt.show()
