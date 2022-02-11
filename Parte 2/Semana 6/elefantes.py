def incomodam(n):
  if n <= 0:
    return ''
  return 'incomodam ' + incomodam(n-1)


def elefantes(n):
  def frase(n):
    return f'\n{n} elefantes {incomodam(n)}muito mais\n{n} elefantes incomodam muita gente'
    
  if n <= 0:
    return ''
  if n == 1:
    return 'Um elefante incomoda muita gente'
  return elefantes(n-1) + frase(n)
