import os

flag = False
i = 0

with open ('XDATCAR') as f:
    for line in f:
        elements = line.strip().split()
    
        if line.startswith('Direct'):
            if int(elements[2]) in [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500,
                                    10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000,
                                    14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500,
                                    19000, 19500, 20000]:
                flag = True
                pos = elements[2]
                continue
            
        if flag == True:
            with open (f'POSCAR_{pos}', 'a') as p:
                p.write(line)
            i += 1
            if i < 135:
                continue
            else:
                flag = False
                i = 0
                
                
new_content =  'CdTe_unitcell\n1\n17.977800    0.000000    0.000000\n0.000000   17.977800    0.000000\n0.000000    0.000000   17.977800\nCs   Pb   Br\n27    27    81\nDirect\n'

for j in [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500,10000, 10500, 11000, 11500, 12000,             12500, 13000, 13500, 14000,14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500,19000,           19500, 20000]:
    j = str(j)
    with open(f'POSCAR_{j}', 'r') as file:
        existing_content = file.read()
        
    with open(f'POSCAR_{j}', 'w') as new_file:
        new_file.write(new_content + existing_content)
        