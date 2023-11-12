import turtle
import pandas
screen=turtle.Screen()
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
screen.title("U.S State")
#to get x and y values by clicking it
# def get_mouse_on_click(x,y):
#     print(x,y)
# screen.onscreenclick(get_mouse_on_click)
# turtle.mainloop()#alternative for exit on click
data=pandas.read_csv("50_states.csv")
# print(data["x"].max())
# print(data["y"].max())
states=data["state"].tolist()
game=True
guessed_letter=[]
to_learn = []

while game:
    answer = screen.textinput(title=f"{len(guessed_letter)}/50 States Correct", prompt="What's the another state?").title()
    if answer=="Exit":
        game=False
    if answer in states and answer not in guessed_letter:
            guessed_letter.append(answer)
            t=turtle.Turtle()
            t.hideturtle()
            t.penup()
            ans2=data[data.state==answer]
            t.goto(int(ans2.x),int(ans2.y))
            t.write(answer)#in place of answer we can use states.state.item()
    elif len(guessed_letter) > 50:
            game=False
#csv for left out
for state in states:
    if state not in guessed_letter:
        to_learn.append(state)
new=pandas.DataFrame(to_learn)
new.to_csv("to learn.csv")


