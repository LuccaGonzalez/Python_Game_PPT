import tkinter
import random
# import Pillow (não posso dar import Pillow - erro de Pylance)

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# cores -----------------------------------
co0 = "#FFFFFF"     # branco
co1 = "#333333"     # cinza escuro
co2 = "#fcc058"     # laranja
co3 = "#38576b"     # valor
co4 = "#3297a8"      # azul
co5 = "#fff873"      # amarelo
co6 = "#fcc058"     # laranja
co7 = "#e85151"      # vermelha
co8 = "#34eb3d"      # verde
co9 = "#edebeb"     # cinza claro
fundo = "#3b3b3b"
# ------------------------------------------

# configuração da janela
janela = Tk()
janela.title('')
janela.geometry('520x580')
janela.configure(bg=fundo)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# divisão da janela
frameCima = Frame(janela, width=520, height=200, bg=co1, relief='raised') # o atributo pady ia ser usado com a cor: co0, porém, foi deixado com a cor padrão
frameCima.grid(row=0, column=0, sticky=NW)

frameBaixo = Frame(janela, width=520, height=380, bg=co0, relief='flat') # o atributo pady ia ser usado com a cor: co0, porém, foi deixado com a cor padrão
frameBaixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# configurando o frame de cima
app1 = Label(frameCima, text="Você", height=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co2) # Texto: "Você"
app1.place(x=85, y=150)

app1_linha_le = Label(frameCima, text="", height=12, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0) # "Led" lateral esquerdo, para indicar que o player "Você" acertou
app1_linha_le.place(x=0, y=0)

app1_pontos = Label(frameCima, text="0", height=1, anchor='center', font=('Ivy 50 bold'), bg=co1, fg=co0) # pontuação do player: "Você"
app1_pontos.place(x=100, y=50)



app_2p = Label(frameCima, text=":", height=1, anchor='center', font=('Ivy 50 bold'), bg=co1, fg=co0) # Texto: ":" (dois pontos)
app_2p.place(x=250, y=45)



app2 = Label(frameCima, text="PC", height=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co4) # Texto: "PC"
app2.place(x=375, y=150)

app2_linha_ld = Label(frameCima, text="", height=12, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0) # "Led" lateral direito, para indicar que o player "PC" acertou
app2_linha_ld.place(x=515, y=0)

app2_pontos = Label(frameCima, text="0", height=1, anchor='center', font=('Ivy 50 bold'), bg=co1, fg=co0) # pontuação do player: "PC"
app2_pontos.place(x=375, y=50)



app_linha_inf = Label(frameCima, text="", width=70, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0) # "Led" inferior, para indicar empate
app_linha_inf.place(x=0, y=195)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Variáveis globais
global player1
global pc
global rodadas
global pontosPlayer1
global pontosPC

pontosPlayer1 = 0
pontosPC = 0
rodadas = 1

# Função lógica do jogo
def jogar(i):
    global rodadas
    global pontosPlayer1
    global pontosPC


    if rodadas <= 5:
        print(rodadas)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opcoes)
        player1 = i

        # Loop para verificar todas as opções de resultados
        for a in opcoes:
            
            if player1 == a:
                
                if pc == 'Tesoura':
                    print('Você Ganhou')
                    app1_linha_le['bg'] = co8 #led "player 1" fica verde
                    app2_linha_ld['bg'] = co0
                    app_linha_inf['bg'] = co0

                    pontosPlayer1 += 1
                    app1_pontos['text'] = pontosPlayer1

                elif pc == 'Pedra':
                    print('Empate')
                    app_linha_inf['bg'] = co2 #led inferior fica laranja
                    app1_linha_le['bg'] = co0
                    app2_linha_ld['bg'] = co0

                else:
                    print('Você Perdeu')
                    app2_linha_ld['bg'] = co8 #led "pc" fica verde
                    app1_linha_le['bg'] = co0
                    app_linha_inf['bg'] = co0

                    pontosPC += 1
                    app2_pontos['text'] = pontosPC

                lblJogadaPC = Label(frameBaixo, text=pc, height=2, width=12, anchor='center', font=('Ivy 13 bold'), bg=co9, fg=co1)
                lblJogadaPC.place(x=388, y=0)
                print(player1)
                print(pc)

        rodadas = rodadas + 1


        if rodadas == 6:
            
            print('Fim do jogo!')
            if pontosPlayer1 > pontosPC: fimDoJogo(1)
            elif pontosPlayer1 < pontosPC: fimDoJogo(2)
            else: fimDoJogo(0)    


# Função iniciar o jogo
def iniciarJogo():

    global iconPedra, iconPapel, iconTesoura, btIconPedra, btIconPapel, btIconTesoura

    iconPedra = Image.open('icons/Pedra.png')
    iconPedra = iconPedra.resize((85, 85)) #Image.ANTIALIAS
    iconPedra = ImageTk.PhotoImage(iconPedra)
    btIconPedra = Button(frameBaixo, command=lambda: jogar('Pedra'), width=85, image=iconPedra, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    btIconPedra.place(x=80,y=150)


    iconPapel = Image.open('icons/Papel.png')
    iconPapel = iconPapel.resize((85, 85)) #Image.ANTIALIAS
    iconPapel = ImageTk.PhotoImage(iconPapel)
    btIconPapel = Button(frameBaixo, command=lambda: jogar('Papel'), width=85, image=iconPapel, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    btIconPapel.place(x=215,y=150)


    iconTesoura = Image.open('icons/Tesoura.png')
    iconTesoura = iconTesoura.resize((85, 85)) #Image.ANTIALIAS
    iconTesoura = ImageTk.PhotoImage(iconTesoura)
    btIconTesoura = Button(frameBaixo, command=lambda: jogar('Tesoura'), width=85, image=iconTesoura, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    btIconTesoura.place(x=355,y=150)


# Função Terminar o jogo
def fimDoJogo(a):
    
    global resultado
    global cor

    lblFimDoJogo = Label(frameBaixo, text='FIM DO JOGO!', height=1, anchor='center', font=('Ivy 12 bold'), bg=co0, fg=co1)
    lblFimDoJogo.place(x=210,y=35)

    if a == 1: resultado = 'Você Venceu!'; cor = co8
    elif a == 2: resultado = 'PC Venceu!'; cor = co7
    else: resultado = 'Empate'; cor = co3

    lblResultado = Label(frameBaixo, text=resultado, height=1, width=10, anchor='center', font=('Ivy 20 bold'), bg=co0, fg=cor)
    lblResultado.place(x=180,y=60)
    

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Configurando o início do jogo
btStartGame = Button(frameBaixo, command=iniciarJogo, width=40, text='JOGAR', compound=CENTER, bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
btStartGame.place(x=100, y=350)


# Executa a janela
janela.mainloop()