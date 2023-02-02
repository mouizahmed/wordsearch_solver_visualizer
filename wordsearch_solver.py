import random
import string
import sys

def create_word_search(words, size):
    grid = [['_' for i in range(size)] for j in range(size)]

    orientations = ["left-right", "right-left", "up-down", "down-up", "diagonal-up-left-right",
                    "diagonal-up-right-left", "diagonal-down-left-right", "diagonal-down-right-left"]

    for word in words:
        word_length = len(word)

        placed = False

        while not placed:
            starting_row = random.randint(0, size-1)
            starting_col = random.randint(0, size-1)

            orientation = random.choice(orientations)

            if orientation == "left-right":
                if starting_col + word_length <= size:
                    for i, letter in enumerate(word):
                        if grid[starting_row][starting_col + i] != '_':
                            break
                    else:
                        for i, letter in enumerate(word):
                            grid[starting_row][starting_col + i] = letter
                        placed = True
            
            elif orientation == "right-left":
                if starting_col - word_length >= 0:
                    for i, letter in enumerate(word):
                        if grid[starting_row][starting_col - i] != '_':
                            break
                    else:
                        for i, letter in enumerate(word):
                            grid[starting_row][starting_col - i] = letter
                        placed = True

            elif orientation == "up-down":
                if starting_row + word_length <= size:
                    for i, letter in enumerate(word):
                        if grid[starting_row+i][starting_col] != '_':
                            break
                    else:
                        for i, letter in enumerate(word):
                            grid[starting_row+i][starting_col] = letter
                        placed = True
            
            elif orientation == "down-up":
                if starting_row - word_length >= 0:
                    for i, letter in enumerate(word):
                        if grid[starting_row - i][starting_col] != '_':
                            break
                    else:
                        for i, letter in enumerate(word):
                            grid[starting_row-i][starting_col] = letter
                        placed = True

            elif orientation == "diagonal-down-left-right":
                if starting_row + word_length <= size and starting_col + word_length <= size:
                    for i, letter in enumerate(word):
                        if grid[starting_row+i][starting_col+i] != '_':
                            break
                    else:
                        for i, letter in enumerate(word):
                            grid[starting_row+i][starting_col+i] = letter
                        placed = True
            
            elif orientation == "diagonal-down-right-left":
                if starting_row + word_length <= size and starting_col - word_length >= 0:
                    for i, letter in enumerate(word):
                        if grid[starting_row+i][starting_col-i] != '_':
                            break
                    else:
                        for i, letter in enumerate(word):
                            grid[starting_row+i][starting_col-i] = letter
                        placed = True
            
            elif orientation == "diagonal-up-left-right":
                if starting_row - word_length >= 0 and starting_col + word_length <= size:
                    for i, letter in enumerate(word):
                        if grid[starting_row-i][starting_col+i] != '_':
                            break
                    else:
                        for i, letter in enumerate(word):
                            grid[starting_row-i][starting_col+i] = letter
                        placed = True

            elif orientation == "diagonal-up-right-left":
                if starting_row - word_length >=0 and starting_col - word_length >= 0:
                    for i, letter in enumerate(word):
                        if grid[starting_row-i][starting_col-i] != '_':
                            break
                    else:
                        for i, letter in enumerate(word):
                            grid[starting_row-i][starting_col-i] = letter
                        placed = True
                    # for loop iterates over all letters in word to check if it collides with any other word. If not, it will execute the else statement after iterating through all the letters. If it does, it will not execute the else statement.

    return grid

def random_letters(grid, size):
    
    
    for i in range(size):
        for j in range(size):
            if grid[i][j] == '_':
                grid[i][j] = random.choice(string.ascii_uppercase)

    return grid



def main():
    args = sys.argv[1:]
    print(args)
    size = int(args[0])

    grid2 = random_letters(create_word_search(args[1:], size), size)

    for row in grid2:
        print(' '.join(row))

if __name__ == "__main__":
    main()


