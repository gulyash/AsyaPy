x, y, r = map(float, input('Please input x, y and r: ',).split())
if x*x + y*y <= r*r:
    print('The point belongs to the circle.')
else:
    print('The point does not belong to the circle. ')
