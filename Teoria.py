#   $ - movimento vazio
#   Os estados finais vao ser definidos dentro de uma lista  
from turtle import pos


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
    strLista = LerArquivo(nomeArquivo).readlines() #.split('\n')
    
    #lista.split(' ')
    
    
    #depois de separa por '|' -> eh retirado o primeiro termo
    # formato: a,b|c,d 
    #lista.split('|')
    
    #lista.remove('\n')                                # Remove o símbolo vazio
    # Transforma a lista em  lista de inteiro
    
    #strLista = list(map(str, lista))
    #print(strLista)
    #print(strLista)
    #print (type(strLista[0].split('|')))
    #print(strLista[0].split('|'))
    for i in range(0, len(strLista) - 1):
        strLista[i] = strLista[i][0:-1] #retirar \n
    #print (strLista)
    for i in range(0, len(strLista)):
        strLista[i] =  strLista[i].split('|')
        #print (strLista)
        #print(type(strLista[i]))
        for j in range(1, len(strLista[i])):
            strLista[i][j] =  strLista[i][j].split('->') # Ex: (a -> Q2) Separando símbolo que aponta pros estados
            #print(strLista[i])
            #print(type(strLista[i]))
            #print(strLista[i][j])
            #for k in range(1, len(strLista[i][j])):
            k = 1
            strLista[i][j][k] = strLista[i][j][k].split(',') # Ex:("q1,q2,q4" --> 'q1','q2','q4') Separando Estados apontados
            print(strLista[i][0],' & ',strLista[i][j][0],' -> ',strLista[i][j][k], '\n')
            #       Estado Qx leu 'a' -> {Qy,Qz}
            #   
    print('Estados disponíveis')
    for i in range(0, len(strLista)):
        print(strLista[i][0])
    #selecionando estados finais
    #       estadosFinais =  input('escolha os estados finais [qx,qy]: \n').split(',')
    #       print(estadosFinais)
    
    # testando Computação vazia
    
    VetorDoEstado = 0
    ExecVazio(VetorDoEstado,strLista)
    
    
    
                    
    return strLista  # retorna a lista em formato de inteiros

def ExecVazio(VetorDoEstado,strLista):
    vazioVai =  ProcurarTransicaoVazias(VetorDoEstado,strLista)
    #print('vetor 001  - ',vazioVai)
    vazioVai = PercorrerVazios(vazioVai,strLista) + vazioVai
    #print('\n \n')
    vazioVai.append([strLista[VetorDoEstado][0]]) # adicionando o nó da raiz
    print('vetor fina retorna do vazio:  ',vazioVai)
    return vazioVai

def ProcurarTransicaoVazias(posEstado,strLista): #recebe a posição do estado
      # testando Computação vazia
    vazioProxEstados = []
    
    for vazia in range (1,len(strLista[posEstado])):
        #print('procurando ',strLista[posEstado][0])
        if strLista[posEstado][vazia][0] == '$': # se for o movimento vazio ele adiciona 
            
            vazioProxEstados.append(strLista[posEstado][vazia][1])   
    
    
    return vazioProxEstados # retorna a lista com os estados que esse vazio aponta
    

def PercorrerVazios(listaEstados,strLista): #lista possui o nome do próprio Estado
    proxEstados = []
    seEntrouAux = proxEstados.copy()

    #print('tamanho da lista passada para percorrer o vazio => ',len(listaEstados))
    for aux in range(0,len(listaEstados)):
        for numEstados in range(0,len(strLista)):
            #print('vetor => ',aux,'  ',listaEstados[aux][0], ' == ', strLista[numEstados][0])
            if listaEstados[aux][0] == strLista[numEstados][0]:
                #procurar pela transição vazia
                #proxEstados.append(ProcurarTransicaoVazias(numEstados,strLista))
                proxEstados += ProcurarTransicaoVazias(numEstados,strLista)
                #print('Dentro do if ------->',numEstados)
                
                #proxEstados.append(vazioAponta)
    #print('tam. ant ',seEntrouAux, ' != ', 'tam desp. ',(proxEstados))
    if len(seEntrouAux) != len(proxEstados) :
        #print('lista da segunda entrada =>>> ',proxEstados)
        #PercorrerVazios(proxEstados,strLista)
        proxEstados += PercorrerVazios(proxEstados,strLista)
    return proxEstados
        
        
                          
            
        
    
nomeArquivo = 'teste'
print( organizarArray(nomeArquivo))
