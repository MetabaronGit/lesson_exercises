film1 = {
'JMENO': 'Shawshank Redemption',
'HODNOCENI': 93,
'ROK': 1994,
'REZISER': 'Frank Darabont',
'HRAJI': ['Tim Robbins', 'Morgan Freeman'],
'STOPAZ': "144 min"
}

film2 = {
'JMENO': 'The Godfather',
'HODNOCENI': 92,
'ROK': 1972,
'REZISER': 'Francis Ford Coppola',
'HRAJI': ['Al Pacino', 'Marlon Brando'],
'STOPAZ': "175 min"
}

film3 = {
'JMENO': 'The Dark Knight',
'HODNOCENI': 90,
'ROK': 2008,
'REZISER': 'Christopher Nolan',
'HRAJI': ['Christian Bale', 'Heath Ledger'],
'STOPAZ': "152 min"
}

Vytvorime si novy soubor, pojmenujeme jej "movie_db.py" a zkopirujeme nasledujici sablonu:

#!/usr/bin/env python3
""" Lekce #3 - Uvod do programovani, Movie dictionary """
# ~~~~~~~~~~~~~~~~~~~ZADANI ULOHA I~~~~~~~~~~~~~~~~~~~
...
# ~~~~~~~~~~~~~~~~~~~~KONEC ZADANI~~~~~~~~~~~~~~~~~~~~

# I. KROK
# Vytvorim novy (prazdny) slovnik + oddelovac


# II. KROK
# Vlozime klice (opet zatim prazdne)


# III. KROK
# Doplnime hodnoty klicu
# Primo + update() metodou
# Kombinace s input()


# IV. KROK
# Vytvorime dalsi dva klice s hodnotami
# Klic *STOPAZ* odstranime pomoci metody *pop*
# Z klice *HRAJI* odstranime pomoci funkce *del*


# V. KROK
# Vytvorime novy slovnik *filmova_db*
# Nestujeme dva zbyvajici slovniky ze zadani


# VI. KROK
# Vytvorime pomyslneho interpreta nasi db
# Ten predstavi nase filmy


# VII. KROK
# Vyzkousime metodu slovniku .get()


# VIII. KROK
# Vyzkousime metodu slovniku .setdefault()
# pp(filmova_db.get(film, filmova_db.setdefault(film, )))
