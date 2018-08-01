"""
Mean Value Adjuster
===================

A python class to adjust the mean (average) value of a dataset by weighing each
value based on its z-score. Values closer to the mean are considered "better"
and so are given more weight.

Usage
-----
Very useful for giving less weight to "troll votes" in rating systems.

Example
-------
>>> values = [100,70,88,91,85,60,99,2]
>>> adjuster = Adjuster(values)
>>> adjuster.get_true_mean()
74.375
>>> adjuster.get_adjusted_mean()
83.54110999572508
"""

from math import cos
from statistics import mean, stdev


class Adjuster:
    def __init__(self, ls=[0]):
        self.ls = ls

    def _apply_weight(self):
        mn = mean(self.ls)
        sd = stdev(self.ls)
        weights = []

        for x in self.ls:
            z_score = (x - mn) / sd if sd is not 0 else 0
            weight = cos(z_score)

            if weight < 0:
                weight = 0

            weights.append({'value': x, 'weight': weight})

        return weights

    def get_true_mean(self):
        return mean(self.ls)

    def get_adjusted_mean(self):
        weights = self._apply_weight()
        sum_value = 0
        sum_weight = 0

        for item in weights:
            sum_value += item['value'] * item['weight']
            sum_weight += item['weight']

        return sum_value / sum_weight


def main():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    main()
