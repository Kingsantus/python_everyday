"""Nesting"""
# adding dictionary in list and having list in dictionary
#{key: [list],key1:{dict}}

# simple dictionary
capitals = {
    'France': 'Paris',
    'Germany': 'Berlin'
}

# nested list in dict it very useful
travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Berline', 'Hamburg', 'Stuttgart']
}

# nesting dict in dict 
travel_log1 = {
    'France': {
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12
    },
    'Germany': {
        'cities_visited': ['Berline', 'Hamburg', 'Stuttgart'],
        'total_visits': 5
    } 
}

# nesting a dictionary in a list
travel_log = [
    {
        'Country': 'France',
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12
    },
    {
        'country': 'Germany',
        'cities_visited': ['Berline', 'Hamburg', 'Stuttgart'],
        'total_visits': 5
    } 
]