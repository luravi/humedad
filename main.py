reading = 0
radio.set_transmit_serial_number(True)
radio.set_group(4)
led.set_brightness(64)

def on_forever():
    global reading
    pins.analog_write_pin(AnalogPin.P1, 1023)
    reading = pins.analog_read_pin(AnalogPin.P0)
    radio.send_number(reading / 4)
    pins.analog_write_pin(AnalogPin.P1, 0)
    led.plot_bar_graph(reading, 1023)
    if input.button_is_pressed(Button.A):
        basic.show_number(reading)
    basic.pause(5000)
basic.forever(on_forever)
