class FourSquare:
    def __init__(self, keys: list, method: str, text):
        self.alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        self.default_matrix = [([n for n in self.alphabet])[m * 5: m * 5 + 5] for m in range(5)]
        self.keys = [list(k for k in keys[i].upper().replace('Ä', 'AE').replace('Ö', 'OE').replace('Ü', 'UE') \
                          if k in self.alphabet) for i in range(len(keys))]
        self.method = 1 if int(method) == 1 else 0
        self.the_text = list(p for p in text.upper().replace('Ä', 'AE').replace('Ö', 'OE').replace('Ü', 'UE') \
                             if p in self.alphabet)

    def create_matrices(self):
        temp = [[], []]
        for i in range(len(self.keys)):
            for k in range(len(self.keys[i])):
                if not self.keys[i][k] in self.keys[i][:k]:
                    temp[i].append(self.keys[i][k])
            temp[i].extend([x for x in self.alphabet if x not in temp[i]])
        matrix1, matrix2 = [], []
        for m in range(5):
            matrix1.append(temp[0][m * 5:5 * m + 5])
            matrix2.append(temp[1][m * 5:5 * m + 5])
        self.matrix1, self.matrix2 = matrix1, matrix2

    def get_result(self):
        if not self.method:
            return self.__decrypt()
        else:
            return self.__encrypt()

    def __decrypt(self):
        bigrams = self.__split_into_bigrams(self.the_text)
        result = []
        for c in bigrams:
            result.extend(self.__chooser_enc(c))
        return ''.join(x for x in result)

    def __encrypt(self):
        bigrams = self.__split_into_bigrams(self.the_text)
        result = []
        for c in bigrams:
            result.extend(self.__chooser_dec(c))
        return ''.join(x for x in result)

    def __chooser_enc(self, inp: list):
        loc1, loc2 = self.__find_in_nested_list(inp[0], self.matrix1), \
                     self.__find_in_nested_list(inp[1], self.matrix2)
        loc1[1], loc2[1] = loc2[1], loc1[1]
        return [self.__convert_coords_to_string(tuple(loc1), self.default_matrix),
                self.__convert_coords_to_string(tuple(loc2), self.default_matrix)]

    def __chooser_dec(self, inp: list):
        loc1, loc2 = self.__find_in_nested_list(inp[0], self.default_matrix), \
                     self.__find_in_nested_list(inp[1], self.default_matrix)
        loc1[1], loc2[1] = loc2[1], loc1[1]
        return [self.__convert_coords_to_string(tuple(loc1), self.matrix1),
                self.__convert_coords_to_string(tuple(loc2), self.matrix2)]

    def __find_in_nested_list(self, a: str, mat: list) -> list:
        for m in range(len(mat)):
            for n in range(len(mat[m])):
                if mat[m][n] == a:
                    return [m, n]

    def __split_into_bigrams(self, inp: list) -> list:
        temp = []
        _ = []
        for m in inp:
            if len(_) == 0:
                _.append(m)
            else:
                _.append(m)
                temp.append(_)
                _ = []
        if _ != []:
            _.append('X')
            temp.append(_)
            _ = []
        return temp

    def __convert_coords_to_string(self, coord: tuple, mat: list) -> str:
        return mat[coord[0]][coord[1]]


if __name__ == '__main__':
    inpkeys = [input('Please type the first key: '), input('Please type the second key: ')]
    inpmeth = input('Do you want to en-[0] or decode[1]? ')
    while not (inpmeth == '1' or inpmeth == '0'):
        print('This was neither 0 nor 1!')
        inpmeth = input('Do you want to en-[0] or decode[1]? ')
    inptext = input('Please type the text to en- or decode: ')

    converter = FourSquare(inpkeys, inpmeth, inptext)
    converter.create_matrices()

    print(converter.get_result())
