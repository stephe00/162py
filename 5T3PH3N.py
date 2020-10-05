#Stephen's Project 0
#162
# October 4th, 2020
#Program with Menu that will 1 day open 5T3PH3N.exe
#All credit to Rick Astley and Never Gonna Give You Up. 
import csv
import sys
import webbrowser

def main():
   menu()


def menu():
    print("*OS V1 Demo Registration*")
    print()

    choice = input("""
                      A: Please Register for Stephen's Chromium Web Based Browser
                      B: Login to 5TE4HE9
                      Q: Logout of 5Te4HEN

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
    #input for future mysql email database for mail updates on 5T3PH3N
    print("Enter first name")
    firstname=input()
    print("Enter last name")
    last_name=input()
    print("Enter Date of Birth Format: dd/mm/yy")
    dob=input()
    print("Enter first line of address")
    firstlineaddress=input()
    print("Enter Postcode")
    postcode=input()
    print("Enter Gender")
    gender=input()
    print("Enter email address")
    email=input()
    substring=dob[-4:]
    print(substring)
    print("Your unique username is", firstname+last_name+substring)
    username=firstname+last_name+substring
    print("Please enter a password -it must contain a capital letter and at least one integer")
    password=input()    
    
    with open('Stephen.txt','a') as Stephenfile:
        StephenfileWriter=csv.writer(Stephenfile)
        StephenfileWriter.writerow([username,password,firstname,last_name,dob,firstlineaddress,postcode,gender,email])
        print("Record has been written to file")
        Stephenfile.close()
        menu()
            
def login():
   #set a variable (boolean type) to true if the user is NOT logged on
   notloggedin="true"
   #while the user is not logged on (i.e. while the login credentials provided do not work ...)
   while notloggedin=="true":
      print("*Please login to 5T3PH3N V1*")
   
   #open file for checking file 
      with open("Stephen.txt",'r') as Stephenfile:
     #login details 
         username=input("Enter username:-")
         password=input("Enter password:-")
      #call upon our reader (this allows us to work with our file)
         StephenfileReader=csv.reader(Stephenfile)
      #for each row that is read by the Reader
         for row in StephenfileReader:
            for field in row:
            
            #search for the required matches in user entry against what is stored in the file for credentials 
               if field==username and row[1]==password:
                  print("You are now entered into 5T3PH3N")
                  display5T3PH3N()
                  notloggedin="false"
                  
              
               
         
                                 
              
     
     

def display5T3PH3N():
   print("*Welcome to 5T3PH3N*")
   print("We're now going to open the best browser on the whole World Wide Web. ")
   webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')  # Go to Stephen's Web Site
   webbrowser.open('https://github.com/stephe00/162py') #Github url 
   
    
#yay 
main()
