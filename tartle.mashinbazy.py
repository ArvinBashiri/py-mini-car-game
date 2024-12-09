import random
import time
import turtle as t
import random as r

player_one = t.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)


player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)


die = [1,2,3,4,5,6]

for i in range(20):
    if player_one.pos() >= (300,100):
        print("player one wins!")
        break
    elif player_two.pos() >= (300,-100):
        print("player two wins!")
        break
    else:
        player_one_turn = input("press 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("the result of the die roll is: ")
        print(die_outcome)
        print("the number of steps will be: ")
        print(20*die_outcome)
        player_one.forward(20*die_outcome)
        player_two_turn = input("press 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("the result of the die roll is: ")
        print(die_outcome)
        print("the number of steps will be: ")
        print(20*die_outcome)
        player_two.forward(20*die_outcome)


time.sleep(5)


