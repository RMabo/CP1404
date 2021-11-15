from prac_08.taxi import Taxi

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi that include fare cost"""
    flagfall = 4.5
    price_per_km = 1.23

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi that is based on parent class."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string of a SilverServiceTaxi that include fare distance"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.current_fare_distance, SilverServiceTaxi *
                                                    self.franciness,
                                                    self.flagfall)

    def get_fare(self):
        """Get the current fare."""
        return self.flagfall + super().get_fare()




