class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User(1, "Alice")
user_2 = User(2, "Bob")

print(user_1.id)  # Output: 1
print(user_1.username)  # Output: Alice        

user_1.follow(user_2)
print(user_1.following)  # Output: 1
print(user_2.followers)  # Output: 1    
