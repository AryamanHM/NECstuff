def find_common_guests(parties):
    party_guests = [set(guests.split(',')) for guests in parties]
    common_guests = set.intersection(*party_guests)
    return len(common_guests)

# Test the function
guests_input = "John,David,Mary,Lisa,Mary,John,David,Lisa,John,David"
parties = guests_input.split(';')  # Assuming party lists are separated by ';'

common_guests_count = find_common_guests(parties)

print("Number of common guests in all parties:", common_guests_count)
