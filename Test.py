
"""This is a caracter creator program."""

# ToDo:
# add file IO
# Create some tests. Maybe to test input and type?      //Work in progress
# add a main funtion        //work in progress
# fix the exit functionality        //possibly fixed(need main() to work.)

import csv
import sys


print("Welcome to my character creator!")
print("Here you can create as many characters as you want.")

class Character:
    """defines a class called Character."""

    def __init__(self, name, hair_color, age, height, race, sex):
        """Construct character by attributes."""
        self.name = name
        self.hair_color = hair_color
        self.age = age
        self.height = height
        self.race = race
        self.sex = sex

def main():
   menu()

def menu():
    print("*Character Creator v1")
    print()

    choice = input("""
                      A: Please Register for Jon Espin's character creator
                      B: Register to Char. Creator.
                      Q: Logout of the char. creator

                      Please enter your choice: """)

    if choice == "A" or choice =="A":
        register()
    elif choice == "B" or choice =="B":
        login()
    elif choice=="Q" or choice=="Q":
        sys.exit
    else:
        print("You must only select either A or B, Q will Quit. ")
        print("Please try again")
        menu()

def register():
    print("enter name:-")
    name=input()
    print("enter age:-")
    age=input()
    

    with open('Test.txt', 'a') as Testfile:
         TestfileWriter=csv.writer(Testfile)
         TestfileWriter.writerow([name,age])
         print("Record has been writen to Test.txt file")
         Testfile.close()
         menu()



# open file for checking
with open('Test.txt', 'r') as Testfile:
    #login info
    name=input ("enter name:-")
    age=input ("enter the age:-")
  #  height=input ("enter the height:-")
  #  race=input ("enter the race:-")
   # sex=input ("enter your sex:-")
#call File
    TestfileReader=csv.reader(Testfile)
    #for each row is read
    for row in TestfileReader:
        for field in row:
        
#search for match

            if field==name and row[1]==age:
                                        print("Thank you for checking this file.  ")
            
def Char_list_append(Temp_char):
    """Add new character to list."""
    char_line_up = []
    for x in Temp_char:
        # Hopefully adds a character with attributes to list.
        char_line_up.append(Character(x))
    return char_line_up


#def Menu_options(self):
 #   """Create a loop for character creation."""
  #  menu_option = True
    #while menu_option is True:

     #   char_name = input("What should we call your character? ")
      #  char_hair = input("What color is your character's hair? ")
        #char_age = input("How old is your character? ")
       # char_height = input("How tall? ")
       # char_race = input("What race is your character? (Nord, Orc, Elf, etc.) ")
       # char_sex = input("What sex is your character? ")

       # # Stores user input into char_1 with Character class applied.
       # Temp_char = Character(char_name, char_hair, char_age, char_height, char_race, char_sex)

       # exit_yn = input("Would you like to add another Character?")
       # if exit_yn == 'y' or 'Y':
       #     menu_option = True
       # if exit_yn == 'n' or 'N':
       #     menu_option = False
       # elif exit_yn != 'y' or 'Y' or 'n' or 'N':
       #     exit_yn = input("Im sorry, I didn't understand. Please type 'y' or 'n'. ")
    # return Temp_char

#def displayText():
#    print("You did it")

#def main():
    #char_line_up = []
    #Menu_options = Menu_options(self)
    #Char_list_append = Char_list_append(Temp_char)
    #Character_sheet = Character_sheet()
    menu()
    displayText()

def displayText():
    print("You did it. You created a character. Good job. ")


if __name__ == "__main__":
    main()

# this is a test line
print("\nGoodbye! Thank you for using my character creator!")
