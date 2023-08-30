# name = input("Type your name: ")
# print("\n You are name is : " + str(name))\

# print("name: " + str(input("name : "))
#     + "\n age: " + str(input("age: "))
#     + "\n phone: " + str(input("phone: "))     
#       )
    
dataSet = {
    "label":["name", "age","phone","address"]
}

# for label in dataSet["label"]:
#     print(label+ " is a" + str(input(label + ":")))

def getUserInfo(dataSet):
  resultSet = []
  for label in dataSet["label"]:
      resultSet.append(label + " is a  " + str(input(label + ": ")))
  return resultSet

print(getUserInfo(dataSet))
