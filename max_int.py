# Fyrst er búinn til stærsti integer (0) til að bera saman við.
# Notandi er síðan beðinn um að slá inn integer sem er borinn saman við stærsta integer.
# Ef integerinn er stærri eða jafn stór, þá er innsláði integerinn hinn nýji stærsti integer.
# Notandinn er spurður aftur þangað til hann slær inn neikvæða tölu og þá endar forritið.

max_int = 0
new_int = int(input("Please enter an integer: "))

while new_int > 0:
    if new_int >= max_int:
        print(new_int, "is the largest integer!")
        max_int = new_int
    else:
        print(new_int, "is not the largest integer.")

    new_int = int(input("Please enter an integer: "))

else:
    print("Show's over.")