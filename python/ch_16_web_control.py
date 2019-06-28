from bottle import route, run
from gpiozero import LED, Button

leds = [LED(18), LED(23), LED(24)]
switch = Button(25)

def switch_status():
    if switch.is_pressed:
        return 'Down'
    else:
        return 'Up'

def html_for_led(led_number):
    i = str(led_number)
    result = " <input type='button' onClick='changed(" + i + ")' value='LED " + i + "'/>"
    return result

@route('/')
@route('/<led_number>')
def index(led_number="n"):
    if led_number != "n":
        leds[int(led_number)].toggle()
    response = "<script>"
    response += "function changed(led)"
    response += "{"
    response += "  window.location.href='/' + led"
    response += "}"
    response += "</script>"
    
    response += '<h1>GPIO Control</h1>'
    response += '<h2>Button=' + switch_status() + '</h2>'
    response += '<h2>LEDs</h2>'
    response += html_for_led(0) 
    response += html_for_led(1) 
    response += html_for_led(2) 
    return response

run(host='0.0.0.0', port=80)
