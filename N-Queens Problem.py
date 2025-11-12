def solveNQueens(n):
    # Helper function to check if placing a queen at board[row][col] is safe
    def is_safe(board, row, col):
        # Check all rows above in the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        # If no queens are attacking this position, it's safe
        return True
    
    # Recursive function to try placing queens row by row
    def backtrack(row, board, result):
        # If we've placed queens in all rows, add this board configuration to results
        if row == n:
            result.append(["".join(row) for row in board])
            return
        
        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_safe(board, row, col):
                # Place a queen at board[row][col]
                board[row][col] = 'Q'
                # Move on to the next row
                backtrack(row + 1, board, result)
                # Remove the queen (backtrack) and try another position
                board[row][col] = '.'
    
    # Initialize an empty chessboard
    board = [['.' for _ in range(n)] for _ in range(n)]
    result = []
    
    # Start backtracking from the first row
    backtrack(0, board, result)
    
    return result


# Ask the user for input and display all possible solutions
hanif = int(input("Enter the number of queens: "))
print(solveNQueens(hanif))

