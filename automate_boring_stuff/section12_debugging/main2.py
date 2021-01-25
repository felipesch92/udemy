market_2nd = {'ns': 'green', 'ew': 'red'}

def switch_lights(intersection):
    for k in intersection.keys():
        if intersection[k] == 'green':
            intersection[k] = 'yellow'
        elif intersection[k] == 'yellow':
            intersection[k] = 'red'
        elif intersection[k] == 'red':
            intersection[k] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)


print(market_2nd)
switch_lights(market_2nd)
print(market_2nd)
switch_lights(market_2nd)
print(market_2nd)
