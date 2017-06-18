''' print out binary place value patterns '''

import math
import argparse


def placevalue_patterner(function, height, width, placevalue, offset_y=0):
    ''' create a visualization of a place value pattern '''
    visual = []
    for i in range(offset_y, offset_y + height):
        row = ''
        for j in range(width):
            value = function(i, j)
            binary = '{0:b}'.format(int(value))
            if len(binary) > placevalue and binary[-1 * placevalue] == '1':
                row += '*'
            else:
                row += ' '
        visual.append(row)
    return '\n'.join(visual)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('function',
                        help='The function to plot, e.g. "x ** 2 * y ** 2"',
                        type=lambda s: eval('lambda x, y: {}'.format(s)))
    parser.add_argument('placevalue', type=int)
    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)
    args = parser.parse_args()
    print(placevalue_patterner(args.function, args.height,
                               args.width, args.placevalue))

