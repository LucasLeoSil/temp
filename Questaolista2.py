with open('Listas/2in.txt', 'r') as file:
    lista = []
    for i in file:
        if i[-1] == "\n":
            lista.append(i[0:-1])
        else:
            lista.append(i)
    
    valor = int(lista.pop(0))
    for i in range(0, valor):
        temp = lista.pop(0)
        number = temp.split(' ')
        tamanho = int(number[0])
        rep = int(number[1])
        esq = 0
        dir = 0
        mov = 0
        for i in range(0,rep):
            li = lista.pop(0)
            rar = li.split(' ')
            if rar[1]== "direito":
                efem = (int(rar[0]))/100
                if efem<=tamanho:
                    if dir+efem>tamanho:
                        dir = efem
                        mov+=1
                    else:
                        dir = dir + efem 
            else:
                efem = (int(rar[0]))/100
                if efem<=tamanho:
                    if esq+efem>tamanho:
                        dir = efem
                        mov+=1
                    else:
                        esq = esq + efem 
        if esq !=0:
            mov+=1
        if dir !=0:
            mov+=1
        print(mov)