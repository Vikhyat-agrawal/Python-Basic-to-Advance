subject_one=int(input("Enter marks of subject one: "))
subject_two=int(input("Enter marks of subject two: "))
subject_three=int(input("Enter marks of subject three: "))
total_marks=subject_one+subject_two+subject_three
percentage=(total_marks/300)*100
if percentage>=33:
    if subject_one>=40 and subject_two>=40 and subject_three>=40:
        print(f"Congratulations! You have passed with {percentage}%")
    else:
        print(f"Sorry! You have failed. You scored {percentage}%")
else:
    print(f"Sorry! You have failed. You scored {percentage}%")