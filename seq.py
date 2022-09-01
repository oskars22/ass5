# Forritið býr til runu af tölum sem byrjar á 1 2 3 og er í áframhaldinu summa þriggja síðustu talnanna.
# Notandi er beðinn um að slá inn lengd rununnar.
# Á meðan ákveðinn counter er undir lengd rununnar er talan hverju sinni lögð saman við þrjár síðustu tölurnar (eða bara 1, 2 og 3 ef þetta er fjórða talan)
# Í fyrstu þrjú skiptin prentast einfaldlega út 1 þegar counterinn er 0, 2 þegar counterinn er 1 og 3 þegar counterinn er 2.

n = int(input("Enter the length of the sequence: "))  # Do not change this line

n1 = 1
n2 = 2
n3 = 3

count = 0
while count < n:
    if count == 0:
        print(n1, end=" ")
    elif count == 1:
        print(n2, end=" ")
    elif count == 2:
        print(n3, end=" ")
    else:
        count >= 3
        nth = n1 + n2 + n3
        print(nth, end=" ")
        n1 = n2
        n2 = n3
        n3 = nth
    count += 1
