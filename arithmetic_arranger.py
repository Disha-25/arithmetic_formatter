def arithmetic_arranger(problems, *args):
  if len(problems)>5:
    return "Error: Too many problems."
  
  arranged_problems=[]
  
  for index, value in enumerate(problems):
    operation = value.split(" ")
    #["32","+"","8"]
    if operation[1] not in "+-":
      return "Error: Operator must be '+' or '-'."

    if len(operation[0])>4 or len(operation[2])>4:
      return "Error: Numbers cannot be more than four digits."
    
    try:
      value_1=int(operation[0])
      value_2=int(operation[2])
    except ValueError:
      return "Error: Numbers must only contain digits."

    #calculate the length of each line
    longest_val = max(len(operation[0]),len(operation[2]))
    width= longest_val +2

    # output = f"{operation[0]:>{width}}\n{f'{operation[1]} {operation[2]}':>{width}}\n{'-'*width}"
    
    l1=f"{operation[0]:>{width}}"
    l2=operation[1] + f"{operation[2]:>{width-1}}"
    d='-'*width
    
    try: 
      arranged_problems[0] += (' '*4)+l1
    except IndexError:
      arranged_problems.append(l1)
    
    try: 
      arranged_problems[1] += (' '*4)+l2
    except IndexError:
      arranged_problems.append(l2)
    
    try: 
      arranged_problems[2] += (' '*4)+d
    except IndexError:
      arranged_problems.append(d)

    if args:
      ans= int(operation[0]) + int(operation[2]) if operation[1] == '+' else int(operation[0]) - int(operation[2])
      a = f"{str(ans):>{width}}"
      
      try: 
        arranged_problems[3] += (' '*4)+a
      except IndexError:
        arranged_problems.append(a)
  
  output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
  output = output +f"\n{arranged_problems[3]}" if args else output
  return output
