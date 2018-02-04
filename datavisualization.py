import matplotlib.pyplot as plt

data_file = open('co2a0000365.txt', 'r')
data_file.readline()

samples=[]
firstline= data_file.readline().split("FP1")
user_id = firstline[0][:3]
voltages = firstline[1][1:-1].split("  ")
voltages.pop()
voltages.pop()
for i in range(len(voltages)):
    samples.append(i+1)
    voltages[i]=float(voltages[i])

menor = voltages[0]
for valor in voltages:
    if valor < menor:
        menor = valor
mayor = voltages[0]
for valor in voltages:
    if valor > mayor:
        mayor = valor

plt.plot(samples, voltages, 'ro')
plt.axis([0, len(voltages), menor, mayor])


plt.xlabel('Samples (number)')
plt.ylabel('Voltage (mV)')
plt.title('Userid: ' + user_id + ', Channel FP1')
plt.grid(True)
plt.show()