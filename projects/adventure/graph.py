from collections import deque


class Graph:
    def __init__(self):
        self.rooms = {}

    def __repr__(self):
        string = "\n"
        for room_id in sorted(self.rooms):
            string += f"{room_id}: {self.rooms[room_id]}\n"
        return string

    def add_room(self, room):
        if room.id not in self.rooms:
            self.rooms[room.id] = {d: "?" for d in room.get_exits()}
        else:
            raise IndexError("Room already exists")

    def add_connection(self, room1, room2):
        """
        Add a directed edge to the graph.
        """
        if room1 in self.rooms and room2 in self.rooms:
            self.rooms[room1].add(room2)
        else:
            raise IndexError(
                "Both rooms must exist in order to add an edge")
