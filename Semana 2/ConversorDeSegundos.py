segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = segundos // (60 * 60 * 24)
segundos_restantes1 = segundos % (60 * 60 * 24)

horas = segundos_restantes1 // (60 * 60)
segundos_restantes2 = segundos % (60 * 60)

minutes = segundos_restantes2 // 60
segundos_finais = segundos_restantes2 % 60

print(dias, 'dias,', horas, 'horas,', minutes, 'minutos e', segundos_finais, 'segundos.')