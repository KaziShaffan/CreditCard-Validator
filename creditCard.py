import customtkinter
from tkinter import *
from tkinter import messagebox

'''
pip install tk
pip install customtkinter
'''
#Validate Credit card
#Name: Kazi Shaffan


#For this assigment I chose to do a credit card validator. It asks user for a credit card number and validates if it real or not.
#If the card is valid then it returns a message saying it the card number is valid and what type of card it is(visa,master,discover,american express)
#The code uses mutiple methods to validate the credit card number inputed by the user


#TO VALIDATE I CHECKED THESE THINGS:
#Must be 16 charecters for most cards or 15 for american express
#4(visa), 5(mastercard), 6(discover), 3(american express) as the first digit of the card number
#Only numbers
#Can have group of 4 digits seprerated by "-" or a space(" ") nothing else in the card number
#Use Luhn algarorithm to validate(is used to validate credit cards)
#Check only visa, american express, mastercard, and discover and lets you know which one it is and if it not any of them it a error

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Function that check if each index of the input of user is a integer
#if it a integer return "Integer" and if not return "Not Integer"
def integer(card_num):
    for i in range(10):
        #check if index of card_num is a integer(0-9)
        if card_num == str(i):
            return "Integer"
    return "Not Integer"   


#Function that removes any "-" or " " from the input so that it could just be a integer number, also validates if it has any charectors it not supposed to in each index
#If indexs are " " or "-" or a integer then it will return the input without the " " and "-"
#If it not and has charecters then not supposed to then return False
def format(card_num):
    new_card_num =str("")

    #loops to compares to see if the index in the sentance is a integer(0-9) which if it is is added to the new_card_num
    for i in range(len(card_num)):
        
        #check if index of card_num is either "-", " " or "Integer"
        #Nested function called integer to check if index of card_num is a integer
        if card_num[i] == "-" or card_num[i] == " " or integer(card_num[i]) == "Integer":
            #removing all the "-" and " "
            for k in range(10):
                if card_num[i] == str(k):
                    new_card_num = new_card_num + str(card_num[i])
        else:
            return False

    return new_card_num



#This function checks if the card_num is the right length to be a valid credit card and if it starts with the right integer
#If 16 charecters for most cards or 15 for american express and Start with 4(visa), 5(mastercard), 6(discover), 3(american express) as the first digit of the card number then return card_num
#If it not the right length or start with the right integer then return False
def valid_nums_integers(card_num):
    #Check First value of visa,master, and discover and length which should be 16
    #If it valid then it just returns the card_ num
    #Else if it not the right length or start num then returns False
    if card_num[0] == "4" or card_num[0] == "5" or card_num[0] == "6":
        if len(card_num) == 16:
            return card_num
        else:
            return False
    #Since american express has a different length I do a elif for it first index is correct and its length
    #If it valid then it just returns the card_ num
    #Else if it not the right length or start num then returns False
    elif card_num[0] == "3":
        if len(card_num) == 15:
            return card_num
        else:
            return False
    else:
        return "Error:Not right card type"





#This function uses the luhn algorithm on card_num
#This algorithm is something that you can use to validate if a card num is real or not which i've coded in python
#1. Basicly it takes the last index of the number and store it into a variable then removes that index from number
#2. You revese the whole number
#3. Every odd index of the number you multiply by 2
#4. If mutiplying it makes it bigger then 9 then you subtract 9 from those odd indexes that are bigger
#5. Then you add all the indexs plus the number we earlier stored in a different variable
#6. Then you module 10 the sum
#If the moduled sum is 0 then card valid and returns the original card_num
#Else if it higher then 0 then you return False
def  luhn_algorithm(card_num):
    #stores original num to a different variable
    original_card_num = card_num
    i = 0
    k = 0

    sum = 0

    #stores last index to different varaible and subtract that
    check_digit = card_num[-1]
    card_num = list(card_num[:-1])

    #reverses the number
    card_num.reverse()
    
    #multiply every odd index by 2 and subtract 9 from any odd index that went over 9
    while (i < len(card_num)):
        card_num[i] = str(int(card_num[i]) * 2)
        if int(card_num[i]) >= 10 :
            card_num[i] = str(int(card_num[i]) - 9)
        i = i + 2

    #Sum all the index
    while (k < len(card_num)):
        sum = sum + int(card_num[k])
        k = k + 1
    total = int(sum)+ int(check_digit)
    
    #check if module 10 of sum is 0 if so returns original_card_num if not then return False
    if total % 10 == 0:
        return original_card_num
    else:
        return False

#Function that finds out what type of card it is
#Start with 4(visa), 5(mastercard), 6(discover), 3(american express) 
def card_type(card_num):
    if card_num[0] == "3":
        return "American Express Card"
    elif card_num[0] == "4":
        return "Visa Card"
    elif card_num[0] == "5":
        return "Mastercard"
    elif card_num[0] == "6":
        return "Discover Card"
    


def Validator():

    card_num = entry.get() 

    #Runs the first validator function called "format"
    #If the function returns false then prints a message saying that it not valid and why
    #Else it moves onto the next validator
    if(len(card_num) != 0):
    
        card_num = format(card_num)

        if card_num == False:
            message = "Not valid card number, reason: Invalid charectors included"
        else:
            
            #Runs the second validator function called "valid_nums_integers"
            #If the function returns false then prints a message saying that it not valid and why
            #Else it moves onto the next validator
            card_num = valid_nums_integers(card_num)

            if card_num == False:
                message = "Not valid card number, reason: Not right amount of charecters"

            elif card_num == "Error:Not right card type":
                message = "Not valid card number, reason: Not visa, mastercard, american express, or discover"

            else:
                #Runs the final validator function called "luhn_algorithm"
                #If the function returns false then prints a message saying that it not valid and why
                #Else it prints out that the card number is valid and the type of card it is
                card_num = luhn_algorithm(card_num)
                if card_num == False:
                    message = "Not valid card number, reason: Didn't pass the luhn algorithm"
                else:
                    type = card_type(card_num)
                    message = "valid"
                    message_valid = "Your",type,":",card_num, "is valid"
    else:
        message = "No Number Inputed"


    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")


    if(message != "valid"):
        messagebox.showerror("Not Valid", message)
    else:
        messagebox.showinfo("Valid", message_valid) 
        

if __name__ == "__main__":

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")


    root = customtkinter.CTk()
    root.geometry("600x350")



    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Credit Card Validator", font=("Roboto", 30))
    label.pack(pady=50, padx=50)

    entry = customtkinter.CTkEntry(master=frame, width=250, placeholder_text="Credit Card Number", font=("Arial", 14))
    entry.pack(pady=12, padx=10)


    button = customtkinter.CTkButton(master=frame, text="Click to Validate", command=Validator, corner_radius= 10)
    button.pack(pady=12, padx=10)

    root.wm_attributes("-toolwindow", 'True')
    root.mainloop()



