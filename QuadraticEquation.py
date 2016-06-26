'''
Solving for roots of a quadratic equation
'''

def roots(a,b,c):

    root1 = (-b+((b**2-4*a*c))**0.5)/(2*a)
    root2 = (-b - ((b ** 2 - 4 * a * c))**0.5) / (2 * a)

    print('root1 = {0}'.format(root1))
    print('root2 = {0}'.format(root2))

if __name__ == '__main__':
    print('aX^2+bX+c = 0\n')
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')

    print('{0}X^2+{1}X+{2}=0'.format(a,b,c))

    roots(float(a),float(b),float(c))
