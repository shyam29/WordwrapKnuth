WordwrapKnuth
=============

Python implementation of word-wrap alogrithm using dynamic programming (Knuth algorithm)

Usage:
python wrap.py <filename> <maxwidth>

Example:
Rathi:WordwrapKnuth Rathi$ python wrap.py example.txt 40
Original print:: 

Call me Ishmael,
Some years ago,
never mind how long precisely,
having little or no money in my purse,
and nothing particular to interest me on shore,
I thought I would sail about a little
and see the watery part of the world.


Pretty print:: 

Call me Ishmael, Some years ago, never
mind how long precisely, having little
or no money in my purse, and nothing
particular to interest me on shore,
I thought I would sail about a little
and see the watery part of the world.


Justified print:: 

Call  me  Ishmael, Some years ago, never
mind  how  long precisely, having little
or  no  money  in  my purse, and nothing
particular  to  interest  me  on  shore,
I  thought  I  would sail about a little
and  see  the  watery part of the world.


