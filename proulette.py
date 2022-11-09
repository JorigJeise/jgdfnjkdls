import random

def proulette():
    colour = random.randint(1, 100)

    if colour <= 50:
        return "Red :red_circle:"
    elif colour >=49 and colour != 99 and colour != 100:
        return "Purple :purple_circle:"
    elif colour == 99 or colour == 100:
        return "Yellow :yellow_circle:"