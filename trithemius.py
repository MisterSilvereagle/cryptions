class Trithemius:
    def __init__(self, displacement: int, method: str, text: str):
        self.displacement = displacement
        self.method = 1 if int(method) == 1 else 0
        self.the_text = text

    def get_results(self):
        pass

if __name__ == '__main__':
    inpdisp = input('Please type the displacement amount: ')
    while not inpdisp.isdigit():
        print('This was NaN!')
        inpdisp = input('Please type the displacement amount: ')
    inpdisp = int(inpdisp)
    inpmeth = input('Do you want to en-[0] or decode[1]? ')
    while not (inpmeth == '1' or inpmeth == '0'):
        print('This was neither 0 nor 1!')
        inpmeth = input('Do you want to en-[0] or decode[1]? ')
    inptext = input('Please type the text to en- or decode: ')

    converter = Trithemius(inpdisp, inpmeth, inptext)

    print(converter.get_results())