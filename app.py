import os
import requests
import datetime

os.system('clear')

inputVal = ''
while inputVal != 'q' or inputVal != 'Q':    
    print("\nEnter a date formatted as MM-DD-YYYY")
    print("Enter 'q' at any time to exit.")
    
    inputVal = input("> ")
    
    if inputVal == 'Q' or inputVal == 'q':
        exit()
    else:
      try:
        datetime.datetime.strptime(inputVal,"%m-%d-%Y")
        requests.post("http://localhost:5000/fibonacci/input/" + inputVal)
      except ValueError as err:
        print("An error occurred.")
        print(err)
