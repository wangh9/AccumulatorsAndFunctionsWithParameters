"""
This module demonstrates simple LOOPS of the form:
   for k in range(blah):
      ... k ...

and also USING OBJECTS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Heda Wang.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math

def main():
    print_sequence1()
    draw_circles1()
    print_sequence2()
    draw_circles2()
    print_sequence3()
    draw_circles3()
    print_cosines()
    draw_cosines_and_sines()
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def print_sequence1():
    c = 0
    for k in range(20):
       c = c + 10
       print(c)

    """
    Prints:
       0
       10
       20
       30
       40
       ...
       200
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence1:')
    print('--------------------------------------------------')


def draw_circles1():
    window = rg.RoseWindow(400,400)
    for k in range(20):
        rad = 0
        rad = 10 * k
        cir1 = rg.Circle(rg.Point(200, 200), rad)
        cir1.attach_to(window)
        window.render(0.05)
    window.close_on_mouse_click()
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws 21 rg.Circle objects such that:
         -- Each is centered at (200, 200)
         -- They have radii:  0  10  20  30  40 ... 200, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles1:  See graphics window')
    print('--------------------------------------------------')


def print_sequence2():
    c = 50
    for k in range(17):
        c = c + 20
        print(c)

    """
    Prints:
      50
      70
      90
      110
      130
      ...
      390.
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence2:')
    print('--------------------------------------------------')


def draw_circles2():
    window = rg.RoseWindow(400, 400)
    x =50
    for k in range(17):
        cir1 = rg.Circle(rg.Point(x, 100), 10)
        cir1.fill_color = 'blue'
        cir1.attach_to(window)
        window.render(0.05)
        x = x + 50
    window.close_on_mouse_click()
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- Each has fill_color 'blue'.
         -- They are centered at, respectively:
               (50, 100)   (70, 100)   (90, 100)  (110, 100) ... (390, 100)
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles2:  See graphics window')
    print('--------------------------------------------------')


def print_sequence3():
    c = 0
    for k in range(100):
        c = c + 1
        print(c)
    """
    Prints:
      1
      2
      3 
      4
      ...
      100.
    """
    # ------------------------------------------------------------------
    # DONE: 6. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence3:')
    print('--------------------------------------------------')


def draw_circles3():
    window = rg.RoseWindow(300, 300)
    x = 1
    for k in range(100):
        cir1 = rg.Circle(rg.Point(200, 150), x)
        cir1.attach_to(window)
        window.render(0.05)
        x = x + 1
    window.close_on_mouse_click()
    """
    -- Constructs an rg.RoseWindow whose width and height are both 300.
    -- Constructs and draws 100 rg.Circle objects such that:
         -- Each is centered at (200, 150)
         -- They have radii:  1  2  3  4  ... 100, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 7. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles3:  See graphics window')
    print('--------------------------------------------------')


def print_cosines():
    c = 0
    for k in range(100):
        print(math.cos(c)* 80)
        c = c + 1


    """
    For each of the integers 0  1  2  ... 100,
    prints 80 times the cosine of that integer.
    Thus, the numbers printed should be about:
       80.0
       43.224184469451174
       -33.29174692377139
       -79.19939972803563
       -52.29148966908895
       22.6929748370581
       76.81362293202928
       60.31218034746437
         ...
       -65.54305962331674
       3.185670431451112
       68.9855097830147
    """
    # ------------------------------------------------------------------
    # DONE: 8. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    #
    # HINT: You need to   import math   at the top of this file
    #       to use math functions like the ones for cosine and sine.
    #       Once you have that import in place, typing
    #            math.
    #       (note the DOT) and pausing will display options that make
    #       it plain what the notation for the cosine function is.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_cosines:')
    print('--------------------------------------------------')


def draw_cosines_and_sines():
    window = rg.RoseWindow(400, 400)
    x = 0
    y = 0
    for k in range(100):
        x = 200 + (80* math.cos(k))
        y = 200 + (80*math.sin(k))
        cir1 = rg.Circle(rg.Point(x, y), 10)
        cir1.attach_to(window)
        window.render(0.05)
    window.close_on_mouse_click()
    """
    -- Constructs a window whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- They are centered at, respectively:
               ( 200 + (80 * cos(0)), 200 + (80 * sin(0) )
               ( 200 + (80 * cos(1)), 200 + (80 * sin(1) )
               ( 200 + (80 * cos(2)), 200 + (80 * sin(2) )
               ( 200 + (80 * cos(3)), 200 + (80 * sin(3) )
                   ...
               ( 200 + (80 * cos(100)), 200 + (80 * sin(100) )
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 9. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_cosines_and_sines:  See graphics window')
    print('--------------------------------------------------')

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
