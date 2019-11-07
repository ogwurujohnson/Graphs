import names
import random
from util import Stack, Queue  # These may come in handy


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif (
            friendID in self.friendships[userID] or userID in self.friendships[friendID]
        ):
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            name = names.get_first_name()
            print(name)
            self.addUser(name)

        # Create friendships
        friendships_created = 0

        # Keep creating relationships until avg is the desired one
        while friendships_created / numUsers != avgFriendships:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)

            while num1 == num2:
                num2 = random.randint(1, 10)

            min_num = min(num1, num2)
            max_num = max(num1, num2)

            # Check if relationship does not exist
            if max_num not in self.friendships[min_num]:
                self.addFriendship(min_num, max_num)
                friendships_created += 2

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = Queue()
        queue.enqueue([userID])

        while queue.size() > 0:
            path = queue.dequeue()
            user = path[-1]

            if user not in visited:
                visited[user] = path

                for next_user in self.friendships[user]:
                    path_copy = list(path)
                    path_copy.append(next_user)
                    queue.enqueue(path_copy)

        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print("\n===========friendships===========================")
    print(sg.friendships)
    print("\n=============connections=============================")
    connections = sg.getAllSocialPaths(1)
    print(connections)
