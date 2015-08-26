# Duration.py

> Module for converting between `datetime.timedelta` and Go's Duration strings.


### Parse

* `ns` - nanoseconds
* `us` - microseconds
* `ms` - millisecond
* `s` - second
* `m` - minute
* `h` - hour
* `d` - day
* `w` - week

``` js
# parse
td = duration.from_str("6w5d4h3m2s1ms");

# format
duration.to_str(td)
```
