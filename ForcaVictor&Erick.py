def main():
    task = '0'
    while True:
        clearScreen()

        # define a ação escolida
        if task == '9':
            break
        elif task == '0':
            viweMenu()
        elif task == '1':
            task = startMenuConfig()
            continue
        elif task == '2':
            if getTotalInLista() > 0:
                task = startMenuJogo()
                continue
            else:
                viweMenu()
                viweAlet('Configure o jogo primeiro.')
        else:
            viweMenu()
            viweAlet('Valor Inválido.')

        task = input("Digite: ")


# --------------------- viwe(s) ---------------------

def viweMenu():
    print('*           JOGO DA FORCA           *')
    print('*                                   *')
    print('* (1) Configuração                  *')
    print('* (2) Jogar                         *')
    print('* (9) Sair                          *')
    print('                                     ')


def viweMenuConfig():
    print('*           CONFIGURAÇÃO            *')
    print('*                                   *')
    print('* (1) Adicionar palavras            *')
    print('* (2) Limpar palavras               *')
    print('* (3) Ver quantidade de palavras    *')
    print('* (9) Concluir configuração         *')
    print('                                     ')


def viweMenuJogo():
    print('*              FORCA                *')
    print('*                                   *')
    print('* (8) Reiniciar                     *')
    print('* (9) Voltar ao menu                *')
    print('*                                   *')
    print('* JOGO >>>>>>>>>>>>>>>>>>>>>>>>>>>> *')
    print('*                                   *')


def viweSubmenuAddPalavra():
    print('*         ADICIONAR PALAVRAS        *')
    print('*                                   *')
    print('* (9) Voltar para Configuração      *')
    print('*                                   *')
    print('* REGRAS >>>>>>>>>>>>>>>>>>>>>>>>>> *')
    print('* 1. Apenas letras e espaços        *')
    print('* 2. Máximo de 20 carácteres        *')
    print('* 3. Minimo de 3 carácteres         *')
    print('* 4. Não pode paralavras repetidas  *')
    print('*                                   *')


def viweSubmenuVerLista():
    print('*         LISTA DE PALAVRAS         *')
    print('*                                   *')
    print('* (9) Voltar para Configuração      *')
    print('*                                   *')
    print('* LISTA  >>>>>>>>>>>>>>>>>>>>>>>>>> *')
    print('*                                   *')
    print('* TOTAL: ' + str(getTotalInLista()) + ((27 - (len(str(getTotalInLista())))) * ' ') + '*')
    print('*                                   *')

    lines = getAllLista(True)
    for index in range(0, len(lines)):
        line = escondePalavraForca(decrypt(lines[index]), '')
        print(('* ' + str(index + 1) + '. ') + line + (((32 - len(str(index + 1))) - (len(line))) * ' ') + '*')
    print('*                                   *')


def viweWin():
    print('*                                   *')
    print('*            YOU WON                *')
    print('*                                   *')
    print('*                                   *')


def viweLose(palavra):
    print('* R: ' + palavra + ((31 - (len(palavra))) * ' ') + '*')
    print('*                                   *')
    print('*            YOU LOSE               *')
    print('*                                   *')
    print('*                                   *')


def viweAlet(mensagem):
    print("Atenção: " + mensagem, end='\n\n')


def viweBoneco(erros):
    if erros < 0:
        erros = 0
    elif erros > 6:
        erros = 6
    erros -= 1

    partes = [
        '*  |        O                       *',
        '*  |        |                       *',
        '*  |       <|                       *',
        '*  |       <|>                      *',
        '*  |       /                        *',
        '*  |       / \\                      *',
    ]
    niveis = [
        partes[0],
        partes[0] + '\n' + partes[1],
        partes[0] + '\n' + partes[2],
        partes[0] + '\n' + partes[3],
        partes[0] + '\n' + partes[3] + '\n' + partes[4],
        partes[0] + '\n' + partes[3] + '\n' + partes[5],
    ]
    print('*  __________                       *')
    print('*  |        |                       *')
    if erros == -1:
        print(len(niveis) * '*  |                                *\n', end='')
    else:
        print(niveis[erros])
        print((len(niveis) - erros) * '*  |                                *\n', end='')


def viweForca(palavra, listaDeLetras):
    text = escondePalavraForca(palavra, listaDeLetras)

    print('*  |  ' + text + ((30 - (len(text))) * ' ') + '*')
    print('* _|_                               *')
    print('*                                   *')


# ----------------- start(s) ---------------------

def startMenuConfig():
    task = '0'
    while True:

        clearScreen()
        if task == '9':
            break

        elif task == '0':
            viweMenuConfig()

        elif task == '1':
            task = startSubmenuAddPalavra()
            continue

        elif task == '2':
            createFile(True)
            viweMenuConfig()
            viweAlet('Lista Limpa com sucesso')

        elif task == '3':
            task = startSubmenuVerLista()
            continue

        else:
            viweMenuConfig()
            viweAlet('Valor Inválido.')

        task = input("Digite: ")
    return '0'


def startSubmenuAddPalavra():
    palavra = None
    while True:
        clearScreen()
        viweSubmenuAddPalavra()

        if palavra == '9':
            break

        if palavra is not None:
            if verifyPalavra(palavra):
                addPalavraArquivo(palavra)
                viweAlet('Palavra Adicionada com sucesso')
            else:
                viweAlet('Palavra Inválida, Tente Novamente!')

        palavra = input("Digite um palavra: ")

    return '0'


def startSubmenuVerLista():
    task = '0'
    while True:
        if task == '9':
            break
        else:
            viweSubmenuVerLista()

        task = input("Digite: ")

    return '0'


def startMenuJogo():
    # Definições
    task = '0'
    erros = 0
    listaDeLetras = []
    palavra = getRandomWord()
    exibirMensagem = ''

    while True:
        clearScreen()
        if task == '9':
            break
        elif task == '8':
            task = '0'
            erros = 0
            listaDeLetras = []
            palavra = getRandomWord()
            exibirMensagem = ''

        # Regras ------------------------------
        if erros < 6 or verifyWin(palavra, listaDeLetras):
            if not isnumber(task):

                task = task.strip()
                if len(task) == 1:
                    if task in listaDeLetras:
                        exibirMensagem = 'Digite outra letra.'
                    else:
                        listaDeLetras.append(task.lower())
                        if task not in palavra:
                            erros += 1
                elif len(task) >= 2:
                    if task.lower() == palavra.lower():
                        listaDeLetras = []
                        for letra in palavra:
                            listaDeLetras.append(letra)
                    else:
                        erros = 6

            elif task != '0':
                exibirMensagem = 'Valor Inválido.'
        else:
            exibirMensagem = 'Recomece o jogo'

        # Vizulização do jogo ------------------------------
        viweMenuJogo()
        viweBoneco(erros)
        viweForca(palavra, listaDeLetras)

        # Exibe a Vitória ou Derrota ------------------------------
        if erros >= 6:
            viweLose(palavra)
        elif verifyWin(palavra, listaDeLetras):
            viweWin()

        # Lista de palavras já escritas ------------------------------
        print('Letras já selecionadas: ')
        print(listaDeLetras)

        # Mesagem caso exista ------------------------------
        if exibirMensagem != '':
            viweAlet(exibirMensagem)
            exibirMensagem = ''

        task = input("Digite: ")
    return '0'


# ----------------- config(s) ---------------------

# Limpa a tela
# return boolean
# Ref: https://pt.stackoverflow.com/questions/72678/como-limpar-o-console-no-python
# #:~:text=Simplesmente%20pressione%20ctrl%20%2B%20L%20(funciona,Isso%20no%20terminal.
def clearScreen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


# Verifica se a palavra correta
# text -> string
# return boolean
# Ref:
# https://pt.stackoverflow.com/questions/495114/verificar-se-a-string-s%C3%B3-cont%C3%A9m-letra-e-espa%C3%A7o-em-python
def verifyPalavra(text):
    # Verica se na palavra existe apenas letras ou espaços
    if all(char.isalpha() or char.isspace() for char in text):
        if 20 >= len(text) >= 3:
            if encrypt(text) not in getAllLista(True):
                return True
    return False


# Verifica se é um número
# palavra -> string
# listaDeLetras -> list
# return boolean
# Ref: https://pt.stackoverflow.com/questions/210010/como-verificar-se-o-valor-de-vari%C3%A1vel-string-%C3%A9-numero
def isnumber(number):
    try:
        float(number)
    except ValueError:
        return False
    return True


# Verifica se o usuario venceu
# palavra -> string
# listaDeLetras -> list
# return boolean
def verifyWin(palavra, listaDeLetras):
    text = ''
    for letra in palavra:
        if letra.lower() in listaDeLetras or letra == ' ':
            text += letra

    if text.lower() == palavra.lower():
        return True
    else:
        return False


# texto da forca
def escondePalavraForca(palavra, listaDeLetras):
    text = ''

    for letra in palavra:
        if letra == ' ':
            text += ' '
        elif letra.lower() in listaDeLetras:
            text += letra
        else:
            text += '_'

    return text


# ----------------- File(s) ---------------------

# salva a palavra no arquivo
# text -> string
# return void
def addPalavraArquivo(text):
    # Tratando o texto
    text = text.strip()
    text = encrypt(text)

    # Adiciona +1 na contagem
    modifyContadorAquivo()

    # Adiciona a o texto
    fa = openLista('a')
    fa.write(text + '\n')
    fa.close()


# Adiciona +1 na primeira linha do arquivo
# return void
def modifyContadorAquivo():
    # cria o arquivo se não existir
    createFile(False)

    lines = getAllLista(False)

    fw = openLista('w')

    # Excreve na 1ª linha o proximo valor
    fw.write(str(int(lines[0]) + 1) + "\n")
    del (lines[0])

    # Adiciona o restanmte das linhas
    for line in lines:
        fw.write(line + '\n')
    fw.close()


# Cria o aquivo se não existir ou reseta se pedir
# reset -> boolean
# return void
def createFile(reset):
    import os.path
    
    if (not os.path.isfile('BancoDePalavra.txt')):
        arq = openLista('x')
        arq = openLista('w')
        arq.write('0\n')
        arq.close()
        
    if (reset):
        arq = openLista('w')
        arq.write('0\n')
        arq.close()
        


# Retorna a lista
# type -> string ['r', 'r+', 'w', 'w+', 'a', 'a+']
# return Arquivo
def openLista(type):
    arquivo = 'BancoDePalavra.txt'
    return open(arquivo, type)


# Encripitografia
# text -> string
# return string
def encrypt(text):
    alphabet = 'abcdefghijklmnopqrstuvwyz'
    key = 4
    newText = ''

    text = text.lower()

    for letter in text:
        if letter in alphabet:

            index = alphabet.find(letter)
            index += key
            if index >= len(alphabet):
                index = index % len(alphabet)

            newText += alphabet[index]
        else:
            newText += letter

        newText = (newText.replace('a', '+'))
        newText = (newText.replace('e', '$'))
        newText = (newText.replace('i', '#'))
        newText = (newText.replace('o', '5'))
        newText = (newText.replace('u', '0'))

    return newText[::-1]


# Decripitografia
# text -> string
# return string
def decrypt(text):
    alphabet = 'abcdefghijklmnopqrstuvwyz'
    key = 4
    newText = ''

    text = text.lower()

    text = (text.replace('+', 'a'))
    text = (text.replace('$', 'e'))
    text = (text.replace('#', 'i'))
    text = (text.replace('5', 'o'))
    text = (text.replace('0', 'u'))

    for letter in text:
        if letter in alphabet:
            index = alphabet.find(letter)
            index -= key
            newText += alphabet[index]
        else:
            newText += letter

    return newText[::-1]


# Retorna uma palavra aleatorio da lista de palavras
# return string
def getRandomWord():
    import random

    lines = getAllLista(True)
    x = random.randint(0, (len(lines) - 1))

    return decrypt(lines[x])


# Retorna a quantidade de palavras na lista
# return int
def getTotalInLista():
    lines = getAllLista(False)
    return int(lines[0])


# Busca toda os elemento do arquivo
# deleteCounter -> boolean
# return List
def getAllLista(deleteCounter):
    createFile(False)
    fr = openLista('r')
    lines = fr.readlines()

    if deleteCounter:
        del (lines[0])

    newLines = []
    for line in lines:
        newLines.append((line.strip('\n')))

    return newLines


main()
