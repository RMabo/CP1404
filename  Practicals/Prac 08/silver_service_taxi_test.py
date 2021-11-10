from prac_08.silver_service_taxi_test import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    hummer.drive(18)
    print(hummer)
    print(hummer.get_fare())


main()

