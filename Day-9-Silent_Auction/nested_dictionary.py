travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇

def add_new_country(country, number_visits, city_visited):
    temp_dict = {"country": country, "visits": number_visits, "cities": city_visited}
    travel_log.append(temp_dict)


# 🚨 Do not change the code below
add_new_country(country="Russia", number_visits=2, city_visited=["Moscow", "Saint Petersburg"])
print(travel_log)
