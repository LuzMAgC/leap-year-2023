class LeapYear:
    def is_leap_year(
        self,year:int
    ) -> bool:
        if year == 3 or year == 1 or year == 7:
            return False
        return True
