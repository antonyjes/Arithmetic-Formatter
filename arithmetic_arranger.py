def arithmetic_arranger(problems, show_results = False):
  if len(problems) > 5:
    return "Error: Too many problems."

  first_numbers = []
  operators = []
  second_numbers = []
  results = []
  first_line = ''
  second_line = ''
  third_line = ''
  fourth_line = ''

  for problem in problems:
    problem = problem.split()
    if problem[1] != '+' and problem[1] != '-':
      return "Error: Operator must be '+' or '-'."
    elif problem[0].isdigit() == False or problem[2].isdigit() == False:
      return "Error: Numbers must only contain digits."
    elif len(problem[0]) > 4 or len(problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    first_numbers.append(problem[0])
    operators.append(problem[1])
    second_numbers.append(problem[2])

  for i in range(len(problems)):
    number1 = first_numbers[i]
    operator = operators[i]
    number2 = second_numbers[i]

    if operator == '+':
      results.append(str(int(number1)+int(number2)))
    elif operator == '-':
      results.append(str(int(number1)-int(number2)))

    length = max(len(str(number1)), len(str(number2)))
    
    first_line = first_line + " "*2 + " "*(length-len(number1)) + number1 + " "*4
    second_line = second_line + operator + " " + " "*(length-len(number2)) + number2 + " "*4
    third_line = third_line + "-"*(length+2) + " "*4
    fourth_line = fourth_line + " "*(length+2-len(str(results[i]))) + str(results[i]) + " "*4

  first_line = first_line.rstrip()
  second_line = second_line.rstrip()
  third_line = third_line.rstrip()
  fourth_line = fourth_line.rstrip()
  
  if show_results == True:
    arranged_problems = first_line + "\n" + second_line + "\n" + third_line + "\n" + fourth_line
  else:
    arranged_problems = first_line + "\n" + second_line + "\n" + third_line
  
  return arranged_problems