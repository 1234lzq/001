def on_button_pressed_a():
    if _001 == 0:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . # # # .
                        . . . . .
                        . . . . .
        """)
        basic.clear_screen()
    elif _001 > 0:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if _001 == 1:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # . # .
                        . # # # .
                        . . . . .
        """)
        basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def doSomething():
    basic.show_leds("""
        . # # # .
                # # . # #
                # . . . #
                . # # # .
                . . . . .
    """)
    basic.pause(500)
    basic.show_leds("""
        . # # # .
                # . # # #
                # . . . #
                . # # # .
                . . . . .
    """)
    basic.pause(500)
    basic.show_leds("""
        . # # # .
                # # # . #
                # . . . #
                . # # # .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . # # # .
                # # . # #
                # . . . #
                . # # # .
    """)
    basic.pause(100)
    basic.show_leds("""
        . # # # .
                # # . # #
                # . . . #
                . # # # .
                . . . . .
    """)
    basic.pause(100)
    basic.show_icon(IconNames.YES)
    basic.clear_screen()

def on_button_pressed_b():
    if _001 > 0:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        basic.clear_screen()
    elif _001 == 0:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . # # # .
                        . . . . .
                        . . . . .
        """)
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

_001 = 0
doSomething()

def on_forever():
    global _001
    _001 = randint(0, 2)
basic.forever(on_forever)
