class plus:
    def __init__(self, a=0, b=0):
        self.var1 = int(a)
        self.var2 = int(b)

    def lplus (self):
        self.result = self.var1 + self.var2

    def get_result (self):
        return self.result

    def __add__(self, other):
        return plus(self.var1 + other.var1, self.var2 + other.var2)

    def __str__(self):
        return str(self.var1) + ' ' + str(self.var2)


a = plus(input('ENTER PLEASE'), input('ENTER AGAIN'))
a.lplus()
b = plus(input('ENTER PLEASE'), input('ENTER AGAIN'))
c = a + b
print('Результат сложения : {}'.format(a.get_result()))
print(c)