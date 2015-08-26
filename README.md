# Duration.py

This is a library for dealing with durations. 


### Parse

* `ms` - millisecond
* `s` - second
* `m` - minute
* `h` - hour
* `d` - day
* `w` - week

``` js
var d = duration.parse("6w5d4h3m2s1ms");

console.log(
    d.milliseconds(), "\n", // => 4075382001
    d.seconds(),      "\n", // => 4075382
    d.minutes(),      "\n", // => 67923
    d.hours(),        "\n", // => 1132
    d.days(),         "\n", // => 47
    d.weeks(),        "\n"  // => 6
);
```

### Format
``` js
print("str: {} ms: {}".format(duration.hour, int(duration.hour)))
# "str: 1h ms: 3600000"
```

### Basic Operations
``` js
// Addition
d1 = duration.parse("6d")
d2 = d1 + duration.day
print(d2) # "168h"

// Multiplication
d3 = duration.parse("5m"),
d4 = d3 * 12
print(d4) # "1h"

// etc ...
```
