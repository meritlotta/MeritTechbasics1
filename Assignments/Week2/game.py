import time
import sys

def type_text(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Welcome
type_text("️🐭: Welcome to this fun guessing game!️")

#Enter your name
name = input("🐭: Please enter your name: ")
time.sleep(1)
print("🐭: Hello " + name)
time.sleep(1)
print("🐭: We will start with the game now 🕺🕺")
time.sleep(1)

# Start of the score system
score = 0

# Question 1
answer_1 = input("🐭: What is the capital of Germany? ")
time.sleep(1)
if answer_1.lower() == "berlin":
    print("🎉Correct! You earned 1 point.🎉")
    score += 1
else:
    print ("️❌This is incorrect. The correct answer would be Berlin. ❌")

# Question 2
time.sleep(1)
answer_2 = input("🌈How many colours are in a Rainbow? Please spell the number🌈: ")
time.sleep(1)
if answer_2.lower() == "seven":
    print("🎉Correct! You earned 1 point.🎉")
    score += 1

    # Following bonus question
    time.sleep(1)
    print("Bonus point if you can tell me all seven colours! ")
    bonus_1 = input("Please make sure, the colours are seperated by a comma: ")
    time.sleep(1)

    user_colors = [color.strip().lower() for color in bonus_1.split(",")]
    correct_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]

    if sorted(user_colors) == sorted(correct_colors):
        print("🎉Wow! That was amazing! Good job!🎉")
        score += 1
    else:
        print("❌Sorry, that was incorrect. But nice try. ❌")
else:
    print ("❌This is incorrect. The correct answer would be seven. ❌")

# Question 3
time.sleep(1)
answer_3 = input("🌊What is the name of the largest ocean on Earth?🌊 ")
time.sleep(1)
if answer_3.lower() == "pacific" or "pacific ocean" or "the pacific ocean":
    print("🎉Correct! You earned 1 point.🎉")
    score += 1
else:
    print ("❌This is incorrect. The correct answer would be the pacific ocean. ❌")

# Question 4
time.sleep(1)
answer_4 = input("🌐In a website browser address bar, what does 'www' stand for?🌐 ")
time.sleep(1)
if answer_4.lower() == "world wide web":
    print("🎉Correct! You earned 1 point.🎉")
    score += 1
else:
    print ("❌This is incorrect. The right answer would be 'world wide web'. ❌")

# Question 5
time.sleep(1)
answer_5 = input("🚕Originally, Amazon only sold what kind of product?🚕 ")
time.sleep(1)
if answer_5.lower() == "books":
    print("🎉Correct! You earned 1 point.🎉")
    score += 1
else:
    print ("❌This is incorrect. The right answer would be books. ❌")

# Question 6
time.sleep(1)
while True:
    answer_6 = input("🏙️What is the population of Tokyo?🏙️ (in millions) ")
    if answer_6.isdigit():
        answer_6 = int(answer_6)
        if 35 <= answer_6 <= 39:
            print("🎉The actual answer is 37 million. You were within the range of 35 and 39, so you earned 1 point!🎉")
            score += 1
        else:
            print("❌This is incorrect. The actual answer is 37 million.❌")
        break  # exit the loop once a valid number is given
    else:
        print("⚠️That was not a valid number. Please try again.⚠️")

# Question 7
time.sleep(1)
answer_7 = input("👑Where is the 'Mona Lisa' painting on display?👑 ")
time.sleep(1)
if answer_7.lower() == "louvre" or "the louvre" or "louvre museum" or "the louvre museum":
    print("🎉Correct! You earned 1 point.🎉")
    score += 1
else:
    print ("❌This is incorrect. The correct answer would be the louvre museum. ❌")

# Question 8
time.sleep(1)
branch = input("🍄You have the choice. Would you rather answer a tricky riddle or a fun fact? Please enter 'tricky' or 'fun'🍄: " )
if branch.lower() == "tricky":
    answer_8 = input("🍊What has keys but can't open locks?🍊 ")
    if answer_8.lower() == "piano":
        print("🎉Correct! You earned 1 point.🎉")
        score += 1
    else:
        print("❌Incorrect. The correct answer is 'piano'.❌")
elif branch.lower() == "fun":
    answer_8 = input("📖What is the best-selling book of all time?📖 " )
    if answer_8.lower() == "bible" or "the bible":
        print("🎉Correct! You earned 1 point.🎉")
        score += 1
    else:
        print("❌Incorrect. The correct answer is 'piano'.❌")
else:
    print("⚠️Invalid choice. Skipping this question.⚠️")


# Print final score
time.sleep(1)
type_text("Final score is loading...")
time.sleep(1)
type_text("3...")
time.sleep(1)
type_text("2...")
time.sleep(1)
type_text("1...")
time.sleep(1)
type_text("Final score: " + str(score) + "/8")
