from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def şifre_oluştur():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for l in range(randint(8, 10))]
    symbol_list = [choice(symbols) for s in range(randint(2, 4))]
    number_list = [choice(numbers) for n in range(randint(2, 4))]
    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)

    password = "".join(password_list)
    şifre_giriş.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def ekle():
    website = website_giriş.get().capitalize()
    email = email_kullanıcıAdı_giriş.get()
    sifre = şifre_giriş.get()
    yeni_data = {
        website: {
            "email": email,
            "sifre": sifre,
        }
    }

    if len(website) == 0 or len(sifre) == 0:
        messagebox.showwarning(title="Oppss", message="Hiçbir alanı boş bırakmayın!")
    else:
        #data.json dosyasını oku
        try:
            with open("data.json", "r") as data_dosyası:
                data = json.load(data_dosyası) #eski veriyi okudu
        #eğer öyle bir dosya yoksa olustur
        except FileNotFoundError:
            with open("data.json", "w") as data_dosyası:
                json.dump(yeni_data, data_dosyası, indent=4)
        #try çalışırsa bunu çalıştır. veriyi günceller ve kaydeder.
        else:
            data.update(yeni_data)
            with open("data.json", "w") as data_dosyası:
                json.dump(data, data_dosyası, indent=4)
        #en nihayetinde bu kodları nolursa olsun çalıstır.İnput kısımlarını temizler
        finally:
            website_giriş.delete(0, END)
            şifre_giriş.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #

def arama():
    aranan_site = website_giriş.get().capitalize()
    try:
        with open("data.json", "r") as data_dosyası:
            data = json.load(data_dosyası)
    except FileNotFoundError:
        messagebox.showwarning(title="Oppss", message="Kaydedilmiş şifreniz yok!")
    else:
        for key, value in data.items():
            if key == aranan_site:
                messagebox.showinfo(title=f"{key}", message=f"E-mail: {value['email']}\n Şifre: {value['sifre']}")
            else:
                messagebox.showwarning(title="Arama", message="Sonuç bulunamadı!")






# ---------------------------- UI SETUP ------------------------------- #

pencere = Tk()
pencere.title("Şifre Yöneticisi")
pencere.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
resim = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=resim)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

email_kullanıcıAdı = Label(text="E-mail/Kullanıcı Adı:")
email_kullanıcıAdı.grid(column=0, row=2)

şifre = Label(text="Şifre:")
şifre.grid(column=0, row=3)

website_giriş = Entry(width=22)
website_giriş.focus()
website_giriş.grid(column=1, row=1)

email_kullanıcıAdı_giriş = Entry(width=37)
email_kullanıcıAdı_giriş.insert(END, "mucahitakca2703@gmail.com")
email_kullanıcıAdı_giriş.grid(column=1, row=2, columnspan=2)

şifre_giriş = Entry(width=22)
şifre_giriş.grid(column=1, row=3)

şifre_oluştur = Button(text="Şifre Oluştur", command=şifre_oluştur)
şifre_oluştur.grid(row=3, column=2)

ekle = Button(text="Ekle", width=36, command=ekle)
ekle.grid(column=1, row=4, columnspan=2)

arama = Button(text="Ara", width=12, command=arama)
arama.grid(column=2, row=1)


pencere.mainloop()