# validsudoku.ipynb
# Author Kyle Larson
# Purpose to tell whether the sudoku solution is valid
def valid_solution(board):
    rows_check_flag =[0,0,0,0,0,0,0,0,0]
    cols_check_flag =[0,0,0,0,0,0,0,0,0]
    sub_square_check =[0,0,0,0,0,0,0,0,0]
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	 checks =0
	 for i in range(len(board)):
	     for j in range(len(board)):
	         for k in range(len(check)):
		          if(check[k]==board[i][j]):
			           rows_check_flag[k] +=1
				    for l in range(len(rows_check_flag)):
					     if(rows_check_flag[l]==1):
								rows_check_flag[l]=0
						      checks+=1
	 for i in range(len(board)):
		     for j in range(len(board)):
		         for k in range(len(check)):
			          if(check[k]==board[j][i]):
				           cols_check_flag[k] +=1
					    for l in range(len(rows_check_flag)):
						     if(cols_check_flag[l]==1):
									cols_check_flag[l]=0
							      checks+=1
		

    if(checks==9*9*9*9):
        return True
    else:
        return False