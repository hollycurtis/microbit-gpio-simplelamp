from microbit import *

def main():
    # LED begins in a known off state
    state = 0
    # Loop forever
    while True:
        if is_button_pushed(pin0):
            state = flip_led_state(pin16, state)

def is_button_pushed(gpio_pin):
    # By default control circuit sends a high signal to pin0
    # When the button is pushed, the signal drops to zero as the switch completes the circuit to ground. The switch will then automatically re-open the original circuit.
    if gpio_pin.read_digital() == 0:
        sleep(10)
        # We double check whether a zero signal is present at pin0 to account for any mechanical issues in the button push
        if gpio_pin.read_digital() == 0:
            return True
    return False

def flip_led_state(gpio_pin, state):
    # If the LED is currently off, set its new state to on and vice versa
    state = not state
    # Switch the LED to its newly determined state
    gpio_pin.write_digital(state)
    # Wait for the switch to reset to an open state before returning to outer loop
    while pin0.read_digital() == 0:
        sleep(10)
    return state

if __name__ == "__main__":
    main()
