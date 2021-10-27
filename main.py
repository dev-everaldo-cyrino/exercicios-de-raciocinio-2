mes = 0
num = 0 
carteira = float(input('quanto você tem inicialmente?: '))
total_investido= 0
rendatotal=0
rendamensal = 0
inv = []
invmes= []
while True:
    print('''----------MENU----------
          1- investir
          2- mostrar carteira
          3- passar tempo
          4- colocar mais dinheiro
          5- sair''')
    print('........................')
    op = int(input('escolha uma opção:  '))
    if op ==5:
        print('--------------programa fechou-----------------')
        break
    if op ==1:
        print('--------------investir-----------------')
        comprar =float(input('preço investido: '))
        rendaum = float(input('quando vai render ao mês (ex:0.3):  '))
        inv.append(comprar)
        invmes.append(rendaum)
        total_investido += comprar
        carteira -= comprar
        print('---------------------------------')
        
    if op ==2:
        print('--------------carteira-----------------')
        print('''
              dinheiro: {:.2f}$ 
              total investido: {:.2f}$
              tempo investido: {}
              renda por mês: {:.2f}$
              total já faturado: {:.2f}$'''
              .format(carteira,total_investido,mes,rendamensal,rendatotal))
        print('---------------------------------')
        
    if op ==3:
        print('--------------passar tempo-----------------')
        mes +=1
        rendamensal=0
        for x in range(len(inv)):
            dinheiro= inv[num] * invmes[num]
            num +=1
            rendatotal +=dinheiro
            rendamensal +=dinheiro
            carteira += dinheiro
        num= 0
        
        print('---------------------------------')
        
    if op ==4:
        print('---------------investir mais dinheiro----------------')
        maisdinheiro= float(input('quanto deseja adicionar: '))
        carteira +=maisdinheiro
        print('''
              o saldo da carteira foi acrescido em {}
              passando de {} para atualmente {}'''
              .format(maisdinheiro,carteira-maisdinheiro,carteira))
        print('---------------------------------')
       

    