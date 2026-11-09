elso_szo = input("Első szó: ")
masodik_szo = input("Második szó: ")

if len(elso_szo) > len(masodik_szo):
    print("A(z) első szó a hosszabb!")
elif len(masodik_szo) > len(elso_szo):
    print("A(z) második szó a hosszabb!")
else:
    print("A két szó egyenlő hosszú!")