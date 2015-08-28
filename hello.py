# reviewing ways to do things in Python
print "Hello world!"

# 1. function to print out the even numbers between 1 and 10,000
def evens():
	# list comprehension - starts with a list and generates another list
	even_list = [x for x in range(1, 10001) if x%2 == 0]
	return even_list

print evens()

# 2. function that returns a list of the numbers btwn 1 and 10,000 that are divisible by 3
def div_three():
	three_list = [x for x in range(1, 10001) if x%3 == 0]
	return three_list

print div_three()

# 3. same as 2, but use Python list comprehensions 
# refer to above

# 4. Write a function get_max that takes a list of numbers and returns the max of those numbers, don't use the builtin max() function. Afterward, try using max()
def get_max(num_list):
	# not using built in functions to find max easier
	highest = num_list[0]
	for i in num_list:
		if i > highest:
			highest = i
	return highest

	# using built in sorting where largest is last
	# sort_num = sorted(num_list)
	# return sort_num[len(sort_num)-1]

	# using built in max()
	# return max(num_list)

print get_max([-8, 10, 2366, 47, 99])
print get_max([-8, -10, -2366, -47, -99])

# 5. Write a function is_odd_or_div_by_7 that returns True if a number is odd or divisble by 7 and False otherwise. Then write it using a lambda function.
def is_odd_or_div_by_7(num):
	# instead of explicitly returning True or False, this conditional will spit a boolean out for us
	return num % 2 != 0 or num % 7 == 0

lambda_odd_7 = lambda x: x % 2 != 0 or x % 7 == 0
# sample use of above lambda function
# print filter(lambda_odd_7, [21,14,87,22])

# 6. Use is_odd_or_div_by_7 and list comprehensions to write a function get_sublist_of_numbers_odd_or_div_by_7 that takes in a list and returns a sublist of those numbers that are either odd or divisible by 7.
def get_sublist_of_numbers_odd_or_div_by_7(main_list):
	return [x for x in main_list if is_odd_or_div_by_7(x)]
	# other possible ways to have written body of function 
	# return filter(lambda_odd_7, main_list)
	# return [x for x in main_list if (lambda_odd_7)(x)]

print get_sublist_of_numbers_odd_or_div_by_7([21,14,87,22])

# 7. Given a list of food orders, e.g. ["burger", "fries", "burger", "tenders", "apple pie"], write a function get_aggregate_order_counts that takes the list and returns a dictionary with the different dishes as keys and the number of times they appear in the list as the values. For example, it takes ["burger", "fries", "burger", "tenders", "apple pie"] and outputs  { "burger": 2, "fries": 1, "tenders": 1, "apple pie": 1 }
def get_aggregate_order_counts(food_list):
	# creating an empty dictionary
	food_dict = {}
	for food in food_list:
		if food in food_dict:
			food_dict[food] += 1
		else:
			food_dict[food] = 1
	return food_dict

# 8. Use collections.Counter to achieve the same functionality.
def count_aggregate_order_counts(food_list):
	# another way to create an empty dictionary
	food_dict = dict()
	# using .count built into Python 
	for food in food_list:
		food_dict[food] = food_list.count(food)
	return food_dict
	# if using the Counter: (no need to create empty dictionary first)
	# from collections import Counter
	# food_dict = Counter(food_list)

# 9. Write a function get_most_popular_order_data that takes a list of orders but instead of returning a dictionary with the counts, it just outputs a tuple: the dish that appears the most in the list and the number of times it appears in the list. So the output given the example would be ("burger", 2). Don't worry about more than one max
def get_most_popular_order_data(order_list):
	# creating dictionary of values is needed ain all three methods
	get_dict = count_aggregate_order_counts(order_list)

	# least DRY method
	# max_count = 0
	# max_name = ''
	# for key in get_dict:
	# 	if get_dict[key] > max_count:
	# 		max_count = get_dict[key]
	# 		max_name = key
	# return (max_name, max_count)

	# OR middle effectiveness (2 cases)
	# Case 1:
	# max_count = max(get_dict.values())
	# max_name = get_dict.keys()[get_dict.values().index(max_count)]
	# return (max_name, max_count)

	# Case 2: only way that takes into account more than one max value
	max_count = max(get_dict.values()) 
	return [x for x in get_dict.items() if x[1] == max_count]

	# OR most efficient
	# max and sorted can take a lambda function
	# .items() in Python returns key, values as a tuple
	#  return max(get_dict.items(), key=lambda x: x[1])

print get_most_popular_order_data(["burger", "fries", "burger", "tenders", "apple pie", "fries"])









