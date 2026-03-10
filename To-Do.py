import tkinter as tk
from tkinter import messagebox

def gorev_ekle():
    gorev = gorev_giris.get()
    if gorev != "":
        gorev_listesi.insert(tk.END, "• " + gorev)
        gorev_giris.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Lütfen boş bir görev eklemeyin.")

def gorev_sil():
    try:
        secili_gorev_index = gorev_listesi.curselection()[0]
        gorev_listesi.delete(secili_gorev_index)
    except IndexError:
        messagebox.showwarning("Uyarı", "Lütfen silmek için bir görev seçin.")

def tumunu_temizle():
    gorev_listesi.delete(0, tk.END)

pencere = tk.Tk()
pencere.title("Yapılacaklar Listesi")
pencere.geometry("400x500")
pencere.config(bg="#2c3e50") 
pencere.resizable(False, False)

ana_font = ("Segoe UI", 12)
baslik_font = ("Segoe UI", 16, "bold")

baslik_etiket = tk.Label(pencere, text="📝 Günlük Görevlerim", font=baslik_font, bg="#2c3e50", fg="#ecf0f1", pady=15)
baslik_etiket.pack()

giris_cercevesi = tk.Frame(pencere, bg="#2c3e50")
giris_cercevesi.pack(pady=10)

gorev_giris = tk.Entry(giris_cercevesi, font=ana_font, width=22, bd=0, relief=tk.FLAT)
gorev_giris.pack(side=tk.LEFT, padx=10, ipady=6)

ekle_butonu = tk.Button(giris_cercevesi, text="Ekle", font=("Segoe UI", 10, "bold"), bg="#27ae60", fg="white", bd=0, cursor="hand2", command=gorev_ekle)
ekle_butonu.pack(side=tk.LEFT, ipadx=12, ipady=4)

liste_cercevesi = tk.Frame(pencere, bg="#2c3e50")
liste_cercevesi.pack(pady=10)

gorev_listesi = tk.Listbox(liste_cercevesi, font=ana_font, width=32, height=12, bg="#34495e", fg="white", bd=0, selectbackground="#2980b9", activestyle="none", highlightthickness=0)
gorev_listesi.pack(side=tk.LEFT, fill=tk.BOTH)

kaydirma_cubugu = tk.Scrollbar(liste_cercevesi)
kaydirma_cubugu.pack(side=tk.RIGHT, fill=tk.Y)
gorev_listesi.config(yscrollcommand=kaydirma_cubugu.set)
kaydirma_cubugu.config(command=gorev_listesi.yview)

buton_cercevesi = tk.Frame(pencere, bg="#2c3e50")
buton_cercevesi.pack(pady=20)

sil_butonu = tk.Button(buton_cercevesi, text="Seçileni Sil", font=("Segoe UI", 10, "bold"), bg="#e74c3c", fg="white", bd=0, cursor="hand2", command=gorev_sil)
sil_butonu.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

temizle_butonu = tk.Button(buton_cercevesi, text="Tümünü Temizle", font=("Segoe UI", 10, "bold"), bg="#f39c12", fg="white", bd=0, cursor="hand2", command=tumunu_temizle)
temizle_butonu.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

pencere.mainloop()