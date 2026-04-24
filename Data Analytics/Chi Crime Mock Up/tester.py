import read_json_file

data = read_json_file.load_data()

# Filter data to district 3
district_3_crimes = read_json_file.filter_by_condition(data, 'district', 3)
for item in district_3_crimes:
    print(f"{item}")

print("")

# Crime count in district 3
district_3_count = read_json_file.count_frequencies(district_3_crimes, 'crime')
print(district_3_count)

print("")

# Arrest percent of crimes in district 3
district_3_arrest = read_json_file.arrest_rate(district_3_crimes, 'crime', 'arrest')
print(district_3_arrest)

print("")

# Frequent locations of crimes
district_3_frequent = read_json_file.most_frequent_location(district_3_crimes, 'location')
print(district_3_frequent)

print("")

# Safest districts within the whole data
most_safe_district = read_json_file.most_safe_location(data, 'district')
print(most_safe_district)