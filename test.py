
import unittest
import durationpy
from datetime import timedelta

millisecond = 1
second      = 1000 * millisecond
minute      = 60   * second
hour        = 60   * minute
day         = 24   * hour
week        = 7    * day
month       = 30   * day
year        = 365  * day

cases = [

  # simple
  ["0", True, 0],
  ["5s", True, 5 * second],
  ["30s", True, 30 * second],
  ["1478s", True, 1478 * second],
  
  # sign
  ["-5s", True, -5 * second],
  ["+5s", True, 5 * second],
  ["-0", True, 0],
  ["+0", True, 0],
  
  # decimal
  ["5.0s", True, 5 * second],
  ["5.6s", True, 5*second + 600*millisecond],
  ["5.s", True, 5 * second],
  [".5s", True, 500 * millisecond],
  ["1.0s", True, 1 * second],
  ["1.00s", True, 1 * second],
  ["1.004s", True, 1*second + 4*millisecond],
  ["1.0040s", True, 1*second + 4*millisecond],
  ["100.00100s", True, 100*second + 1*millisecond],
  
  # different units
  ["13ms", True, 13 * millisecond],
  ["14s", True, 14 * second],
  ["15m", True, 15 * minute],
  ["16h", True, 16 * hour],
  ["11d", True, 11 * day],
  ["10w", True, 10 * week],
  
  # composite durations
  ["3h30m", True, 3*hour + 30*minute],
  ["10.5s4m", True, 4*minute + 10*second + 500*millisecond],
  ["-2m3.4s", True, -(2*minute + 3*second + 400*millisecond)],
  ["1h2m3s4ms", True, 1*hour + 2*minute + 3*second + 4*millisecond],
  ["10w5d39h9m14.425s", True, 10*week + 5*day + 39*hour + 9*minute + 14*second + 425*millisecond],
  
  # large value
  ["52763797000ms", True, 52763797000 * millisecond],
  
  # errors
  ["", False, 0],
  ["3", False, 0],
  ["-", False, 0],
  ["s", False, 0],
  [".", False, 0],
  ["-.", False, 0],
  [".s", False, 0],
  ["+.s", False, 0],
 
  # extended
  ["5y2mm", True, 5*year + 2*month]
]

class DurationTest(unittest.TestCase):

    def test_good_input(self):
        for [input, passes, expected] in cases:
            if passes:
                actual = durationpy.from_str(input).total_seconds() * 1000
                self.assertEquals(
                    expected, actual,
                    "{}, expecting {}, got {}".format(input, expected, actual)) 

    def test_bad_input(self):
        for [input, passes, expected] in cases:
            if not passes:
                with self.assertRaises(Exception):
                    durationpy.from_str(input)

if __name__ == '__main__':
    unittest.main()

