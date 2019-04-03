## Abrindo navegador
import webbrowser
import pyautogui
import time
import csv
import pyperclip
from tkinter import *

mensagem = ""

#Solicita Login, baixa CSV
def _pega_planilha(): 
    
     
    a_website = "https://admin.menutecnologia.com/index.php/kairos"
    webbrowser.open_new(a_website)

    def _login_magento():
        a=Tk()
        a.title('Confirmação')
        a.geometry('600x800+300+300')
        a.lift()
        a.attributes('-topmost',True)
    
        def destroy():
            a.destroy()
    
        labl1=Label(text="Para iniciar, siga os próximos passos:", font=20).pack()
        labl2=Label(text="1. Faça login na página que foi aberta", font=20).pack()
        labl3=Label(text="2. Acesse o módulo de clientes como no exemplo abaixo:", font=20).pack()
        passo1 = PhotoImage(file="passo1.PNG")
        passo2 = PhotoImage(file="passo2.PNG")
        passo3 = PhotoImage(file="passo3.PNG")
        Label(a, image=passo1, height="200", width="220").pack()
        labl4=Label(text="3. No módulo de clientes, filtre a coluna 'Contato' por 'WhatsApp':", font=20).pack()
        Label(a, image=passo2, height="180", width="296").pack()
        labl5=Label(text="4. Por último, aplique os filtros clicando no seguinte botão:", font=20).pack()
        Label(a, image=passo3, height="180", width="400").pack()
        a.lift()
        a.attributes('-topmost',True)
        button1= Button(text='Concluído', command= destroy).pack()
        a.mainloop() 
    
    _login_magento()

    time.sleep(2)
    combo = pyautogui.locateOnScreen('combo.png')
    combo
    combo[0]
    combo.left
    combocenter = pyautogui.center(combo)
    combocenter
    combocenter[0]
    combocenter.x
    combox, comboy = combocenter
    pyautogui.click('combo.png')
    time.sleep(2) 
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')

_pega_planilha()

##Solicita e armazena o texto que será passado

def _solicita_msg():
    global mensagem
    time.sleep(1)
    a=Tk()
    a.geometry('500x200+300+300')
    a.title("Mensagem")
    b = StringVar()
    a.lift()
    a.attributes('-topmost',True)
    mensagem = ""
    def com():
        global mensagem
        a.lift()
        a.attributes('-topmost',True)   
        c=b.get()
        labl2=Label(text=c,font=20).pack()
        mensagem = c
        a.destroy()
        
        return mensagem
    
    labl1=Label(text="Abaixo, escreva o que deseja enviar.", font=30).pack()
    labl2=Label(text="A mensagem será enviada no seguinte padrão:", font=30).pack()
    labl3=Label(text="Olá, (nome do cliente). (Sua mensagem vai aqui).", font=30).pack()
    text = Entry(textvariable=b, width=60).pack()
    button1= Button(text='Enviar!', command= com).pack()
    a.lift()
    a.attributes('-topmost',True)
    a.mainloop() 

_solicita_msg()

#Solicita login no WhatsApp

def _login_zap():
    w_website = "http://web.whatsapp.com"
    webbrowser.open_new(w_website)
    a=Tk()
    a.title('Confirmação')
    a.geometry('400x100+300+300')
    a.lift()
    a.attributes('-topmost',True)

    def destroy():
        a.destroy()
    
    labl1=Label(text="Após validar o QR Code do Whatsapp, \n clique no botão para prosseguir", font=20).pack()
    button1= Button(text='Concluído', command= destroy).pack()
    a.lift()
    a.attributes('-topmost',True)

    a.mainloop() 

_login_zap()

#Faz a busca de contatos e envio de mensagens
def _csv_envia_zap():
    w_website = "http://web.whatsapp.com"
    webbrowser.open_new(w_website)
    arquivo = open("../../Downloads/customers.csv")
    customers = csv.DictReader(arquivo)
    telefones = ''
    nomes = ''
    
    for customer in customers:
        nome = customer["Nome"]
        telefone = customer["Telefone"]
        nomes += nome + "_"
        telefones += telefone + "_"

    

    lista_telefones = telefones.split("_")
    lista_nomes = nomes.split("_")

    for i in range(len(lista_telefones)):
        tels = lista_telefones[i]
        names = lista_nomes[i]
        time.sleep(7) 
        pyautogui.press('tab')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(2)
        pyautogui.press('backspace')
        time.sleep(1)
        pyautogui.typewrite("{0}".format(tels))
        time.sleep(2) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.typewrite("Ola {0}, ".format(names))
        time.sleep(1)
        pyperclip.copy(mensagem)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2) 
        pyautogui.press('enter')
        time.sleep(2) 
        pyautogui.press('esc')
        
_csv_envia_zap()

def _fim():
    
    a=Tk()
    a.title('Finalizado')
    a.geometry('400x100+300+300')
    a.lift()
    a.attributes('-topmost',True)

    def destroy():
        a.destroy()
    
    labl1=Label(text="Finalizado!", font=20).pack()
    button1= Button(text='OK!', command= destroy).pack()
    a.lift()
    a.attributes('-topmost',True)

    a.mainloop() 

_fim()
    
