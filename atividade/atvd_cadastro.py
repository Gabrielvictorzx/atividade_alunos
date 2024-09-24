alunos = {}
while True:
    print()
    print(30 * '=', 'MENU' , 30 * '=')
    print('1. Cadastrar Aluno')
    print('2. Calcular media das notas')
    print()
    opcao = input('Digite uma das opções: ')

    if opcao =='1':
        matricula = input('Digite o nome da matricula do aluno: ')
        nome = input('Digite o nome do aluno: ')
        nota1 = float(input('Digite sua nota em matematica: '))
        nota2 = float(input('Digite sua nota em portugues: '))
        nota3 = float(input('Digite sua nota em fisica: '))


        media = (nota1 + nota2+ nota3)/ 3

        alunos[matricula] = {'nome' : nome, 'matematica' : nota1, 'portugues' : nota2, 'fisica' : nota3, 'media' : media}

    elif opcao =='2':
        for chave, dados in alunos.items():
            print(f'Matricula: {chave}, Nome: {dados['nome']}, Matematica: {dados['matematica']}, Portugues: {dados['fisica']}, Fisica: {dados['fisica']}, Media: {dados['media']:.3f}')
