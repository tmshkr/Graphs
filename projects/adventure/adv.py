from room import Room
from player import Player
from world import World

from ast import literal_eval

from collections import deque
import random
import sys
sys.setrecursionlimit(2000)

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


def add_room(room):
    rooms[room.id] = {d: room.get_room_in_direction(
        d).id for d in room.get_exits()}


def bfs(room):
    # breadth-first search to find the shortest path
    # to the nearest unvisited room
    q = deque()
    q.append([("_", room.id)])

    searched = set()

    while len(q) > 0:
        path = q.popleft()
        (_, r) = path[-1]

        if r not in searched:
            searched.add(r)
            for (d, to) in rooms[r].items():
                if to not in rooms:
                    path = path[1:] + [(d, to)]
                    return tuple(map(lambda t: t[0], path))
                q.append(path + [(d, to)])


def traverse(directions):
    for d in directions:
        from_room = player.current_room

        # travel in next direction
        player.travel(d)
        traversal_path.append(d)
        to_room = player.current_room
        if to_room not in rooms:
            add_room(to_room)
        print(f"{d} from {from_room.id} to {to_room.id}")

    # get path to next unvisited room
    path = bfs(player.current_room)
    print(path)
    if path:
        traverse(path)
    else:
        print("All rooms explored!")
        print("len(traversal_path)", len(traversal_path))
        print("len(rooms)", len(rooms))


curr = player.current_room
add_room(curr)
initial_move = random.choice(curr.get_exits())
traverse((initial_move))
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
