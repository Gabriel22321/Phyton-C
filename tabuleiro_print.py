import os

tab = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def print_tab(tab): #cria função
    os.system('cls') #limpa a tela

    print(" " + tab[0], tab[1], tab[2], sep="  |")
    print("+---+---+---+")
    print(" " + tab[3], tab[4], tab[5], sep="  |")
    print("+---+---+---+")
    print(" " + tab[6], tab[7], tab[8], sep="  |")
    
print_tab(tab) #retorna a função
