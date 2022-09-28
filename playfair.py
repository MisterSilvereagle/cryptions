class Playfair:
    def __init__(self, key: str, method: str, text: str):
        self.alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        self.key = list(k for k in key.upper().replace('Ä', 'AE').replace('Ö', 'OE').replace('Ü', 'UE')\
                        if k in self.alphabet)
        self.the_text = list(p for p in text.upper().replace('Ä', 'AE').replace('Ö', 'OE').replace('Ü', 'UE')\
                             if p in self.alphabet)
        self.method = 1 if int(method) == 1 else -1

    def create_matrix(self):
        temp = []
        for k in range(len(self.key)):
            if not self.key[k] in self.key[:k]:
                temp.append(self.key[k])
        temp.extend([x for x in self.alphabet if x not in temp])
        matrix = []
        for m in range(5):
            matrix.append(temp[m*5:5*m+5])
        self.matrix = matrix

    def __find_in_nested_list(self, a: str, mat: list) -> list:
        for m in range(len(mat)):
            for n in range(len(mat[m])):
                if mat[m][n] == a:
                    return [m, n]

    def __move_right(self, a: list, b: list) -> tuple:
        a[1] = (a[1] + self.method)%5
        b[1] = (b[1] + self.method)%5
        return (a, b)

    def __move_down(self, a: list, b: list) -> tuple:
        a[0] = (a[0] + self.method)%5
        b[0] = (b[0] + self.method)%5
        return (a, b)

    def __move_cross(self, a: list, b: list) -> tuple:
        a[1], b[1] = b[1], a[1]
        return (a, b)

    def __convert_coords_to_string(self, coord: tuple, mat: list) -> str:
        return mat[coord[0]][coord[1]]

    def __chooser(self, inp: list) -> list:
        loc_a = self.__find_in_nested_list(inp[0], self.matrix)
        loc_b = self.__find_in_nested_list(inp[1], self.matrix)
        if loc_a == loc_b:
            return ['ERROR']
        elif loc_a[0] == loc_b[0]:
            temp = self.__move_right(loc_a, loc_b)
        elif loc_a[1] == loc_b[1]:
            temp = self.__move_down(loc_a, loc_b)
        else:
            temp = self.__move_cross(loc_a, loc_b)
        return [self.__convert_coords_to_string(x, self.matrix) for x in temp]

    def __split_into_bigrams(self, inp: list) -> list:
        temp = []
        _ = []
        for m in inp:
            if len(_) == 0:
                _.append(m)
            elif len(_) == 1:
                if _[0] != m:
                    _.append(m)
                    temp.append(_)
                    _ = []
                elif _[0] != 'X':
                    _.append('X')
                    temp.append(_)
                    _ = [m]
                else:
                    _.append('Q')
                    temp.append(_)
                    _ = [m]
        if _ != []:
            if _[0] != 'X':
                _.append('X')
            else:
                _.append('Q')
            temp.append(_)
            _ = []

        return temp

    def get_result(self):
        bigrams = self.__split_into_bigrams(self.the_text)
        result = []
        for c in bigrams:
            result.extend(self.__chooser(c))
        return ''.join(x for x in result)


if __name__ == '__main__':
    inpkey = input('Please type the key: ')
    while not (inpmeth := input('Do you want to en-[0] or decode[1]? ') in ['0', '1']):
        print('This was neither 0 nor 1!')
    inptext = input('Please type the text to en- or decode: ')

    converter = Playfair(inpkey, inpmeth, inptext)
    converter.create_matrix()

    print(converter.get_result())   # 89
