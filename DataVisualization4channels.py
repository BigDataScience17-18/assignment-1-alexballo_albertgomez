import matplotlib.pyplot as plt


def get_voltages(line):

    voltages = line[1:-1].split("  ")
    voltages.pop()
    voltages.pop()
    return voltages


def find_min(value, voltagesChannel):
    for valor in voltagesChannel:
        if valor < value:
            value = valor
    return value


def find_max(value, voltagesChannel):
    for valor in voltagesChannel:
        if valor > value:
            value = valor
    return value


data_file = open('co2a0000365.txt', 'r')
data_file.readline()
samples = []
line = data_file.readline().split("FP1")
user_id = line[0][:3]
voltagesFP1 = get_voltages(line[1])
line = data_file.readline().split("FP2")
voltagesFP2 = get_voltages(line[1])
line = data_file.readline().split("F7")
voltagesF7 = get_voltages(line[1])
line = data_file.readline().split("F8")
voltagesF8 = get_voltages(line[1])

for i in range(len(voltagesFP1)):
    samples.append(i+1)
    voltagesFP1[i] = float(voltagesFP1[i])
    voltagesFP2[i] = float(voltagesFP2[i])
    voltagesF7[i] = float(voltagesF7[i])
    voltagesF8[i] = float(voltagesF8[i])

minor = voltagesFP1[0]
minor = find_min(minor, voltagesFP1)
minor = find_min(minor, voltagesFP2)
minor = find_min(minor, voltagesF7)
minor = find_min(minor, voltagesF8)

mayor = voltagesFP1[0]
mayor = find_max(mayor, voltagesFP1)
mayor = find_max(mayor, voltagesFP2)
mayor = find_max(mayor, voltagesF7)
mayor = find_max(mayor, voltagesF8)

plt.axis([0, len(voltagesFP1), minor, mayor])
plt.plot(samples,voltagesFP1, label="FP1")
plt.plot(samples, voltagesFP2, label="FP2")
plt.plot(samples, voltagesF7, label="F7")
plt.plot(samples, voltagesF8, label="F8")
plt.legend()
plt.xlabel('Samples (number)')
plt.ylabel('Voltage (mV)')
plt.title('Userid: ' + user_id + ', Channels: FP1, FP2, F7, F8')
plt.grid(True)
plt.show()