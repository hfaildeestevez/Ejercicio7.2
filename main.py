# parte1


fichas1 = (3, 4)
fichas2 = (4, 5)


def encaje(combinacion1, combincacion2):
    if combinacion1[1] == combincacion2[0] or combinacion1[1] == combincacion2[1]:

        return "encaja"
    else:
        return "no encaja"


print(encaje(fichas1, fichas2))

# parte 2

