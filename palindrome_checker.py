str1 = input(str("Digite uma frase ou palavra: ")).lower()

symbols_table = str.maketrans(
    "áàãâéèêíìîóòõôúùûç", "aaaaeeeiiioooouuuc", "!@#$%:;,.><"
)

symbols_table2 = str.maketrans(
    "!@#$%:;,.><", "           "
)

str1 = str1.translate(symbols_table)

str1 = str1.translate(symbols_table2)

str1 = str1.replace(" ","")

str2 = str1[::-1]

if str1 == str2:
    print("É palindromo!")
else:
    print("Não é palindromo!")