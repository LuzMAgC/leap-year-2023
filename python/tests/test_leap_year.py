from src.leap_year import LeapYear


class TestLeapYear:

    def test_3_is_not_leap(
        self,
    ):
        # Given
        leap_year = LeapYear()
        # When

        # Then
        assert leap_year.is_leap_year(3) == False

    def test_8_is_leap(
        self,
    ):
        # Given
        lear_year = LeapYear()
        # When

        # Then
        assert lear_year.is_leap_year(8) == True
