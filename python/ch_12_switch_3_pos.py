from gpiozero import Button

switch_top = Button(18)
switch_bottom = Button(23)

switch_position = "unknown"

while True:
    new_switch_position = "unknown"
    if switch_top.is_pressed:
        new_switch_position = "top"
    elif switch_bottom.is_pressed:
        new_switch_position = "bottom"
    else:
        new_switch_position = "center"

    if new_switch_position != switch_position:
        switch_position = new_switch_position
        print(switch_position)
