class LeapYear:
    def is_leap_year(
        self,year:int
    ) -> bool:
        if year % 4 != 0:
            return False
        return True
