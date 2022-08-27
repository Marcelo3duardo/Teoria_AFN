#   $ - movimento vazio
#   Os estados finais vao ser definidos dentro de uma lista  
from asyncio.windows_events import NULL
from imp import NullImporter
from turtle import pos


def LerArquivo(nomeArquivo):
    
    try:
        arquivoArray = open(nomeArquivo, 'r')
        return arquivoArray  # retorna uma lista str com os números

    except:
        print('Erro de abertura do arquivo: ' + nomeArquivo)
        return


def organizarArray(nomeArquivo):
    #lista = LerArquivo(nomeArquivo).readline().split('|')
    #print(LerArquivo(nomeArquivo).readline())
    strLista = LerArquivo(nomeArquivo).readlines() #.split('\n')
    listaDoAlfabeto = [] #lista do alfabeto
   
    #depois de separa por '|' -> eh retirado o primeiro termo
    # formato: a,b|c,d 
    #lista.split('|')
    
    #lista.remove('\n')                                # Remove o símbolo vazio
    
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
            #print(strLista[i][0],' & ',strLista[i][j][0],' -> ',strLista[i][j][k], '\n')
            #       Estado Qx leu 'a' -> {Qy,Qz}
            
            listaDoAlfabeto += listarAlfabeto(strLista[i][j][0])
            listaDoAlfabeto = list(set(listaDoAlfabeto))
    
    print('lista do Alfabeto -> ',listaDoAlfabeto)
    '''print('Estados disponíveis')
    for i in range(0, len(strLista)):
        print(strLista[i][0])'''
    #selecionando estados finais
    #       estadosFinais =  input('escolha os estados finais [qx,qy]: \n').split(',')
    #       print(estadosFinais)
    
    # testando Computação vazia
    '''
    começando os testes
    
    sempre inicia no Q1
    '''
    VetorDoEstado = 0 # testando
    print('inicial ', strLista[VetorDoEstado][0] )
    listaEstados = [strLista[0][0]]
    listaEstados = ExecVazio(VetorDoEstado,strLista)
    
    #listaEstados.append([(strLista[VetorDoEstado][0])]) 
    
    #print('lista de estados -->> ', listaEstados, '\n \n')
    # Organizando lista de estados
    vetores = []
    for i in range(0,len(listaEstados)):
        vetores += listaEstados[i]
    
    vetores = list(set(vetores)) # Retirando repetições
    # transformando em posições
    #print('############## vetores dos estados',vetores)
    '''
    leu a primeira transição vazia
    
    '''
    
    
    coordenadasEstados = transfCordEstado(vetores,strLista)
    #coordenadasEstados = transfCordEstado(listaEstados,strLista)
    #print('coordenadas dos estados',coordenadasEstados)
    
    '''
    Testando para um elemento
    
    '''
    
    nomeElemento = 'a' # provisório ainda falta a lista com os elementos 
    #print ('testando elemento a ')
    EstadosExecutados = ExecEstado(coordenadasEstados,nomeElemento,strLista)
    print('\n \n##### estados executados --->', EstadosExecutados)
    vetoresExecutados = []
    for i in range(0,len(EstadosExecutados)):
            vetoresExecutados += listaEstados[i]
   
    #chama mais uma vez a transição vazia agora para os estados executados 
    listPosEst2 = transfCordEstado(vetoresExecutados,strLista)
    print('\n \n listPosEst2 --->',listPosEst2,'\n \n')
    
    '''
    Segunda execução do vazio
    '''
    
    listaSegExecVazio = []
    for a in range(0,len(listPosEst2)):
        
        listaSegExecVazio.append( ExecVazio(listPosEst2[a],strLista))#(pos, lista)
        #listaSegExecVazio += ExecVazio(listPosEst2[a],strLista)
    
    #print('listaSegExecVazio --->>>', listaSegExecVazio)
                    
    return strLista  # retorna a lista em formato de inteiros

def listarAlfabeto(elemento):
    if elemento != '$':
        return elemento
    return ''
    
    
    

def ExecEstado(coordenadasEstados,nomeElemento,strLista):
    EstadosTest = []    #armazena os estados apontados
    for aux in range(0,len(coordenadasEstados)):
       
        coordenadasElementos = transfCordElementos(coordenadasEstados[aux],nomeElemento,strLista)
        print('coordenadas elementos ',coordenadasElementos)
        for aux2 in range(0,len(coordenadasElementos)):
            #vai pegar os próximos estados
            
            #print(coordenadasEstados[aux],'----',coordenadasElementos[aux2][1])
            EstadosTest.append(strLista[coordenadasEstados[aux]][coordenadasElementos[aux2]][1])
            
    print('Estados Teste',EstadosTest)
    return EstadosTest

def transfCordEstado(vetores,strLista):
    coordenadas = set()
    for aux1 in range(0,len(vetores)): 
        for aux2 in range(0,len(strLista)):
            #print(vetores[aux1], ' == '  ,strLista[aux2][0])
            if vetores[aux1] == strLista[aux2][0]:
                coordenadas.append(int(aux2))
    return coordenadas

def transfCordElementos(coordenadaEstado,nomeElemento,strLista):
    coordenadasElementos = []
    for aux in range(1,len(strLista[coordenadaEstado])):
        #print('trans form elem 1 |-> ',aux,' ^^', strLista[coordenadaEstado][aux][0])
        if strLista[coordenadaEstado][aux][0] == nomeElemento :
            #print('trans form elem 2', strLista[coordenadaEstado][aux][0])
            coordenadasElementos.append(int(aux))
    return coordenadasElementos

def ExecVazio(VetorDoEstado,strLista):
    vazioVai =  ProcurarTransicaoVazias(VetorDoEstado,strLista)
    #print('vetor 001  - ',vazioVai)
    vazioVai = PercorrerVazios(vazioVai,strLista) + vazioVai
    #print('\n \n')
    vazioVai.append([strLista[VetorDoEstado][0]]) # adicionando o nó da raiz
    #print('vetor fina retorna do vazio:  ',vazioVai)
    lisAux = []
    for i in range(0,len(vazioVai)):
        lisAux += vazioVai[i]
    print('vetorAux fina retorna do vazio ->:  ',lisAux) 
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
    proxEstados = set()
    seEntrouAux = proxEstados.copy()
    proxEstadosAux = []

    #print('tamanho da lista passada para percorrer o vazio => ',len(listaEstados))
    for aux in range(0,len(listaEstados)):
        for numEstados in range(0,len(strLista)):
            #print('vetor => ',aux,'  ',listaEstados[aux][0], ' == ', strLista[numEstados][0])
            if listaEstados[aux][0] == strLista[numEstados][0]:
                #procurar pela transição vazia
                #proxEstados.append(ProcurarTransicaoVazias(numEstados,strLista))
                #print( '555555555 funcao entrega procurar <<->>',ProcurarTransicaoVazias(numEstados,strLista))
               
                proxEstados += ProcurarTransicaoVazias(numEstados,strLista)
                #proxEstados = list(set(proxEstados))
                
                #print('55555555555555 Dentro do if ------->', proxEstados)
                
                #proxEstados.append(vazioAponta)
    #print('tam. ant ',seEntrouAux, ' != ', 'tam desp. ',(proxEstados))
    if len(seEntrouAux) != len(proxEstados) :
        print('lista da segunda entrada p1 =>>> ',proxEstados)
        #PercorrerVazios(proxEstados,strLista)
        proxEstados += PercorrerVazios(proxEstados,strLista)
        print( 'funcao entrega <<->>',PercorrerVazios(proxEstados,strLista))
        
        print('lista da segunda entrada p2 =>>> ',proxEstados)
    return proxEstados
        

    
nomeArquivo = 'teste'
print( organizarArray(nomeArquivo))
