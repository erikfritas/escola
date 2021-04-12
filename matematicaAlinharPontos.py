# Alinhar pontos
# se os pontos são colineares ou se eles estão alinhados

print("OBS: Calcular com letras em fase de testes")
print("por favor considere escolher a opção 'A' ")
optLN = str(input("Equação com normal(A) ou letra(B)? ")).upper()

if optLN == "A":
    opt = str(input("Calcular se estão alinhados(A) ou se é um triangulo(B)? ")).upper()

    if opt == "A":
        xa = int(input("Digite o xA: "))
        ya = int(input("Digite o yA: "))
        xb = int(input("Digite o xB: "))
        yb = int(input("Digite o yB: "))
        xc = int(input("Digite o xC: "))
        yc = int(input("Digite o yC: "))

        resD1 = xa * yb
        resD2 = xb * yc
        resD3 = xc * ya
        resD = resD1 + resD2 + resD3

        resE1 = ya * xb
        resE2 = yb * xc
        resE3 = yc * xa
        resE = resE1 + resE2 + resE3

        res = resD - resE

        print("")
        print(f"\t|\t{xa}\t{ya}\t|\t")
        print(f"{resE1}\t|\t{xb}\t{yb}\t|\t{resD1}")
        print(f"{resE2}\t|\t{xc}\t{yc}\t|\t{resD2}")
        print(f"{resE3}\t|\t{xa}\t{ya}\t|\t{resD3}")
        print(f"__\t\t\t\t\t__")
        print(f"{resE}\t\t\t\t\t{resD} ")
        print("")

        if resE < 0:
            fresE = resE * -1
            print(f"   {resD} + {fresE} = {res}    ")
        else:
            print(f"   {resD} - {resE} = {res}    ")

        if res == 0:
            print("estão alinhados, pois o resultado é zero")
        else:
            print("não estão alinhados, pois o resultado não é zero")

    # ========================

    elif opt == "B":
        xa = int(input("Digite o xA: "))
        ya = int(input("Digite o yA: "))
        xb = int(input("Digite o xB: "))
        yb = int(input("Digite o yB: "))
        xc = int(input("Digite o xC: "))
        yc = int(input("Digite o yC: "))

        resD1 = xa * yb
        resD2 = xb * yc
        resD3 = xc * ya
        resD = resD1 + resD2 + resD3

        resE1 = ya * xb
        resE2 = yb * xc
        resE3 = yc * xa
        resE = resE1 + resE2 + resE3

        res = resD - resE

        print("")
        print(f"\t|\t{xa}\t{ya}\t|\t")
        print(f"{resE1}\t|\t{xb}\t{yb}\t|\t{resD1}")
        print(f"{resE2}\t|\t{xc}\t{yc}\t|\t{resD2}")
        print(f"{resE3}\t|\t{xa}\t{ya}\t|\t{resD3}")
        print(f"__\t\t\t\t\t__")
        print(f"{resE}\t\t\t\t\t{resD} ")
        print("")

        if resE < 0:
            fresE = resE * -1
            print(f"   {resD} + {fresE} = {res}    ")
        else:
            print(f"   {resD} - {resE} = {res}    ")

        if res == 0:
            print("não é um triângulo, pois o resultado é zero")
        else:
            print("é um triângulo, pois o resultado é diferente de zero")

# ============

# Calcular com letras em fase de testes

# ============
elif optLN == "B":
    opt = str(input("Calcular se estão alinhados(A) ou se é um triangulo(B)? ")).upper()

    if opt == "A":
        print("OBS:")
        print("xA yA")
        print("xB yB")
        print("xC yC")
        letra = str(input("Onde fica a letra? ")).upper()

        letras = []
        numeros = []

        if letra == "XA":
            xa = str(input("Digite o xA: "))
            letras.append(xa)
        else:
            xa = int(input("Digite o xA: "))
            numeros.append(xa)
        if letra == "YA":
            ya = str(input("Digite o yA: "))
            letras.append(ya)
        else:
            ya = int(input("Digite o yA: "))
            numeros.append(ya)
        if letra == "XB":
            xb = str(input("Digite o xB: "))
            letras.append(xb)
        else:
            xb = int(input("Digite o xB: "))
            numeros.append(xb)
        if letra == "YB":
            yb = str(input("Digite o yB: "))
            letras.append(yb)
        else:
            yb = int(input("Digite o yB: "))
            numeros.append(yb)
        if letra == "XC":
            xc = str(input("Digite o xC: "))
            letras.append(xc)
        else:
            xc = int(input("Digite o xC: "))
            numeros.append(xc)
        if letra == "YC":
            yc = str(input("Digite o yC: "))
            letras.append(yc)
        else:
            yc = int(input("Digite o yC: "))
            numeros.append(yc)

        if type(xa) is str:
            print("xa = str")
            fxa = 0
        else:
            fxa = xa
        if type(ya) is str:
            print("ya = str")
            fya = 0
        else:
            fya = ya
        if type(xb) is str:
            print("xb = str")
            fxb = 0
        else:
            fxb = xb
        if type(yb) is str:
            print("yb = str")
            fyb = 0
        else:
            fyb = yb
        if type(xc) is str:
            print("xc = str")
            fxc = 0
        else:
            fxc = xc
        if type(yc) is str:
            print("yc = str")
            fyc = 0
        else:
            fyc = yc

        resD1 = fxa * fyb
        resD2 = fxb * fyc
        resD3 = fxc * fya
        resE3 = fyc * fxa
        resE1 = fya * fxb
        resE2 = fyb * fxc
        resD = resD1 + resD2 + resD3
        resE = resE1 + resE2 + resE3

        res1 = resD - resE

        if letra == "YA":
            vresD3 = f"{fxc}{ya}"
            vresE1 = f"{fxb}{ya}"

            print("")
            print(f"\t|\t{xa}\t{ya}\t|\t")
            print(f"{vresE1}\t|\t{xb}\t{yb}\t|\t{resD1}")
            print(f"{resE2}\t|\t{xc}\t{yc}\t|\t{resD2}")
            print(f"{resE3}\t|\t{xa}\t{ya}\t|\t{vresD3}")
            print(f"__\t\t\t\t\t__")
            print(f"{resE}\t\t\t\t\t{resD} ")
            print("")

            if resE > 0:
                fresE = resE * -1
                teste = True
                if teste:
                    print(f"   {resD} - {vresE1} - ({resE} + {vresE1}) = 0    ")
                    print(f"   {resD} - {vresE1} - {resE} - {vresD3} = 0")
                    vresL = -xb+xc
                    vresL2 = vresL * -1
                    print(f"   {vresL}{ya} = {res1}")
                    print(f"   {ya} = {res1}")
                    print(f"\t\t----")
                    print(f"\t\t {vresL2}")
                    resFinal = res1/vresL2
                    print(f"   {ya} = {resFinal}")
            else:
                print(f"else")

        elif letra == "XC":
            vresE2 = f"{fyb}{xc}"
            vresD3 = f"{fya}{xc}"

            var = xc

            print("")
            print(f"\t|\t{xa}\t{ya}\t|\t")
            print(f"{resE1}\t|\t{xb}\t{yb}\t|\t{resD1}")
            print(f"{vresE2}\t|\t{xc}\t{yc}\t|\t{resD2}")
            print(f"{resE3}\t|\t{xa}\t{ya}\t|\t{vresD3}")
            print(f"__\t\t\t\t\t__")
            print(f"{resE}\t\t\t\t\t{resD} ")
            print("")

            if resE > 0:
                fresE = resE * -1
                teste = True
                if teste:
                    print(f"   {resD} + {var} - ({resE} - {var}) = 0    ")
                    print(f"   {resD} + {var} - {resE} + {var} = 0")
                    vresL = yb + ya*-1
                    print(f"   {vresL}{var} = {res1}")
                    print(f"   {var} = {res1}")
                    print(f"\t\t----")
                    print(f"\t\t {vresL}")
                    resFinal = res1 / vresL
                    print(f"   {var} = {resFinal}")
            else:
                print(f"else")

        if res1 == 0:
            print("estão alinhados, pois o resultado é zero")
        else:
            print("não estão alinhados, pois o resultado não é zero")

    # ========================

    elif opt == "B":
        xa = int(input("Digite o xA: "))
        ya = int(input("Digite o yA: "))
        xb = int(input("Digite o xB: "))
        yb = int(input("Digite o yB: "))
        xc = int(input("Digite o xC: "))
        yc = int(input("Digite o yC: "))

        resD1 = xa * yb
        resD2 = xb * yc
        resD3 = xc * ya
        resD = resD1 + resD2 + resD3

        resE1 = ya * xb
        resE2 = yb * xc
        resE3 = yc * xa
        resE = resE1 + resE2 + resE3

        res = resD - resE

        print("")
        print(f"\t|\t{xa}\t{ya}\t|\t")
        print(f"{resE1}\t|\t{xb}\t{yb}\t|\t{resD1}")
        print(f"{resE2}\t|\t{xc}\t{yc}\t|\t{resD2}")
        print(f"{resE3}\t|\t{xa}\t{ya}\t|\t{resD3}")
        print(f"__\t\t\t\t\t__")
        print(f"{resE}\t\t\t\t\t{resD} ")
        print("")

        if resE < 0:
            fresE = resE * -1
            print(f"   {resD} + {fresE} = {res}    ")
        else:
            print(f"   {resD} - {resE} = {res}    ")

        if res == 0:
            print("não é um triângulo, pois o resultado é zero")
        else:
            print("é um triângulo, pois o resultado é diferente de zero")



