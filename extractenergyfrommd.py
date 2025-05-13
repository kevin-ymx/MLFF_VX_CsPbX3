energies = []
i = 1

with open('OSZICAR', 'r') as file:
    for line in file:
        if i < 2001:
            i = i + 1
            continue
        
        line_data = line.strip().split()
        E_data1 = line_data[4]
        E_data2 = E_data1.split(".", "E")
        E_value = int(E_data2[1])/10000
        energies.append(E_value)
        line_data.clear()
        E_data1.clear()
        E_data2.clear()
        E_value.clear()
        i = i + 1
        
print(-1 * sum(energies) / len(energies))