# Pra falar a verdade não me lembro o nome deste calculo só sei que a forma de calcula-lo é esse mesmo

# F = K . Q1 . Q2
#     -----------
#         d2

Q1 = int(input("Digite o Q1: "))
Q01 = int(input("Digite o Q01: "))
Q001 = int(input("Digite o Q001: "))
Q2 = int(input("Digite o Q2: "))
Q02 = int(input("Digite o Q02: "))
Q002 = int(input("Digite o Q002: "))

OptD = str(input("Digite a unidade de medidas da distância: (cm ou m) ").upper())
d01 = int(input("Digite a distância: "))

if OptD == "CM":
    d = d01/100
elif OptD == "M":
    d = d01

print("\n Se o K for o padrão (9.10^9) então digite S, caso contrário digite N")
print("Exemplo: \n K01 = 9\nK02 = 10\nK03 = 9\n Resultado = K01 * K02**K03\n traduzido = 9 * 10**9")
K = str(input("K padrão? (S/N) ").upper())

if K == "N":
    K01 = int(input("Digite o K01: "))
    K02 = int(input("Digite o K02: "))
    K03 = int(input("Digite o K03: "))

if K == "S":
    K01 = 9
    K02 = 10
    K03 = 9

Fc1 = (K01 * K02**K03 * Q1 * Q01**Q001 * Q2 * Q02**Q002)
Fc = Fc1 + 0.01
Fb = int(Fc/d**2)

print(f"{Fc:3}\n\n{Fb}")




