# Fyrst er búinn til stærsti integer (0) til að bera saman við.
# Notandi er síðan beðinn um að slá inn integer sem er borinn saman við stærsta integer.
# Ef integerinn er stærri eða jafn stór, þá er innslegni integerinn hinn nýji stærsti integer.
# Notandinn er spurður aftur þangað til hann slær inn neikvæða tölu og þá endar forritið.

max_int = 0
num_int = int(input("Input a number: "))

while num_int >= 0:
    if num_int >= max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)  # Do not change this line