
def arithmetic_arranger(problems, solve = False):
  if len(problems) > 5 :
    return "Error: Too many problems."


  str1, str2, str3, str4 = '', '', '', '' 
  
  for p in problems : 
    problem = p.strip().split()
    
    if problem[1] not in {'+', '-'} : 
      return "Error: Operator must be '+' or '-'." 
      
    if not (problem[0].isnumeric() and problem[2].isnumeric()) :
      return "Error: Numbers must only contain digits." 
      
    if len(problem[0]) > 4 or len(problem[2]) > 4 : 
      return "Error: Numbers cannot be more than four digits." 

    n1 = problem[0]
    n2 = problem[2] 
    ans = '' 
    
    if problem[1] == '-' :
      ans = str(int(problem[0]) - int(problem[2])) 
    else : 
      ans = str(int(problem[0]) + int(problem[2])) 

    m = max(len(n1), len(n2)) + 2 
    
    n1 = n1.rjust(m) 
    n2 = problem[1] + n2.rjust(m-1) 
    dash = '-'*m 
    ans = ans.rjust(m) 

    str1 += n1
    str2 += n2 
    str3 += dash 
    str4 += ans 
    if p != problems[-1]:
      str1 += '    '
      str2 += '    '
      str3 += '    ' 
      str4 += '    ' 
  if solve : 
    return '\n'.join([str1, str2, str3, str4])
  else : 
    return '\n'.join([str1, str2, str3])