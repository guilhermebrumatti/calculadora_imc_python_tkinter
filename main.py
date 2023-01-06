from tkinter import *
from tkinter import ttk

# ---------------- relação de cores ---------------------

co1 = "#feffff"  # branca
co2 = "#FF0000"  # vermelha
co3 = "#545748"  # preto

janela = Tk()
janela.title('')
janela.geometry('230x270')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# ---------------- Divisão da janela ---------------------

frame_A = Frame(janela, width=400, height=60,bg=co1, pady=0, padx=0, relief="flat",)
frame_A.grid(row=0, column=0, sticky=NSEW)

frame_B = Frame(janela, width=400, bg=co1, pady=0, padx=0, relief="flat",)
frame_B.grid(row=2, column=0, sticky=NSEW)
 
style = ttk.Style(janela)
style.theme_use("clam")

# ---------------- Texto da versão do app ---------------------

l_versao = Label(janela, text='v1.0', padx=1, pady=1, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co3)
l_versao.place(x=193, y=240)

# ---------------- FRAME A(título) ---------------------

app_nome = Label(frame_A, text="Calculadora de IMC", width=18, height=1, padx=0, relief="flat", anchor="center", font=('Ivy 14 bold'), bg=co1, fg=co3)
app_nome.place(x=0, y=2)
 
app_linha = Label(frame_A, text="", width=380, height=1, padx=0, relief="flat", anchor="nw", font=('Arial 1'), bg=co3, fg=co1)
app_linha.place(x=0, y=35)

# ---------------- FRAME C(Input do peso e altura) ---------------------
 
l_peso = Label(frame_B , text="Insira seu peso", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co3)
l_peso.grid(row=0, column=0, columnspan=1,  sticky=NW, pady=10, padx=3)
e_peso = Entry(frame_B, width=5, font=('Ivy 10 bold'),justify='center',relief=SOLID)
e_peso.grid(row=0, column=1, columnspan=1,  sticky=NSEW, pady=10, padx=3)
 
l_altura = Label(frame_B , text="Insira sua altura", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co3)
l_altura.grid(row=1, column=0, columnspan=1,  sticky=NW, pady=10, padx=3)
e_altura = Entry(frame_B, width=5, font=('Ivy 10 bold'),justify='center',relief=SOLID)
e_altura.grid(row=1, column=1, columnspan=1,  sticky=NSEW, pady=10, padx=3) 
 
l_resultado = Label(frame_B ,width=5, text="---", height=1, pady=12, relief="flat", anchor="center", font=('Ivy 24 bold'), bg=co1, fg=co1)
l_resultado.grid(row=2, column=1)
 
l_resultado_texto = Label(frame_B , width=30, text="", height=1, padx=-3, pady=12, relief="flat", anchor="center", font=('Ivy 12 bold'), bg=co1, fg=co3)
l_resultado_texto.place(x=-40, y=85)

# ---------------- IFs com os calculos do IMC ---------------------

def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get())**2
    resultado = peso/altura
    
    if resultado < 18.6:
        l_resultado_texto['text'] = "Seu IMC é: Abaixo do peso"
    elif resultado >= 18.5 and resultado < 24.9:
        l_resultado_texto['text'] = "Seu IMC é: Normal"
    elif resultado >=25 and resultado < 29.9:
        l_resultado_texto['text'] ="Seu IMC é: Sobrepeso"
    else:
        l_resultado_texto['text'] = "Seu IMC é: Obesidade"
        
    l_resultado['text'] = "{:.{}f}".format( resultado, 2 )

# ------------ Botao calcular ------------------ 

b_calcular = Button(frame_B,command=calcular, text="Calcular", width=26, height=1, overrelief=SOLID, bg=co2, fg=co1, font=('Ivy 10 bold'), anchor="center", relief=RAISED )
b_calcular.grid(row=4, column=0, sticky=NSEW, padx=5, columnspan=30)

janela.mainloop()
