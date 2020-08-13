from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from graph import Graph
from collections import deque
import random

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

rooms = {}


def bfs(room):
    # breadth-first search to find the shortest path
    # to the next unexplored room
    q = deque()
    q.append([("_", room.id)])

    searched = set()

    while len(q) > 0:
        path = q.popleft()
        (_, r) = path[-1]

        if r not in searched:
            searched.add(r)
            for (d, to) in rooms[r].items():
                if to == "?":
                    return list(map(lambda t: t[0], path[1:]))
                q.append(path + [(d, to)])


def dft(directions):
    for d in directions:
        # add room travelling from
        from_room = player.current_room
        traversal_path.append(d)
        if from_room.id not in rooms:
            rooms[from_room.id] = {d: "?" for d in from_room.get_exits()}

        # travel in next direction
        player.travel(d)
        to_room = player.current_room
        rooms[from_room.id][d] = to_room.id
        print(f"{d} from {from_room.id} to {to_room.id}")

    if to_room.id in rooms:
        choices = [d for (d, to) in rooms[to_room.id].items() if to == "?"]
    else:
        choices = to_room.get_exits()

    if len(choices) > 0:
        next_move = random.choice(choices)
        dft([next_move])
    else:
        print(f"all directions in room {to_room.id} explored")
        # get path to next unexplored room
        path = bfs(player.current_room)
        print(path)
        if path:
            dft(path)
        else:
            print("All rooms explored!")
            print("len(traversal_path)", len(traversal_path))
            print("len(rooms)", len(rooms))


initial_move = random.choice(player.current_room.get_exits())
dft([initial_move])
# print(g)
# print(traversal_path)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

"""
#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
"""
print("\n")
