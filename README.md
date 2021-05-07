# SudokuAI
This is a Python project that solves Sudoku puzzles using topics in Artificial Intelligence. 

## Entering a Sudoku Puzzle 
When entering a Sudoku puzzle, be sure to enter **each subgrid as a row in the input file** and enter empty cells with `0`.
For example, if this is the grid:

0 0 0   4 0 0   0 5 0   
4 0 0   9 0 0   0 0 0   
3 0 2   8 0 0   0 0 0   

0 0 0   0 0 0   0 6 9   
0 0 0   0 0 7   0 0 3   
0 0 1   0 8 0   0 0 0   

0 9 0   0 5 0   4 0 1   
0 6 0   0 3 0   5 0 0   
0 2 0   0 0 0   9 0 0   
```

Then the input file would look like:
```
0,0,0,4,0,0,3,0,2
4,0,0,9,0,0,8,0,0
0,5,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,1
0,0,0,0,0,7,0,8,0
0,6,9,0,0,3,0,0,0
0,9,0,0,6,0,0,2,0
0,5,0,0,3,0,0,0,0
4,0,1,5,0,0,9,0,0
```

The input file is `input_sudoku_puzzle.txt` in the root of the file.

See more examples of this in [formatted_soduku_puzzle.txt](formatted_soduku_puzzle.txt) in the root of this file.

## Running the Project 
You run this project using a Python 2.x interpreter. 
Make sure the grid you want is entered in `input_sudoku_puzzle.txt` in the same format as mentioned above and run the code.

To run the code you use this command: 
$ python2 SudokuAILoops.py
```

The program will first prompt you to hit `ENTER` to get started. It will then prompt you to enter either `1` to use AI or `2` to use Brute force. 

The program outputs every step along the way, if you want to see what the programs actually doing. For example:
```
|3|          |2|          |4|          		|5|          |6|          |7|          		|9|          |8|          |1|          		
|1|          |5|          |6|          		|2|          |8|          |9|          		|4|          |3|          |7|          		
|7|          |9|          |8|          		|1|          |4|          |3|          		|2|          |6|          |5|          		



|2|          |6|          |9|          		|8|          |7|          |4|          		|1|          |5|          |3|          		
|5|          |8|          |3|          		|6|          |2|          |1|          		|7|          |4|          |9|          		
|4|          |7|          |1|          		|3|          |9|          |5|          		|6|          |2|          |8|          		



|8|          |4|          |5|          		|0|79        |1|          |2|          		|3|          |0|79        |6|          		
|0|6         |1|          |7|          		|4|          |3|          |8|          		|0|5         |0|9         |0|2         		
|9|          |3|          |2|          		|0|7         |5|          |6|          		|8|          |0|17        |0|4         		
```
The numbers between the pipe symbols show you a number that's been solved.  Numbers that are outside the two pipes are possible values for that cell (only occurs if the number has not been solved). 

For example, `|0|123` would mean 1, 2 or 3 could go in that position.  
`|3|` would mean that this cell's value must be 3.

## Performance Measurements:
At the end, the program prints a summary to allow you to see how efficient the algorithm was, like this:
```
Board Solved! Performance Measure: 49
Time: 55.8531284332 milliseconds
```

The printed performance heuristic reflects how many steps the program took to solve the puzzle (higher score means more efficient).  For brute force, you'll see a negative score in the thousands, whereas for AI, you'll likely see a score between 40 and 60.

The second performance measurement used is the time taken to solve the program (you'll see a number in the thousands of milliseconds for brute force, but around 50ms for AI). 
