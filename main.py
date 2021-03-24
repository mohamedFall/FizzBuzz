from fizzbuzz_checker import FizzbuzzChecker


def main():
    is_playing = True
    print("BIENVENUE DANS FIZZBUZZ")
    while is_playing:
        try:
            number = int(input("Veuillez entrer un chiffre : \n"))
            print(FizzbuzzChecker.fizzbuzz(number))
        except ValueError as error:
            is_playing = False
            print("Une erreur est levee [{0}]".format(error))


if __name__ == "__main__":
    main()
