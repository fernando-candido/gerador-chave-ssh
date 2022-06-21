import os



inscritos_recentes = ['Rebeca Karla Damaceno Psicopedagoga', 'pedrinho', 'joaozinho']

with open('inscritos.txt', 'w', newline='') as file:
    for line in inscritos_recentes:
        file.write(line + os.linesep)