def solve_operation(num1, num2, operator):
  if(operator == '+'):
    return num1 + num2
  else:
    return num1 - num2


def arithmetic_arranger(*args):

  problems = args[0]
  should_solve = False

  if(len(args) > 1):
    should_solve = args[1]
  
  arranged_problems = []
  counter = 1
  
  num1 = ''
  num2 = ''
  lines = ''
  solutions = ''
  for x in problems:

    counter += 1
    
    line = x.split(" ")

    # Check for errors
    wrongFormat = False

    if(len(problems) > 5):
      return 'Error: Too many problems.'
    elif(len(line[0]) > 4 or len(line[2]) > 4): 
      return 'Error: Numbers cannot be more than four digits.'
    elif(line[1] != "+" and line[1] != "-"):
      return "Error: Operator must be '+' or '-'."
    elif(line[0].isdigit() != True or line[2].isdigit() != True):
      return 'Error: Numbers must only contain digits.'


    rjustnum = 0

    if(len(str(line[0])) >= len(str(line[2]))):
      rjustnum = len(str(line[0])) + 2
    else:
      rjustnum = len(str(line[2])) + 2
    
    if(counter == 2): #First Operation
      num1 = num1 + str(line[0].rjust(rjustnum)) + "    "
      num2 = num2 + str(line[1]) + " " + str(line[2].rjust(rjustnum - 2)) + "    "
      lines = lines + '-'*rjustnum + "    "
      solutions = solutions + str(solve_operation(int(line[0]), int(line[2]), line[1])).rjust(rjustnum) + "    "   
    elif(counter > len(problems)):#Last Operation
      num1 = num1 + str(line[0].rjust(rjustnum)) + "\n"
      num2 = num2 + str(line[1].rjust(1)) + " " + str(line[2].rjust(rjustnum - 2)) + "\n"
      # Check if should be solved
      if(should_solve):
        lines = lines + '-'*rjustnum + "\n"
        solutions = solutions + str(solve_operation(int(line[0]), int(line[2]), line[1])).rjust(rjustnum)
      else:
        lines = lines + '-'*rjustnum
      
    else:#Middle Operations
      num1 = num1 + str(line[0].rjust(rjustnum)) + "    "
      num2 = num2 + str(line[1].rjust(1)) + " " + str(line[2].rjust(rjustnum - 2)) + "    "
      lines = lines + '-'*rjustnum + "    "
      solutions = solutions + str(solve_operation(int(line[0]), int(line[2]), line[1])).rjust(rjustnum) + "    " 
    


  if(should_solve):
     arranged_problems = num1 + num2 + lines + solutions
  else:
     arranged_problems = num1 + num2 + lines
 

     
  

  return arranged_problems