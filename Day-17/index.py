class User:
    def __init__(self, user_id, username):
        self.id = user_id #attribute
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Kingsantus")
user_2 = User("002", "Favour")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

#constructor used to initialize the attribute
#attribute is variable
#function attached to an object is a method




#user_1 = User()
#user_1.id = "001"
#user_1.username = "Kingsantus"
#print(user_1.username)









camelCase = "small case followed by Capital case eg helloWorld"
snake_case = "all small letter with underscore eg hello_world"
PascalCase = "all words start with capital case eg HelloWorld"