import os

for x in range(1,10):
    if not os.path.isdir(f'./dec0{x}'):
        os.makedirs(f'./dec0{x}')
for x in range(10,32):
    if not os.path.isdir(f'./dec{x}'):
        os.makedirs(f'./dec{x}')
