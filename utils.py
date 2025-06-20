import time

try:
    import winsound
except ImportError:
    winsound = None

def countdown(message_turtle):
    for i in range(3, 0, -1):
        message_turtle.clear()
        message_turtle.write(f"Moving in... {i}", align="center", font=("Arial", 14, "bold"))
        time.sleep(1)

def fake_lookaround(turtle_obj, destinations):
    for color in destinations:
        turtle_obj.setheading(turtle_obj.towards(destinations[color]))
        time.sleep(0.2)

def play_sound(success=True):
    if winsound:
        freq = 1000 if success else 400
        winsound.Beep(freq, 200)
