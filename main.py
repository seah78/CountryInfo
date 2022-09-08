from countryinfo import CountryInfo

country = input("Enter your country : ")
countryInfo = CountryInfo(country)

print("Capitale : ", countryInfo.capital())
print("Devise : ", countryInfo.currencies())
print("Langue : ", countryInfo.languages())
print("Bordé par : ", countryInfo.borders())
print("Autres noms : ", countryInfo.alt_spellings())