from random import randint

pole = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
win = False
game_work = True
player = "X"


def output(pole):
    print(f"""<snap>   -------   </snap> 
  <snap>  |{pole[0]}|{pole[1]}|{pole[2]}|</snap> 
  <snap>  -------</snap> 
  <snap>  |{pole[3]}|{pole[4]}|{pole[5]}|</snap> 
  <snap>  -------</snap> 
  <snap>  |{pole[6]}|{pole[7]}|{pole[8]}|</snap> 
  <snap>  -------</snap> """)


def player_input(pole):
    while True:
        if player == "X":
            pl = int(input("1-9 please:"))
        else:
            pl = randint(1, 10)
        if pl >= 1 and pl <= 9 and pole[pl - 1] == "-":
            print(player)
            pole[pl - 1] = player
            break
        else:
            print("No, plese not again and 1-9: ")
            continue
        output(pole)


def chandge_player():
    global player
    print("chandging...")
    if player == "X":
        player = "O"
    else:
        player = "X"


def chek_win(pole):
    global game_work
    if pole[0] == pole[1] == pole[2] != "-" or pole[3] == pole[4] == pole[5] != "-" or pole[6] == pole[7] == pole[
        8] != "-" or pole[0] == pole[3] == pole[6] != "-" or pole[1] == pole[4] == pole[7] != "-" or pole[2] == pole[
        5] == pole[8] != "-" or pole[0] == pole[4] == pole[8] != "-" or pole[2] == pole[4] == pole[6] != "-":
        output(pole)
        game_work = False
    else:
        output(pole)


def chek_nicha(pole):
    global game_work
    if "-" not in pole:
        output(pole)
        print("Nicha")
        game_work = False


while game_work:
    output(pole)
    player_input(pole)
    chek_win(pole)
    chek_nicha(pole)
    chandge_player()

print(f"""X or O is winner!!!""")
a = input()
