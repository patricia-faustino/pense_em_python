# 42 = n
# x = y = 1
# print(x)
# print(y)
# print(1);
# print(1).
x = 1
y = 2
# print(xy)

# Calculadora
raio = 5
pi = 3.14
volume = (4 / 3) * pi * raio
# print(volume)

valor_capa = 24.95
desconto = 24.95 * (1 - 0.4)
transporte_primeiro = 3
transporte_demais = 0.75
quantidade = 60
valor_total = ((desconto + transporte_primeiro) + ((desconto + transporte_demais) * (quantidade - 1)))
# print(valor_total)


tempo_primeiro_passo = 8 * 60 + 15
tempo_segundo_passo = (7 * 60 + 12) * 3
tempo_terceiro_passo = tempo_primeiro_passo

tempo_total_em_segundos = tempo_primeiro_passo + tempo_segundo_passo + tempo_terceiro_passo
tempo_total_em_minutos = tempo_total_em_segundos / 60
# print(tempo_total_em_minutos)

inicio_hora = 6
inicio_minuto = 52
inicio_mais_total = (inicio_minuto + tempo_total_em_minutos) / 60
total_time_float = inicio_hora + inicio_mais_total
hora_final = int(total_time_float)
minuto_final = int((total_time_float - hora_final) * 60)
print(hora_final, ':', minuto_final)
# print(inicio_mais_total)
