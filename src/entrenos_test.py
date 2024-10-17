from entrenos import *


def lee_entrenos_test(ruta):
    lista_entrenos = lee_entrenos(ruta)

    print("-" * 30)
    print("\nProbando la función lee_entrenos...")
    print("Imprimiendo los primeros 3 entrenos...\n")
    for entreno in lista_entrenos[1:4]:
        print(entreno, "\n")
    print("-" * 30)

    return lista_entrenos


def tipos_entrenos_test(entrenos):
    tipos = tipos_entrenos(entrenos)

    print("-" * 30)
    print("Probando la función tipos_entrenos...")
    print(f"Los tipos de entrenos que hay en la lista son {tipos}")
    print("-" * 30)

    
def entrenos_duracion_superior_test(lista_entrenos, d):
    entrenos_superiores = entrenos_duracion_superior(lista_entrenos, d)

    print("-" * 30)
    print("Probando la función entrenos_duracion_superior...")
    print(f"Los entrenos con duración superior a {d} son {entrenos_superiores}")
    print("-" * 30)


def suma_calorias_test(lista_entrenos, f_inicio, f_fin):
    suma = suma_calorias(lista_entrenos, f_inicio, f_fin)

    print("-" * 30)
    print("Probando la función suma_calorias...")
    print("La suma de las calorias quemadas en todos los "
          f"entrenamientos realizados entre {f_inicio} y {f_fin} es {suma}")
    print("-" * 30) 


if __name__ == "__main__":

    lista_entrenos = lee_entrenos("data/entrenos.csv")
    lee_entrenos_test("data/entrenos.csv")
    # tipos_entrenos_test(lista_entrenos)
    # entrenos_duracion_superior_test(lista_entrenos, 115)
    # suma_calorias_test(lista_entrenos, "5/5/2019", "10/10/2019")