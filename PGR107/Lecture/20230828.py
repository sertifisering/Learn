# case 1
# name = input("Type your name: ")
# print("\n You are name is : " + str(name))\

# case 2
# print("name: " + str(input("name : "))
#     + "\n age: " + str(input("age: "))
#     + "\n phone: " + str(input("phone: "))     
#       )
    
dataSet = {
    "label":["name", "age","phone","address"]
}

# case 3
# for label in dataSet["label"]:
#     print(label+ " is a" + str(input(label + ":")))

# case 4
def getUserInfo(dataSet):
  resultSet = []
  for label in dataSet["label"]:
      resultSet.append(label + " is a  " + str(input(label + ": " )))
  return resultSet

print(getUserInfo(dataSet))

#case 5
