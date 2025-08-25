import random
Dice_Number=[1,2,3,4,5,6]
print(" Choose a no. between 1 to 6")

computer=random.choice(Dice_Number)

user=int(input("Enter a No."))

if 1<=user<=6:
   print(f"Computer choose:{computer}")
   print(f"user choose:{user}")
   if user==computer:
      print("Draw 🤝")
   elif user>computer :
       print("User Wins 🎉")
   else :
        print("Computer Wins 🎉")
else:
    print(" ❌ Invalid choice, Choose Again. ")

