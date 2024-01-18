"""Travel log"""
country = input('the name of country\n')
visits = int(input("Enter how many times you visited\n"))
list_of_cities = eval(input("Enter cities visited\n"))

travel_log = [
    {
        'country': 'France',
        'visits': 12,
        'cities': ['Paris', 'Lille', 'Dijon']
    },
    {
        'country': 'Germany',
        'visits': 5,
        'cities': ['Berlin', 'Hamburg', 'Stuttgart']
    }
]

add_new = {}

def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country['country'] = name
    new_country['Visits'] = times_visited
    new_country['cities'] = cities_visited
    travel_log.append[new_country]

add_new_country(country, visits, list_of_cities)
print(f'I ve been to {travel_log[2]['country']} {travel_log[2]['visits']} times.')
print(f'My favourite city was {travel_log[2]['cities'][0]}.')