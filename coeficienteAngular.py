# Calcular coeficiente angular, se é crescente ou decrescente

xA = int(input('Digite o xA: '))
yA = int(input('Digite o yA: '))
xB = int(input('Digite o xB: '))
yB = int(input('Digite o yB: '))

dABy = yB - yA
dABx = xB - xA
dAB = dABy/dABx

print('\n')
print('m = yB - yA')
print('---------------')
print('m = xB - xA')
print('\n')
print(f'm = {yB} - {yA}')
print(f'-----------------')
print(f'm = {xB} - {xA}')
print('\n')
print(f'm = {dABy}')
print(f'-----------------')
print(f'm = {dABx}')
print('\n')
print(f'm = {dAB}')
if dAB > 0:
    print('reta crescente, pois o resultado é maior que 0')
elif dAB < 0:
    print('reta decrescente, pois o resultado é menor que 0')
elif dABx == 0:
    print('reta perpendicular, pois o xAB é igual a 0')
elif dABy == 0:
    print('reta constante, pois o yAB é igual a 0')
else:
    print('Resultado indefinido')



