import numpy as np
from numpy import ndarray
from typing import Tuple


def check_number(data: list, n: str) -> None:
    for i, d in enumerate(data):
        if d == n:
            data[i] = "A"


def organize_in_boards(data: list) -> ndarray:
    list_aux = []
    board = []

    for i, d in enumerate(data):
        list_aux.append(d)
        if (i+1) % 5 == 0 and i != 0:
            board.append(list_aux)
            list_aux = []

    list_aux = []
    boards = []

    for i, b in enumerate(board):
        list_aux.append(b)
        if (i+1) % 5 == 0 and i != 0:
            boards.append(list_aux)
            list_aux = []

    return np.array(boards)


def results(data: list) -> Tuple[bool, ndarray]:
    if type(data) == list:
        boards = organize_in_boards(data)
    else: 
        boards = data
    
    # for each matrix (board)
    for i, b in enumerate(boards):
        for row in b:
            count = 0
            count = np.count_nonzero(row == 'A')
            if count == 5:
                return True, b, i
        
        bt = b.T
        for row in enumerate(bt):
            count = 0
            count = np.count_nonzero(row == 'A')
            if count == 5:
                return True, b, i        

    return False, None, i


def answer(b: ndarray, n: int) -> int:
    count = 0

    for line in b:
        for value in line:
            if value != "A":
                count += int(value)
    
    return count*n


def part_1(data: list, numbers: list):
    winning_number = None

    for n in numbers:
        check_number(data, n)
        has_won, winning_board, _ = results(data)
        if has_won: 
            winning_number = int(n)
            break

    print("Part 1: ",answer(winning_board, winning_number))
    print(winning_board)
    print(winning_number)

    
# def part_2(data: list, numbers: list):  
#     losing_number = None
#     count_winning_boards = 0
    
#     for n in numbers:
#         check_number(data, n)
#         has_won, _  = results(data)
#         print(_)
    
#         if has_won:
#             winning_board = _
#             losing_number = int(n)
#             count_winning_boards += 1
#             winning_list = winning_board.reshape(-1, 1)#.tolist()#[0]
#             print(winning_list)
#             print(len(data))
#             print(count_winning_boards)
#             for v in winning_list:
#                 data.remove(v)
#     print(data)
#     print("\nPart 2:", answer(winning_board, losing_number))
#     # print(winning_board)
#     print(losing_number)
#     # print(count_winning_boards)
#     # print(data)
#     # print(winning_list)

def answer_part_2(data: list, numbers:list) -> int:
    winning_number = None
    count_winning_boards = 0
    boards = organize_in_boards(data)
    winning_board = None
    c = 0
    for n in numbers:
        boards[boards == n] = 'A' # check in board
        print("\n", boards)
        print(c)
        c += 1
        has_won, b, i = results(boards)
        if has_won:
            count_winning_boards += 0
            winning_number = int(n)
            boards = np.delete(boards, i, axis=0)
            winning_board = b
        
    # print(winning_number)
    # print(count_winning_boards)
    # print(winning_board)
    # # print(boards)
    # print(i)

def main():
    with open("data_4.txt") as f:
        numbers = f.read()[0:289].split(",")

        f.seek(0)
        data = f.read()[290::].split()

        # part_1(data, numbers)
        # part_2(data, numbers)
        answer_part_2(data, numbers)
        # boards = organize_in_boards(data)
        # print(boards[0])
        # board_del = np.delete(boards, 0, axis=0)
        # print(board_del[0])

main()
