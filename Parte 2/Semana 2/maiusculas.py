def maiusculas(frase):
  palavra = ''
  for letra in frase:
    if ord(letra) >= 65 and ord(letra) <= 90:
      palavra += letra
  
  return palavra


def maiusculas2(frase):
  palavra = ''
  for letra in frase:
    if letra.isupper():
      palavra += letra
  
  return palavra
