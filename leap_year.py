def leap_year():
        txt=int(input("Ingrese un año:"))
    print(txt)
    if txt % 4 == 0 and txt % 100!= 0 or (txt % 400 == 0):
        print(f"El año {txt} es bisiesto")
    else:
        print(f"El año{txt} no es bisiesto")
