def any_a(string):
    any_a = string.lower().count('a')
    if any_a > 0:
        return f"A letra 'a' ocorre {any_a} vezes"
    else:
        return "A letra 'a' não está presente"
    
texto = input("Escreva uma algo: ")
print(any_a(texto))