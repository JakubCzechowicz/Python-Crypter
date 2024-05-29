import hashlib
import tkinter as tk
from tkinter import ttk


def szyfruj():
    tekst_szyfrowany = tekst_wejsciowy.get()
    metoda_szyfrowania = metoda_combobox.current()
    format_wyjsciowy = format_combobox.current()

    if metoda_szyfrowania == 0:
        h = hashlib.sha256()
    elif metoda_szyfrowania == 1:
        h = hashlib.sha512()
    elif metoda_szyfrowania == 2:
        h = hashlib.blake2b()
    elif metoda_szyfrowania == 3:
        h = hashlib.sha1()
    elif metoda_szyfrowania == 4:
        h = hashlib.md5()
    elif metoda_szyfrowania == 5:
        h = hashlib.sha384()
    elif metoda_szyfrowania == 6:
        h = hashlib.sha224()
    else:
        wynik_label.configure(text="Nieznana metoda szyfrowania")
        return

    h.update(tekst_szyfrowany.encode('utf-8'))

    if format_wyjsciowy == 0:
        wynik_label.configure(text="Zaszyfrowany tekst: " + h.digest().hex())
    elif format_wyjsciowy == 1:
        wynik_label.configure(text="Zaszyfrowany tekst: " + h.hexdigest())
    else:
        wynik_label.configure(text="Nieznany format wyjściowy")

root = tk.Tk()
root.title("Program Szyfrujący")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(mainframe, text="Podaj tekst, który chcesz zaszyfrować:").grid(column=0, row=0, sticky=tk.W)
tekst_wejsciowy = ttk.Entry(mainframe, width=50)
tekst_wejsciowy.grid(column=0, row=1)

ttk.Label(mainframe, text="Wybierz metode szyfrowania:").grid(column=0, row=2, sticky=tk.W)
metoda_combobox = ttk.Combobox(mainframe, values=["sha-256", "sha-512", "blake2b", "sha-1", "md5", "sha-384", "sha-224"])
metoda_combobox.grid(column=0, row=3)
metoda_combobox.current(0)

ttk.Label(mainframe, text="Wybierz format wyjściowy:").grid(column=0, row=4, sticky=tk.W)
format_combobox = ttk.Combobox(mainframe, values=["digest", "hexdigest"])
format_combobox.grid(column=0, row=5)
format_combobox.current(0)

szyfruj_button = ttk.Button(mainframe, text="Szyfruj", command=szyfruj)
szyfruj_button.grid(column=0, row=6)

wynik_label = ttk.Label(mainframe, text="")
wynik_label.grid(column=0, row=7)

root.mainloop()
