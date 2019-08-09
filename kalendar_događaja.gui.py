from tkinter import *
from sqlite3 import *

con = connect("kalendar_događaja.db") 
k = con.cursor() 

master = Tk()
master.title("Kalendar Događaja") 
master.geometry("1050x760")
master.configure(background = "#08295e")



Zaglavlje = Label(master, text="- Kalendar događaja -", font=("Times", 36,"bold"), fg="#08295e", bg="#f5b79a", bd="5", relief="raised").place(relx=0.5, rely=0.01, relwidth=0.65, relheight=0.1, anchor="n")

L0 = Label(master, text = "Dodajte novi događaj:", font=("Times", 18, "bold"), bd="3.5", fg="#08295e", bg="#f5b79a", relief="raised").place(relx=0.2, rely=0.13, relwidth=0.25, relheight=0.05, anchor="n")

L1 = Label(master, text = "Naziv događaja", font=("Times", 18, "bold"), bd="3.5", fg="#08295e", bg="#f5b79a", relief="raised").place(relx=0.1, rely=0.2, relwidth=0.18, relheight=0.05, anchor="n")

L2 = Label(master, text = "Datum događaja", font=("Times", 18, "bold"), bd="3.5", fg="#08295e", bg="#f5b79a", relief="raised").place(relx=0.3, rely=0.2, relwidth=0.18, relheight=0.05, anchor="n")
                                                                                                         
L3 = Label(master, text = "Opis događaja", font=("Times", 18, "bold"), bd="3.5", fg="#08295e", bg="#f5b79a", relief="raised").place(relx=0.2, rely=0.32, relwidth=0.3, relheight=0.05, anchor="n")

L4 = Label(master, text = "Potražite događaj:", font=("Times", 18, "bold"), bd="3.5", fg="#08295e", bg="#f5b79a", relief="raised").place(relx=0.75, rely=0.13, relwidth=0.35, relheight=0.05, anchor="n")

L5 = Label(master, text = "Navedite događaj koji želite uklonuti:", font=("Times", 18, "bold"), bd="3.5", fg="#08295e", bg="#f5b79a", relief="raised").place(relx=0.75, rely=0.85, relwidth=0.45, relheight=0.05, anchor="n")


naziv_događaja = Entry(master, bg="#ff5900", fg="#91bde3", font=("Times", 16))
naziv_događaja.place(relx=0.1, rely=0.25, relwidth=0.18, relheight=0.05, anchor="n")

datum_događaja = Entry(master, bg="#ff5900", fg="#91bde3", font=("Times", 16))
datum_događaja.place(relx=0.3, rely=0.25, relwidth=0.18, relheight=0.05, anchor="n")

opis_događaja = Entry(master, bg="#ff5900", fg="#91bde3", font=("Times", 16))
opis_događaja.place(relx=0.2, rely=0.4, relwidth=0.3, relheight=0.5, anchor="n")

event_name = Entry(master, bg="#ff5900", fg="#91bde3", font=("Times", 16))
event_name.place(relx=0.7, rely=0.2, relwidth=0.18, relheight=0.05, anchor="n")

uklanjanje_događaja = Entry(master, bg="#ff5900", fg="#91bde3", font=("Times", 16))
uklanjanje_događaja.place(relx=0.65, rely=0.92, relwidth=0.2, relheight=0.05, anchor="n")

okvir = Frame(master, bg="#ff5900")
okvir.place(relx=0.75, rely=0.28, relwidth=0.25, relheight=0.4, anchor="n")
            
popis = Listbox(okvir, bg="#ff5900", fg="#91bde3", height = 12, width = 53, font=("Times", 12), selectmode="single") 
popis.pack(side = LEFT, fill = Y)
            
scroll = Scrollbar(okvir, orient = VERTICAL)
scroll.config(command = popis.yview)
scroll.pack(side = RIGHT, fill = Y)
popis.config(yscrollcommand = scroll.set)



def dodaj_događaj():
        print("Dodali ste događaj.")
        k.execute("INSERT INTO događaji (naziv_događaja, datum_događaja, opis_događaja) VALUES (?, ?, ?)", (naziv_događaja.get(), datum_događaja.get(),  opis_događaja.get() ))
        con.commit()

        naziv_događaja.delete(0, END)
        opis_događaja.delete(0, END)
        datum_događaja.delete(0,END)
        
       

def popis_događaja():
        print("Potražili ste:")     
        k.execute("SELECT * FROM događaji WHERE naziv_događaja = ?", (event_name.get(),))
        
        a = k.execute("SELECT naziv_događaja FROM događaji WHERE naziv_događaja LIKE (?)", (event_name.get(),))
        podaci = k.fetchall()
        for a in podaci:
                popis.insert(1, a)

        con.commit()

        event_name.delete(0, END)
        

def ispis():
        print("Pronađeni su sljedeći događaji: ")
        k.execute("SELECT naziv_događaja FROM događaji ORDER BY naziv_događaja ASC")
        podaci = k.fetchall()
            
        for row in podaci:
                popis.insert(1, row)         

        con.commit()

def prikaz():
       index = popis.curselection()[0]
       k.execute("SELECT * FROM događaji ORDER BY naziv_događaja ASC")
       podaci = k.fetchall()
       događaj = podaci[index]
       naslov_prikaza = događaj[0]
       datum_prikaza = događaj[1]
       tekst_prikaza = događaj[2]
       
       print("Odabrali ste događaj: " + str(naslov_prikaza))
       
       događaj_prikaz = Toplevel(master)
       događaj_prikaz.title((naslov_prikaza)) 
       događaj_prikaz.geometry("360x420")
       događaj_prikaz.configure(background="#08295e")
       display = Label(događaj_prikaz, text=(str(naslov_prikaza)+"\n"+"\n"+str(datum_prikaza)+"\n"+"\n"+str(tekst_prikaza)), font=("Times", 16),  bg="#f5b79a", fg="#08295e")
       display.pack()

def clear():
        popis.delete(0, END)

def delete():
        k.execute("DELETE FROM događaji WHERE naziv_događaja = '" + uklanjanje_događaja.get() + "'")
        print("Uklonuli ste navedeni događaj")
        uklanjanje_događaja.delete(0, END)
        
        con.commit()
        

save = Button(master, text="Pohrani", command=dodaj_događaj, font=("Times", 16, "bold"), fg="#08295e",  bg="#f5b79a", relief="raised")
save.place(relx=0.2, rely=0.920, relwidth=0.12, relheight=0.05, anchor="n")

search = Button(master, text="Potraži", command=popis_događaja, font=("Times", 16, "bold"), fg="#08295e", bg="#f5b79a", relief="raised")
search.place(relx=0.85, rely=0.2, relwidth=0.10, relheight=0.05, anchor="n")

show_list = Button(master, text="Izlistaj sve", command=ispis, font=("Times", 16, "bold"), fg="#08295e", bg="#f5b79a", relief="raised")
show_list.place(relx=0.75, rely=0.7, relwidth=0.28, relheight=0.05, anchor="n")

show = Button(master, text="Prikaži", command=prikaz, font=("Times", 16, "bold"), fg="#08295e", bg="#f5b79a", relief="raised")
show.place(relx=0.65, rely=0.76, relwidth=0.15, relheight=0.05, anchor="n")

clear = Button(master, text="Očisti", command=clear, font=("Times", 16, "bold"), fg="#08295e", bg="#f5b79a", relief="raised")
clear.place(relx=0.85, rely=0.76, relwidth=0.15, relheight=0.05, anchor="n")

delete_button = Button(master, text="Ukloni", command=delete, font=("Times", 16, "bold"), fg="#08295e", bg="#f5b79a", relief="raised")
delete_button.place(relx=0.85, rely=0.92, relwidth=0.10, relheight=0.05, anchor="n")


master.mainloop()
k.close()
con.close()
