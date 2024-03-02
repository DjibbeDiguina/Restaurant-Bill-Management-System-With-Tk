import tempfile
from tkinter import *
from tkinter import messagebox
import random, os
import subprocess


#-------FUNCTION PART-----------------------------
if not os.path.exists('bills'):
    os.mkdir('bills')
def print_data():
    if textArea.get(1.0, 'end') == "\n":
        messagebox.showerror('Error', 'la facture est vide')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textArea.get(1.0, 'end'))
        #os.startfile(file, 'print')
        subprocess.run(['print', file])
def search():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billEntry.get():

            f = open(f'bills/{i}','r')
            textArea.delete(1.0, 'end')
            for data in f:
                textArea.insert('end', data)
            f.close()
            break
        else:
            messagebox.showerror('Erreur', 'sorry you got Error!!')


if not os.path.exists('bills'):
    os.mkdir('bills')
def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Voulez Vous Enregistrez La Facture?')
    if result:
        bill_content = textArea.get(1.0, 'end')
        file = open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'La facture num {billnumber} est enregistre correct!')
        billnumber = random.randint(500, 1000)



billnumber = random.randint(500,1000)
def bill_area():
    #if nameEntry.get() == '' or phoneEntry.get() == '':
    #    messagebox.showerror('Error', 'Detail de Client Obligatoire')
    #elif cosmeticpriceEntry.get() == '' and grocerypriceEntry.get() == '' and colddrinkEntry.get() == '':
    #    messagebox.showerror('Error', 'Pas De Produit Selectionner')
    #elif cosmeticpriceEntry.get() == '0 $' and grocerypriceEntry.get() == '0 $' and colddrinkEntry.get() == '0 $':
     #   messagebox.showerror('Error', 'Pas De Produit Selectionner')
    #else:
    textArea.delete(1.0, 'end')

    textArea.insert('end', '\t\t***Bienvenu Client***\n')
    textArea.insert('end', f'\n  N0_Facture: {billnumber}')
    textArea.insert('end', f'\n  Nom Client: {nameEntry.get()}')
    textArea.insert('end', f'\n  Telephone N0: {phoneEntry.get()}')
    textArea.insert('end', '\n=========================================================')
    textArea.insert('end', '\n  Produit\t\t\tQuantite\t\t\tPrix')
    textArea.insert('end', '\n=========================================================')
#-------------cosmetic-----------------------------------
    if bathEntry.get()!='0':
        textArea.insert('end', f'\n  Savon\t\t\t{bathEntry.get()}\t\t\t{savon} $')
    if creamEntry.get()!='0':
        textArea.insert('end', f'\n  Cream\t\t\t{creamEntry.get()}\t\t\t{cream} $')

    if washEntry.get()!='0':
        textArea.insert('end', f'\n  Lave Visage\t\t\t{washEntry.get()}\t\t\t{wash} $')

    if hairEntry.get()!='0':
        textArea.insert('end', f'\n  Cream Cheveux\t\t\t{hairEntry.get()}\t\t\t{hair} $')

    if gelEntry.get()!='0':
        textArea.insert('end', f'\n  Champagne\t\t\t{gelEntry.get()}\t\t\t{gel} $')

    if bodyEntry.get()!='0':
        textArea.insert('end', f'\n  Parfum\t\t\t{bodyEntry.get()}\t\t\t{body} $')
#-----------------------------Grocery--------------------------------------------------------------

    if riceEntry.get()!='0':
        textArea.insert('end', f'\n  Riz\t\t\t{riceEntry.get()}\t\t\t{rice} $')

    if oilEntry.get()!='0':
        textArea.insert('end', f'\n  Huile\t\t\t{oilEntry.get()}\t\t\t{oil} $')

    if wheatEntry.get()!='0':
        textArea.insert('end', f'\n  Farine\t\t\t{wheatEntry.get()}\t\t\t{wheat} $')

    if dealEntry.get()!='0':
        textArea.insert('end', f'\n  Haricot\t\t\t{dealEntry.get()}\t\t\t{deal} $')

    if sugarEntry.get()!='0':
        textArea.insert('end', f'\n  Sucre\t\t\t{sugarEntry.get()}\t\t\t{sugar} $')

    if teaEntry.get()!='0':
        textArea.insert('end', f'\n  Sardine\t\t\t{teaEntry.get()}\t\t\t{tea} $')
#-----------------------------------------drink cold----------------------------------------------

    if mazzaEntry.get()!='0':
        textArea.insert('end', f'\n  Mazza\t\t\t{mazzaEntry.get()}\t\t\t{mazza} $')

    if pepsiEntry.get()!='0':
        textArea.insert('end', f'\n  Pepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsi} $')

    if spriteEntry.get()!='0':
        textArea.insert('end', f'\n  Sprite\t\t\t{spriteEntry.get()}\t\t\t{sprite} $')

    if dewEntry.get()!='0':
        textArea.insert('end', f'\n  Dew\t\t\t{dewEntry.get()}\t\t\t{dew} $')

    if frootiEntry.get()!='0':
        textArea.insert('end', f'\n  Frooti\t\t\t{frootiEntry.get()}\t\t\t{frooti} $')

    if cocaEntry.get()!='0':
        textArea.insert('end', f'\n  Coca\t\t\t{cocaEntry.get()}\t\t\t{coca} $')
    textArea.insert('end', '\n---------------------------------------------------------\n')

    if cosmetictaxEntry.get()!='0.0':
        textArea.insert('end', f'\n    Cosmetics Tax\t\t\t\t\t\t{cosmetictaxEntry.get()} $')
    if grocerytaxEntry.get()!='0.0':
        textArea.insert('end', f'\n    Nourriture Tax\t\t\t\t\t\t{grocerytaxEntry.get()} $')
    if coldtaxEntry.get()!='0.0':
        textArea.insert('end', f'\n    Biere Tax\t\t\t\t\t\t{coldtaxEntry.get()} $')
    textArea.insert('end', f'\n\n  TOTAL BILL: \t\t\t\t\t\t{totalbill} $')
    textArea.insert('end', '\n---------------------------------------------------------\n')
    save_bill()

def total():
#---------cosmetic------------------------------
    global totalbill
    global savon,cream,wash,hair,gel,body
    savon = int(bathEntry.get()) * 20
    cream = int(creamEntry.get()) * 100
    wash = int(washEntry.get()) * 50
    hair = int(hairEntry.get()) * 60
    gel = int(gelEntry.get()) * 10
    body = int(bodyEntry.get()) * 80
    cosmeticValues = savon + cream + wash + hair + gel + body
    cosmeticpriceEntry.delete(0 , 'end')
    cosmeticpriceEntry.insert(0, f'{cosmeticValues} $')

    cosmeticTax = cosmeticValues*0.50
    cosmetictaxEntry.delete(0, 'end')
    cosmetictaxEntry.insert(0, cosmeticTax)

#-----------------------food part-------------
    global rice, oil, wheat, deal, sugar, tea
    rice = int(riceEntry.get()) * 25
    oil = int(oilEntry.get()) * 10
    wheat = int(wheatEntry.get()) * 30
    deal = int(dealEntry.get()) * 12
    sugar = int(sugarEntry.get()) * 50
    tea = int(teaEntry.get()) * 15
    foodValues = rice+oil+wheat+deal+sugar+tea
    grocerypriceEntry.delete(0, 'end')
    grocerypriceEntry.insert(0, f'{foodValues} $')

    foodTax = foodValues*0.12
    grocerytaxEntry.delete(0, 'end')
    grocerytaxEntry.insert(0, foodTax)

#----------------------cold biere part------------------
    global mazza, pepsi, sprite, dew, frooti, coca
    mazza = int(mazzaEntry.get()) * 10
    pepsi = int(pepsiEntry.get()) * 5
    sprite = int(spriteEntry.get()) * 3
    dew = int(dewEntry.get()) * 3
    frooti = int(frootiEntry.get()) * 5
    coca = int(cocaEntry.get()) * 2
    drinkValues = mazza+pepsi+sprite+dew+frooti+coca
    colddrinkEntry.delete(0, 'end')
    colddrinkEntry.insert(0, f'{drinkValues} $')

    colddrinkTax = drinkValues*0.80
    coldtaxEntry.delete(0, 'end')
    coldtaxEntry.insert(0, colddrinkTax)

    totalbill = drinkValues + foodValues + cosmeticValues

#GUI PARTI---------------------------------------
root = Tk()
root.title("System de Facture Fait Par Djibbe Diguina")
root.geometry("1470x750")
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

title = Label(root, text="System De Facturation Detail", font=('Arial', 30, 'bold'), bg='#2B3467', fg='#EB455F', bd=12, relief='groove')
title.pack(fill=X, pady=5)
customerFrame = LabelFrame(root, text="Detail Du Client", bg='#2B3467', fg='#EB455F', bd=8, relief='groove', font=('Arial', 15, 'bold'))
customerFrame.pack(fill=X, pady=5)
#-------------------------------customer Details----------------------------------------------------------
nameLabel = Label(customerFrame, text="Nom", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
nameLabel.grid(row=0, column=0, padx=10, pady=5)
nameEntry = Entry(customerFrame, bd=3, width=30, font=('Arial', 15, 'bold'))
nameEntry.grid(row=0, column=1, padx=10, pady=5)

phoneLabel = Label(customerFrame, text="Phone", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
phoneLabel.grid(row=0, column=2, padx=10, pady=5)
phoneEntry = Entry(customerFrame, bd=3, width=25, font=('Arial', 15, 'bold'))
phoneEntry.grid(row=0, column=3, padx=10, pady=5)

billLabel = Label(customerFrame, text="N-Facture", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
billLabel.grid(row=0, column=4, padx=10, pady=5)
billEntry = Entry(customerFrame, bd=3, width=25, font=('Arial', 15, 'bold'))
billEntry.grid(row=0, column=5, padx=10, pady=5)

searchButton = Button(customerFrame, text="Search", font=('Arial', 15, 'bold'), bg='#EB455F', fg='#FCFFE7', width=12, command=search)
searchButton.grid(row=0, column=6, padx=30, pady=5)

#------------------------------------product info------------------------------------------------------------------
productFrame = Frame(root)
productFrame.pack(fill=X)

cosmeticsFrame = LabelFrame(productFrame, text="Cosmetics", bg='#2B3467', fg='#EB455F', bd=8, relief='groove', font=('Arial', 15, 'bold'))
cosmeticsFrame.grid(row=0, column=0)

bathLabel = Label(cosmeticsFrame, text="Savon Toillete", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
bathLabel.grid(row=0, column=0, padx=30, pady=5, sticky='w')
bathEntry = Entry(cosmeticsFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
bathEntry.grid(row=0, column=1, padx=10, pady=10)
bathEntry.insert(0, 0)

creamLabel = Label(cosmeticsFrame, text="Cream de Face", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
creamLabel.grid(row=1, column=0, padx=30, pady=5, sticky='w')
creamEntry = Entry(cosmeticsFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
creamEntry.grid(row=1, column=1, padx=10, pady=10)
creamEntry.insert(0, 0)

washLabel = Label(cosmeticsFrame, text="Lave Visage", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
washLabel.grid(row=2, column=0, padx=30, pady=5, sticky='w')
washEntry = Entry(cosmeticsFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
washEntry.grid(row=2, column=1, padx=10, pady=10)
washEntry.insert(0, 0)

hairLabel = Label(cosmeticsFrame, text="Cream Cheveux", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
hairLabel.grid(row=3, column=0, padx=30, pady=5, sticky='w')
hairEntry = Entry(cosmeticsFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
hairEntry.grid(row=3, column=1, padx=10, pady=10)
hairEntry.insert(0, 0)


gelLabel = Label(cosmeticsFrame, text="Champagne", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
gelLabel.grid(row=4, column=0, padx=30, pady=5, sticky='w')
gelEntry = Entry(cosmeticsFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
gelEntry.grid(row=4, column=1, padx=10, pady=10)
gelEntry.insert(0, 0)

bodyLabel = Label(cosmeticsFrame, text="Parfum", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
bodyLabel.grid(row=5, column=0, padx=30, pady=5, sticky='w')
bodyEntry = Entry(cosmeticsFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
bodyEntry.grid(row=5, column=1, padx=10, pady=10)
bodyEntry.insert(0, 0)



#------------------------------------------------food eat category Grocery----------------------------------------------
groceryFrame = LabelFrame(productFrame, text="Nourriture", bg='#2B3467', fg='#EB455F', bd=8, relief='groove', font=('Arial', 15, 'bold'))
groceryFrame.grid(row=0, column=1)

riceLabel = Label(groceryFrame, text="Riz", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
riceLabel.grid(row=0, column=0, padx=30, pady=5, sticky='w')
riceEntry = Entry(groceryFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
riceEntry.grid(row=0, column=1, padx=10, pady=10)
riceEntry.insert(0, 0)

oilLabel = Label(groceryFrame, text="Oil", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
oilLabel.grid(row=1, column=0, padx=30, pady=5, sticky='w')
oilEntry = Entry(groceryFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
oilEntry.grid(row=1, column=1, padx=10, pady=10)
oilEntry.insert(0, 0)

dealLabel = Label(groceryFrame, text="Farine", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
dealLabel.grid(row=2, column=0, padx=30, pady=5, sticky='w')
dealEntry = Entry(groceryFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
dealEntry.grid(row=2, column=1, padx=10, pady=10)
dealEntry.insert(0, 0)

wheatLabel = Label(groceryFrame, text="Haricot", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
wheatLabel.grid(row=3, column=0, padx=30, pady=5, sticky='w')
wheatEntry = Entry(groceryFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
wheatEntry.grid(row=3, column=1, padx=10, pady=10)
wheatEntry.insert(0, 0)

sugarLabel = Label(groceryFrame, text="Sucre", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
sugarLabel.grid(row=4, column=0, padx=30, pady=5, sticky='w')
sugarEntry = Entry(groceryFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
sugarEntry.grid(row=4, column=1, padx=10, pady=10)
sugarEntry.insert(0, 0)

teaLabel = Label(groceryFrame, text="Sardine", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
teaLabel.grid(row=5, column=0, padx=30, pady=5, sticky='w')
teaEntry = Entry(groceryFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
teaEntry.grid(row=5, column=1, padx=10, pady=10)
teaEntry.insert(0, 0)
#----------------------------------------------------------cold drinks--------------------------------------------

cold_drinkFrame = LabelFrame(productFrame, text="Biere", bg='#2B3467', fg='#EB455F', bd=8, relief='groove', font=('Arial', 15, 'bold'))
cold_drinkFrame.grid(row=0, column=2)

mazzaLabel = Label(cold_drinkFrame, text="Mazza", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
mazzaLabel.grid(row=0, column=0, padx=30, pady=5, sticky='w')
mazzaEntry = Entry(cold_drinkFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
mazzaEntry.grid(row=0, column=1, padx=10, pady=10)
mazzaEntry.insert(0, 0)

pepsiLabel = Label(cold_drinkFrame, text="Pepsi", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
pepsiLabel.grid(row=1, column=0, padx=30, pady=5, sticky='w')
pepsiEntry = Entry(cold_drinkFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
pepsiEntry.grid(row=1, column=1, padx=10, pady=10)
pepsiEntry.insert(0, 0)

spriteLabel = Label(cold_drinkFrame, text="Sprite", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
spriteLabel.grid(row=2, column=0, padx=30, pady=5, sticky='w')
spriteEntry = Entry(cold_drinkFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
spriteEntry.grid(row=2, column=1, padx=10, pady=10)
spriteEntry.insert(0, 0)

dewLabel = Label(cold_drinkFrame, text="Dew", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
dewLabel.grid(row=3, column=0, padx=30, pady=5, sticky='w')
dewEntry = Entry(cold_drinkFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
dewEntry.grid(row=3, column=1, padx=10, pady=10)
dewEntry.insert(0, 0)

frootiLabel = Label(cold_drinkFrame, text="Frooti", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
frootiLabel.grid(row=4, column=0, padx=30, pady=5, sticky='w')
frootiEntry = Entry(cold_drinkFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
frootiEntry.grid(row=4, column=1, padx=10, pady=10)
frootiEntry.insert(0, 0)

cocaLabel = Label(cold_drinkFrame, text="Coca Cola", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
cocaLabel.grid(row=5, column=0, padx=30, pady=5, sticky='w')
cocaEntry = Entry(cold_drinkFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
cocaEntry.grid(row=5, column=1, padx=10, pady=10)
cocaEntry.insert(0, 0)

#----------------------------------------------------------------text area frame----------------------------------------------------------

billFrame = Frame(productFrame, bd=8, relief='groove', bg='#FCFFE7')
billFrame.grid(row=0, column=3)

billName = Label(billFrame, text="Bill Area", font=('Arial', 15, 'bold'), bd=5, relief='groove', fg='#EB455F', bg='#FCFFE7')
billName.pack(fill=X)

scrollbar = Scrollbar(billFrame, orient='vertical')
scrollbar.pack(side='right', fill=Y)


textArea = Text(billFrame, width=57, height=18, yscrollcommand=scrollbar.set)
textArea.pack()
scrollbar.configure(command=textArea.yview)

#-----------------------------------------------------------------bill menu---------------------------------------------------------

billmenuFrame = LabelFrame(root, text="Menu Facture", bg='#2B3467', fg='#EB455F', bd=8, relief='groove', font=('Arial', 15, 'bold'))
billmenuFrame.pack(fill=X, pady=5)

cosmeticpriceLabel = Label(billmenuFrame, text="Cosmetic Prix", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
cosmeticpriceLabel.grid(row=0, column=0, padx=30, pady=5, sticky='w')
cosmeticpriceEntry = Entry(billmenuFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
cosmeticpriceEntry.grid(row=0, column=1, padx=10, pady=10)

grocerypriceLabel = Label(billmenuFrame, text="Nourriture Prix", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
grocerypriceLabel.grid(row=1, column=0, padx=30, pady=5, sticky='w')
grocerypriceEntry = Entry(billmenuFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
grocerypriceEntry.grid(row=1, column=1, padx=10, pady=10)

colddrinkLabel = Label(billmenuFrame, text="Biere Prix", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
colddrinkLabel.grid(row=2, column=0, padx=30, pady=5, sticky='w')
colddrinkEntry = Entry(billmenuFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
colddrinkEntry.grid(row=2, column=1, padx=10, pady=10)

cosmetictaxLabel = Label(billmenuFrame, text="Cosmetic Tax", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
cosmetictaxLabel.grid(row=0, column=2, padx=40, pady=5, sticky='w')
cosmetictaxEntry = Entry(billmenuFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
cosmetictaxEntry.grid(row=0, column=3, padx=10, pady=10)

grocerytaxLabel = Label(billmenuFrame, text="Nourriture Tax", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
grocerytaxLabel.grid(row=1, column=2, padx=40, pady=5, sticky='w')
grocerytaxEntry = Entry(billmenuFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
grocerytaxEntry.grid(row=1, column=3, padx=10, pady=10)

coldtaxLabel = Label(billmenuFrame, text="Biere Tax", font=('Arial', 15, 'bold'), fg='#FCFFE7', bg='#2B3467')
coldtaxLabel.grid(row=2, column=2, padx=40, pady=5, sticky='w')
coldtaxEntry = Entry(billmenuFrame, width=10, bd=3, font=('Arial', 15, 'bold'))
coldtaxEntry.grid(row=2, column=3, padx=10, pady=10)
#------------------------------------------------button menu----------------------------------------------------------

totalButton = Button(billmenuFrame, text="Total", font=('Arial', 15, 'bold'), bg='#EB455F', fg='#FCFFE7', height=2, command=total)
totalButton.grid(row=1, column=4, pady=5, padx=25)

billButton = Button(billmenuFrame, text="Facture", font=('Arial', 15, 'bold'), bg='#EB455F', fg='#FCFFE7', height=2, command=bill_area)
billButton.grid(row=1, column=5, pady=5, padx=25)

emailButton = Button(billmenuFrame, text="Email", font=('Arial', 15, 'bold'), bg='#EB455F', fg='#FCFFE7', height=2)
emailButton.grid(row=1, column=6, pady=5, padx=25)

printButton = Button(billmenuFrame, text="Imprimer", font=('Arial', 15, 'bold'), bg='#EB455F', fg='#FCFFE7', height=2, command=print_data)
printButton.grid(row=1, column=7, pady=5, padx=25)

clearButton = Button(billmenuFrame, text="Supprimer", font=('Arial', 15, 'bold'), bg='#EB455F', fg='#FCFFE7', height=2)
clearButton.grid(row=1, column=8, pady=5, padx=25)





root.mainloop()
