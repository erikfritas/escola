# Calculadora de Ponto Medio

script = True
encerrar = False
encerrar_script = False

while True:
    print("\033[m")
    if encerrar:
        if encerrar_script:
            print("eu se fui agora, tiau")
            break
        else:
            script = False
            exitOPT = str(input("Deseja encerrar o script? S/N ")).upper()
            print("\033[m")
            if exitOPT == "S":
                break
            elif exitOPT == "N":
                print("Continuando o script...")
                script = True
            else:
                print(
                    f"To te falano, é (S) ou (N), se vc digitar {exitOPT} de novo, nois vai entra na porrada, e eu num vo arrega pa tu naum...")

    if script:

        xA = int(input("Digite o xA: "))
        yA = int(input("Digite o yA: "))
        xB = int(input("Digite o xB: "))
        yB = int(input("Digite o yB: "))

        xM1 = 0
        xM = 0
        yM1 = 0
        yM = 0

        while True:
            print("\033[m")
            opt1 = str(input("Deseja retornar somente um número inteiro? S/N \033[32m")).upper()
            print("\033[m")
            if opt1 == "S":
                xM1 = xA + xB
                xM = int(xM1 / 2)
                yM1 = yA + yB
                yM = int(yM1 / 2)
            elif opt1 == "N":
                xM1 = xA + xB
                xM = xM1 / 2
                yM1 = yA + yB
                yM = yM1 / 2
            else:
                print(f'É (S) ou (N), {opt1} nem é uma opção seu jumento')
            print("\033[m")
            print(f"\033[32mxM = (xA + xB)/2  \033[35me\033[38m  yM = (yA + yB)/2 \n xM = ({xA} + {xB})/2  \033[35me\033[38m  yM = ({yA} + {yB})/2 \n xM = {xM1}/2  \033[35me\033[38m  yM = {yM1}/2 \n xM = {xM}  \033[35me\033[38m  yM = {yM}")
            opt2 = str(input("Deseja encerrar o script? S/N \033[32m")).upper()
            if opt2 == "S":
                encerrar = True
                encerrar_script = True
                break
            elif opt2 == "N":
                print("Continuando...")
            else:
                print(f"num é {opt2} não seu jegue, é (S) ou (N)")
            print("\033[m")



