import sys
import datetime
from math import pi
import calendar
import os, platform
import socket
import struct
from timeit import default_timer
import json
from inspect import getmodule
from math import sqrt
import collections
import functools
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

    def print_date(self):
        exam_start = (11,11,2019)
        print("Exam date will start from: %i / %i / %i " % exam_start)
    def get_calendar(self):
        yy = int(input('type the year'))
        mm = int(input('type the month'))
        print(calendar.month(yy,mm))

    def odd_product(self,numbs):
        for i in range(1,len(numbs)):
            for j in range(1,len(numbs)):
                if numbs[i] != numbs[j]:
                    product = numbs[i] * numbs[j]
                    if product & 1:
                        return True
                        return False

    def sum_of_cubes(self,num):
        sum = 0
        n = 1
        while n < num:
            sum = n*n*n
            n += 1
        return sum

    def min_max(self,data):
        l = data[0]
        s = data[0]
        for num in data:
            if num > l:
                l = num
            elif num < s:
                s = num
        return l,s

    def multiple(self,m,n):
        return True if m % n == 0 else False

    def validate_ip_address(self):
        ip = '192.168.0.109'
        try:
            socket.inet_aton(ip)
            print('valid ip')
        except socket.error:
            print('invalid ip')

    def check_type(self,data):
        if type(data) is list:
            print('list...')
        elif type(data) is set:
            print('set...')
        elif type(data) is tuple:
            print('tuple...')
        else:
            print('Neither a list, set or tuple')

    def timer(self,n):
        start = default_timer()
        for i in range(n):
            print(i)
        print(default_timer()-start)




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
    print('###...Get string form addition...###')
    b.print_int()
    print('###...print exam start date...###')
    b.print_date()
    print('###...print doc string of absolute function...###')
    print(abs.__doc__)
    print('###...print calendar format of given month and year...###')
    b.get_calendar()
    print('###To check if odd product is there in list### ')
    dt1 = [2,4,8,12]
    dt2 = [2,3,5,4,6]
    print('List dt1 has odd product: ', b.odd_product(dt1))
    print('List dt2 has odd product: ', b.odd_product(dt2))
    print('### sum of cubes ###')
    print(b.sum_of_cubes(8))
    print('###  largest and smallest ###')
    print(b.min_max(dt1))
    print(b.multiple(9,3))
    print(b.multiple(9, 4))
    print(sys.modules)
    print(sys.path)
    print(os.path)
    print(isinstance(25,int) or isinstance(25,str) )
    print(isinstance([25],int) or isinstance([25],str))
    print(isinstance("25",int) or isinstance("25",str))
    print('###  validating ip address ###')
    b.validate_ip_address()
    print('###  validating type of list ###')
    data = [1,2,3]
    b.check_type(data)
    data = (1,2,3)
    b.check_type(data)
    data = {1,2,4}
    b.check_type(data)
    print('###  system details ###')
    print(os.name)
    print(platform.system())
    print(platform.release())
    print(struct.calcsize("P") * 8)
    print('###  convert decimal to hexadecimal ###')
    print(format(30, '02x'))
    print(format(12, '08b'))
    print(format(12, '010b'))
    d = {'RED': 'GREEN'}
    (c1, c2), = d.items()
    print(c1)
    print(c2)
    x = 30
    print('value of x is "{}"'.format(x))
    print('### use of map ###')
    print('type value of x & y')
    print(list(map(int, input().split())))
    b.timer(20)
    print(json.dumps({'Alex' : 1, 'Hari': 2,'Agi': 3}))
    print(getmodule(sqrt))
    num = [2, 2, 4, 6, 6, 8, 6, 10, 4]
    print(sum(collections.Counter(num).values()))
    print(sys.int_info)
    print(sys.float_info)
    print(sys.maxsize)
    str_num = "1234567890"
    print()
    print('%.6s' % str_num)
    print()
    order_amt = 212.374
    print('\nThe total order amount comes to %f' % order_amt)
    print('The total order amount comes to %.2f' % order_amt)
    print()
    print(functools.reduce(lambda a, b: a+b, num))
    import operator
    print(functools.reduce(operator.mul, num))


