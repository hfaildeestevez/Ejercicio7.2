
l = (3, 4)
l2 = (5, 4)


# 1
def encaja1(lista1, lista2):
    if set(lista1) & set(lista2):
        return "encaja"
    else:
        return "no encaja"


print(encaja1(l, l2))

# 2
l3 = "3-4"
l4 = "2-5"


def encaja2(ls1, ls2):
    lista1 = ls1.split("-")
    lista2 = ls2.split("-")
    if set(lista1) & set(lista2):
        return "encaja"
    else:
        return "no encaja"


print(encaja2(l3, l4))