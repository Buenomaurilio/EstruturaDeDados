mat = [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]
for l in range(0,5):
    for c in range(0,5):
        mat [l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0,5):
    for c in range(0,5):
        print(f'[{mat [l][c]:^5}]', end='')
    print()    



            