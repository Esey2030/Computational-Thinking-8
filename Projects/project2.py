soccer_points=0
basketball_points=0


answer = input("On a weekend would you rather A) play soccer all day, or B) play basketball?")
if answer == "A":
    soccer_points += 1
elif answer == "B":
	basketball_points += 1
      

answer = input("Are you A) an introvert, or B) an extrovert?")
if answer == "A":
	soccer_points += 1
elif answer == "B":
    basketball_points += 1


answer = input("Would you rather A)have a small group of friends or B) with a big group?")
if answer == "A":
	soccer_points += 1
elif answer == "B":
	basketball_points += 1

print(f"basketball points = {basketball_points}")
print(f"soccer points = {soccer_points}")