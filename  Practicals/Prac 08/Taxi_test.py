from prac_08.taxi import Taxi


def taxi_fare():
    prius = Taxi("Prius 1", 100)
    prius.drive(40)
    print(prius)
    prius.start_fare()
    prius.drive(100)
    print(prius)


taxi_fare()
