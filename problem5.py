def check_winner(board):
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        elif board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        elif board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
        
    return "No Winner"

board_no_winner = [
	['X', 'O', 'X'],
	['X', 'O', 'O'],
	['O', 'X', 'X']
]

print(check_winner(board_no_winner))
