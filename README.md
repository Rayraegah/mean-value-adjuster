# Mean Value Adjuster

A python class to adjust the mean(average) value of a dataset by weighing each
value based on its z - score. Values closer to the mean are considered "better"
and so are given more weight.

# In ranking systems

Adjusted mean be used to give toll votes less weight.

# Example

```python
import mva

vote_values = [100, 70, 88, 91, 85, 60, 99, 2]

adjuster = mva.Adjuster(vote_values)

adjuster.get_true_mean()

adjuster.get_adjusted_mean()
```

# License

Released under MIT license
