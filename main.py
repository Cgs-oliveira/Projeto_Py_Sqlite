from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from webbrowser import BackgroundBrowser
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date

from view import *



#cores

co0 = "#2e2d2b" #preto
co1 = "#feffff" #branco
co2 = "#4fa882" #verde
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#e06636" #profit
co6 = "#038cfc" #azul
co7 = "#3fbfb9" #verde
co8 = "#263238" #+verde
co9 = "#e9edf5" #++verde


#crinado janela 

janela = Tk()
janela.title('TRABALHO ATIVIDADE DE BANCO DE DADOS')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE) #Fixar tamanho da janela

style = ttk.Style (janela)
style.theme_use("clam")

#criando blocos
FrameCima = Frame(janela, width=1043, height=50,bg=co1, relief=FLAT)
FrameCima.grid(row=0,column=0)

FrameMeio = Frame(janela, width=1043, height=303,bg=co1,pady=20, relief=FLAT)
FrameMeio.grid(row=1,column=0,pady=1,padx=0, sticky=NSEW)

FrameBaixo = Frame(janela, width=1043, height=300,bg=co1,pady=20, relief=FLAT)
FrameBaixo.grid(row=2,column=0,pady=0,padx=0, sticky=NSEW)


#criando funções
global tree
# função inserir
def inserir():
    global imagem, imagem_string, l_imagem
    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    model = e_model.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serie.get()
    Imagem = imagem_string

    lista_inserir = [nome, local, descricao, model,data,valor,serie,Imagem]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror ('ERRO',' Preencha todos os campos')
            return
    inserir_from(lista_inserir)

    messagebox.showinfo ('Os dados foram lançados com sucesso!!')


    e_nome.delete(0,'end')
    e_local.delete(0,'end')
    e_descricao.delete (0,'end')
    e_model.delete (0,'end')
    e_cal.delete (0,'end')
    e_valor.delete (0,'end')
    e_serie.delete (0,'end')


    for widget in FrameMeio.winfo_children():
        widget.destroy

    mostrar()

#escolher imagem
global imagem, imagem_string, l_imagem

def escolher_img():
    global imagem, imagem_string, l_imagem
    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize ((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(FrameMeio, image=imagem,bg=co1,fg=co4)
    l_imagem.place(x=700, y=10)

#atualiza
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]
        e_nome.delete(0,'end')
        e_local.delete(0,'end')
        e_descricao.delete (0,'end')
        e_model.delete (0,'end')
        e_cal.delete (0,'end')
        e_valor.delete (0,'end')
        e_serie.delete (0,'end')

        id=int(treev_lista[0])
        e_nome.insert(0,treev_lista[1])
        e_local.insert(0,treev_lista[2])
        e_descricao.insert (0,treev_lista[3])
        e_model.insert (0,treev_lista[4])
        e_cal.insert (0,treev_lista[5])
        e_valor.insert (0,treev_lista[6])
        e_serie.insert (0,treev_lista[7])

        def update():
            global imagem, imagem_string, l_imagem
            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            model = e_model.get()
            data = e_cal.get()
            valor = e_valor.get()
            serie = e_serie.get()
            Imagem = imagem_string
            if imagem == '':
                imagem= e_serie.INSERT (0,treev_lista[7])

            lista_atualizar = [nome, local, descricao, model,data,valor,serie,Imagem]

            for i in lista_atualizar:
                if i=='':
                    messagebox.showerror('Erro, preencha todos os campos')
                    return
            atualizar(lista_atualizar)
            messagebox.showinfo ('Os dados foram atualizados com sucesso!!')

            e_nome.delete(0,'end')
            e_local.delete(0,'end')
            e_descricao.delete (0,'end')
            e_model.delete (0,'end')
            e_cal.delete (0,'end')
            e_valor.delete (0,'end')
            e_serie.delete (0,'end')
    except IndexError:
        messagebox.showinfo ('Erro, selecione os dados da tabela')



# ver imagem
def ver_imagem():
    global imagem, imagem_string, l_imagem
    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]
    print(valor)


    iten = ver_item(valor)
    imagem = iten[0][8]
    

    imagem = Image.open(imagem)
    imagem = imagem.resize ((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(FrameMeio, image=imagem, bg=co1,fg=co4)

    l_imagem.place(x=700, y=10)



#abrindo imagem
app_img = Image.open('Invent.png')
app_img = app_img.resize ((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(FrameCima, image=app_img, text='Inventário Doméstico', width=900,compound=LEFT, relief=RAISED, anchor=NW, font= ('verdana 20 bold'),bg=co1,fg=co4)

app_logo.place(x=0, y=0)


#frameCima

#entradas
l_nome = Label(FrameMeio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry (FrameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

l_local = Label(FrameMeio, text='Sala/Área', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)
e_local = Entry (FrameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)

l_descricao = Label(FrameMeio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry (FrameMeio, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=71)

l_model = Label(FrameMeio, text='Marca', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_model.place(x=10, y=100)
e_model = Entry (FrameMeio, width=30, justify='left', relief=SOLID)
e_model.place(x=130, y=101)

l_cal = Label(FrameMeio, text='Data da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry (FrameMeio, width=12, background='darkblue', borderwidth=2, year=2024 )
e_cal.place(x=130, y=131)

l_valor = Label(FrameMeio, text='Valor da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry (FrameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=161)

l_serie = Label(FrameMeio, text='Num série', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_serie.place(x=10, y=190)
e_serie = Entry (FrameMeio, width=30, justify='left', relief=SOLID)
e_serie.place(x=130, y=191)

#botões

#carrregar
l_img = Label(FrameMeio, text='Imagem do Item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_img.place(x=10, y=220)
b_img = Button(FrameMeio,command=escolher_img, width=29, text='Carregar arquivo'.upper(),compound=CENTER, height=1, anchor=CENTER, overrelief=RIDGE,font=('Ivy 8'), bg=co1, fg=co0)
b_img.place(x=130, y=221)

#ADDimg
img_add = Image.open('add.png')
img_add = img_add.resize ((20,20))
img_add = ImageTk.PhotoImage(img_add)
#inserir

b_inserir = Button(FrameMeio,command=inserir,image=img_add, width=95, text='  Adicionar  '.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE,font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=330, y=10)


#ADDimg
img_update = Image.open('update.png')
img_update = img_update.resize ((20,20))
img_update = ImageTk.PhotoImage(img_update)
#ATT

b_update = Button(FrameMeio,command=atualizar,image=img_update, width=95, text='  Atualizar  '.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE,font=('Ivy 8'), bg=co1, fg=co0)
b_update.place(x=330, y=50)

#ADDimg
img_delete = Image.open('del.png')
img_delete = img_delete.resize ((20,20))
img_delete = ImageTk.PhotoImage(img_delete)
#delete

b_delete = Button(FrameMeio,image=img_delete, width=95, text='  Deletar  '.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE,font=('Ivy 8'), bg=co1, fg=co0)
b_delete.place(x=330, y=90)

#VER IMG
img_item = Image.open('upgrade.png')
img_item = img_item.resize ((20,20))
img_item = ImageTk.PhotoImage(img_item)
#IMG

b_item = Button(FrameMeio,command=ver_imagem,image=img_item, width=95, text='  Ver Item  '.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE,font=('Ivy 8'), bg=co1, fg=co0)
b_item.place(x=330, y=221)

#labels qauntidade e valores

l_total = Label(FrameMeio, text='', width=14, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total.place(x=450, y=17)
l_total = Label(FrameMeio, text='   Valor Total de todos os Itens ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_total.place(x=450, y=12)

l_qtd = Label(FrameMeio, text='', width=14, height=2,pady=5, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_qtd.place(x=450, y=90)
l_qtd = Label(FrameMeio, text='  Quantidade total de itens', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd.place(x=450, y=92)

def mostrar():
    global tree

    tabela_head = ['#Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

    lista_itens = ver_from()

    #global tree

    tree = ttk.Treeview(FrameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(FrameBaixo, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(FrameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    FrameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
    #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    #inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = [8888,88]

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens

mostrar()

janela.mainloop()