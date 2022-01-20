#!/usr/bin/env python

from random import shuffle
import unittest

import circuit2
class RangeIndexTest(unittest.TestCase):
  def _reset(self):
    self.range_index = circuit2.RangeIndex()

  @unittest.skipIf(
    circuit2.RangeIndex.__base__ is not circuit2.UnorderedListWithinBoundsAvlTreeRangeIndex,
    'no find_ge_node method'
  )
  def testFindGeNode(self):
    self._reset()
    n = self.range_index.find_ge_node(100)
    self.assertIsNone(n)

    self._reset()
    self.range_index.add(0)
    n = self.range_index.find_ge_node(0)
    self.assertEqual(n.key, 0)
    n = self.range_index.find_ge_node(1)
    self.assertIsNone(n)
    n = self.range_index.find_ge_node(-1)
    self.assertEqual(n.key, 0)

    self._reset()
    [self.range_index.add(i) for i in range(5)]
    n = self.range_index.find_ge_node(1.5)
    self.assertEqual(n.key, 2)
    n = self.range_index.find_ge_node(4)
    self.assertEqual(n.key, 4)

    self._reset()
    [self.range_index.add(i) for i in [6, 2, 7, 3, 9, 0, 5, 8, 1, 4]]
    n = self.range_index.find_ge_node(3)
    self.assertEqual(n.key, 3)

  @unittest.skipIf(
    circuit2.RangeIndex.__base__ is not circuit2.UnorderedListWithinBoundsAvlTreeRangeIndex,
    'no find_le_node method'
  )
  def testFindLeNode(self):
    self._reset()
    n = self.range_index.find_le_node(100)
    self.assertIsNone(n)

    self._reset()
    self.range_index.add(0)
    n = self.range_index.find_le_node(0)
    self.assertEqual(n.key, 0)
    n = self.range_index.find_le_node(-1)
    self.assertIsNone(n)
    n = self.range_index.find_le_node(1)
    self.assertEqual(n.key, 0)

    self._reset()
    [self.range_index.add(i) for i in range(5)]
    n = self.range_index.find_le_node(3.5)
    self.assertEqual(n.key, 3)
    n = self.range_index.find_le_node(0)
    self.assertEqual(n.key, 0)

    self._reset()
    [self.range_index.add(i) for i in [6, 2, 7, 3, 9, 0, 5, 8, 1, 4]]
    n = self.range_index.find_le_node(6)
    self.assertEqual(n.key, 6)

  def testList(self):
    self._reset()
    self.range_index.add(0)
    l = self.range_index.list(0, 2)
    self.assertEqual(len(l), 1)
    self.assertEqual(set(l), set([0]))

    self._reset()
    for i in range(5):
      self.range_index.add(i)
    l = self.range_index.list(0, 2)
    if len(l) != 3:
      print(len(l), l)
      print(self.range_index.t)
    self.assertEqual(len(l), 3)
    self.assertEqual(set(l), set([0, 1, 2]))

    self._reset()
    lst = list(range(10))
    shuffle(lst)
    for i in lst:
      self.range_index.add(i)

    low, high = 3, 6
    l = self.range_index.list(low, high)
    if len(l) != high-low+1:
      print('lst', lst)
      print(len(l), l)
      print(self.range_index.t)
    self.assertEqual(len(l), high-low+1)
    self.assertEqual(set(l), set(range(low, high+1)))

if __name__ == '__main__':
  unittest.main()
