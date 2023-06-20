import random

def generate_level(walls, wall_density):
    level = walls.copy()

    for row in range(1, len(walls) - 1):
        for col in range(1, len(walls[row]) - 1):
            if row == 1 or col == 1 or row == len(walls) / 2 or col == len(walls[row]) / 2 or row == len(walls) - 2 or col == len(walls[row]) - 2:
                continue
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

    for row in range(1, len(walls) - 1):
        for col in range(1, len(walls[row]) - 1):
            if row == 1 or col == 1 or row == len(walls) - 1 or row == len(walls) - 2 or \
                col == len(walls[row]) - 1 or col == len(walls[row]) - 2:
                continue 
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
                        
            if level[row][col] == ' ' and level[row - 1][col] == 'W' and \
                   level[row][col - 1] == 'W' and level[row][col + 1] == 'W':
                    remove = random.randint(1,3)
                    if remove == 1:
                        level[row] = level[row][:col-1] + ' ' + level[row][col:]
                    if remove == 2:
                        level[row-1] = level[row-1][:col] + ' ' + level[row-1][col + 1:]
                    if remove == 3:
                        level[row] = level[row][:col+1] + ' ' + level[row][col + 2:]
                        
            if level[row][col] == ' ' and level[row - 1][col] == 'W' and level[row + 1][col] == 'W' and level[row][col + 1] == 'W':
                    remove = random.randint(1,3)
                    if remove == 1:
                        level[row+1] = level[row+1][:col] + ' ' + level[row+1][col + 1:]
                    if remove == 2:
                        level[row] = level[row][:col-1] + ' ' + level[row][col:]
                    if remove == 3:
                        level[row] = level[row][:col+1] + ' ' + level[row][col + 2:]
                        
            if level[row][col] == ' ' and level[row - 1][col] == 'W' and level[row + 1][col] == 'W' and level[row][col - 1] == 'W':
                    remove = random.randint(1,3)
                    if remove == 1:
                        level[row+1] = level[row+1][:col] + ' ' + level[row+1][col + 1:]
                    if remove == 2:
                        level[row] = level[row][:col-1] + ' ' + level[row][col:]
                    if remove == 3:
                        level[row-1] = level[row-1][:col] + ' ' + level[row-1][col + 1:]
                        
            if level[row][col] == ' ' and level[row - 1][col] == 'W' and level[row + 1][col] == 'W' and level[row][col + 1] == 'W':
                    remove = random.randint(1,3)
                    if remove == 1:
                        level[row+1] = level[row+1][:col] + ' ' + level[row+1][col + 1:]
                    if remove == 2:
                        level[row-1] = level[row-1][:col] + ' ' + level[row-1][col + 1:]
                    if remove == 3:
                        level[row] = level[row][:col+1] + ' ' + level[row][col + 2:]
    return level

# walls = [
#     "WWWWWWWWWWWWWWWWWWWW",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "W                  W",
#     "WWWWWWWWWWWWWWWWWWWW",
# ]

# wall_density = 0.35  # Probability of generating a wall in the space between existing walls

# generated_level = generate_level(walls, wall_density)
# generated_level = check_validity(generate_level(walls, wall_density))
# for row in generated_level:
#     print(row)
