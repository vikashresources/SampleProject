import sys
import datetime
from math import pi
class Basic:
    def __init__(self):
        print('ooh la la, here we go...')

    def print_twinkle(self):
        print(
            "Twinkle, twinkle, little star, \n\tHow I wonder what you are! "
            "\n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. "
            "\nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
    def get_version(self):
        print('python version:')
        print(sys.version)
        print('version info')
        print(sys.version_info)

    def get_time(self):
        now = datetime.datetime.now()
        print('Current date and time is: ')
        print(now.strftime("%Y-%m-%d %H:%M:%S"))

    def calc_area(self,radius):
        print('Area of circle with given radius ' + str(radius) + ' is: ' + str(pi * radius**2))

    def reverse_name(self):
        fname = input('Enter first name: ')
        lname = input('Enter last name: ')
        print('Hello ' + lname + ' ' + fname)

    def convert_CSV(self):
        csv = input("Enter some comma apart values: ")
        lst = csv.split(',')
        tple = tuple(lst)
        print('List : ', lst)
        print('Tuple: ', tple)

    def get_ext(self):
        filename = 'demo.python'
        ext = filename.split('.')
        print('Ext. of file is ' + repr(ext[-1]))

    def get_color(self):
        color_list = ['RED','GREEN','BLACK','YELLOW']
        print('First color ', color_list[0])
        print('Last color ',color_list[3])

    def print_int(self):
        a = 5
        n1 = int('%s' % a)
        n2 = int('%s%s' % (a,a))
        n3 = int('%s%s%s' %(a,a,a))
        print(n1+n2+n3)


if __name__ == '__main__':
    b = Basic()
    print('###...print twinkle twinkle start...###')
    b.print_twinkle()
    print('###...print python version...###')
    b.get_version()
    print('###...print current date and time...###')
    b.get_time()
    print('###...calculate area of circle...###')
    rad = float(input('Provide the radius of circle...'))
    b.calc_area(rad)
    print('###...reverse last name and first name...###')
    b.reverse_name()
    print('###...Convert CSV into list and tupples...###')
    b.convert_CSV()
    print('###...Get file ext...###')
    b.get_ext()
    print('###...Get list color...###')
    b.get_color()
    print('###...Get string rep of 5...###')
    b.print_int()








