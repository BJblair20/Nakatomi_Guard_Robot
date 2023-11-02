import mysql.connector

class Profiles(id, actList, image, name, description, active):
    def __init__(self, id, actList, image, name, description, active):
        self.id = id
        self.actList = actList
        self.image = image
        self.name = name 
        self.description = description
        self.active = active
      
    def setInactive(active):
        active = False

    def setActive(active):
        active = True


profiledb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = profiledb.cursor()

mycursor.execute("CREATE DATABASE Profiles")
