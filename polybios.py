class Polybios:
    def __init__(self, key: str, method: str, text: str):
        self.alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        self.key = list(k for k in key.upper().replace('Ä', 'AE').replace('Ö', 'OE').replace('Ü', 'UE') \
                        if k in self.alphabet)
        self.method = 1 if int(method) == 1 else 0
        if not self.method:
            self.the_text = list(p for p in text.upper().replace('Ä', 'AE').replace('Ö', 'OE').replace('Ü', 'UE') \
                                 if p in self.alphabet)
        else:
            self.code = list(x for x in text.split(' '))

    def create_matrix(self):
        temp = []
        for k in range(len(self.key)):
            if not self.key[k] in self.key[:k]:
                temp.append(self.key[k])
        temp.extend([x for x in self.alphabet if x not in temp])
        matrix = []
        for m in range(5):
            matrix.append(temp[m * 5:5 * m + 5])
        self.matrix = matrix

    def crypt(self):
        if not self.method:
            return self.__encrypt()
        else:
            return self.__decrypt()

    def __encrypt(self):
        __converter = dict()
        for i in self.matrix:
            for j in i:
                __converter[j] = str(self.matrix.index(i) + 1) + str(i.index(j) + 1)
        return ' '.join(__converter[a] for a in self.the_text)

    def __decrypt(self):
        return ''.join(self.matrix[int(x[0])-1][int(x[1])-1] for x in self.code)

if __name__ == '__main__':
    inpkey = input('Please type the key: ')
    inpmeth = input('Do you want to en-[0] or decode[1]? ')
    while not (inpmeth == '1' or inpmeth == '0'):
        print('This was neither 0 nor 1!')
        inpmeth = input('Do you want to en-[0] or decode[1]? ')
    inptext = input('Please type the text to en- or decode: ')

    converter = Polybios(inpkey, inpmeth, inptext)
    converter.create_matrix()

    print(converter.crypt())