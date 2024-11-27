import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def create_board(size, fill_value=' '):
    board = [[fill_value for _ in range(size + 1)] for _ in range(size + 1)]
    for col in range(1, size + 1):
        board[0][col] = chr(64 + col)
    for row in range(1, size + 1):
        board[row][0] = row
    return board


def display_table(table):
    cols = len(table[0])

    cell_width = 4
    horizontal_border = "+" + ("-" * cell_width + "+") * cols

    print(horizontal_border)
    for row in table:
        print("|" + "|".join(f"{str(cell):^{cell_width}}" for cell in row) + "|")
        print(horizontal_border)

def game_mode_display(table1, table2, title1="Tablero del contrincante:", title2="Tu tablero:"):
    title_width = max(len(title1), len(title2))
    cell_width = 4  

    print(f"{title1:^{title_width}}                                  {title2:^{title_width}}")
    print("-" * (title_width + 80 + title_width))

    rows1 = len(table1)
    rows2 = len(table2)
    max_rows = max(rows1, rows2)

    horizontal_border1 = "+" + ("-" * cell_width + "+") * len(table1[0])
    horizontal_border2 = "+" + ("-" * cell_width + "+") * len(table2[0])

    for i in range(max_rows):
        row1 = table1[i] if i < rows1 else [" "] * len(table1[0])
        row2 = table2[i] if i < rows2 else [" "] * len(table2[0])

        print(f"{'|' + '|'.join(f'{str(cell):^{cell_width}}' for cell in row1) + '|'}   "
              f"{'|' + '|'.join(f'{str(cell):^{cell_width}}' for cell in row2) + '|'}")

        print(horizontal_border1 + "   " + horizontal_border2)

def update_board(table, row, col, new_value):
    if 0 <= row < len(table) and 0 <= col < len(table[0]):
        table[row][col] = new_value
    else:
        print("Coordenadas invalidas!")

def ship_placement(board, ships):
    for ship in ships:
        try:
            display_table(board)
            print(f"Coloca el barco de tamaño {ship}")
            row = int(input("Coloca el renglon deseado: "))
            col = int(input("Coloca la columna deseada: "))
            direction = input("¿Horizontal (H) o Vertical (V)? ").strip().upper()
            '''if direction in ["H", "V"] and can_place_ship(board, row, col, ship_size, orientation):
                #place_ship(board, row, col, ship_size, orientation)
            else:
                print("No se puede colocar el barco aquí (demasiado cerca de otro o fuera del tablero). Intenta de nuevo.")'''
            clear_screen()
        except (ValueError, IndexError):
            print("Entrada inválida. Por favor, intenta de nuevo.")
    return



def play_game():
    size = 10
    ship_size = [4,3,3,2,2,2,1,1,1,1]
    first_player_b = create_board(size)
    second_player_b = create_board(size)
    
    payer_one = input("Cual es el nombre del primer jugador? ")
    payer_two = input("Cual es el nombre del segundo jugador? ")

    clear_screen()
    print(f"{payer_one} coloca tus barcos")
    ship_placement(first_player_b, ship_size)


if __name__ == "__main__":
    clear_screen()
    play_game()
