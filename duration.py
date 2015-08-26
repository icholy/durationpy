import re

_millisecond_size = 1.0
_second_size      = 100.0 * _millisecond_size
_minute_size      = 60.0  * _second_size
_hour_size        = 60.0  * _minute_size
_day_size         = 24.0  * _hour_size
_week_size        = 7.0   * _day_size

class Duration():


    def __init__(self, value):
        self._milliseconds = value


    def nanoseconds(self):
        return int(self._milliseconds * 1000000)


    def microseconds(self):
        return int(self._milliseconds * 1000)


    def millisecond(self):
        return self._milliseconds


    def seconds(self):
        return int(self._milliseconds / _second_size)


    def minutes(self):
        return int(self._milliseconds / _minute_size)


    def hours(self):
        return int(self._milliseconds / _hour_size)


    def days(self):
        return int(self._milliseconds / _day_size)


    def weeks(self):
        return int(self._milliseconds / _week_size)


    def __str__(self):
        result_str = ""
        milliseconds = abs(self._milliseconds)
        sign = "-" if self._milliseconds < 0 else ""

        if not milliseconds:
            return "0"

        hours = int(milliseconds / _hour_size)
        if hours:
            milliseconds -= _hour_size * hours
            result_str += "{}h".format(hours)

        minutes = int(milliseconds / _minute_size)
        if minutes:
            milliseconds -= _minute_size * minutes
            result_str += "{}m".format(minutes)

        seconds = int(milliseconds / _second_size)
        if seconds:
            milliseconds -= _second_size * seconds
            result_str += "{}s".format(seconds)

        if milliseconds:
            result_str += "{}ms".format(milliseconds)

        return "{}{}".format(sign, result_str)


    def __repr__(self):
        return "Duration({})".format(self.__str__())


    def __int__(self):
        return int(self._milliseconds)


    def __float__(self):
        return float(self._milliseconds)

    
    def __long__(self):
        return long(self._milliseconds)

    
    def __add__(self, other):
        return Duration(int(self) + int(other))

    def __sub__(self, other):
        return Duration(int(self) - int(other))


    def __mul__(self, other):
        return Duration(int(self) * int(other))


    def __div__(self, other):
        return Duration(int(self) / int(other))


    def __neg__(self):
        return Duration(-int(self))


    def __pos__(self):
        return Duration(int(self))


    def __abs__(self):
        return Duration(abs(int(self)))


def parse(duration):

    units = {
        "ms" : _millisecond_size,
        "s"  : _second_size,
        "m"  : _minute_size,
        "h"  : _hour_size,
        "d"  : _day_size,
        "w"  : _week_size
    }

    if duration == "0" or duration == "+0" or duration == "-0":
        return Duration(0)

    pattern = re.compile('([\-\+\d\.]+)([a-z]+)')
    total = 0
    sign = -1 if duration[0] == '-' else 1
    matches = pattern.findall(duration)

    if not len(matches):
        raise Exception("invalid duration")

    for (value, unit) in matches:
        try:
            total += int(value) * units[unit]
        except:
            raise Exception("invalid duration")

    return Duration(sign * total)


millisecond = Duration(_millisecond_size)
second      = Duration(_second_size)
minute      = Duration(_minute_size)
hour        = Duration(_hour_size)
day         = Duration(_day_size)
week        = Duration(_week_size)
