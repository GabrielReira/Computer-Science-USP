segundos = int(input('Digite o valor em segundos: '))

horas = segundos // (60 * 60)
segundos_restantes = segundos - (horas * 60 * 60)

minutos = segundos_restantes // 60
segundos_finais = segundos_restantes - (minutos * 60)

print(horas, 'horas,', minutos, 'minutos e', segundos_finais, 'segundos.')


# RESOLUÇÃO DO PROFESSOR
segundos_str = input("Entre com o número de segundos: ")
total_segs = int(segundos_str)

horas = total_segs // 3600
segs_restantes = total_segs % 3600

minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(horas, "horas,", minutos, "minutos e", segs_restantes_final, "segundos.")