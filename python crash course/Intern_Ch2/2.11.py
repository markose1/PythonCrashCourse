age = 23
message = 'Happy' + age +'rd Birthday!' #error because age must be in a str(), cannot be an integer
print (message)

message = 'Happy' + str(age) +'rd Birthday!' #casting = str()
print (message)