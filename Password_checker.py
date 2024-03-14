import sys

print('''
      - === - Menu - === -
      1.Password Checker 
      2.Quit
      ''')

menu_selection = int(input("Please enter menu selection > ")) 

if menu_selection == 1:
    print("Password")
if menu_selection ==2:
    sys.exit      