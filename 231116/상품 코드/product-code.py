class Code:
    def __init__(self, name = 'codetree', code = '50'):
        self.name = name
        self.code = code

name, code = input().split()
code1 = Code()
print(f'product {code1.code} is {code1.name}')
code1.name = name
code1.code = code
print(f'product {code1.code} is {code1.name}')