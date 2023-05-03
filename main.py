from connectBoard import ConnectBoard

def main():
    game = ConnectBoard()
    print(game)
    while True:
        col = int(input("Enter column: "))
        if not game.drop_piece(col):
            print("Invalid move")
            continue
        print(game)
        print("-----------------")
        if game.check_win():
            print("Player {} wins in a {} move!".format(game.last_piece, game.winCondition))
            break



if __name__ == "__main__":
    main()