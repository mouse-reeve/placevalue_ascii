''' print out binary place value patterns '''

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

# example
if __name__ == '__main__':
    func = lambda x, y: x ** 2 * y ** 2
    print placevalue_patterner(func, 128, 128, 7)
