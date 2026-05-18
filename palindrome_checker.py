str1 = input("Digite uma frase ou palavra: ").lower()

symbols_table = str.maketrans(
    "áàãâéèêíìîóòõôúùûç", "aaaaeeeiiioooouuuc", " !@#$%:;,.><-_"
)

str1 = str1.translate(symbols_table)

if str1 == str1[::-1]:
    print("É palindromo!")
else:
    print("Não é palindromo!")