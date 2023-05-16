import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label(
    "Hello World",
    font_name="Times New Roman",
    font_size=36,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center",
)

DICE_PADDING = 0.15

NUM_DICE = 5

dice = [
    pyglet.text.Label(
        str(i + 1),
        font_name="Times New Roman",
        font_size=36,
        x=window.width * (DICE_PADDING + (i * (1 - DICE_PADDING)) / (NUM_DICE)),
        y=window.height // 2,
        anchor_x="center",
        anchor_y="center",
    )
    for i in range(NUM_DICE)
]

label.text = "5"


@window.event
def on_draw():
    window.clear()
    for die in dice:
        die.draw()


pyglet.app.run()
