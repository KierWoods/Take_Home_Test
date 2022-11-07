# Program to identify and vaildate ISBN numbers.
# import modules


from tkinter import *

def isbn_checker(isbn_input): 
	letters = [' ','a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','y','z']
	isbn_input = isbn_input.lower()
	isbn_list = list(isbn_input)

    # Ensure user input is only 10 or 13 digits and contains only numbers or an X. 
	if len(isbn_input) < 10:
		label_error = Label(root, text="ISBN must be 10 or 13 digits only")
		label_error.grid(row=2,column=1)
		label_error.after(5000, destroy, label_error)
		

	if len(isbn_input) > 13:
		label_error = Label(root, text="ISBN must be 10 or 13 digits only")
		label_error.grid(row=2,column=1)
		label_error.after(5000, destroy, label_error)
		
		
	if len(isbn_input) == 11 or len(isbn_input) == 12:
		label_error = Label(root, text="ISBN must be 10 or 13 digits only")
		label_error.grid(row=2,column=1)
		label_error.after(5000, destroy, label_error)
		

	for i in letters:
		if i in isbn_input:
			label_error = Label(root, text="Only X can be in an ISBN")
			label_error.grid(row=2,column=1)
			label_error.after(5000, destroy, label_error)

	if len(isbn_input) == 13:
		letters.append('x')

    # Verify 10 digit ISBN.
	if len(isbn_input) == 10:

        # Convert isbn_list to integers from string for calculation and replace x with value 10. 
		isbn_list = [i if i != "x" else 10 for i in isbn_list]
		isbn_list = [int(i) for i in isbn_list]

        # Declare list for calculating ISBN with 10 digits. 
		multiply_isbn = [10,9,8,7,6,5,4,3,2,1]

        # Multiply each element of the ISBN with the reverse index. 
		
		multiply_result = [isbn_digit * index for isbn_digit, index in zip(isbn_list, multiply_isbn)]

        # Sum integers and divide by 11, if divisible by 11 ISBN is valid. 
		isbn_addition = sum(multiply_result)

        # Print message to user informing them of valid ISBN.
		if isbn_addition % 11 == 0:
			label_valid = Label(root, text="Valid")
			label_valid.grid(row=2, column=1)
			label_valid.after(5000, destroy, label_valid)
			

            # Add 978 prefix and remove check digit.
			isbn_list.insert(0, 9)
			isbn_list.insert(1, 7)
			isbn_list.insert(2, 8)
			del isbn_list[-1]

            # Multiply remaining 12 digits 
			multiply_isbn13 = [1,3,1,3,1,3,1,3,1,3,1,3]
			
			multiply_result13 = [isbn_digit * index for isbn_digit, index in zip(isbn_list, multiply_isbn13)]

            # Sum 12 digits divide by 10, subtract the remainder from 10 to find the check digit. 
			isbn_addition13 = sum(multiply_result13)
			check_digit_calculation = isbn_addition13 % 10
			check_digit = 10 - check_digit_calculation
			           
            # Append check_digit to isbn_list. 
			isbn_list.append(int(check_digit))
			
            # Convert back to string and print to user.
			isbn13_convert = "".join(str(i) for i in isbn_list)
			label_converted = Label(root, text="ISBN-13 Conversion: " + isbn13_convert)
			label_converted.grid(row=2, column=1)
			label_converted.after(5000, destroy, label_converted)
			print(isbn13_convert)
			return isbn13_convert

        # Print to user if ISBN is invalid.  
		else:
			label_invalid = Label(root, text="Invalid")
			label_invalid.grid(row=2, column=1)
			label_invalid.after(5000, destroy, label_invalid)
			print("Invalid")

    # Verify 13 digit ISBN         
	elif len(isbn_input) == 13:
		isbn_list = [int(i) for i in isbn_list]
		multiply_isbn13 = [1,3,1,3,1,3,1,3,1,3,1,3,1]
		list(zip(isbn_list, multiply_isbn13))
		multiply_result13 = [isbn_digit * index for isbn_digit, index in zip(isbn_list, multiply_isbn13)]
		isbn_addition13 = sum(multiply_result13)

		if isbn_addition13 % 10 == 0:
			label_valid = Label(root, text="Valid")
			label_valid.grid(row=2, column=1)
			label_valid.after(5000, destroy, label_valid)
			print("Valid")
		else:
			label_invalid = Label(root, text="Invalid")
			label_invalid.grid(row=2, column=1)
			label_invalid.after(5000, destroy, label_invalid)
			print("Invalid")

# Clear button functionality. 
def clear():
	e_input.delete(0, END)

# Delete labels from GUI after 5 seconds. 
def destroy(label):
	label.destroy()
	pass

# Build gui interface for user. 
root = Tk()
root.title("ISBN CHECKER")
root.geometry("550x100")

# Create widgets
e_input = Entry(root,width=50, borderwidth=2)
e_input.insert(0, "0316066524")
title_label = Label(root, text="ISBN CHECKER")
input_label = Label(root, text="ISBN number: ")
submit_button = Button(root, text="Submit", padx=35, command=lambda: isbn_checker(e_input.get()))
clear_button = Button(root, text="Clear", padx=40, command=lambda: clear())

# Display to user. 
title_label.grid(row=0, column=1)
input_label.grid(row=1, column=0)
e_input.grid(row=1, column=1)
clear_button.grid(row=2, column=2,)
submit_button.grid(row=1, column=2)

# Event loop. 
if __name__=="__main__":
	root.mainloop()