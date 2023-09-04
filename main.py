import turtle
import pandas
import writer

screen = turtle.Screen()
screen.setup(725, 491)
screen.title('U.S. States Game')

bgimage = 'BlankStateImg.gif'
screen.addshape(bgimage)

turtle.shape(bgimage)

tim = writer.Writer()

data = pandas.read_csv('states.csv')

answer = screen.textinput('Guess the state!', 'Enter state names here:').title()

correctstates = []
while len(correctstates) != 50:
    if answer == 'Exit':
        statelist = data.state.to_list()
        for correctstate in correctstates:
            for state in statelist:
                if correctstate == state:
                    statelist.remove(state)
                    
        learndict = {
            'state': statelist
            }
        pandas.DataFrame(learndict).to_csv('StatesYouShouldLearn.csv')

        break

    for state in data.state:
        if answer == state:
            xcor = int(data[data.state == state].x)
            ycor = int(data[data.state == state].y)

            tim.gotolocation(xcor, ycor)
            tim.updatescreen(state)

            correctstates.append(state)

    answer = screen.textinput(f'{len(correctstates)}/50 States Correct.', 'Enter state names here:').title()