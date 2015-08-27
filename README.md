# Duration.py

> Module for converting between `datetime.timedelta` and Go's Duration strings.


### Parse

* `ns` - nanoseconds
* `us` - microseconds
* `ms` - millisecond
* `s` - second
* `m` - minute
* `h` - hour

``` py
# parse
td = duration.from_str("4h3m2s1ms");

# format
duration.to_str(td)
```

**Note:** nanosecond precision is lost because `datetime.timedelta` uses microsecond resolution.
