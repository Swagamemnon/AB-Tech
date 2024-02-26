# create dictionary of people and their favorite places
favorite_places = {'noah': ['montana', 'costa rica', 'asheville'],
                   'hannah': ['california', 'jamaica', 'atlanta'],
                   'austin': ['utah', 'greenville']
                   }

# print a statement about each person and list their favorite places
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")