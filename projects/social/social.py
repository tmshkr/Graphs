import random
from collections import deque


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.next_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.users[self.next_id] = User(name)
        self.friendships[self.next_id] = set()
        self.next_id += 1  # automatically increment the ID to assign the new user

    def are_friends(self, user_a, user_b):
        return user_a in self.friendships[user_b] and user_b in self.friendships[user_a]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.next_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(f"user-{i}")

        # Create friendships
        for _ in range((num_users * avg_friendships) // 2):
            while True:
                user_id = random.randint(0, self.next_id - 1)
                friend_id = random.randint(0, self.next_id - 1)
                if user_id != friend_id:
                    if not self.are_friends(user_id, friend_id):
                        self.add_friendship(user_id, friend_id)
                        break

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        paths = {}

        q = deque()
        q.append([user_id])

        while len(q) > 0:
            path = q.popleft()
            v = path[-1]

            if v not in paths:
                paths[v] = path

                for f in self.friendships[v]:
                    q.append(path + [f])

        return paths


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    print("************")
    connections = sg.get_all_social_paths(1)
    print(connections)
