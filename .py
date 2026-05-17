def contar_vocales(texto):
    
    texto = texto.lower()
    vocales = "aeiouáéíóú"  
    contador = 0
    
    for letra in texto:
        if letra in vocales:
            contador += 1  
            
    return contador

print(contar_vocales("Python es genial"))   
print(contar_vocales("Hola"))