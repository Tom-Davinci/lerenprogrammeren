print('speeltuin entree')

# welkom voor kinderen van 12 of onder de 12, maar alleen met een begeleider van 20 of ouder
# of welkom als ze onder de 14 zijn en een speeltuinpasje hebben
# of welkom als ze een begeleider hebben met de naam Vladimir 

age = 20
pasje = 'ja'
begeleider = 'ja'
age_begeleider = 20
naam_begeleider = 'Joseph'

if age == 12:
  print("Welkom")
elif age < 12 and age_begeleider >= 20:
  print("Welkom met een begeleider")
elif age <= 14 and pasje == "ja":
  print("Welkom met een pasje")
elif naam_begeleider == "Vladimir":
  print("Welkom oh grote Vladimir")
else:
  print("Je bent niet welkom")