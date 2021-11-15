from prac_06.guitar_class import Guitar


def main_test():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar('Another', 2013, 2000)
    print('Gibson L-5 CES get_age() - Expected 98. Got {}'.format(gibson.get_age()))
    print('Another get_age() - Expected 7. Got {}'.format(guitar2.get_age()))
    print('Gibson L-5 CES is_vintage() - Expected True. Got {}'.format(gibson.is_vintage(gibson.get_age())))
    print('Another is_vintage() - Expected False. Got {}'.format(guitar2.is_vintage(guitar2.get_age())))


main_test()
