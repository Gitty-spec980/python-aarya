import turtle

def draw_star(size=100, color="yellow", bgcolor="black"):
    """Draws a star using Python's turtle graphics."""
    screen = turtle.Screen()
    screen.bgcolor(bgcolor)
    screen.title("Turtle Star")

    star = turtle.Turtle()
    star.color(color)
    star.pensize(2)
    star.speed(3)

    # Draw the star
    for _ in range(5):
        star.forward(size)
        star.right(144)  # Angle for a 5-pointed star

    turtle.done()

if __name__ == "__main__":
    try:
        draw_star(size=150, color="gold", bgcolor="navy")
    except turtle.Terminator:
        print("Turtle graphics window closed.")
