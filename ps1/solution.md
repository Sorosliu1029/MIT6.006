### algorithm1

runtime complexity: `O(log(numCol) * numRow)`, i.e. `O(n * log(n))`

this algorithm is correct

### algorithm2

runtime complexity: `O(numCol * numRow)`, i.e. `O(n^2)`

this algorithm is correct

### algorithm3

~~runtime complexity: `O(min(log(numCol), log(numRow)) * (numCol + numRow))`, i.e. `O(n * log(n))`~~

runtime complexity should be: `O(n)`

~~this algorithm is correct~~

this algorithm is incorrect

counterexample:

```python
problemMatrix = [
  [ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
  [ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
  [ 4,  5,  6,  7,  8,  9,  6,  5,  4,  3,  2],
  [ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
  [ 4,  5,  6,  10,  8,  7,  6,  5,  4,  3,  2],
  [ 4,  5,  6,  9,  8,  7,  6,  5,  4,  3,  2],
  [ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
  [ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
  [ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
  [ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
  [ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
]
```

### algorithm4

runtime complexity: `O(numCol)` or `O(numRow)`, depends, i.e. `O(n)`

this algorithm is correct

