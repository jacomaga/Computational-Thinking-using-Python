#salario base, hora-atividade, descanso semanal remunerado
#salario base = numero de aulas semanais por 4,5 semanais e pelo valor hora-aula
#salariobase=numeroaula*4,5*valor-hora
#descansosemanal = salariobase/(1/6)
#hora-atividade = (salariobase+descansosemanal)*0.05
naulassem = int(input("Digite o número de aulas semanais ministradas: "))
valorhoraaula = int(input("Digite o valor da hora da aula: "))
salariobase = naulassem*4.5*valorhoraaula
descansosemanal = salariobase*(1/6)
horaatividade=(salariobase+descansosemanal)*0.05
salariomensal = salariobase+descansosemanal+horaatividade
print(salariomensal)