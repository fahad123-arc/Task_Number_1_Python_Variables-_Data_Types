#Q1Declare two variables, num1 and num2, with any integer values. Use these to calculate their sum and print the result. Understand how variables store numerical values and perform basic arithmetic in Python.


num1=int(input("Enter the number:", ))
num2=int(input("Enter the number:", ))
sum=num1+num2
print("The sum of num1 and num2 is :", sum)


#Q2Create a variable called message and give it a string value. Append the string " World!" to it and print the updated message. Explore basic string operations in Python.
message=str(input("Enter the number:", ))
append="Hello!"
print(append," ", message)


#Q3Declare a variable, is_python_fun, and assign it a boolean value. Print a statement based on whether Python is considered fun. Learn to use boolean variables for decision-making in Python.
is_python_fun=True
if is_python_fun:
    print("Python is fun!")
else:
    print("Python might not be considered fun by everyone.")

#Q4Create a list called fruits with at least three different fruit names. Print the list, add a new fruit, and then print the updated list. Understand the basics of working with lists in Python.
fruits=["apple","mango","orange"]
print(fruits)
fruits.append("Grapes")
print(fruits)

#Q5Declare a variable called price with a floating-point value. Convert it to an integer and print both the original and converted values. Explore how to convert between different data types in Python.
price=10.5
conv_price=int(price)
print(price)
print(conv_price)

#Q6Create a dictionary named student_info with keys for 'name', 'age', and 'grade'. Assign corresponding values and print the dictionary. Learn how to work with dictionaries, a versatile data structure in Python.
student_info={"Name":"Aman","age": "23"}
print(student_info)


#Q7Create a tuple named days_of_week with the names of the days. Access and print the third day of the week. Understand the basics of working with tuples in Python.
days_of_week=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
third_day_of_week=days_of_week[2]
print(third_day_of_week)





