from tkinter import *

root = Tk()  # cria a janela do programa


class Application():
    def __init__(self):
        self.root = root  # faz uma equivalencia porque o root nao ta dentro da class
        self.tela()  # inicializa a def tela
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()  # cria o loot para a janela do programa nao fechar

    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.configure(background='#062530')
        self.root.geometry("700x500")  # Horizontal x Vertical
        # Vai permitir mecher no tamanho da tela em X ou em Y
        self.root.resizable(True, True)
        # dita o tamanho maximo da tela
        self.root.maxsize(width=900, height=700)
        # dita o tamanho minimo da tela
        self.root.minsize(width=400, height=300)

    def frames_da_tela(self):
        # os locais aonde vao aparecer os botoes e as exibições(2 retangulos na tela)
        # bd BORDA, bg COR FUNDO, highlightbackground CorDaBorda, highlightthickness TAMANHO BORDA
        self.frame_1 = Frame(self.root, bd=1, bg='#0a4257',
                             highlightbackground='#113642',
                             highlightthickness='3')
        # POSICIONAR O FRAME relxy 0 seria 0% e 1 seria 100%, esquerda para direita, cima para baixo
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        # bd BORDA, bg COR FUNDO, highlightbackground CorDaBorda, highlightthickness TAMANHO BORDA
        self.frame_2 = Frame(self.root, bd=1, bg='#0a4257',
                             highlightbackground='#113642',
                             highlightthickness='3')
        # POSICIONAR O FRAME relxy 0 seria 0% e 1 seria 100%, esquerda para direita, cima para baixo
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.48)

    def widgets_frame1(self):
        # Botão Limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar')
        self.bt_limpar.place(relx=0.256, rely=0.1,
                             relwidth=0.1, relheight=0.15)
        # Botão Buscar
        self.bt_limpar = Button(self.frame_1, text='Buscar')
        self.bt_limpar.place(relx=0.153, rely=0.1,
                             relwidth=0.1, relheight=0.15)
        # Botão Novo
        self.bt_limpar = Button(self.frame_1, text='Novo')
        self.bt_limpar.place(relx=0.05, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão Alterar
        self.bt_limpar = Button(self.frame_1, text='Alterar')
        self.bt_limpar.place(relx=0.65, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão Apagar
        self.bt_limpar = Button(self.frame_1, text='Apagar')
        self.bt_limpar.place(relx=0.753, rely=0.1,
                             relwidth=0.1, relheight=0.15)


Application()  # chama a class
