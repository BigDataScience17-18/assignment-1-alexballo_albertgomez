import matplotlib.pyplot as plt

data_file = open('co2a0000365.txt', 'r')
data_file.readline()



samples=[]
firstline= data_file.readline().split("FP1")
user_id = firstline[0][:3]
voltages = firstline[1][1:-1].split("  ")
voltages.pop()
voltages.pop()

secondline=data_file.readline().split("FP2")
voltages2= secondline[1][1:-1].split("  ")
voltages2.pop()
voltages2.pop()
thirdline=data_file.readline().split("F7")
voltages3= thirdline[1][1:-1].split("  ")
voltages3.pop()
voltages3.pop()

for i in range(len(voltages)):
    samples.append(i+1)
    voltages[i]=float(voltages[i])
    voltages2[i] = float(voltages2[i])
    voltages3[i] = float(voltages3[i])
menor = voltages[0]
for valor in voltages:
    if valor < menor:
        menor = valor
mayor = voltages[0]
for valor in voltages:
    if valor > mayor:
        mayor = valor


plt.axis([0, len(voltages), menor, mayor])
plt.plot(samples,voltages,label="FP1")
plt.plot(samples, voltages2,label="FP2")
plt.plot(samples, voltages3,label="F7")
plt.legend()
plt.xlabel('Samples (number)')
plt.ylabel('Voltage (mV)')
plt.title('Userid: ' + user_id + ', Channel FP1')
plt.grid(True)
plt.show()