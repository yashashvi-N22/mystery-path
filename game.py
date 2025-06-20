import turtle
import random
from utils import countdown, fake_lookaround, play_sound
import time

class MysteryPathGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Mystery Path: Guess the Turtle's Destination")
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600)

        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.t.color("white")
        self.t.penup()
        self.t.speed(1)

        self.destinations = {
            "red": (-200, 200),
            "green": (200, 200),
            "yellow": (-200, -200),
            "blue": (200, -200)
        }

        self.score = 0
        self.total = 0
        self.max_rounds = 3
        self.history = []

        self.message = turtle.Turtle()
        self.message.hideturtle()
        self.message.color("white")
        self.message.penup()
        self.message.goto(0, 250)

        self.mark_destinations()
        self.bind_keys()
        self.correct_color = random.choice(list(self.destinations.keys()))
        self.show_instructions()

        self.screen.mainloop()

    def mark_destinations(self):
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        for color, pos in self.destinations.items():
            marker.goto(pos)
            marker.dot(50, color)

    def bind_keys(self):
        self.screen.listen()
        for color in self.destinations:
            self.screen.onkey(lambda c=color: self.guess(c), color[0])  # r, g, y, b

    def show_instructions(self):
        self.message.clear()
        self.message.write("🎯 Guess the turtle's destination!\nPress R, G, Y, or B for Red, Green, Yellow, or Blue.",
                           align="center", font=("Arial", 14, "bold"))

    def guess(self, user_guess):
        if self.total >= self.max_rounds:
            return

        self.total += 1
        self.message.clear()
        self.t.goto(0, 0)
        self.t.setheading(0)
        self.t.color("white")
        self.t.pendown()

        fake_lookaround(self.t, self.destinations)
        countdown(self.message)
        self.t.setheading(self.t.towards(self.destinations[self.correct_color]))
        self.t.goto(self.destinations[self.correct_color])
        self.t.penup()

        if user_guess == self.correct_color:
            self.score += 1
            play_sound(True)
            result = f"✅ Correct! The turtle went to {self.correct_color.upper()}."
        else:
            play_sound(False)
            result = f"❌ Wrong! You guessed {user_guess.upper()}, but it went to {self.correct_color.upper()}."

        self.history.append((user_guess, self.correct_color))

        if self.total < self.max_rounds:
            result += f"\nRound: {self.total}/{self.max_rounds} | Score: {self.score}"
            result += "\n\nPress R, G, Y, or B for next round."
        else:
            result += f"\n\n🏁 Game Over!\nFinal Score: {self.score}/{self.max_rounds}"
            result += f"\n\n📜 Guess History: {self.history}"

        self.message.clear()
        self.message.write(result, align="center", font=("Arial", 14, "bold"))
        self.correct_color = random.choice(list(self.destinations.keys()))
