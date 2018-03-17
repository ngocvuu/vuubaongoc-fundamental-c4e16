map_sokoban = {
    "x" : 5,
    "y" : 5,

}

player = {
    "x" : 0,
    "y" : 4
}

boxes = [
    {"x" : 1, "y" : 1},
    {"x" : 2, "y" : 2},
    {"x" : 3, "y" : 3},

]

destinations = [
    {"x" : 2, "y": 1},
    {"x" : 3, "y": 2},
    {"x" : 4, "y": 3},
]
while True:
    for y in range(map_sokoban["y"]):
        for x in range(map_sokoban["x"]):

            box_is_here = False
            for box in boxes:
                if box["x"] == x and box["y"] == y:
                    # print(("B"), end = " ")
                    box_is_here = True
                    break

            destination_is_here = False
            for destination in destinations:
                if destination["x"] == x and destination["y"] == y:
                    # print(("D"), end = " ")
                    destination_is_here = True
                    break
            player_is_here = False
            if x == player["x"] and y == player["y"]:
                # print("P", end = " ")
                player_is_here = True
            # elif box_is_here is False and destination_is_here is False:
            #     print("-", end = " ")

            if box_is_here:
                print("B", end = " ")
            elif destination_is_here:
                print("D", end = " ")
            elif player_is_here:
                print("P", end = " ")
            else:
                print("-", end = " ")
    #xuống dòng
        print()

    win = True
    for box in boxes:
        if box not in destinations:
            win = False

    if win:
        print("You WIn!")
        break

    move = input("Your move? ").upper()

    dx = 0
    dy = 0

    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1

    if 0 <= player["x"] + dx < map_sokoban["x"] \
    and 0 <= player["y"] + dy < map_sokoban["y"]:
        player["x"] += dx
        player["y"] += dy

    for box in boxes:
        if box["x"] == player["x"] and box["y"] == player["y"]:
            box["x"] += dx
            box["y"] += dy
