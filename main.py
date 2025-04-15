from tkinter import *
from tkinter import ttk
import sqlite3
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image


root = Tk()  # cria a janela do programa

class Relatorios():
    def printCliente(self):
        #chamar o browser
        webbrowser.open("cliente.pdf")
    def gerarRelatorio(self):
        self.c = canvas.Canvas("cliente.pdf")
        #criar uma variavel para cada entry que vai vim pro relatorio
        self.codRelatorio = self.codigo_entry.get()
        self.nomeRelatorio = self.nome_entry.get()
        self.telefoneRelatorio = self.telefone_entry.get()
        self.cidadeRelatorio = self.cidade_entry.get()
        


class Funcs():
    def limpar_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect(
            'projetoclientes.bd')  # conecta e da o nome
        # disse que é pra ficar mais facil e dar uma melhorada
        self.cursor = self.conn.cursor()
        print('Conectando ao BD')

    def desconecta_bd(self):
        self.conn.close()
        print('Desconectando ao BD')

    def montaTabelas(self):
        self.conecta_bd()
        # Criar tabela, not null nao pode ter o campo sem nada,
        # tipos e tamanhos dos campos, primary key alimenta sozinho com numeros
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS projetoclientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit()
        print('Banco de dados criado')
        self.desconecta_bd()

    def variaveis(self):
        # pega os valores e atribui a variavel
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.cidade = self.cidade_entry.get()
        self.telefone = self.telefone_entry.get()

    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(
            """ INSERT INTO projetoclientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_tela()

    def select_lista(self):
        self.listaCliente.delete(*self.listaCliente.get_children())
        self.conecta_bd()
        # pegando os dados do Banco de DADOS
        lista = self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, 
            cidade FROM projetoclientes ORDER BY nome_cliente ASC;  """)
        for i in lista:
            self.listaCliente.insert("", END, values=i)
        self.desconecta_bd()

    def onDoubleClick(self, event):
        # teve que passar o parametro event porque
        # há interação com essa def e ai se vc nao colocar ela nao roda
        self.limpar_tela()
        self.listaCliente.selection()

        for n in self.listaCliente.selection():
            col1, col2, col3, col4 = self.listaCliente.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(
            """ DELETE FROM projetoclientes WHERE cod = ? """, (self.codigo,))
        # passa essa virgula no final do execute para dizer que é uma tupla
        self.conn.commit()
        self.desconecta_bd()
        self.limpar_tela()
        self.select_lista()

    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE projetoclientes SET nome_cliente = ?,
        telefone = ?, cidade = ?
        WHERE cod = ? """, (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_tela()

    def Menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        # criando as variaveis para cada menu bar que for colocar
        filemenu1 = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()
        # aqui diz que opções vai estar dentro de filemenu
        menubar.add_cascade(label="Opções", menu=filemenu1)
        menubar.add_cascade(label='Sobre', menu=filemenu2)
        # comand é pra ir adicioanndo as opções dentro do menu
        filemenu1.add_command(label="Sair", command=Quit)
        filemenu1.add_command(label="Limpa Cliente", command=self.limpar_tela)


class Application(Funcs):
    def __init__(self):
        self.root = root  # faz uma equivalencia porque o root nao ta dentro da class
        self.tela()  # inicializa a def tela
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menu()
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
        self.frame_1 = Frame(self.root, bd=1, bg='#d1e8f0',
                             highlightbackground='#113642',
                             highlightthickness='3')
        # POSICIONAR O FRAME relxy 0 seria 0% e 1 seria 100%, esquerda para direita, cima para baixo
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        # bd BORDA, bg COR FUNDO, highlightbackground CorDaBorda, highlightthickness TAMANHO BORDA
        self.frame_2 = Frame(self.root, bd=1, bg='#d1e8f0',
                             highlightbackground='#113642',
                             highlightthickness='3')
        # POSICIONAR O FRAME relxy 0 seria 0% e 1 seria 100%, esquerda para direita, cima para baixo
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.48)

    def widgets_frame1(self):
        # Botão Limpar, bd = tipo do botao, bg=cor de fundo do botao,
        # fg= cor da letra, font=('font', 'tamanho', 'estilo negrito italico, sublindado etc')
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=3,
                                bg='white', fg='black', font=('', 9, 'bold'),
                                command=self.limpar_tela)
        self.bt_limpar.place(relx=0.456, rely=0.1,
                             relwidth=0.1, relheight=0.15)
        # Botão Buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=3,
                                bg='white', fg='black', font=('', 9, 'bold'))
        self.bt_buscar.place(relx=0.353, rely=0.1,
                             relwidth=0.1, relheight=0.15)
        # Botão Novo
        self.bt_novo = Button(self.frame_1, text='Novo', bd=3,
                              bg='white', fg='black', font=('', 9, 'bold'),
                              command=self.add_cliente)
        self.bt_novo.place(relx=0.25, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão Alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=3,
                                 bg='white', fg='black', font=('', 9, 'bold'),
                                 command=self.altera_cliente)
        self.bt_alterar.place(relx=0.65, rely=0.1,
                              relwidth=0.1, relheight=0.15)
        # Botão Apagarr
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=3,
                                bg='white', fg='black', font=('', 9, 'bold'),
                                command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.753, rely=0.1,
                             relwidth=0.1, relheight=0.15)

        # Criação e posição da label no frame 1 e entrada do CÓDIGO no frame 1
        self.lb_codigo = Label(
            self.frame_1, text="Código", background='#d1e8f0')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.06, rely=0.15, relwidth=0.08)
        # Criação da label e entrada do NOME no frame 1
        self.lb_nome = Label(
            self.frame_1, text="Nome", background="#d1e8f0")
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.06, rely=0.45, relwidth=0.5)
        # Criação da label e entrada do TELEFONER no frame 1
        self.lb_telefone = Label(
            self.frame_1, text="Telefone", background="#d1e8f0")
        self.lb_telefone.place(relx=0.05, rely=0.65)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.06, rely=0.75, relwidth=0.3)
        # Criação da label e entrada do CIDADE no frame 1
        self.lb_cidade = Label(
            self.frame_1, text="Cidade", background="#d1e8f0")
        self.lb_cidade.place(relx=0.5, rely=0.65)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.51, rely=0.75, relwidth=0.4)

    def lista_frame2(self):
        self.listaCliente = ttk.Treeview(self.frame_2, height=3, columns=(
            'col1', 'col2', 'col3', 'col4'))  # cria a lista no frame 2 e coloca os nomes
        self.listaCliente.heading("#0", text="")
        self.listaCliente.heading('#1', text='Código')
        self.listaCliente.heading('#2', text='Nome')
        self.listaCliente.heading('#3', text='Telefone')
        self.listaCliente.heading('#4', text='Cidade')
        # define o tamanho de cada parte da lista
        self.listaCliente.column('#0', width=1)
        self.listaCliente.column('#1', width=50)
        self.listaCliente.column('#2', width=200)
        self.listaCliente.column('#3', width=125)
        self.listaCliente.column('#4', width=125)
        # Posiciona ela
        self.listaCliente.place(relx=0.01, rely=0.1,
                                relwidth=0.95, relheight=0.85)
        # cria a barra de rolagem nela
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCliente.configure(
            yscroll=self.scroolLista.set)  # coloca ela na tela
        self.scroolLista.place(relx=0.96, rely=0.1,
                               relheight=0.85, relwidth=0.03)  # posiciona ela
        # fazer interação com a lista
        self.listaCliente.bind("<Double-1>", self.onDoubleClick)


Application()  # chama a class
