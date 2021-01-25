def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if width < 2 or height < 2:
        raise Exception('width and height needs to be great or equal to 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


box_print('-', 15, 10)
