#Question 1

#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name): #this is my function and passing parameter user_name
    USERNAME = user_name #I am assigning user for my user_name
    return USERNAME #am going to return username

    new_username = hello_name("username")  #am calling my function and assigning it to new username
    print("hello_"+  new_username.upper()+ "!") #am printing it out by concatenatat hello_ to my username and my output is hello username

                

#Question 2

#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds(numbers):
    for numbers in range(1,100,2):
        if numbers % 2 == 1:
         return numbers 


        
                

#Question 3

#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

    def max_num_in_list(a_list): #this is my function(max_num_in_list) passing in list as my parameter a_list
        a_list.sort() #this function sorts my list
        return a_list[-1] #this funtion will return the last number to the left of my list
    
                

#Question 4

#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

    def is_leap_year(a_year):
        if a_year % 2 ==0 and (a_year % 100 !=0 or a_year % 400 ==0): #this if statment goes through the year
            return True #if my statment is true and the year is a leap year it will return true
        return False #if the statement is false and the year is not a leap year it will return false
    
                

#Question 5

#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

    def is_consecutive(a_list):
        return sorted(a_list) == list(range(min(a_list),max(a_list)+1)) #have sorted list with a range from smallest to largest plus 1 to every number
                
