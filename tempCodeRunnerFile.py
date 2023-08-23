
            break
        elif is_full(board):
            print("It's a draw!")
            break

        player_row = int(input("\nEnter row (0, 1, or 2): "))
        player_col = int(input("Enter column (0, 1, or 2): "))
        
        if board[player_row][player_col] == EMPTY:
            board[player_row][player_col] = PLAYER
        else:
            print("Cell is already occupied. Try again.")
            continue
