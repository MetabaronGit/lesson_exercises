# výběr čísel z listu a jejich součet
# -----------------------------------
# #sectete vsechna cisla z listu! Pozor i True ma nejakou ciselnou hodnotu!
# list_znaku_a_cisel = v
#
# list_znaku_a_cisel = str(list_znaku_a_cisel)
# list_znaku_a_cisel = list_znaku_a_cisel.replace("[", "")
# list_znaku_a_cisel = list_znaku_a_cisel.replace("]", "")
# list_znaku_a_cisel = list_znaku_a_cisel.replace(",", "+")
# list_znaku_a_cisel = list_znaku_a_cisel.replace("'", "")
# list_znaku_a_cisel = list_znaku_a_cisel.replace("True", "1")
# # list_znaku_a_cisel = list_znaku_a_cisel.replace(range(), "")
#
# print(int(2+ 3 + 6 +8))

#stejne zadani
# list_znaku_a_cisel = [4, 6, 8, 14, 900, "5", "ahoj", 34, True, "ddjj5", ["5", 7, True, "ddh5"]]

# ------------------------------------------------------------------------------------------------

my_list = [4, 6, 8, 14, 900, "5", "ahoj", 34, True, "ddjj5", "ahoj"]
my_list.remove("ahoj")
my_index = my_list.index("ahoj")
print(my_list)
print(my_index)