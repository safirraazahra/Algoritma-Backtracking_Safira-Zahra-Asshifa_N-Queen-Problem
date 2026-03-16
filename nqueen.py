import time

N = 4

def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col):

    # cek kiri baris
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # cek diagonal atas kiri
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # cek diagonal bawah kiri
    i = row
    j = col
    while j >= 0 and i < N:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True


def solve_nqueen(board, col):

    if col >= N:
        return True

    for i in range(N):

        print(f"Mencoba menaruh ratu di baris {i}, kolom {col}")
        time.sleep(1)

        if is_safe(board, i, col):

            board[i][col] = "Q"
            print("Posisi aman, ratu ditempatkan")
            print_board(board)
            time.sleep(1)

            if solve_nqueen(board, col + 1):
                return True

            print("Backtracking... menghapus ratu")
            board[i][col] = "."
            print_board(board)
            time.sleep(1)

    return False


def main():

    board = [["." for _ in range(N)] for _ in range(N)]

    if solve_nqueen(board, 0):
        print("Solusi ditemukan:\n")
        print_board(board)
    else:
        print("Tidak ada solusi")


main()