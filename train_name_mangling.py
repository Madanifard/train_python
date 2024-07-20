class Test:
    def __init__(self):
        self.bar = 10
        self._bar = 100
        self.__bar = 1000

    def hello(self):
        return 'Hello World! '

    def _hello(self):
        return 'Hello World! 2'

    def __hello(self):
        return 'Hello World! 3'


if __name__ == '__main__':
    test = Test()
    print(dir(test))
    # ['_Test__bar', '_Test__hello', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
    # '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
    # '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
    # '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bar', '_hello', 'bar', 'hello']
    print(test.bar)
    print(test._bar)
    print(test._Test__bar)
