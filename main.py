from tkinter import *
import tkintermapview

root = Tk()
root.geometry("1200x700")
root.title("Mapa szkół")


ramka_lista_obiektow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)


# ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_obiektow, text="Lista:")
label_lista_obiektow.grid(row=0, column=0)

listbox_lista_obiektow=Listbox(ramka_lista_obiektow, width=50, height=10)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)

button_pokaz_szczegoly=Button(ramka_lista_obiektow, text='Pokaż szczegóły')
button_pokaz_szczegoly.grid(row=2, column=0)

button_usun_obiekt=Button(ramka_lista_obiektow, text='Usuń')
button_usun_obiekt.grid(row=2, column=1)

button_edytuj_obiekt=Button(ramka_lista_obiektow, text='Edytuj')
button_edytuj_obiekt.grid(row=2, column=2)



# 3_ramki_formularzy
ramka_szkola = Frame(ramka_formularz)
ramka_pracownik = Frame(ramka_formularz)
ramka_uczen = Frame(ramka_formularz)

button_formularz_szkola = Button(ramka_formularz, text="Formularz szkoły")
button_formularz_szkola.grid(row=0, column=0)

button_formularz_pracownik = Button(ramka_formularz, text="Formularz pracownika")
button_formularz_pracownik.grid(row=0, column=1)

button_formularz_uczen = Button(ramka_formularz, text="Formularz ucznia")
button_formularz_uczen.grid(row=0, column=2)



#formularz_szkoly
label_rodzaj_szkoly = Label(ramka_szkola, text="Rodzaj szkoły:")
label_rodzaj_szkoly.grid(row=0, column=0, sticky=W)
entry_rodzaj_szkoly = Entry(ramka_szkola)
entry_rodzaj_szkoly.grid(row=0, column=1)

label_numer_szkoly = Label(ramka_szkola, text="Numer szkoły:")
label_numer_szkoly.grid(row=1, column=0, sticky=W)
entry_numer_szkoly = Entry(ramka_szkola)
entry_numer_szkoly.grid(row=1, column=1)

label_szkola_miejscowosc = Label(ramka_szkola, text="Miejscowość:")
label_szkola_miejscowosc.grid(row=2, column=0, sticky=W)
entry_szkola_miejscowosc = Entry(ramka_szkola)
entry_szkola_miejscowosc.grid(row=2, column=1)

button_dodaj_szkole = Button(ramka_szkola, text="Dodaj szkołę")
button_dodaj_szkole.grid(row=2, column=0, columnspan=2)



# Formularz pracownika
label_pracownik_imie = Label(ramka_pracownik, text="Imię:")
label_pracownik_imie.grid(row=0, column=0, sticky=W)
entry_pracownik_imie = Entry(ramka_pracownik)
entry_pracownik_imie.grid(row=0, column=1)

label_pracownik_nazwisko = Label(ramka_pracownik, text="Nazwisko:")
label_pracownik_nazwisko.grid(row=1, column=0, sticky=W)
entry_pracownik_nazwisko = Entry(ramka_pracownik)
entry_pracownik_nazwisko.grid(row=1, column=1)

label_pracownik_stanowisko = Label(ramka_pracownik, text="Stanowisko:")
label_pracownik_stanowisko.grid(row=2, column=0, sticky=W)
entry_pracownik_stanowisko = Entry(ramka_pracownik)
entry_pracownik_stanowisko.grid(row=2, column=1)

button_dodaj_pracownika = Button(ramka_pracownik, text="Dodaj pracownika")
button_dodaj_pracownika.grid(row=3, column=0, columnspan=2)



# Formularz ucznia
label_uczen_imie = Label(ramka_uczen, text="Imię:")
label_uczen_imie.grid(row=0, column=0, sticky=W)
entry_uczen_imie = Entry(ramka_uczen)
entry_uczen_imie.grid(row=0, column=1)

label_uczen_nazwisko = Label(ramka_uczen, text="Nazwisko:")
label_uczen_nazwisko.grid(row=1, column=0, sticky=W)
entry_uczen_nazwisko = Entry(ramka_uczen)
entry_uczen_nazwisko.grid(row=1, column=1)

label_uczen_klasa = Label(ramka_uczen, text="Klasa:")
label_uczen_klasa.grid(row=2, column=0, sticky=W)
entry_uczen_klasa = Entry(ramka_uczen)
entry_uczen_klasa.grid(row=2, column=1)

button_dodaj_ucznia = Button(ramka_uczen, text="Dodaj ucznia")
button_dodaj_ucznia.grid(row=4, column=0, columnspan=2)



# ramka_szczegoly_obiektow
ramka_szczegoly_szkola = Frame(ramka_szczegoly_obiektow)
ramka_szczegoly_pracownik = Frame(ramka_szczegoly_obiektow)
ramka_szczegoly_uczen = Frame(ramka_szczegoly_obiektow)



# Szczegóły szkoły
label_szczegoly_szkola = Label(ramka_szczegoly_szkola, text="Szczegóły szkoły:")
label_szczegoly_szkola.grid(row=0, column=0)

label_szczegoly_szkola_rodzaj = Label(ramka_szczegoly_szkola, text="Rodzaj:")
label_szczegoly_szkola_rodzaj.grid(row=1, column=0)

label_szczegoly_szkola_rodzaj_wartosc = Label(ramka_szczegoly_szkola, text="....")
label_szczegoly_szkola_rodzaj_wartosc.grid(row=1, column=1)

label_szczegoly_szkola_numer = Label(ramka_szczegoly_szkola, text="Numer:")
label_szczegoly_szkola_numer.grid(row=1, column=2)

label_szczegoly_szkola_numer_wartosc = Label(ramka_szczegoly_szkola, text="....")
label_szczegoly_szkola_numer_wartosc.grid(row=1, column=3)

label_szczegoly_szkola_miejscowosc = Label(ramka_szczegoly_szkola, text="Miejscowość:")
label_szczegoly_szkola_miejscowosc.grid(row=1, column=4)

label_szczegoly_szkola_miejscowosc_wartosc = Label(ramka_szczegoly_szkola, text="....")
label_szczegoly_szkola_miejscowosc_wartosc.grid(row=1, column=5)



# Szczegóły pracownika
label_szczegoly_pracownik = Label(ramka_szczegoly_pracownik, text="Szczegóły pracownika:")
label_szczegoly_pracownik.grid(row=0, column=0)

label_szczegoly_pracownik_imie = Label(ramka_szczegoly_pracownik, text="Imię:")
label_szczegoly_pracownik_imie.grid(row=1, column=0)

label_szczegoly_pracownik_imie_wartosc = Label(ramka_szczegoly_pracownik, text="....")
label_szczegoly_pracownik_imie_wartosc.grid(row=1, column=1)

label_szczegoly_pracownik_nazwisko = Label(ramka_szczegoly_pracownik, text="Nazwisko:")
label_szczegoly_pracownik_nazwisko.grid(row=1, column=2)

label_szczegoly_pracownik_nazwisko_wartosc = Label(ramka_szczegoly_pracownik, text="....")
label_szczegoly_pracownik_nazwisko_wartosc.grid(row=1, column=3)

label_szczegoly_pracownik_stanowisko = Label(ramka_szczegoly_pracownik, text="Stanowisko:")
label_szczegoly_pracownik_stanowisko.grid(row=1, column=4)

label_szczegoly_pracownik_stanowisko_wartosc = Label(ramka_szczegoly_pracownik, text="....")
label_szczegoly_pracownik_stanowisko_wartosc.grid(row=1, column=5)



# Szczegóły ucznia
label_szczegoly_uczen = Label(ramka_szczegoly_uczen, text="Szczegóły ucznia:")
label_szczegoly_uczen.grid(row=0, column=0)

label_szczegoly_uczen_imie = Label(ramka_szczegoly_uczen, text="Imię:")
label_szczegoly_uczen_imie.grid(row=1, column=0)

label_szczegoly_uczen_imie_wartosc = Label(ramka_szczegoly_uczen, text="....")
label_szczegoly_uczen_imie_wartosc.grid(row=1, column=1)

label_szczegoly_uczen_nazwisko = Label(ramka_szczegoly_uczen, text="Nazwisko:")
label_szczegoly_uczen_nazwisko.grid(row=1, column=2)

label_szczegoly_uczen_nazwisko_wartosc = Label(ramka_szczegoly_uczen, text="....")
label_szczegoly_uczen_nazwisko_wartosc.grid(row=1, column=3)

label_szczegoly_uczen_klasa = Label(ramka_szczegoly_uczen, text="Klasa:")
label_szczegoly_uczen_klasa.grid(row=1, column=4)

label_szczegoly_uczen_klasa_wartosc = Label(ramka_szczegoly_uczen, text="....")
label_szczegoly_uczen_klasa_wartosc.grid(row=1, column=5)



# Pokaż tylko szczegóły szkoły na start
ramka_szczegoly_szkola.grid(row=0, column=0)



# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=400, corner_radius=0)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23, 21.00)
map_widget.set_zoom(6)




root.mainloop()