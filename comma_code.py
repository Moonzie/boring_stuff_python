def formatter(list_of_stuff):
	list_length = len(list_of_stuff)
	sentence = ''
	final_sentence = ''
	empty_list = True 

	if list_length == 0:
		print ("this list is empty!")
	else:
		empty_list = False
		for item in list_of_stuff[:-1]:
			sentence +=  str(item) + ", " 

	if empty_list == False: 
		final_sentence = sentence + "and " + str(list_of_stuff[-1])
		print (final_sentence)



groceries = ['apple', 'banana', 'bacon']
groceries2 = []
groceries3 = [1,2,3]
formatter(groceries3)


'''
Comma Code
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and inserted before the last item. 
For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. 
But your func- tion should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.
'''