def escalera(n):
    for numAlmohadillas in range(1, n + 1):
        print(" "*(n - numAlmohadillas) + "# "*numAlmohadillas)

n = int(input("¿De qué tamaño quieres que sea tu escalera?: "))
escalera(n)