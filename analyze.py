# csv = comma separated values
import csv
import re
from collections import Counter

# opening up raw csv file
csv_file = open('rock.csv', 'rb') # try 'r' or 'rU' if 'rb' throws error

# creating an instance DictReader 
# reads in data into Python dictionaries
reader = csv.DictReader(csv_file)

# reading everything in file
rows = [row for row in reader]

# 1. How many songs are from 1981?
songs = [x for x in rows if x["Release Year"] == "1981"]
print len(songs)

# 2. How many songs are from before 1984?
# if not using regex
def is_valid_year(year):
	try: 
		int(year)
	except ValueError:
		return False
	else: 
		return int(year) > 1900

print "There are {} songs before 1984.".format(len([x for x in rows if re.match("^[0-9]", x["Release Year"]) and int(x["Release Year"]) < 1984]))

# 3. What is the earliest release year in the data? (HINT: You might have to account for/clean up dirty data)
valid_years = [int(x["Release Year"]) for x in rows if is_valid_year(x["Release Year"])]
print min(valid_years)

# 4. What are the top 20 songs by play count (HINT: use builtin sorted() function, documentation here: https://wiki.python.org/moin/HowTo/Sorting)
def is_valid_count(playcount):
	try: 
		int(playcount)
	except ValueError:
		return False
	else:
		return True

get_counts = [x for x in rows if is_valid_count(x["PlayCount"])]
top_songs = sorted(get_counts, key=lambda x: x["PlayCount"])
# OR top_songs = sorted(get_counts, key=lambda x: x["PlayCount"], reverse=True)
print [(x["Song Clean"], x["PlayCount"]) for x in top_songs[len(top_songs)-20:]]


# 5. Who are the top 10 most prolific artists in the data along with the number of their songs that appear in the data?
def find_artist(artist_list):
	sort_artists = {}
	all_artists = [x["ARTIST CLEAN"] for x in artist_list]
	for artist in all_artists:
		sort_artists[artist] = all_artists.count(artist)
	return sorted(sort_artists.items(), key=lambda x: x[1], reverse=True)
print find_artist(rows)[:10]

# OR the easier way to do it with Python's built in function
all_artists = [x["ARTIST CLEAN"] for x in rows]
artists_by_count = Counter(all_artists)
top_ten_artists = sorted(artists_by_count.items(), key=lambda x: x[1], reverse=True)
print top_ten_artists[:10]

# 6. How many different artists appear in the data?
# set is unique
print len(set(all_artists))

# 7. How songs does 'Rock' appear in the title of?
find_rock = [x for x in rows if re.search('rock', x["Song Clean"], re.IGNORECASE)]
print len(find_rock)


# python's debugger; like pry in Ruby
# import ipdb; ipdb.set_trace()







