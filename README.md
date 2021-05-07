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

Then the input file would look like:

0,0,0,4,0,0,3,0,2
4,0,0,9,0,0,8,0,0
0,5,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,1
0,0,0,0,0,7,0,8,0
0,6,9,0,0,3,0,0,0
0,9,0,0,6,0,0,2,0
0,5,0,0,3,0,0,0,0
4,0,1,5,0,0,9,0,0

The input file is `input_sudoku_puzzle.txt` in the root of the file.

See more examples of this in [formatted_soduku_puzzle.txt](formatted_soduku_puzzle.txt) in the root of this file.

## Running the Project 
You run this project using a Python 2.x interpreter. 
Make sure the grid you want is entered in `input_sudoku_puzzle.txt` in the same format as mentioned above and run the code.

To run the code you type this command into your command line interface: 
"python2 SudokuAILoops.py"

I would recomend running this in the code editor Visual Studio Code (VSCode) as this comes with an integrated terminal that you can use to run the software. But equally feel free to use any code editor you feel comfortable with.

At first the program will prompt you to hit `ENTER` to get it started. The it will ask you to enter either `1` to use AI or `2` to use Brute force. 

The program outputs every step it takes along the way, if you want to see what the programs actually doing. For example:

|3|          |2|          |4|          		|5|          |6|          |7|          		|9|          |8|          |1|          		
|1|          |5|          |6|          		|2|          |8|          |9|          		|4|          |3|          |7|          		
|7|          |9|          |8|          		|1|          |4|          |3|          		|2|          |6|          |5|          		



|2|          |6|          |9|          		|8|          |7|          |4|          		|1|          |5|          |3|          		
|5|          |8|          |3|          		|6|          |2|          |1|          		|7|          |4|          |9|          		
|4|          |7|          |1|          		|3|          |9|          |5|          		|6|          |2|          |8|          		



|8|          |4|          |5|          		|0|79        |1|          |2|          		|3|          |0|79        |6|          		
|0|6         |1|          |7|          		|4|          |3|          |8|          		|0|5         |0|9         |0|2         		
|9|          |3|          |2|          		|0|7         |5|          |6|          		|8|          |0|17        |0|4         		

The numbers between the pipe symbols show you a number that's been solved.  Numbers that are outside the two pipes are possible values for that cell (only occurs if the number has not been solved). 

For example, `|0|123` would mean 1, 2 or 3 could go in that position.  
`|3|` would mean that this cell's value can only be 3.

## Performance Measurements:
At the end, the program will print a summary of the program to allow you to see how efficient and effective the algorithm was.
For example:

Board Solved! Performance Measure: 49
Time: 55.8531284332 milliseconds

The printed `Performance Measure:` tells you how many steps the program took to solve the puzzle (the higher the score, the more efficient the program was). For the brute force option, it is likely you will see a negative score in the thousands, whereas for the AI option, you will probably see a score thats between 40 and 60.

The second thing displayed `Time:` tells you how long the program has actually taken to solve the program (you should see a number in the thousands of milliseconds for the brute force option, and around 50ms for the AI option). 
