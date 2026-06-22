print("\n     /\\     ")
print("    /  \\    ")
print("   /    \\   ")
print("  /      \\  ")
print(" /        \\ ")
print("/__________\\ \n \n")

print("    ▜     ▜    ▌         ▄ ")
print("▛▘▀▌▐ ▛▘▌▌▐ ▀▌▛▌▛▌▛▘▀▌  ▖▌▌")
print("▙▖█▌▐▖▙▖▙▌▐▖█▌▙▌▙▌▌ █▌  ▖▙▘ \n \n")



print("insira um numero")
num = int(input())
print("insira uma operacao ( +, - , * , / )")
op = input()
#while op not in ["+", "-", "*", "/"]: #isso aq diz "enquanto a operacao nao for as que eu dei, repetir o "insira uma operacao" "
#   print("operacao invalida, porfavor coloque uma valida")
#   print("insira uma operacao ( +, - , * , / )")
#   op = input()
print("insira outro numero")
num2 = int(input())

print("resultado:")
if op == "+":
    print(num + num2)
elif op == "-":
    print(num - num2)
elif op == "*":
    print(num * num2)
elif op == "/":
    print(num / num2)
