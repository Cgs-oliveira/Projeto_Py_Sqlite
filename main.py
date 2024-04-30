from tkinter import*
from tkinter import Tk, StringVar, ttk

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


janela.mainloop()