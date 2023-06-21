import random

def generate_level(walls, wall_density):
    level = walls.copy()

    for row in range(1, len(walls)):
        for col in range(1, len(walls[row])):
            if row == 1 or col == 1 or row == len(walls) // 2 or col == len(walls[row]) // 2 or row == len(walls) - 2 or col == len(walls[row]) - 2:
                continue
            # print(row, col)
            if walls[row][col] == ' ':
                # Check if the surrounding area is empty
                if walls[row - 1][col] == ' ' or walls[row + 1][col] == ' ' or \
                   walls[row][col - 1] == ' ' or walls[row][col + 1] == ' ':
                    # Randomly generate a wall in the space between existing walls
                    if random.random() < wall_density:
                        level[row] = level[row][:col] + 'W' + level[row][col + 1:]
        

    return level

def check_validity(walls):
    level = walls.copy()

    for row in range(1, len(walls)):
        for col in range(1, len(walls[row])):
            if row == 1 or col == 1 or row == len(walls) - 2 or col == len(walls[row]) - 2:
                continue 
            # print(row, col)
            # check whether an empty tile is surrounded by walls on each side, if so, remove a wall from a random side
            if level[row][col] == ' ' and level[row - 1][col] == 'W' and level[row + 1][col] == 'W' and \
                   level[row][col - 1] == 'W' and level[row][col + 1] == 'W':
                    remove = random.randint(1,4)
                    if remove == 1:
                        level[row+1] = level[row+1][:col] + ' ' + level[row+1][col + 1:]
                    if remove == 2:
                        level[row] = level[row][:col-1] + ' ' + level[row][col:]
                    if remove == 3:
                        level[row-1] = level[row-1][:col] + ' ' + level[row-1][col + 1:]
                    if remove == 4:
                        level[row] = level[row][:col+1] + ' ' + level[row][col + 2:]
            # check whether an empty tile is surrouded by walls on 3 sides, if so, remove a wall from a random side
            # (done for 4 possible combinations)
            if level[row][col] == ' ' and level[row - 1][col] == 'W' and level[row][col - 1] == 'W' and level[row][col + 1] == 'W':
                    # print('case bottom empty', row, col)
                    remove = random.randint(1,3)
                    if remove == 1:
                        # print('removing left', row, col-1)
                        level[row] = level[row][:col-1] + ' ' + level[row][col:]
                    if remove == 2:
                        # print('removing top', row-1, col)
                        level[row-1] = level[row-1][:col] + ' ' + level[row-1][col + 1:]
                    if remove == 3:
                        # print('removing right', row, col+1)
                        level[row] = level[row][:col+1] + ' ' + level[row][col + 2:]
                        
            if level[row][col] == ' ' and level[row - 1][col] == 'W' and level[row + 1][col] == 'W' and level[row][col + 1] == 'W':
                    # print('case left empty', row, col)
                    remove = random.randint(1,3)
                    if remove == 1:
                        # print('removing bottom', row+1, col)
                        level[row+1] = level[row+1][:col] + ' ' + level[row+1][col + 1:]
                    if remove == 2:
                        # print('removing top', row-1, col)
                        level[row-1] = level[row-1][:col] + ' ' + level[row-1][col + 1:]
                    if remove == 3:
                        # print('removing right', row, col+1)
                        level[row] = level[row][:col+1] + ' ' + level[row][col + 2:]
                        
            if level[row][col] == ' ' and level[row - 1][col] == 'W' and level[row + 1][col] == 'W' and level[row][col - 1] == 'W':
                    # print('case right empty', row, col)
                    remove = random.randint(1,3)
                    if remove == 1:
                        # print('removing bottom', row+1, col)
                        level[row+1] = level[row+1][:col] + ' ' + level[row+1][col + 1:]
                    if remove == 2:
                        # print('removing left', row, col-1)
                        level[row] = level[row][:col-1] + ' ' + level[row][col:]
                    if remove == 3:
                        # print('removing top', row-1, col)
                        level[row-1] = level[row-1][:col] + ' ' + level[row-1][col + 1:]
                        
            if level[row][col] == ' ' and level[row][col - 1] == 'W' and level[row + 1][col] == 'W' and level[row][col + 1] == 'W':
                    # print('case top empty', row, col)
                    remove = random.randint(1,3)
                    if remove == 1:
                        # print('removing bottom', row+1, col)
                        level[row+1] = level[row+1][:col] + ' ' + level[row+1][col + 1:]
                    if remove == 2:
                        # print('removing left', row, col-1)
                        level[row-1] = level[row][:col-1] + ' ' + level[row-1][col:]
                    if remove == 3:
                        # print('removing right', row, col+1)
                        level[row] = level[row][:col+1] + ' ' + level[row][col + 2:]
    return level

# code to see whether the validation works
# walls = [
#     "WWWWWWWWWWWWWWWWWWWWW",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "W                   W",
#     "WWWWWWWWWWWWWWWWWWWWW",
# ]

# wall_density = 0.7  # Probability of generating a wall in the space between existing walls

# generated_level_pre = generate_level(walls, wall_density)
# # for row in generated_level:
#     # print(row)
# for row in generated_level_pre:
#     print(row)

     
# generated_level_post = check_validity(generated_level_pre)


# for row in generated_level_post:
#      print(row)
