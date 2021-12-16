from polybios import Polybios

inpkey = input('Please type the key: ')
inpmeth = input('Do you want to en-[0] or decode[1]? ')
while not (inpmeth == '1' or inpmeth == '0'):
    print('This was neither 0 nor 1!')
    inpmeth = input('Do you want to en-[0] or decode[1]? ')
inptext = input('Please type the text to en- or decode: ')
inpmeth = int(inpmeth)

if inpmeth:
    converter = Polybios(inpkey, '0', inptext)
    converter.create_matrix()
    step1 = converter.crypt()

    step1 = [x for x in step1.split(' ')]
    left = []
    right = []
    for i in range(len(step1)):
        left.append(step1[i][0])
        right.append(step1[i][1])
    left.extend(right)

    step2 = ''.join(x for x in left)
    step2 = ' '.join([step2[i:i+2] for i in range(0, len(step2), 2)])
    converter2 = Polybios(inpkey, '1', step2)
    converter2.create_matrix()

    print(converter2.crypt())
else:
    converter = Polybios(inpkey, '0', inptext)
    converter.create_matrix()
    step1 = converter.crypt()

    step1 = ''.join([x for x in step1.split(' ')])
    left = step1[:len(step1)//2]
    right = step1[len(step1)//2:]
    merged = []
    for i in range(len(left)):
        merged.append(left[i])
        merged.append(right[i])

    step2 = ''.join(x for x in merged)
    step2 = ' '.join([step2[i:i + 2] for i in range(0, len(step2), 2)])
    converter2 = Polybios(inpkey, '1', step2)
    converter2.create_matrix()

    print(converter2.crypt())