# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# NewList = []  # New List for numbers less than 5
#
# for i in a:
#     if i < 5:
#         print(i)  # Write a program that prints out all the elements of the list that are less than 5.
#         NewList.append(i)  # Make a new list that has all the elements less than 5 and print out this new list
# print(NewList)
#
# print("Hello friend. Please write a number")  # Asking a number from the user
#
# UserInfo = int(input())  # Adding the number entered by the user
# # UserInfo = int(input("Hello friend. Enter a number: "))  # Using input in another way (video)
# List2 = []  # New list 2 for number less than the user's
#
# for t in a:
#     if t < UserInfo:
#         List2.append(t)
# print("The list of numbers less than " + str(UserInfo) + ", from the original list, is: " + str(List2))#

# contador = 1
# while contador < 1000:
#     print(contador)
#     contador = contador + 1

n = int(input("Ingresa un número: ").strip())
if n < 1 and n > 100:
    if n % 2 != 0:
        print("Weird")
    else:
        if n > 2 and n < 5:
            print("Not Weird")
        else:
            if n > 6 and n < 20:
                print("Weird")
            else:
                print("Not Weird")
