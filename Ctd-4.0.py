import datetime

def calculate_age(birthday):
  today = datetime.date.today()
  age = today.year - birthday.year
  return age

def input_entry():
  while True:
    try:
      name, birthday_str = input("Input your entry (name, DD/MM/YYYY): ").split(", ")
      birthday = datetime.datetime.strptime(birthday_str, "%d/%m/%Y").date()
      if birthday > datetime.date.today():
        raise ValueError("Upcoming birthday")
      if not name.isalpha():
        raise ValueError("Name containing number")
      age = calculate_age(birthday)
      name = name.capitalize()
      database[name] = {"birthday": birthday, "age": age}
      print(f"Successfully entered: {name}, {age} years old")
      break
    except ValueError as e :
      print(e)

def read_entries():
  print("List of entries:")
  for name in database:
    entry = database[name]
    print(f"{name}, {entry['age']} years old")

def delete_entry():
  name = input("Input the name of the entry you want to delete: ").capitalize()
  if name in database:
    del database[name]
    print(f"Successfully deleted: {name}")
  else:
    print(f"{name} not found in the database")

database = {}

while True:
  action = input("What do you want to do (input, read, delete, exit): ")
  if action == "input":
    input_entry()
  elif action == "read":
    read_entries()
  elif action == "delete":
    delete_entry()
  elif action == "exit":
    print("Goodbye")
    break
  else:
    print("Invalid action")
