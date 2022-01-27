import time

hora_atual = time.time()

dias = hora_atual // 24
horas = hora_atual - dias * 24
minutos = (horas - int(horas)) * 60
segundos = (minutos - int(minutos)) * 60

print(f'Tempo total passado: {int(dias)} dias, {int(horas)}' 
    f'horas : {int(minutos)} minutos : {int(segundos)} segundos.')
