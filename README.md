# Placevalue Ascii

Creates an ascii representation of the binary ouput of two variable function at a certian place value, arrayed on a grid.

## What?
Consider the function `f(x, y) = x + y`.
Now, make a grid of the outputs of this function for incrementing integer values of `x` and `y`, like so:
```
_|_0___1___2___3__
0| 0   1   2   3
1| 1   2   3   4 
2| 2   3   4   5
3| 3   4   5   6
```

Convert each number to binary:
```
_|_0___1___2___3__
0| 000 001 010 011
1| 001 010 011 100 
2| 010 011 100 101
3| 011 100 101 110
```

Reduce the grid to only the digits at a certain place value, let's say 3:
```
_|_0___1___2___3__
0| 0   0   0   0
1| 0   0   0   1 
2| 0   0   1   1
3| 0   1   1   1
```

Now, replace the `1`s with an asterisk, `*` and the `0` with a space, ` `:
```
    
   *
  **
 ***
```

## Script example
This command produces a 16 by 16 ascii pattern for the function `f(x, y) = x + y` at place value.
``` bash
$ python placevalue_ascii.py "x + y" 3 16 16
            ****
           **** 
          ****  
         ****   
        ****    
       ****    *
      ****    **
     ****    ***
    ****    ****
   ****    **** 
  ****    ****  
 ****    ****   
****    ****    
***    ****    *
**    ****    **
*    ****    ***
```
