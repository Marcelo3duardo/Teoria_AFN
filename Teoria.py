def LerArquivo(nomeArquivo):
    
    try:
        arquivoArray = open(nomeArquivo, 'r')
        return arquivoArray  # retorna uma lista str com os números

    except:
        print('Erro de abertura do arquivo: ' + nomeArquivo)
        return


def organizarArray(nomeArquivo):
    
    # para ler em matriz vou ter ler linha a linha 
    #formato: a|a,b|c,d 
    
    #lista = LerArquivo(nomeArquivo).readline().split('|')
    #print(LerArquivo(nomeArquivo).readline())
    lista = LerArquivo(nomeArquivo).readlines() #.split('\n')
    
    #lista.split(' ')
    
    
    #depois de separa por '|' -> eh retirado o primeiro termo
    # formato: a,b|c,d 
    #lista.split('|')
    
    #lista.remove('\n')                                # Remove o símbolo vazio
    # Transforma a lista em  lista de inteiro
    
    strLista = list(map(str, lista))
    
    #print(strLista)
    #print (type(strLista[0].split('|')))
    #print(strLista[0].split('|'))
    for i in range(0, len(strLista) - 1):
        strLista[i] = strLista[i][0:-1] #retirar \n
    #print (strLista)
    for i in range(0, len(strLista)):
        strLista[i] =  strLista[i].split('|')
        #print (strLista[i][1])
        #print(type(strLista[i]))
        for j in range(1, len(strLista[i])):
            strLista[i][j] =  strLista[i][j].split('->')
            #print(strLista[i])
            #print(type(strLista[i]))
            print(strLista[i][j])
            #for k in range(1, len(strLista[i][j])):
            k = 1
            strLista[i][j][k] = strLista[i][j][k].split(',')
            print(strLista[i][0],' & ',strLista[i][j][0],' -> ',strLista[i][j][k], '\n')
            #       Estado Qx leu 'a' -> {Qy,Qz}
            #git
            
                
                
        
        
        
    return strLista  # retorna a lista em formato de inteiros


nomeArquivo = 'teste'
print( organizarArray(nomeArquivo))
