import random
from functools import reduce
from itertools import combinations


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
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
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
        self.last_id += 1  # automatically increment the ID to assign the new user

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
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(f"user-{i}")

        # Create friendships

        # generate a list representing the number of friendships
        # per user, with the expected average
        def get_num_friendships(mean, min_num, max_num, n):
            total = mean * n - (min_num * n)
            l = [min_num] * n
            while total > 0:
                num = random.randint(min_num, max_num)
                index = random.randint(0, n - 1)
                if num > total:
                    num = total
                if l[index] + num > max_num:
                    break
                l[index] += num
                total -= num

            return l

        num_friendships = get_num_friendships(avg_friendships, 0, 2 *
                                              avg_friendships, num_users)

        def get_possible_friend_id(user_id):
            choices = []
            for i, num in enumerate(num_friendships):
                if i != user_id and num > 0 and not self.are_friends(user_id, i):
                    choices.append(i)

            if len(choices) == 0:
                return -1  # no possible friend found
            return random.choice(choices)

        for i in range(num_users):
            for _ in range(num_friendships[i]):
                friend_id = get_possible_friend_id(i)
                if friend_id == -1:
                    # if there is no possible friend found,
                    # try again with different num_friendships
                    return self.populate_graph(num_users, avg_friendships)
                self.add_friendship(i, friend_id)
                num_friendships[i] -= 1
                num_friendships[friend_id] -= 1

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
