from DubinModel import DubinModel
import pickle
import matplotlib.pyplot as plt

Ts = 0.01
v = 1
rho = 4
x = []
y = []

# 6.3 seconds for 90degree turn with displacement of 4,4
model = DubinModel(Ts, v, rho)
for i in range(1000):
    x1, y1 = model.update(-1)
    x.append(x1)
    y.append(y1)
    # print(str(i) + "," + str(x1) + "," + str(y1))
plt.plot(x, y)
advance = x.index(max(x))
coords = [x[0:advance], y[0:advance]]
with open('90turn', 'wb') as f:
    pickle.dump(coords, f)
plt.show()
