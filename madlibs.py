def main():
	# write your code here
	print("Mad libs where libs get mad.")
	print("Start below:")
	print("\n")
	number = input("Enter a number from 1 to 12: ")
	noun = input("Enter a noun (plural): ")
	name = input("Enter a name: ")
	sentence = input("Enter any sentence: ")
	verb = input("Enter a verb: ")
	print("\n")
	print("The story goes...")
	print("\n")
	print("It was {} o'clock when I heard a knock at the door.".format(number))
	print("""I opened the door and there was a box full of {} with a note saying "From Mr. {}." """.format(noun,name.title()))
	print("""Just as I closed the door I heard a scream "{}" """.format(sentence.upper()))
	print("I froze in place and all I could do was {}.".format(verb))


if __name__ == '__main__':
	main()
