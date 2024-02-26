# create a dictionary of rivers
rivers = {
    'danube': 'germany',
    'amazon': 'brazil',
    'yangtze': 'china'
}
# print a statement about each river and country
for river, country in rivers.items():
    print(f"\nThe {river.title()} River flows through {country.title()}.")
