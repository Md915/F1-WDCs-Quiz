# This is the Formula 1 World Drivers Champions Quiz (1.1). 
# Andrés Nicolau Bucur. 1.0 @ 26/11/2025 10:23:00 UTC +1 Madrid

from random import choice
from time import sleep
from os import system, name

#def main():
  
def driver_generator():
  global random_driver, random_year, championship_number
  random_driver, championships = choice(list(drivers.items()))
  random_year = choice(championships)
  championship_number = championships.index(random_year) + 1  # +1 because indexing starts at 0

def cls(): #Clear console
  system('cls' if name == 'nt' else 'clear')
sleep(1)
cls()
sleep(1)
drivers = {
  "Max Verstappen":(2021,2022,2023,2024),
  "Lewis Hamilton": (2008, 2014, 2015, 2017, 2018, 2019, 2020),
  "Nico Rosberg": (2016,),
  "Sebastian Vettel": (2010, 2011, 2012, 2013),
  "Jenson Button": (2009,),
  "Kimi Raïkonnen": (2007,),
  "Fernando Alonso": (2005, 2006),
  "Michael Schumacher": (1994, 1995, 2000, 2001, 2002, 2003, 2004),
  "Mika Häkkinen": (1998, 1999),
  "Jacques Villeneuve": (1997,),
  "Damon Hill": (1996,),
  "Alain Prost": (1985, 1986, 1989, 1993),
  "Nigel Mansell": (1992,),
  "Ayrton Senna": (1988, 1990, 1991),
  "Nelson Piquet": (1981, 1983, 1987),
  "Niki Lauda": (1975, 1977, 1984),
  "Keke Rosberg" : (1982,),
  "Alan Jones" : (1980,),
  "Jody Scheckter": (1979,),
  "Mario Andretti": (1978,),
  "James Hunt": (1976,),
  "Emmerson Fittipaldi":(1972, 1974),
  "Jackie Stewart": (1969, 1971, 1973),
  "Jochen Rindt": (1970,),
  "Graham Hill":(1962, 1968),
  "Denny Hulme": (1967,),
  "Jack Brabham": (1959, 1960, 1966),
  "Jim Clark": (1963, 1965),
  "John Surtees": (1964,),
  "Phil Hill": (1961,),
  "Mike Hawthorn": (1958,),
  "Juan Manuel Fangio": (1951, 1954, 1955, 1956, 1957),
  "Alberto Ascari": (1952, 1953),
  "Giuseppe 'Nino' Farina": (1950,),
  }

good = 0
bad = 0

wrong_guesses = {}

print("Welcome to the F1 World Drivers' Championships Quiz!")
sleep(2)
print("Your objective is to guess correctly the WDC from the driver and the number of the title (i.e. Max Verstappen's 4th title.)")
sleep(2)


iterations = input("Before we start, specify the amount of tries you want to do, if you want to do an infinite mode, write 'True', 'infinite' or 'inf': ").strip().lower()

while True:
  if iterations in ('true', 'infinite', 'inf'):
    iterations = True
    break
  else:
    try:
      iterations = int(float(iterations))  # converts float to int
      if iterations > 0:
        break
      else:
        iterations = input("Please enter a positive number or 'True', 'infinite' or 'inf' for infinite mode: ").strip().lower()
    except ValueError:
      iterations = input("I didn't catch that, please specify the amount of tries you want to do, if you want to do an infinite mode, write 'True': ").strip().lower()

sleep(2)
print("Perfect, we'll begin in 3, 2, 1...")
sleep(3)
print("Go.")
sleep(0.5)
cls()

guess = ""

if iterations is True:
  print("Infinite mode enabled. Type 'exit' to exit the program.")
  while True:
    driver_generator()
    if guess == "exit":
      break
    while True:
      guess = input(f"{random_driver}'s {championship_number}: ")
      if guess.lower() == 'exit':
          guess = "exit"
          break
      try:
        if int(guess) == random_year:
          print("Nice.")
          good +=1
          break
        else:
          print(f"Wrong, it was {random_year}")
          bad += 1
          # record wrong guess: store a list of (championship_number, year) for each driver
          wrong_guesses.setdefault(random_driver, []).append((championship_number, random_year))
          break
      except ValueError:
        if guess.lower() == 'exit':
          break
        else:
          print("Wrong format, please try again")
          continue
      #main()


elif isinstance(iterations, int):
  guess = ""
  for i in range(iterations):
    driver_generator()
  
    while True:
      if guess.lower() == 'exit':
          break
      guess = input(f"{random_driver}'s {championship_number}: ")
      try:
        if int(guess) == random_year:
          print("Nice.")
          good +=1
          break
        else:
          print(f"Wrong, it was {random_year}")
          bad += 1
          # record wrong guess: store a list of (championship_number, year) for each driver
          wrong_guesses.setdefault(random_driver, []).append((championship_number, random_year))
          break
      except ValueError:
        if guess.lower() == 'exit':
          break
        else:
          print("Wrong format, please try again")
          continue
      #main()


print(f"You've done {good} good guesses and {bad} bad guesses")