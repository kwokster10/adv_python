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
	# sort_num = sorted(num_list)
	# return sort_num[len(sort_num)-1]
	highest = num_list[0]
	for i in range(len(num_list)):
		if i > highest:
			highest = i
	return highest

# max(num_list)


# 5. Write a function is_odd_or_div_by_7 that returns True if a number is odd or divisble by 7 and False otherwise. Then write it using a lambda function.
def is_odd_or_div_by_7(num):
	return num % 2 != 0 or num % 7 == 0:

lambda_odd_7 = lambda x: x % 2 != 0 or x % 7 == 0
# print filter(lambda_odd_7, [21,14,87,22])

# 6. Use is_odd_or_div_by_7 and list comprehensions to write a function get_sublist_of_numbers_odd_or_div_by_7 that takes in a list and returns a sublist of those numbers that are either odd or divisible by 7.
def get_sublist_of_numbers_odd_or_div_by_7(main_list):
	return [x for x in main_list if is_odd_or_div_by_7(x)]
	# return filter(lambda x: x % 2 != 0 or x % 7 == 0, main_list)
	# return [x for x in main_list if (lambda x: x % 2 != 0 or x % 7 == 0)(x)]

# 7. Given a list of food orders, e.g. ["burger", "fries", "burger", "tenders", "apple pie"], write a function get_aggregate_order_counts that takes the list and returns a dictionary with the different dishes as keys and the number of times they appear in the list as the values. For example, it takes ["burger", "fries", "burger", "tenders", "apple pie"] and outputs  { "burger": 2, "fries": 1, "tenders": 1, "apple pie": 1 }
def get_aggregate_order_counts(food_list):
	food_dict = {}
	for food in food_list:
		if food in food_dict:
			food_dict[food] += 1
		else:
			food_dict[food] = 1
	return food_dict

# 8. Use collections.Counter to achieve the same functionality.
def count_aggregate_order_counts(food_list):
	food_dict = {}
	for food in food_list:
		food_dict[food] = food_list.count(food)
	return food_dict

# 9. Write a function get_most_popular_order_data that takes a list of orders but instead of returning a dictionary with the counts, it just outputs a tuple: the dish that appears the most in the list and the number of times it appears in the list. So the output given the example would be ("burger", 2)
def get_most_popular_order_data(order_list):
	get_dict = count_aggregate_order_counts(order_list)
	max_count = 0
	max_name = ''
	for key in get_dict:
		if get_dict[key] > max_count:
			max_count = get_dict[key]
			max_name = key
	return (max_name, max_count)










