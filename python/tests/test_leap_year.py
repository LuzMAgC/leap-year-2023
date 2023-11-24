from src.leap_year import LeapYear


class TestLeapYear:

    def test_3_is_not_leap(
        self,
    ):
        # Given
        my_class = LeapYear()
        # When

        # Then
        assert my_class.is_leap_year(3) == False

    def test_8_is_leap(
        self,
    ):
        # Given
        my_class = LeapYear()
        # When

        # Then
        assert my_class.is_leap_year(8) == True
