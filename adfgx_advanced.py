from adfgx import Adfgx

class Advanced_ADFGX:
    def __init__(self, inpkey1: str, inpkey2: str, inpmeth: str, inptext: str):
        __converter = Adfgx(inpkey1, inpmeth, inptext)
        __converter.create_matrix()
        self.step1 = __converter.crypt().replace(' ', '')
        self.key = inpkey2.upper()

    def create_matrix(self):
        self.lenx = len(self.key)
        self.leny = (len(self.step1)+self.lenx-1)//self.lenx
        _, __ = [], []
        for i in range(self.leny):
            for j in range(self.lenx):
                try:
                    __.append(self.step1[i * self.lenx + j])
                except Exception:
                    __.append('X')
            _.append(__)
            __ = []
        self.matrix = _

    def create_switcher(self):
        _ = []
        for c in self.key:
            _.append(c)
        _.sort()
        __ = []
        for c in self.key:
            __.append(_.index(c))
            _[_.index(c)] = '0'
        self.switcher = __

    def rot_matrix(self):
        _ = [[] for x in range(self.leny - 1)]
        for c in range(self.lenx):
            _[c].extend([self.matrix[x][c] for x in range(self.leny)])
        self.matrix = _

    def get_results(self):
        _ = []
        for i in self.switcher:
            _.append(self.matrix[i])
        return _

if __name__ == '__main__':
    inpkey = input('Please type the key: ')
    inpkey2 = input('Please type the second key: ')
    inpmeth = input('Do you want to en-[0] or decode[1]? ')
    while not (inpmeth == '1' or inpmeth == '0'):
        print('This was neither 0 nor 1!')
        inpmeth = input('Do you want to en-[0] or decode[1]? ')
    inptext = input('Please type the text to en- or decode: ')

    converter = Advanced_ADFGX(inpkey, inpkey2, inpmeth, inptext)
    converter.create_matrix()
    converter.create_switcher()
    converter.rot_matrix()
    print(converter.get_results())
