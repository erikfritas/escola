from math import *

# x das absissas e y das ordenadas
opt = str(input('Deseja calcular a distancia(A) ou o perimetro(B)? ')).upper()

if opt == 'A':
    xA = int(input("Digite o xA: "))
    yA = int(input("Digite o yA: "))
    xB = int(input("Digite o xB: "))
    yB = int(input("Digite o yB: "))

    xAB = (xB - xA)**2
    yAB = (yB - yA)**2
    xy = xAB + yAB

    dAB = sqrt(xy)
    lt = str(input('Digite as letras: ')).upper()
    print('rz = raiz quadrada')
    print('** = potencia(elevado)')

    print(f"d{lt} = rz[(xB - xA)**2 + (yB - yA)**2]")
    print(f"d{lt} = rz[({xB} - {xA})**2 + ({yB} - {yA})**2]")
    print(f"d{lt} = rz[{xAB} + {yAB}]")
    print(f"d{lt} = rz[{xy}]")
    print(f"d{lt} = {dAB}")
elif opt == 'B':
    xA = int(input("Digite o xA: "))
    yA = int(input("Digite o yA: "))
    xB = int(input("Digite o xB: "))
    yB = int(input("Digite o yB: "))
    xA2 = int(input("Digite o xA2: "))
    yA2 = int(input("Digite o yA2: "))
    xB2 = int(input("Digite o xB2: "))
    yB2 = int(input("Digite o yB2: "))
    xA3 = int(input("Digite o xA3: "))
    yA3 = int(input("Digite o yA3: "))
    xB3 = int(input("Digite o xB3: "))
    yB3 = int(input("Digite o yB3: "))

    xAB = (xB - xA) ** 2
    yAB = (yB - yA) ** 2
    xy = xAB + yAB

    dAB = sqrt(xy)

    xAB2 = (xB2 - xA2) ** 2
    yAB2 = (yB2 - yA2) ** 2
    xy2 = xAB2 + yAB2

    dAB2 = sqrt(xy2)

    xAB3 = (xB3 - xA3) ** 2
    yAB3 = (yB3 - yA3) ** 2
    xy3 = xAB3 + yAB3

    dAB3 = sqrt(xy3)
    lt = str(input('Digite as letras 1 e 2: ')).upper()
    lt2 = str(input('Digite as letras 2 e 3: ')).upper()
    lt3 = str(input('Digite as letras 1 e 3: ')).upper()
    print('rz = raiz quadrada')
    print('** = potencia(elevado)')

    print(f"d{lt} = rz[(xB - xA)**2 + (yB - yA)**2]")
    print(f"d{lt} = rz[({xB} - {xA})**2 + ({yB} - {yA})**2]")
    print(f"d{lt} = rz[{xAB} + {yAB}]")
    print(f"d{lt} = rz[{xy}]")
    print(f"d{lt} = {dAB}")

    print(f"d{lt2} = rz[({xB2} - {xA2})**2 + ({yB2} - {yA2})**2]")
    print(f"d{lt2} = rz[{xAB2} + {yAB2}]")
    print(f"d{lt2} = rz[{xy2}]")
    print(f"d{lt2} = {dAB2}")

    print(f"d{lt3} = rz[({xB3} - {xA3})**2 + ({yB3} - {yA3})**2]")
    print(f"d{lt3} = rz[{xAB3} + {yAB3}]")
    print(f"d{lt3} = rz[{xy3}]")
    print(f"d{lt3} = {dAB3}")

    perimetro = dAB + dAB2 + dAB3
    print(f'perimetro = {dAB} + {dAB2} + {dAB3}')
    print(f'perimetro = {perimetro}')
