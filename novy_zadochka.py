def parnye_slova():
    with open('slova.txt', 'r', encoding="UTF-8") as file:
        prikol = file.read()
    print(prikol)
parnye_slova()
