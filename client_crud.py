import sys
import Pyro4

PedroRenan = Pyro4.Proxy("PYRONAME:PedroRenan")

try:
    PedroRenan._pyroBind()
except Pyro4.errors.CommunicationError:
    print("Remote Object not found. Closing Execution")
    sys.exit(1)
    pass

op = 1

while op != 5:

    print('Digite:')
    print('1 - Registrar filme Assistido (CREATE)')
    print('2 - Ver Filme (READ)')
    print('3 - Corrigir filme (UPDATE)')
    print('4 - Excluir filme (DELETE)')
    print('5 Sair')

    op = int(input())

    if op >= 1 and op <= 4:

        if op == 1:
            print('id do filme:')
            movie_id = int(input())
            print('Nome do filme:')
            movie_name = input()
            print('Duração do filme (minutos):')
            movie_time = int(input())
            print('Diretor do filme:')
            movie_director = input()
            
            data = {'id':movie_id,'name': movie_name, 'duration': movie_time, 'director': movie_director}
           

            print(PedroRenan.create(data))

        elif op == 3:
            print('id do filme (UPDATE):')
            movie_id = int(input())
            print('Nome do filme (UPDATE):')
            movie_name = input()
            print('Duração do filme (minutos) (UPDATE):')
            movie_time = int(input())
            print('Diretor do filme (UPDATE):')
            movie_director = input()

            data = {'id':movie_id,'name': movie_name, 'duration': movie_time, 'director': movie_director}
    
            print(PedroRenan.update(data))

        elif op == 2:
            print('id do filme:')
            movie_id = int(input())

            print(PedroRenan.read(movie_id))
        
        elif op == 4:
            print('id do filme:')
            movie_id = int(input())

            print(PedroRenan.delete(movie_id))



    elif op == 5:
        print('Exit')

input('aperte enter para encerrar')