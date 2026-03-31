input_filename = "country_info.txt"

countries= {}
code_lookup= {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip("\n").split("|")
        country, capital, code, code3, dialing, timezone, currency = data
        #print(country, capital, code, code3, dialing, timezone, currency, sep="\n\t")
        country_dict = {
            "name": country,
            "capital": capital,
            "cc3": code,
            "dialing_code": dialing,
            "timezone": timezone,
            "currency": currency,
        }
        #print(country_dict)
        countries[country.casefold()] = country_dict
        #code_lookup[code.casefold()] = country
        countries[code.casefold()] = country_dict
#print(countries)

while True:
    chosen_country = input("Please enter the name of the country: ")
    country_key = chosen_country.casefold()
    if country_key == "quit":
        break
    
    if country_key in countries:
        country_data = countries[country_key]
        
        if country_data['capital'] == "":
            print(f"{chosen_country} does not have a capital city")
        else:
            print(f"The capital of {chosen_country} is {country_data['capital']}")
    else:
        print(f"{chosen_country} is not a valid country name.")
