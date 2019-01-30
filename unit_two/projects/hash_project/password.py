import pw_hash
pass_hash = pw_hash.pass_hash
def user_pw(input):
   for key, value in pass_hash.items():
       if input == value:
           print("your pass word is the number", key,"most common password")
user_pw('123456')
user_input = input("What is your password?")
user_pw(user_input)
# make a function
# user will input password
# go over the hash
# if top
