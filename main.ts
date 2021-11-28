input.onButtonPressed(Button.A, function () {
    if (_001 == 0) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            `)
        basic.clearScreen()
    } else if (_001 > 0) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.AB, function () {
    if (_001 == 1) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # . # .
            . # # # .
            . . . . .
            `)
        basic.clearScreen()
    }
})
function doSomething () {
    basic.showLeds(`
        . # # # .
        # # . # #
        # . . . #
        . # # # .
        . . . . .
        `)
    basic.pause(500)
    basic.showLeds(`
        . # # # .
        # . # # #
        # . . . #
        . # # # .
        . . . . .
        `)
    basic.pause(500)
    basic.showLeds(`
        . # # # .
        # # # . #
        # . . . #
        . # # # .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . # # # .
        # # . # #
        # . . . #
        . # # # .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # # # .
        # # . # #
        # . . . #
        . # # # .
        . . . . .
        `)
    basic.pause(100)
    basic.showIcon(IconNames.Yes)
    basic.clearScreen()
}
input.onButtonPressed(Button.B, function () {
    if (_001 > 0) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        basic.clearScreen()
    } else if (_001 == 0) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            `)
        basic.clearScreen()
    }
})
let _001 = 0
doSomething()
basic.forever(function () {
    _001 = randint(0, 2)
})
