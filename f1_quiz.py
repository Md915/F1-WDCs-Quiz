# This is the Formula 1 World Drivers Champions Quiz (1.1). On later versions, I'll include an extra option to also guess the WCC from the same year. All drivers have been included. I'll also add which F1 drivers championships you failed, (as well as constructors). I can do it in reverse, which gives you the year and you have to guess the driver. I'll also make them not repeat after being guessed and I'll add an infinite mode in the future.
# Andrés Nicolau Bucur. 1.0 @ 26/11/2025 10:23:00 UTC +1 Madrid

import random
import time
import os

def cls(): #Clear console
  os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)
cls()
time.sleep(1)
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

print("Welcome to the F1 World Drivers' Championships Quiz!")
time.sleep(2)
print("Your objective is to guess correctly the WDC from the driver and the number of the title (i.e. Max Verstappen's 4th title.)")
time.sleep(5)
print("We'll begin in 3, 2, 1...")
time.sleep(3)
print("Go.")
time.sleep(0.5)
cls()

for i in range(100):
  random_driver, championships = random.choice(list(drivers.items()))
  random_year = random.choice(championships)
  championship_number = championships.index(random_year) + 1  # +1 because indexing starts at 0


  guess = int(input(f"{random_driver}'s {championship_number}: "))
  if guess == random_year:
    print("Nice.")
    good +=1
  
  else:
    print(f"Wrong, it was {random_year}")
    bad +=1

print(f"You've done {good} good guesses and {bad} bad guesses")

  #print(f"{random_driver}'s {championship_number} title was in {random_year}")