###############################################################################
#
#   Do this WITH YOUR INSTRUCTOR (live in class):
#
#   Read the code below.  Predict (in your head)
#   what will get printed (i.e., displayed) when the code runs.
#
#   Then run this module by right clicking anywhere in this window
#   and then selecting:
#        Run 'name of file'
#   (i.e.  Run 'm1e_comments_strings...')  Or, use the Windows keyboard
#   shortcut:  Control + Shift + Function-F10.  (That is, hold the
#   Control, Shift and Function keys down and press the F10 key.)
#
#   Confirm that you see the output in the  "Run"  window that appears.
#     Note: I recommend that you click on the "Gear" symbol at the top-right
#           part of that window and select
#              Move to  ~  Right
#           to make the output easier to see.
#   Confirm that the output is what you expected, asking questions as desired.
#
#   This module is just an example (m1e, note the 'e').
#   After you have read and run the code,
#   feel free to play with it briefly, then move on to m2.
#
###############################################################################
import rosegraphics as rg
import math

# def problem1(m):
#     sum = 0
#     for k in range(m,4*m+1):
#         if math.cos(k) > 0:
#             sum = sum + math.cos(k)
#     return sum
#
# print(problem1(1))
#
# def problem2a(circle,window):
#     circle.attach_to(window)
#     h_line = rg.Line(rg.Point(circle.center.x - circle.radius,circle.center.y), rg.Point(circle.center.x + circle.radius,circle.center.y))
#     v_line = rg.Line(rg.Point(circle.center.x,circle.center.y - circle.radius), rg.Point(circle.center.x,circle.center.y + circle.radius))
#     h_line.attach_to(window)
#     v_line.attach_to(window)
#     window.render()
#


a = ([1,2,3],[3,4,5])
print(a)
list1 = a[1]
list1[0] = 6
print(a)


# print('test1')
# win = rg.RoseWindow()
# circle = rg.Circle(rg.Point(200,200),20)
# problem2a(circle,win)
#
# def problem2b(circle,dx,dy,n,window):
#     for k in range(n):
#         new_center = rg.Point(circle.center.x + k*dx,circle.center.y + k*dy)
#         c_clone = rg.Circle(new_center,circle.radius)
#         c_clone.attach_to(window)
#         problem2a(c_clone,window)
#     window.render()
#     window.close_on_mouse_click()
#
#
# circle2 = rg.Circle(rg.Point(200, 250), 20)
# window = rg.RoseWindow()
#
# problem2b(circle2,5,10,4,window)
# win.close_on_mouse_click()




# class Mini(object):
#     def __init__(self,a):
#         self.a = 3
#         self.m = a + 5
#
#         print(self.m)
#
# m1 = Mini(10)

# print('Hello, World')
# print('hi there')
# print('one', 'two', 'buckle my shoe')
#
# print(3 + 9)
# print('3 + 9', 'versus', 3 + 9)


