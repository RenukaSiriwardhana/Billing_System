import tempfile
from fileinput import filename
from tkinter import *
from tkinter import messagebox
import random,os,tempfile
import sys
from tkinter import messagebox, END
import os
from fpdf import FPDF

global totalbill
def print_bill():
    global file_path
    if not os.path.exists("bills"):
        os.makedirs("bills")

    # File path for the PDF
    file_path = os.path.join("bills", f"{billnumber}bill.pdf")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)

    # Split content into lines and add each line to the PDF
    for line in bill_content.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True, align='C')

    # Save PDF with a unique name (optional: use bill number)
    file_path = os.path.join("bills", f"{billnumber}bill.pdf")
    pdf.output(file_path)

    # Open the PDF for preview
    os.startfile(file_path)


def search_bill():
    bill_no = BillnumberEntry.get().strip()
    filename = f"{bill_no}.txt"
    file_path = os.path.join('bills', filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            textarea.delete(1.0, END)
            for line in f:
                textarea.insert(END, line)
    else:
        messagebox.showerror('Error', 'Invalid Bill Num')


if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global bill_content,billnumber
    result= messagebox.askyesno('confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number{billnumber}is saved successfully')


billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get()=='':
        messagebox.showerror('Error','Customer details Are Required')
    elif cosmeticpriceEntry.get()==''  or grocerypriceEntry.get()=='' or drinkspriceEntry.get()=='':
        messagebox.showerror('Error', 'No products are selected')
    elif cosmeticpriceEntry.get()=='0 Rs' and  grocerypriceEntry.get()=='0 Rs'  and drinkspriceEntry.get()=='0 Rs'  :
        messagebox.showerror('Error','No products are selected')
    else:
        textarea.delete(1.0, END)

        textarea.insert(END, '\t\t**Welcome Customer**\n')
        textarea.insert(END, f'\nBill Number:{billnumber}\n')
        textarea.insert(END, f'\nCustomer Name:{nameEntry.get()}\n')
        textarea.insert(END, f'\nCustomer Phone Number:{phoneEntry.get()}\n')
        textarea.insert(END, '\n*******************************************************')
        textarea.insert(END, 'Products\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n*******************************************************\n\n')

        if bathsoapEntry.get() != '0':
            textarea.insert(END, f'Bath Soap\t\t\t{bathsoapEntry.get()}\t\t\tRs:{soapprice}\n')
        if facecreamEntry.get() != '0':
            textarea.insert(END, f'Face Cream\t\t\t{facecreamEntry.get()}\t\t\tRs:{facecreamprice} \n')
        if facewashEntry.get() != '0':
            textarea.insert(END, f'Face Wash\t\t\t{facewashEntry.get()}\t\t\tRs:{facewashprice}\n ')
        if HairGelEntry.get() != '0':
            textarea.insert(END, f'Hair Gel\t\t\t{HairGelEntry.get()}\t\t\tRs:{hairgelprice}\n ')
        if hairSprayEntry.get() != '0':
            textarea.insert(END, f'Hair Spray\t\t\t{hairSprayEntry.get()}\t\t\tRs:{hairsprayprice}\n ')
        if BodyLotionEntry.get() != '0':
            textarea.insert(END, f'Body Lotion\t\t\t{BodyLotionEntry.get()}\t\t\t{bodylotionprice}\n ')

        if RiceEntry.get() != '0':
            textarea.insert(END, f'Rice\t\t\t{RiceEntry.get()}\t\t\tRs:{riceprice}\n')
        if DhalEntry.get() != '0':
            textarea.insert(END, f'Dhal\t\t\t{DhalEntry.get()}\t\t\tRs:{dhalprice}\n ')
        if oilEntry.get() != '0':
            textarea.insert(END, f'Oil\t\t\t{oilEntry.get()}\t\t\tRs:{oilprice}\n ')
        if WheatEntry.get() != '0':
            textarea.insert(END, f'Wheat\t\t\t{WheatEntry.get()}\t\t\tRs:{wheatprice} \n ')
        if SugarEntry.get() != '0':
            textarea.insert(END, f'Sugar \t\t\t{SugarEntry.get()}\t\t\tRs:{sugarprice}\n ')
        if TeaEntry.get() != '0':
            textarea.insert(END, f'Tea\t\t\t{TeaEntry.get()}\t\t\tRs:{teaprice}\n')

        if OrangeEntry.get() != '0':
            textarea.insert(END, f'Orange \t\t\t{OrangeEntry.get()}\t\t\tRs:{orangeprice}\n')
        if PepsiEntry.get() != '0':
            textarea.insert(END, f'Pepsi\t\t\t{PepsiEntry.get()}\t\t\tRs:{Pepsiprice}\n')
        if SpriteEntry.get() != '0':
            textarea.insert(END, f'Sprite\t\t\t {SpriteEntry.get()}\t\t\tRs:{spriteprice} \n')
        if DewEntry.get() != '0':
            textarea.insert(END, f'Mountain Dew\t\t\t{DewEntry.get()}\t\t\tRs:{dewprice}\n ')
        if MirindaEntry.get() != '0':
            textarea.insert(END, f'Mirinda\t\t\t{MirindaEntry.get()}\t\t\tRs:{mirindaprice} \n')
        if CocacolaEntry.get() != '0':
            textarea.insert(END, f'Coca-Cola\t\t\t{CocacolaEntry.get()}\t\t\tRs:{cocacolaprice} \n')
        textarea.insert(END, '\n.......................................................\n')

        save_bill()
        print_bill()

    if cosmetictaxEntry.get()!='0':
        textarea.insert(END,f'Cosmetic-Tax\t\t\t{cosmetictaxEntry.get()}\n')
    if grocerytaxEntry.get()!='0':
        textarea.insert(END,f'Grocery-Tax\t\t\t{grocerytaxEntry.get()}\n')
    if drinkstaxEntry.get()!='0':
        textarea.insert(END,f'Drinks-Tax\t\t\t{drinkstaxEntry.get()}\n')
    textarea.insert(END, f'\n{"="*45}\n💰 TOTAL BILL:\t\t\tRs. {totalbill} 💰\n{"="*45}')


def total():
    global soapprice, facecreamprice, facewashprice, hairsprayprice, hairgelprice, bodylotionprice

    global riceprice, dhalprice, wheatprice, oilprice, sugarprice, teaprice

    global orangeprice, Pepsiprice, spriteprice, mirindaprice, cocacolaprice, dewprice,totalbill
    soapprice=int(bathsoapEntry.get())*140
    facecreamprice=int(facecreamEntry.get())*650
    facewashprice=int(facewashEntry.get())*350
    hairsprayprice=int(hairSprayEntry.get()) * 1500
    hairgelprice=int(HairGelEntry.get())*300
    bodylotionprice=int(BodyLotionEntry.get())*600

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairgelprice+hairsprayprice+bodylotionprice

    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'Rs:{totalcosmeticprice} ')
    cosmetictax= totalcosmeticprice * 0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0, 'Rs:' + str(cosmetictax))



    riceprice=int(RiceEntry.get())*320
    dhalprice = int(DhalEntry.get()) * 200
    wheatprice = int(WheatEntry.get()) * 320
    oilprice = int(oilEntry.get()) * 120
    sugarprice = int(SugarEntry.get()) * 160
    teaprice = int(TeaEntry.get()) * 160

    totalgroceryprice=riceprice+dhalprice+wheatprice + oilprice +sugarprice + teaprice

    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,'Rs:'+ str(totalgroceryprice))
    grocerytax = totalgroceryprice * 0.10
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0,'Rs:'+  str(grocerytax))


    orangeprice=int(OrangeEntry.get())*120
    Pepsiprice = int(PepsiEntry.get()) * 200
    spriteprice = int(SpriteEntry.get()) * 120
    mirindaprice = int(MirindaEntry.get()) * 120
    cocacolaprice = int(CocacolaEntry.get()) * 160
    dewprice = int(DewEntry.get()) * 180

    totaldrinkprice= orangeprice+ Pepsiprice + spriteprice + mirindaprice +cocacolaprice + dewprice
    drinkspriceEntry.delete(0, END)
    drinkspriceEntry.insert(0,'Rs'+  str(totaldrinkprice))
    drinkstax = totaldrinkprice * 0.08
    drinkstaxEntry.delete(0, END)
    drinkstaxEntry.insert(0, 'Rs:'+ str(drinkstax) )

    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinkprice+cosmetictax+grocerytax+drinkstax

root=Tk()
root.title('Retail Management System')
root.geometry('1270x800')
root.iconbitmap('icon.ico')
headingLabel=Label(root,text='Billing System',font=('Times New Roman',30,'bold')
                   ,bg='gray10',fg='chocolate1',bd=12,relief="groove")
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('Times new roman',15,'bold')
                                 , fg='gold',bd=10,relief=GROOVE,bg='gray20')
customer_details_frame.pack()

nameLabel=Label(customer_details_frame,text='Name',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

BillnumberLabel=Label(customer_details_frame,text='Bill Number',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
BillnumberLabel.grid(row=0,column=4,padx=20,pady=2)

BillnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
BillnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('Times new roman',13,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0,pady=10)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=10)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='Facewash',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
facewashLabel.grid(row=2,column=0,pady=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=10,sticky='w')
facewashEntry.insert(0,0)

hairSprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
hairSprayLabel.grid(row=3,column=0,pady=10,sticky='w')

hairSprayEntry=Entry(cosmeticsFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
hairSprayEntry.grid(row=3,column=1,pady=10,sticky='w')
hairSprayEntry.insert(0,0)


HairGelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
HairGelLabel.grid(row=4,column=0,pady=10,sticky='w')

HairGelEntry=Entry(cosmeticsFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
HairGelEntry.grid(row=4,column=1,pady=10,sticky='w')
HairGelEntry.insert(0,0)

BodyLotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
BodyLotionLabel.grid(row=5,column=0,pady=10)

BodyLotionEntry=Entry(cosmeticsFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
BodyLotionEntry.grid(row=5,column=1,pady=10,sticky='w')
BodyLotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('Times new roman',13,'bold'),fg='gold',bd=9,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)

RiceLabel=Label(groceryFrame,text='Rice',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
RiceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

RiceEntry=Entry(groceryFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
RiceEntry.grid(row=0,column=1,pady=9,padx=10)
RiceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=10)
oilEntry.insert(0,0)

DhalLabel=Label(groceryFrame,text='Dhal',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
DhalLabel.grid(row=2,column=0,pady=10,sticky='w')

DhalEntry=Entry(groceryFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
DhalEntry.grid(row=2,column=1,pady=10)
DhalEntry.insert(0,0)

WheatLabel=Label(groceryFrame,text='Wheat',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
WheatLabel.grid(row=3,column=0,pady=10,sticky='w')

WheatEntry=Entry(groceryFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
WheatEntry.grid(row=3,column=1,pady=10)
WheatEntry.insert(0,0)

SugarLabel=Label(groceryFrame,text='Sugar',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
SugarLabel.grid(row=4,column=0,pady=10,sticky='w')

SugarEntry=Entry(groceryFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
SugarEntry.grid(row=4,column=1,pady=10)
SugarEntry.insert(0,0)

TeaLabel=Label(groceryFrame,text='Tea',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
TeaLabel.grid(row=5,column=0,pady=10,sticky='w')

TeaEntry=Entry(groceryFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
TeaEntry.grid(row=5,column=1,pady=10)
TeaEntry.insert(0,0)

drinksFrame=LabelFrame(productsFrame,text='Drinks',font=('Times new roman',13,'bold'),fg='gold',bd=10,relief=GROOVE,bg='gray20')
drinksFrame.grid(row=0,column=2)

OrangeLabel=Label(drinksFrame,text='Orange',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
OrangeLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

OrangeEntry=Entry(drinksFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
OrangeEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
OrangeEntry.insert(0,0)

PepsiLabel=Label(drinksFrame,text='Pepsi',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
PepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

PepsiEntry=Entry(drinksFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
PepsiEntry.grid(row=1,column=1,pady=10)
PepsiEntry.insert(0,0)

SpriteLabel=Label(drinksFrame,text='Sprite',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
SpriteLabel.grid(row=2,column=0,pady=10,sticky='w')

SpriteEntry=Entry(drinksFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
SpriteEntry.grid(row=2,column=1,pady=10)
SpriteEntry.insert(0,0)

MirindaLabel=Label(drinksFrame,text='Mirinda',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
MirindaLabel.grid(row=3,column=0,pady=10,sticky='w')

MirindaEntry=Entry(drinksFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
MirindaEntry.grid(row=3,column=1,pady=10)
MirindaEntry.insert(0,0)

CocacolaLabel=Label(drinksFrame,text='Coca-cola',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
CocacolaLabel.grid(row=4,column=0,pady=10,sticky='w')

CocacolaEntry=Entry(drinksFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
CocacolaEntry.grid(row=4,column=1,pady=10)
CocacolaEntry.insert(0,0)

DewLabel=Label(drinksFrame,text='Mountain-Dew',font=('Times new roman',13,'bold'),bg='gray20',fg='white')
DewLabel.grid(row=5,column=0,pady=10,sticky='w')

DewEntry=Entry(drinksFrame,font=('Times new roman',13,'bold'),width=10,bd=5)
DewEntry.grid(row=5,column=1,pady=10)
DewEntry.insert(0,0)

billframe=Frame(productsFrame,bd=5,relief=GROOVE)
billframe.grid(row=0,column=3,padx=12)

billareaLabel=Label(billframe,text='Bill Area',font=('Times New Roman',13,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

BillMenuFrame=LabelFrame(root,text='Bill Menu',font=('Times new roman',12,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
BillMenuFrame.pack()

coLabel=Label(BillMenuFrame, text='Cosmetic Price', font=('Times new roman', 12, 'bold'), bg='gray20', fg='white')
coLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

cosmeticpriceEntry=Entry(BillMenuFrame,font=('Times new roman',12,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=9,padx=10)

grocerypriceLabel=Label(BillMenuFrame, text='Grocery Price', font=('Times new roman', 12, 'bold'), bg='gray20', fg='white')
grocerypriceLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

grocerypriceEntry=Entry(BillMenuFrame,font=('Times new roman',12,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=9,padx=10)

drinkspriceLabel=Label(BillMenuFrame, text='Drinks Price', font=('Times new roman', 12, 'bold'), bg='gray20', fg='white')
drinkspriceLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

drinkspriceEntry=Entry(BillMenuFrame,font=('Times new roman',12,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=9,padx=10)



cosmetictaxLabel=Label(BillMenuFrame, text='Cosmetic Tax', font=('Times new roman', 12, 'bold'), bg='gray20', fg='white')
cosmetictaxLabel.grid(row=0, column=2, pady=9, padx=10, sticky='w')

cosmetictaxEntry=Entry(BillMenuFrame,font=('Times new roman',12,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=9,padx=10)

grocerytaxLabel=Label(BillMenuFrame, text='Grocery Tax', font=('Times new roman', 12, 'bold'), bg='gray20', fg='white')
grocerytaxLabel.grid(row=1, column=2, pady=9, padx=10, sticky='w')

grocerytaxEntry=Entry(BillMenuFrame,font=('Times new roman',12,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=9,padx=10)

drinkstaxLabel=Label(BillMenuFrame, text='Drinks Tax', font=('Times new roman', 12, 'bold'), bg='gray20', fg='white')
drinkstaxLabel.grid(row=2, column=2, pady=9, padx=10, sticky='w')

drinkstaxEntry=Entry(BillMenuFrame,font=('Times new roman',12,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=9,padx=10)

buttonFrame=Frame(BillMenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

TotalButton=Button(buttonFrame, text='Total', font=('arial', 16, 'bold')
                   , bg='gray20', fg='white', bd=5, width=8, pady=10,command=total)
TotalButton.grid(row=0, column=0, pady=20, padx=5)

BillButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold')
                   ,bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area )
BillButton.grid(row=0,column=1,pady=20,padx=5)

EmailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold')
                   ,bg='gray20',fg='white',bd=5,width=8,pady=10)
EmailButton.grid(row=0,column=2,pady=20,padx=5)

PrintButton=Button(buttonFrame,text='Print',font=('arial',16,'bold')
                   ,bg='gray20',fg='white',bd=5,width=8,pady=10,command=print_bill)
PrintButton.grid(row=0,column=3,pady=20,padx=5)

ClearButton=Button(buttonFrame, text='Clear', font=('arial', 16, 'bold')
                   , bg='gray20', fg='white', bd=5, width=8, pady=10)
ClearButton.grid(row=0, column=4, pady=20, padx=5)



root.mainloop()
