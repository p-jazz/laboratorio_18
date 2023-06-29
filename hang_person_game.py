word_to_guess = "computador"
guess_word = ""
display_word = "_ "*len(word_to_guess)
user_option = ""
user_chars = []

print("BIENVENIDO AL AHORCADO")
print(display_word)

hang_person = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
print(hang_person [0])
while user_option != "·":
    print(f"Adivina esta palabra si quieres vivir\n"
          f"1. Adivinar la letra o la palabra\n"
          f"2. Resultados\n"
          f"3. Salir")

    user_option = input("Indica una opción \n")    #char/chars = caracter o letra

    if user_option == "1":
        exit_game = False
        while not exit_game:
            print("Intenta adivinando una letra o la palabra completa")
            user_guess = input("")
            guess_word = ""

        #Si el usuario ingresó una letra
            if len(user_guess) == 1:
                #Si es una letra nueva, se agrega al listado de letras intentadas
                if(not user_guess in user_chars):
                    user_chars.append(user_guess)   

                if (user_guess in word_to_guess):
                    print ("adivinaste una letra")

                    for char in word_to_guess:
                        if char in user_chars:
                            guess_word += char

                        else:
                            guess_word += "_ "
                    print(guess_word)
                else:
                    print("Esa letra no esta en la palabra")
                    print(hang_person[len(user_chars)])
            elif(user_guess == "salir"):
                exit = True


            else:
                #si la palabra del usuario es lo mismo
                if(user_guess == word_to_guess):
                    print("Ganaste")
                    exit(1)
                else:
                    print("no no no")
                    print("PERdiste y te quemaras en el infierno")
                    print(hang_person[-1])
                    exit(1)

    elif (user_option == "2"):
        print("Has intentado las siguientes letras: {user_chars}")
    
    elif (user_option == "3"):
        print("Adios")



    
