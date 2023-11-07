#!/usr/bin/env python3

#
# This is a demonstration of quicksort implemented without recursion.
#

#
# Generate some random data for testing.
#
import random
n = random.randint(100, 200)
a = []

i = 0
while i < n:
   a.append(random.randint(10, 250))
   i = i + 1

#
# `jobs` is a list of jobs.
#
# Each job is a pair of integers (i, j) indicating that a[i:j] remains to be sorted.
#
# Initially, the entire list remains to be sorted, so jobs is: [(0, len(a))].
#
jobs = [ [0, len(a)] ]

# Keep going while jobs remain.
#
while 0 < len(jobs):
   job = jobs.pop()
   start, end = job[0], job[1]

   if 1 < end - start:
      position = (start + end) // 2  # pivot position (pick the middle, because... why not?)
      pivot = a[position]            # pivot value

      # Take the pivot out of the range.
      #
      a[position] = a[start]

      i = start + 1
      j = end
      while i < j:
         if a[i] <= pivot:
            i = i + 1
         elif pivot < a[j - 1]:
            j = j - 1
         else:
            # On this branch, we don't actually make progress with either i or j.
            # However, we swap the elements which guarantees that we will make progress on the next iteration.
            #
            assert i != j - 1  # because otherwise we should have used one of the two branches above
            a[i], a[j - 1] = a[j - 1], a[i]

         assert i == start + 1 or a[i - 1] <= pivot
         assert j == end       or pivot    <  a[j]

      # Replace the pivot.
      #
      a[start], a[i - 1] = a[i - 1], pivot

      assert i - 1 < end  # hence, progress is guaranteed
      jobs.append([start, i - 1])

      assert start < i    # hence, progress is guaranteed
      jobs.append([i, end])

i = 0
while i < len(a):
   print(a[i])
   assert i == 0 or a[i - 1] <= a[i]  # verify that the list is indeed sorted
   i = i + 1
