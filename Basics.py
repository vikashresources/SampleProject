import sys
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

if __name__ == '__main__':
    b = Basic()
    print('###...print twinkle twinkle start...###')
    b.print_twinkle()
    print('###...print python version...###')
    b.get_version()






