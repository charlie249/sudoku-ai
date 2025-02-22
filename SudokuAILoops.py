from copy import deepcopy
import time 

#Agent that solves Sudoku puzzles
present_mode = True; 

class Sudoku:
    def __init__(self):
        self.boards_so_far = []
        self.sudoku_table = [0]*9
        self.read_table()
        self.heuristic = 0 #Number of zeros 

        for i in range(0,len(self.sudoku_table)):
            for j in range(0,len(self.sudoku_table)):
                if self.sudoku_table[i][j] == "0":

                    #Heuristic starts off as number of zeros
                    self.heuristic += 1

                    self.sudoku_table[i][j]+= self.get_possibilities(i,j,self.sudoku_table)

        #for x in range(0,len(self.sudoku_table)):
        #   for y in range(0,len(self.sudoku_table)):
                
    def read_table(self):
        """ Reads sudoku puzzle from file, each row represents one section, 9 sections total
       	
        Ex. 
        For the puzzle:
        8 0 0   4 0 6   0 0 7   
        0 0 0   0 0 0   4 0 0   
        0 1 0   0 0 0   6 5 0   
        
        5 0 9   0 3 0   7 8 0   
        0 0 0   0 7 0   0 0 0   
        0 4 8   0 2 0   1 0 3   
        
        0 5 2   0 0 0   0 9 0   
        0 0 1   0 0 0   0 0 0   
        3 0 0   9 0 2   0 0 5  
        
        8,0,0,0,0,0,0,1,0 would be line 1 of input,
        4,0,6,0,0,0,0,0,0 would be line 2 of input,
        etc.
        
        Stored in nested array with each index representing a section which contains another array.
        For the puzzle above, resulting data structure is:
        [['8', '0', '0', '0', '0', '0', '0', '1', '0'], ['4', '0', '6', '0', '0', '0', '0', '0', '0'], ['0', '0', '7', '4', '0', '0', '6', '5', '0'], 
        ['5', '0', '9', '0', '0', '0', '0', '4', '8'], ['0', '3', '0', '0', '7', '0', '0', '2', '0'], ['7', '8', '0', '0', '0', '0', '1', '0', '3'], 
        ['0', '5', '2', '0', '0', '1', '3', '0', '0'], ['0', '0', '0', '0', '0', '0', '9', '0', '2'], ['0', '9', '0', '0', '0', '0', '0', '0', '5']]
        
        """
        sudoku_file = open("input_sudoku_puzzle.txt", "r")
        self.sudoku_table = [0]*9
        for i in range(len(self.sudoku_table)):
       	    self.sudoku_table[i]  = sudoku_file.readline().rstrip('\n').split(',')
        
    #Prints Sudoku in a nice, standard format
    def print_table_with_possibilities(self, board):
            for sections_of_three in range(3):
           	    for row in range(3):
          		for i in range(0+sections_of_three*3,3*(sections_of_three+1)):
         			if i % 3 == 0 :
            				print ""

    				for z in range(0+(row*3),3*(row+1)):
   					#Print "\nrow is %s " % row
   					#Print "\ntimes run %s"  % z
   					#Print "\n i is %s" % i
   					if self.sudoku_table[i][z][1:] != "":
   					    print "|%s|%-9s" % (board[i][z][0], board[i][z][1:]),
   					else:
                                            print "|%s|%-9s" % (board[i][z][0], ""),
    				print "\t\t", 
           	    print "\n\n"
            
    def print_table(self,board):
            for sections_of_three in range(3):
           	    for row in range(3):
          		for i in range(0+sections_of_three*3,3*(sections_of_three+1)):
         			if i % 3 ==0 :
            				print ""
            				for z in range(0+(row*3),3*(row+1)):
           					#Print "\nrow is %s " % row
           					#Print "\ntimes run %s"  % z
           					#Print "\n i is %s" % i
           					
           					print "%s" % board[i][z][0],
           					
            				print " ",
         			else:
            				for z in range(0+(row*3),3*(row+1)):
           					#Print "\nrow is %s " % row
           					#Print "\ntimes run %s"  % z
           					#Print "\n i is %s" % i
           					
           					print "%s" % board[i][z][0],
           					
            				print " ",
           	    print ""

    def get_possibilities(self,i,j,board):
        possibilites = ""
        for potential_poss in range(1,10):
            #Get first character of each location of section
            first_character_list = list()
            for x in range(0,9):
                first_character_list.append(board[i][x][0])
            #Check section
            if str(potential_poss) not in first_character_list:
                #Check row
                row = list()
                row_i_start = 3 * (i/3)
                row_j_start = 3 * (j/3)

                for row_i_iterator in range(row_i_start, row_i_start + 3): 
                    for row_j_iterator in range(row_j_start, row_j_start + 3): 
                        row.append(board[row_i_iterator][row_j_iterator][0])
    
                if str(potential_poss) not in row:
                    #Check columns
                    column = list()
                    col_i_start = i%3;
                    col_j_start = j%3;

                    for col_i_iter in xrange(col_i_start, col_i_start + 7, 3):
                        for col_j_iter in xrange(col_j_start, col_j_start + 7, 3):
                            column.append(board[col_i_iter][col_j_iter][0])
            
                    if str(potential_poss) not in column:
                        possibilites+=str(potential_poss)  
        
        return possibilites
    
    def skip_invalid_single_possibilities(self, board,i,j):
        value = board[i][j]
                                      
        #Iterate through row
        row_i_start = 3 * (i/3)
        row_j_start = 3 * (j/3)
                
        for row_i_iterator in range(row_i_start, row_i_start + 3): 
            for row_j_iterator in range(row_j_start, row_j_start + 3): 
                if board[row_i_iterator][row_j_iterator] in value and not (row_i_iterator == i and row_j_iterator == j) and len(board[row_i_iterator][row_j_iterator])==2:
                    print "skipped"
                    print "position"+str(i) + str(j)
                    return True
        print '\n'
        #Iterate through columns
        col_i_start = i%3;
        col_j_start = j%3;
                
        for col_i_iter in xrange(col_i_start, col_i_start + 7, 3):
            for col_j_iter in xrange(col_j_start, col_j_start + 7, 3):
                if board[col_i_iter][col_j_iter] in value and not (col_i_iter == i and col_j_iter == j) and len(board[col_i_iter][col_j_iter])==2:
                    print "skipped"
                    print "position"+str(i) + str(j)
                    return True
        print '\n'
        for x in range(0,9): 
            if board[i][x] in value and x != j and len(board[i][x])==2:
                print "skipped"
                print "position"+str(i) + str(j)
                return True
        return False
    
    #Returns a list of triples which contain c[0] sector, c[1] position, and c[2] string of possibilities
    def get_cells_with_allowed_num_poss(self, count, board, previous_possibilities):
        list = []
        for i in range(9):
            for j in range(9):
                if len(board[i][j]) == count:
                    if self.skip_invalid_single_possibilities(board,i,j):
                        continue

                    print list
                    for value in previous_possibilities:
                        if value == [i,j,board[i][j]]:
                            continue
                    list.append([i,j,board[i][j]])
        return list

    #Returns a boolean depending upon if each cell has a single possibility
    def board_filled(self,board):
        for i in range(9):
            for j in range(9):
                if len(board[i][j]) > 1:
                    return False
        return True

    def no_more_possibilites(self,board):
        #Iterate through board 
        #Find any cell with value 0 AND length 1 
        for x in range(0,9):
            for y in xrange(0,9):
               
                if(len(board[x][y]) == 1 and board[x][y][0] == '0'): 
                    
                    #This is a bad cell, no more possibilities for this cell 
                    return True 

        #Good board, we can continue 
        return False

    def place_poss_in_board(self,value,section, position, board):
        new_board = deepcopy(board)
        new_board[section][position]=str(value)
        return new_board

    def violation_occured(self,section, position, board):
        value = board[section][position][0]
        row_i_start = 3 * (section/3)
        row_j_start = 3 * (position/3)

        for row_i_iterator in range(row_i_start, row_i_start + 3): 
            for row_j_iterator in range(row_j_start, row_j_start + 3): 
                if value in board[row_i_iterator][row_j_iterator][0] and not (row_i_iterator == section and row_j_iterator == position):
                    print board[row_i_iterator][row_j_iterator]
                    return True

        print '\n'
        #Iterate through columns
        col_i_start = section%3;
        col_j_start = position%3;

        for col_i_iter in xrange(col_i_start, col_i_start + 7, 3):
            for col_j_iter in xrange(col_j_start, col_j_start + 7, 3):
                if value in board[col_i_iter][col_j_iter][0] and not (col_i_iter == section and col_j_iter == position):
                    print board[col_i_iter][col_j_iter]
                    return True
        print '\n'
        for x in range(0,9):
            if value in board[section][x][0] and x != position:
                print board[section][x]
                return True
        
        return False
        
    def unmark_board(self, section, position, board):
        value = board[section][position]
      
        print "position"+str(section) + str(position)
        #Iterate through row
        row_i_start = 3 * (section/3)
        row_j_start = 3 * (position/3)

        for row_i_iterator in range(row_i_start, row_i_start + 3): 
            for row_j_iterator in range(row_j_start, row_j_start + 3): 
                if value not in board[row_i_iterator][row_j_iterator] and not (row_i_iterator == section and row_j_iterator == position):
                    board[row_i_iterator][row_j_iterator]=board[row_i_iterator][row_j_iterator]+value
                    board[row_i_iterator][row_j_iterator] = board[row_i_iterator][row_j_iterator][0]+''.join(sorted(board[row_i_iterator][row_j_iterator][1:]))
                    print board[row_i_iterator][row_j_iterator]    
                    
        print '\n'
        #Iterate through columns
        col_i_start = section%3;
        col_j_start = position%3;

        for col_i_iter in xrange(col_i_start, col_i_start + 7, 3):
            for col_j_iter in xrange(col_j_start, col_j_start + 7, 3):
                if value not in board[col_i_iter][col_j_iter] and not (col_i_iter == section and col_j_iter == position):
                    board[col_i_iter][col_j_iter]=board[col_i_iter][col_j_iter]+ value
                    board[col_i_iter][col_j_iter] = board[col_i_iter][col_j_iter][0] + ''.join(sorted(board[col_i_iter][col_j_iter][1:]))
                    print board[col_i_iter][col_j_iter]
        print '\n'
        for x in range(0,9):
            if value not in board[section][x] and x != position:
                board[section][x]=board[section][x]+value
                board[section][x]=board[section][x][0] + ''.join(sorted(board[section][x][1:]))
                print board[section][x]
        board[section][position] = board[section][position].replace(value, '0')
        board[section][position] = board[section][position]+value
        board[section][position] = ''.join(sorted(board[section][position]))
 
        return

    def remark_board(self, section, position, board):
        value = board[section][position]
      
        print "position"+str(section) + str(position)
        #Iterate through row
        row_i_start = 3 * (section/3)
        row_j_start = 3 * (position/3)

        for row_i_iterator in range(row_i_start, row_i_start + 3): 
            for row_j_iterator in range(row_j_start, row_j_start + 3): 
                if value in board[row_i_iterator][row_j_iterator] and not (row_i_iterator == section and row_j_iterator == position):
                    board[row_i_iterator][row_j_iterator]=board[row_i_iterator][row_j_iterator].replace(value, "")
                    print board[row_i_iterator][row_j_iterator]
        print '\n'
        #Iterate through columns
        col_i_start = section%3;
        col_j_start = position%3;

        for col_i_iter in xrange(col_i_start, col_i_start + 7, 3):
            for col_j_iter in xrange(col_j_start, col_j_start + 7, 3):
                if value in board[col_i_iter][col_j_iter] and not (col_i_iter == section and col_j_iter == position):
                    board[col_i_iter][col_j_iter]=board[col_i_iter][col_j_iter].replace(value, "")
                    print board[col_i_iter][col_j_iter]
        print '\n'
        for x in range(0,9):
            if value in board[section][x] and x != position:
                board[section][x]=board[section][x].replace(value, "")
                print board[section][x]
        return

    def hidden_double(self, board):
        cells_so_far = []
        potential_double = []
        for i in range(9):
            for j in range(9):
                #Iterate through row
                row_i_start = 3 * (i/3)
                row_j_start = 3 * (j/3)
                        
                for row_i_iterator in range(row_i_start, row_i_start + 3):
                    for row_j_iterator in range(row_j_start, row_j_start + 3):
                        if [row_i_iterator,row_j_iterator,board[row_i_iterator][row_j_iterator]] in cells_so_far and len(board[row_i_iterator][row_j_iterator]) == 3:
                          
                            potential_double.append[row_i_iterator,row_j_iterator,[board[row_i_iterator][row_j_iterator]]]
                        
                        elif len(board[row_i_iterator][row_j_iterator]) == 3:
                          
                           cells_so_far.append[row_i_iterator,row_j_iterator,[board[row_i_iterator][row_j_iterator]]]
                col_i_start = i%3;
                col_j_start = j%3;
                for col_i_iter in range(col_i_start, col_j_start + 3):
                    for col_j_iter in range(col_i_start, col_j_start + 3):
                        if [col_i_iter,col_j_iter,board[col_i_iter][col_j_iter]] in cells_so_far and len(board[col_i_iter][col_j_iter]) == 3 :
                          
                            potential_double.append[col_i_iter,col_j_iter,[board[col_i_iter][col_j_iter]]]
                        
                        elif len(board[col_i_iter][col_j_iter]) == 3:
                          
                           cells_so_far.append[col_i_iter,col_j_iter,[board[col_i_iter][col_j_iter]]]
                            
        cell_holder = []
        for index in range(0, len(potential_double)):
            for index2 in range(0, len(cell_holder)):
                #SAME ROW
                if potential_double[index][0] == cell_holder[index2][0] and potential_double[index][2] == cell_holder[index2][2]:
                    cell_holder
                
        for value in potential_double:
            for character in range(1,len(value[2])):
                row_i_start = 3 * (value[0]/3)
                row_j_start = 3 * (value[1]/3)
                        
                for row_i_iterator in range(row_i_start, row_i_start + 3):
                    for row_j_iterator in range(row_j_start, row_j_start + 3):
                        if [row_i_iterator,row_j_iterator,board[row_i_iterator][row_j_iterator]] in cells_so_far and len(board[row_i_iterator][row_j_iterator]) == 3 :
                          
                            potential_double.append[row_i_iterator,row_j_iterator,[board[row_i_iterator][row_j_iterator]]]
                        
                        elif len(board[row_i_iterator][row_j_iterator]) == 3:
                          
                           cells_so_far.append[row_i_iterator,row_j_iterator,[board[row_i_iterator][row_j_iterator]]]
                col_i_start = i%3;
                col_j_start = j%3;
                for col_i_iter in range(col_i_start, col_j_start + 3):
                    for col_j_iter in range(col_i_start, col_j_start + 3):
                        if [col_i_iter,col_j_iter,board[col_i_iter][col_j_iter]] in cells_so_far and len(board[col_i_iter][col_j_iter]) == 3 :
                          
                            potential_double.append[col_i_iter,col_j_iter,[board[col_i_iter][col_j_iter]]]
                        
                        elif len(board[col_i_iter][col_j_iter]) == 3:
                          
                           cells_so_far.append[col_i_iter,col_j_iter,[board[col_i_iter][col_j_iter]]]
        
    #Violation_occured may not be needed, new no possibilites method used
    def solveAlt(self,board):
        
        if self.no_more_possibilites(board):
            print "FAIL"
            #Need to backtrack, update heuristic 
            self.print_table(board)
            self.print_table_with_possibilities(board)

            self.heuristic -= 1;

            return False
        elif self.board_filled(board):
            #May need deepcopy
            self.board = deepcopy(board)

            print "Board Solved! Performance Measure: " + str(self.heuristic)

            self.board = board
            return True
        previously_allowed_possibilities = []
        for i in range(2,10):
            print "index is at " + str(i)
            allowed_possibilities = self.get_cells_with_allowed_num_poss(i, board, previously_allowed_possibilities)
            previously_allowed_possibilities + allowed_possibilities
            for cell in allowed_possibilities:
                for charPos in range(1,len(cell[2])):
                    #Cell[2] should contain possibilites, starting for loop at 1 to skip 0 value
                    newBoard = self.place_poss_in_board(cell[2][charPos],cell[0], cell[1], board)

                    #Added an item, update the heuristic
                    self.heuristic += 1;
                    
                    self.remark_board(cell[0],cell[1],newBoard)
                    self.print_table(newBoard)
                    self.print_table_with_possibilities(newBoard)
                    
                    repeated_count = 0
                    for i in self.boards_so_far:
                        if i == newBoard:
                            continue
                            repeated_count = repeated_count+1
                            
                    copy = deepcopy(newBoard)  
                    self.boards_so_far.append(copy)    
                    print "Repeated boards = " + str(repeated_count)     
                    
                    if self.solveAlt(newBoard):
                        return True

        return False     

"""
Test
"""
s = Sudoku() #Instantiate Sudoku, read the file input_sudoku_puzzle

print "Welcome to The Sudoku Solver"
print ""

if present_mode: 
    raw_input("Press <ENTER> to see the puzzle")

#Show the table before starting 
s.print_table(s.sudoku_table)
s.print_table_with_possibilities(s.sudoku_table)


if present_mode: 
    raw_input("Press <ENTER> when you want to start solving the puzzle")
    start = time.time()    
    s.solveAlt(s.sudoku_table)

#Calculate the elapsed time 
end = time.time()

#Show the elapsed time
print "Time: "  + str((end - start) * 1000) + " milliseconds"