from tkinter import *
import tkintermapview
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import StringVar


root = Tk()
root.geometry("1200x700")
root.title("Zarządzanie szkołami w mieście, uczniami i pracownikami")



#SZKOLY
schools: list = []
selected_school = None

class School:
    def __init__(self, rodzaj, numer, miejscowosc, map_widget):
        self.rodzaj = rodzaj
        self.numer = numer
        self.miejscowosc = miejscowosc
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1], text=f'{self.rodzaj} {self.numer}')


    def get_coordinates(self)-> list:
        import requests
        from bs4 import BeautifulSoup
        adres_url = f'https://pl.wikipedia.org/wiki/{self.miejscowosc}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.'))
        ]

def add_school():
    rodzaj = entry_rodzaj_szkoly.get()
    numer = entry_numer_szkoly.get()
    miejscowosc = entry_szkola_miejscowosc.get()

    new_school = School(rodzaj=rodzaj, numer=numer, miejscowosc=miejscowosc, map_widget=map_widget)
    schools.append(new_school)
    print(schools)

    entry_rodzaj_szkoly.delete(0, END)
    entry_numer_szkoly.delete(0, END)
    entry_szkola_miejscowosc.delete(0, END)

    entry_rodzaj_szkoly.focus()
    show_schools()
    update_dropdown()

dropdown_school = ttk.Combobox(root, values=[])


def update_dropdown():
    dropdown_school['values'] = [f'{s.rodzaj} {s.numer}' for s in schools]
    schools_combobox_employee['values'] = [f'{s.rodzaj} {s.numer}' for s in schools]
    schools_combobox_student['values'] = [f'{s.rodzaj} {s.numer}' for s in schools]


def show_schools():
    listbox_lista_szkol.delete(0,END)
    for idx,school in enumerate(schools):
        listbox_lista_szkol.insert(idx, f'{idx+1}. {school.rodzaj} nr {school.numer} ({school.miejscowosc})')


def delete_school():
    i = listbox_lista_szkol.index(ACTIVE)
    delete_school = schools [i]
    print(i)
    schools[i].marker.delete()

    #Usuwanie uczniów przypisanych do szkoły
    for student in students:
        if student.szkola == delete_school:
            student.marker.delete()
            students.remove(student)

    #Usuwanie pracowników przypisanych do szkoły
    for employee in employees:
        if employee.szkola == delete_school:
            employee.marker.delete()
            employees.remove(employee)

    schools.pop(i)
    show_schools()
    update_dropdown()
    show_students()
    show_employees()


def edit_school():
    i = listbox_lista_szkol.index(ACTIVE)
    school = schools[i]
    rodzaj = school.rodzaj
    numer = school.numer
    miejscowosc = school.miejscowosc

    entry_rodzaj_szkoly.insert(0, school.rodzaj)
    entry_numer_szkoly.insert(0, school.numer)
    entry_szkola_miejscowosc.insert(0, school.miejscowosc)

    button_dodaj_szkole.config(text="Zapisz", command=lambda: update_school(i))

    update_dropdown()


def update_school(i):
    rodzaj = entry_rodzaj_szkoly.get()
    numer = entry_numer_szkoly.get()
    miejscowosc = entry_szkola_miejscowosc.get()

    schools[i].rodzaj = rodzaj
    schools[i].numer = numer
    schools[i].miejscowosc = miejscowosc

    schools[i].coordinates = schools[i].get_coordinates()
    schools[i].marker.delete()
    schools[i].marker = map_widget.set_marker(schools[i].coordinates[0], schools[i].coordinates[1], text=f'{rodzaj} {numer}')

    # Aktualizowanie uczniów szkoły
    for student in students:
        if student.szkola == schools[i]:
            student.miejscowosc = miejscowosc
            student.coordinates = student.get_coordinates()
            student.marker.delete()
            student.marker = map_widget_uczen.set_marker(
                student.coordinates[0], student.coordinates[1],
                text=f'{student.imie} {student.nazwisko}'
            )

    #Aktualizowanie pracowników szkoły
    for employee in employees:
        if employee.szkola == schools[i]:
            employee.miejscowosc = miejscowosc
            employee.coordinates = employee.get_coordinates()
            employee.marker.delete()
            employee.marker = map_widget_pracownik.set_marker(
                employee.coordinates[0], employee.coordinates[1],
                text=f'{employee.imie} {employee.nazwisko}'
            )

    entry_rodzaj_szkoly.delete(0, END)
    entry_numer_szkoly.delete(0, END)
    entry_szkola_miejscowosc.delete(0, END)
    button_dodaj_szkole.config(text="Dodaj szkołę", command=add_school)

    show_schools()
    update_dropdown()


def show_school_details():
    i = listbox_lista_szkol.index(ACTIVE)
    selected_school = schools[i]

    listbox_lista_pracownikow.delete(0, END)
    listbox_lista_uczniow.delete(0, END)

    for employee in employees:
        if employee.szkola == selected_school:
                listbox_lista_pracownikow.insert(END, f'{employee.imie} {employee.nazwisko} {employee.stanowisko} ({employee.klasa})')

    for student in students:
        if student.szkola == selected_school:
            listbox_lista_uczniow.insert(END, f'{student.imie} {student.nazwisko} ({student.klasa})')

    map_widget.set_zoom(15)
    map_widget.set_position(schools[i].coordinates[0], schools[i].coordinates[1])


def get_location_by_school_rodzaj(szkola_rodzaj: str) -> str:
    for school in schools:
        if f"{school.rodzaj} {school.numer}" == szkola_rodzaj:
            return school.miejscowosc
    return None



#UCZNIOWIE
students: list =[]

class Student:
    def __init__(self, imie, nazwisko, klasa, szkola, miejscowosc, map_widget):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
        self.szkola = szkola
        self.miejscowosc = miejscowosc
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],text=f'{self.imie} {self.nazwisko}')

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/{self.miejscowosc}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]


def add_student():
    imie = entry_uczen_imie.get()
    nazwisko = entry_uczen_nazwisko.get()
    klasa = entry_uczen_klasa.get()
    selected_school = schools_combobox_student.get()
    miejscowosc = get_location_by_school_rodzaj(selected_school)

    selected_school = schools[schools_combobox_employee.current()]

    new_student = Student(imie=imie, nazwisko=nazwisko, klasa=klasa, szkola=selected_school, miejscowosc=miejscowosc, map_widget=map_widget_uczen)

    students.append(new_student)
    print(students)

    entry_uczen_imie.delete(0, END)
    entry_uczen_nazwisko.delete(0, END)
    entry_uczen_klasa.delete(0, END)
    schools_combobox_student.set('')

    entry_uczen_imie.focus()
    show_students()


def show_students():
    listbox_lista_uczniow.delete(0, END)
    for idx, student in enumerate(students):
        listbox_lista_uczniow.insert(idx, f'{idx+1}. {student.imie} {student.nazwisko} ({student.klasa})')


def delete_student():
    i = listbox_lista_uczniow.index(ACTIVE)
    print(i)
    students[i].marker.delete()
    students.pop(i)
    show_students()


def edit_student():
    i = listbox_lista_uczniow.index(ACTIVE)
    Student = students[i]
    imie = students[i].imie
    nazwisko = students[i].nazwisko
    klasa = students[i].klasa
    szkola = students[i].szkola
    miejscowosc = students[i].miejscowosc

    entry_uczen_imie.insert(0, Student.imie)
    entry_uczen_nazwisko.insert(0, Student.nazwisko)
    entry_uczen_klasa.insert(0, Student.klasa)
    entry_uczen_miejscowosc.insert(0, Student.miejscowosc)

    szkola_var = StringVar()
    optionmenu_szkola = OptionMenu(root, szkola_var, ramka_lista_szkol)
    szkola_var.set(szkola)

    button_dodaj_ucznia.config(text="Zapisz", command=lambda: update_student(i))


def update_student(i):
    imie = entry_uczen_imie.get()
    nazwisko = entry_uczen_nazwisko.get()
    klasa = entry_uczen_klasa.get()
    miejscowosc = entry_uczen_miejscowosc.get()

    students[i].imie = imie
    students[i].nazwisko = nazwisko
    students[i].klasa = klasa
    students[i].miejscowosc = miejscowosc

    students[i].coordinates = students[i].get_coordinates()
    students[i].marker.delete()
    students[i].marker = map_widget_uczen.set_marker(students[i].coordinates[0], students[i].coordinates[1],text=f'{students[i].imie} {students[i].nazwisko}')

    entry_uczen_imie.delete(0, END)
    entry_uczen_nazwisko.delete(0, END)
    entry_uczen_klasa.delete(0, END)
    entry_uczen_miejscowosc.delete(0, END)

    button_dodaj_ucznia.config(text="Dodaj ucznia", command=add_student)
    show_students()


def show_student_details():
    i = listbox_lista_uczniow.index(ACTIVE)
    map_widget_uczen.set_zoom(15)
    map_widget_uczen.set_position(students[i].coordinates[0], students[i].coordinates[1])



#PRACOWNICY
employees: list = []

class Employee:
    def __init__(self, imie, nazwisko, stanowisko, klasa, szkola, miejscowosc, map_widget):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.klasa = klasa
        self.szkola = szkola
        self.miejscowosc = miejscowosc
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1], text=f'{self.imie} {self.nazwisko}')


    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/{self.miejscowosc}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]


def add_employee():
    imie = entry_pracownik_imie.get()
    nazwisko = entry_pracownik_nazwisko.get()
    stanowisko = entry_pracownik_stanowisko.get()
    klasa = entry_pracownik_klasa.get()
    selected_school = schools_combobox_employee.get()
    miejscowosc = get_location_by_school_rodzaj(selected_school)

    selected_school = schools[schools_combobox_employee.current()]

    new_employee = Employee(imie=imie, nazwisko=nazwisko, stanowisko=stanowisko, klasa=klasa, szkola=selected_school, miejscowosc=miejscowosc, map_widget = map_widget_pracownik)

    employees.append(new_employee)
    print(employees)

    entry_pracownik_imie.delete(0, END)
    entry_pracownik_nazwisko.delete(0, END)
    entry_pracownik_stanowisko.delete(0, END)
    entry_pracownik_klasa.delete(0, END)
    schools_combobox_employee.set('')

    entry_pracownik_imie.focus()
    show_employees()


def show_employees():
    listbox_lista_pracownikow.delete(0, END)
    for idx, employee in enumerate(employees):
        listbox_lista_pracownikow.insert(idx, f'{idx+1}. {employee.imie} {employee.nazwisko} {employee.stanowisko} ({employee.klasa})')


def delete_employee():
    i = listbox_lista_pracownikow.index(ACTIVE)
    print(i)
    employees[i].marker.delete()
    employees.pop(i)
    show_employees()


def edit_employee():
    i = listbox_lista_pracownikow.index(ACTIVE)
    Employee = employees[i]
    imie = employees[i].imie
    nazwisko = employees[i].nazwisko
    stanowisko = employees[i].stanowisko
    klasa = employees[i].klasa
    miejscowosc = employees[i].miejscowosc

    entry_pracownik_imie.insert(0, Employee.imie)
    entry_pracownik_nazwisko.insert(0, Employee.nazwisko)
    entry_pracownik_stanowisko.insert(0, Employee.stanowisko)
    entry_pracownik_klasa.insert(0, Employee.klasa)

    button_dodaj_pracownika.config(text="Zapisz", command=lambda: update_employee(i))


def update_employee(i):
    imie = entry_pracownik_imie.get()
    nazwisko = entry_pracownik_nazwisko.get()
    stanowisko = entry_pracownik_stanowisko.get()
    klasa = entry_pracownik_klasa.get()
    miejscowosc = entry_pracownik_miejscowosc.get()

    employees[i].imie = imie
    employees[i].nazwisko = nazwisko
    employees[i].stanowisko = stanowisko
    employees[i].klasa = klasa
    employees[i].miejscowosc = miejscowosc

    employees[i].coordinates = employees[i].get_coordinates()
    employees[i].marker.delete()
    employees[i].marker = map_widget_pracownik.set_marker(employees[i].coordinates[0], employees[i].coordinates[1], text=f'{employees[i].imie} {employees[i].nazwisko}')

    entry_pracownik_imie.delete(0, END)
    entry_pracownik_nazwisko.delete(0, END)
    entry_pracownik_stanowisko.delete(0, END)
    entry_pracownik_klasa.delete(0, END)
    entry_pracownik_miejscowosc.delete(0, END)

    button_dodaj_pracownika.config(text="Dodaj pracownika", command=add_employee)
    show_employees()


def show_employee_details():
    i = listbox_lista_pracownikow.index(ACTIVE)
    map_widget_pracownik.set_zoom(15)
    map_widget_pracownik.set_position(employees[i].coordinates[0], employees[i].coordinates[1])



# RAMKI
ramka_lista_szkol=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_szkol.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)



# ramka_lista_szkol
label_lista_szkol=Label(ramka_lista_szkol, text="Lista szkół:")
label_lista_szkol.grid(row=0, column=0)

listbox_lista_szkol=Listbox(ramka_lista_szkol, width=50, height=10)
listbox_lista_szkol.grid(row=1, column=0, columnspan=3)

button_pokaz_szczegoly_szkola=Button(ramka_lista_szkol, text='Pokaż szczegóły', command=show_school_details)
button_pokaz_szczegoly_szkola.grid(row=2, column=0)

button_usun_obiekt=Button(ramka_lista_szkol, text='Usuń', command=delete_school)
button_usun_obiekt.grid(row=2, column=1)

button_edytuj_obiekt=Button(ramka_lista_szkol, text='Edytuj', command=edit_school)
button_edytuj_obiekt.grid(row=2, column=2)



#ramka_szczegoly_obiektow
#PRACOWNICY
label_pracownicy = Label(ramka_szczegoly_obiektow, text="Lista pracowników:")
label_pracownicy.grid(row=0, column=0)

listbox_lista_pracownikow = Listbox(ramka_szczegoly_obiektow, width=50, height=8)
listbox_lista_pracownikow.grid(row=1, column=0)

button_pokaz_szczegoly_pracownika=Button(ramka_szczegoly_obiektow, text='Pokaż szczegóły', command=show_employee_details)
button_pokaz_szczegoly_pracownika.grid(row=2, column=0, sticky=W)

button_edytuj_pracownika=Button(ramka_szczegoly_obiektow, text='Edytuj', command=edit_employee)
button_edytuj_pracownika.grid(row=2, column=0, padx=30)

button_usun_pracownika=Button(ramka_szczegoly_obiektow, text='Usuń', command=delete_employee)
button_usun_pracownika.grid(row=2, column=0, sticky=E)


#UCZNIOWIE
label_uczniowie = Label(ramka_szczegoly_obiektow, text="Lista uczniów:")
label_uczniowie.grid(row=0, column=1)

listbox_lista_uczniow = Listbox(ramka_szczegoly_obiektow, width=50, height=8)
listbox_lista_uczniow.grid(row=1, column=1)

button_pokaz_szczegoly_ucznia=Button(ramka_szczegoly_obiektow, text='Pokaż szczegóły', command=show_student_details)
button_pokaz_szczegoly_ucznia.grid(row=2, column=1, sticky=W)

button_edytuj_ucznia=Button(ramka_szczegoly_obiektow, text='Edytuj', command=edit_student)
button_edytuj_ucznia.grid(row=2, column=1)

button_usun_ucznia=Button(ramka_szczegoly_obiektow, text='Usuń', command=delete_student)
button_usun_ucznia.grid(row=2, column=1, sticky=E)



# 3 RAMKI FORMULARZY
ramka_szkola = Frame(ramka_formularz)
ramka_pracownik = Frame(ramka_formularz)
ramka_uczen = Frame(ramka_formularz)


def pokaz_formularz_szkola():
    ramka_szkola.grid(row=1, column=0, columnspan=3)
    ramka_pracownik.grid_forget()
    ramka_uczen.grid_forget()

def pokaz_formularz_pracownik():
    ramka_pracownik.grid(row=1, column=0, columnspan=3)
    ramka_szkola.grid_forget()
    ramka_uczen.grid_forget()

def pokaz_formularz_uczen():
    ramka_uczen.grid(row=1, column=0, columnspan=3)
    ramka_szkola.grid_forget()
    ramka_pracownik.grid_forget()


button_formularz_szkola = Button(ramka_formularz, text="Formularz szkoły", command=pokaz_formularz_szkola)
button_formularz_szkola.grid(row=0, column=0)

button_formularz_pracownik = Button(ramka_formularz, text="Formularz pracownika", command=pokaz_formularz_pracownik)
button_formularz_pracownik.grid(row=0, column=1)

button_formularz_uczen = Button(ramka_formularz, text="Formularz ucznia", command=pokaz_formularz_uczen)
button_formularz_uczen.grid(row=0, column=2)



# Formularz szkoły
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

button_dodaj_szkole = Button(ramka_szkola, text="Dodaj szkołę", command=add_school)
button_dodaj_szkole.grid(row=3, column=0, columnspan=2)



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

label_pracownik_klasa = Label(ramka_pracownik, text="Klasa:")
label_pracownik_klasa.grid(row=3, column=0, sticky=W)
entry_pracownik_klasa = Entry(ramka_pracownik)
entry_pracownik_klasa.grid(row=3, column=1)

label_szkola_dla_pracownika = Label(ramka_pracownik, text="Szkoła:")
label_szkola_dla_pracownika.grid(row=4, column=0, sticky=W)
schools_combobox_employee = Combobox(ramka_pracownik)
schools_combobox_employee.grid(row=4, column=1)

button_dodaj_pracownika = Button(ramka_pracownik, text="Dodaj pracownika", command=add_employee)
button_dodaj_pracownika.grid(row=5, column=0, columnspan=2)

entry_pracownik_miejscowosc = Entry(ramka_pracownik)


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

label_szkola_dla_ucznia = Label(ramka_uczen, text="Szkoła:")
label_szkola_dla_ucznia.grid(row=3, column=0, sticky=W)
schools_combobox_student = Combobox(ramka_uczen)
schools_combobox_student.grid(row=3, column=1)

button_dodaj_ucznia = Button(ramka_uczen, text="Dodaj ucznia", command=add_student)
button_dodaj_ucznia.grid(row=4, column=0, columnspan=2)

entry_uczen_miejscowosc = Entry(ramka_uczen)



# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=400, height=400, corner_radius=0)
map_widget.grid(row=0, column=0)
map_widget.set_position(52.23, 21.00)
map_widget.set_zoom(6)


map_widget_uczen = tkintermapview.TkinterMapView(ramka_mapa, width=400, height=400, corner_radius=0)
map_widget_uczen.grid(row=0, column=3)
map_widget_uczen.set_position(52.23, 21.00)
map_widget_uczen.set_zoom(6)


map_widget_pracownik = tkintermapview.TkinterMapView(ramka_mapa, width=400, height=400, corner_radius=0)
map_widget_pracownik.grid(row=0, column=2)
map_widget_pracownik.set_position(52.23, 21.00)
map_widget_pracownik.set_zoom(6)



root.mainloop()