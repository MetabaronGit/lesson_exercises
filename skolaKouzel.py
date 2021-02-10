# Promenne
PREDMETY = (
    'Premenovani',
    'Astronomie',
    'Obrana_proti_cerne_magii',
    'Bylinkarstvi',
    'Lektvary'
)

SKUP_PREMENOVANI = ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann', 'Ron', 'Hermiona']
SKUP_ASTRONOMIE = ['Marcus','Alex','Glenn','Samuel', 'Hermiona', 'Clara','Chelsea']
SKUP_OBRANA = ['Hermiona', 'Adam','Tyler', 'Alex','Clara']
SKUP_BYLINKARSTVI = ['Abraham','Marcus', 'Hermiona', 'Alex','Glenn','Clara']
SKUP_LEKTVARY = ['Alfred', 'Curt','Oliver','Tyler', 'Hermiona', 'Ann']

# ~~~~~~~~~~~~~~~~~~~~KONEC ZADANI~~~~~~~~~~~~~~~~~~~~
# I. KROK
# Vytvorim prazdny slovnik "rozvrh"
rozvrh = dict()
print(rozvrh)

# II. KROK
# Klice slovniku budou stringy z promenne PREDMETY
# Hodnoty klicu jsou seznamy skupin
rozvrh = rozvrh.fromkeys(PREDMETY)
rozvrh["Blesky"] = None
print(rozvrh)

# III. KROK
# Vytvorime sety studentu v jednotlivych klicich
rozvrh["Premenovani"] = set(SKUP_PREMENOVANI)
rozvrh["Astronomie"] = set(SKUP_ASTRONOMIE)
rozvrh["Obrana_proti_cerne_magii"] = set(SKUP_OBRANA)
rozvrh["Bylinkarstvi"] = set(SKUP_BYLINKARSTVI)
rozvrh["Lektvary"] = set(SKUP_LEKTVARY)

# IV. KROK
# Do *set_premenovani* studenta se jmenem *Harry*
rozvrh["Astronomie"].add("Harry")

# Ze setu *set_astronomie* odebereme *Samuel*
rozvrh["Astronomie"].discard("Samuel")

# V. KROK
# Vypiseme zmeny po pridani/odebrani
print("Astronomie:", rozvrh["Astronomie"])
print("Lektvary:", rozvrh["Lektvary"])
# VI. KROK
# Zjistime, kdo navstevuje vsechny predmety


# VII. KROK
# bool test na podmnoziny (S.issubset())
# Je vsichni studenti z hodin obrany v hodine premenovani


# VIII. KROK
# S.isdisjoint()
# Jsou studenti v prom. *NOVI_STUDENTI* uplne odlisne hodnoty 