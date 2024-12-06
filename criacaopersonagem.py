import time


iniciaounao = input('Seja bem vindo a um mundo imenso, onde você poderá viver imensas fan-tasias o que você sempre quis viver, divirta-se com seus amigos e    construa o seu melhor psêudonimo está pronto?(sim/não)')
iniciaounao = iniciaounao.upper
def iniciaounaof():
    if iniciaounao in ('NAO','NÃO'):
        print('Que pena, caso queira jogar outra hora é só me chamar, mas até lá, tchau :)')
    elif iniciaounao == 'SIM':
        print(criacaodepersonagem)    
    else:
        iniciaounao =input('Por favor digite algo que esteja dentro dos parametros de sim ou não')
        iniciaounaof()
def criacaodepersonagem():
    print('Ótimo já que você pode jogar agora o que acha de começarmos preenchendo sua ficha?')
    print('Eu pensei em fazermos uma dinâmica aonde eu irei pedir para você me responder e eu preencho sua ficha aqui ok?')
    normalnao = input('Você, já tem em mente o que você querpara o seu personagem, caso não tenha eu vou seguir uma ordem diferente da que eu usaria do que com quem já sabe, faça o favor de responder com sim ou não')
    if normalnao in ('nao','não'):
        print(criacaopersonagemsemnadaemmente())
    elif normalnao == 'sim':
        print(criacaopersonagemnormal())
    else:
        print('Por favor escreva algo entre sim ou não.')
    def criacaopersonagemsemnadaemmente():
        print()