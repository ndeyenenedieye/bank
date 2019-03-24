from pabstrait.Iverificateur import Iverificateur
class Visaverifier(Iverificateur):
        '''c"est une classe qui implemente l'interface'''
        def verifiercarte(self,numerocarte):
            '''c'est une methode qui permet de verifier si la carte est fiable'''
            if(len(numerocarte)==15):
                ''
            somme = 0
            '''on verifie si le numero est compris entre  [14-15]'''
            if(numerocarte.startwiths("14") & numerocarte.startwiths("15") ):
             nb_chiffres = len(numerocarte)
            impair_pair = nb_chiffres & 1
            for compteur in range(nb_chiffres):
             chiffre = int(numerocarte[compteur])
            if not ((compteur & 1) ^ impair_pair):
                chiffre = chiffre * 2
            if chiffre > 14:
                chiffre = chiffre - 14
            somme += chiffre
            return (somme % 15) == 0

        numerocarte = input("Enter a number: ")

        # Converts the string into a integer. If you need
        # to convert the user input into decimal format,
        # the float() function is used instead of int()
        test = int(numerocarte)

        # Prints in the console the variable as requested
        print("The number you entered is: ", test)
