def arithmetic_arranger(problems, show_answers=False):
    opr = [problem.split(' ')[1] for problem in problems]
    
    top_row = [problem.split(' ')[0] for problem in problems]
    bottom_row = [problem.split(' ')[2] for problem in problems]
    
    top_str = []
    middle_str = []
    bottom_str = []
    ans = []
    max_lengths = []

    if len(problems) > 5:
        return 'Error: Too many problems.'
    elif '*' in opr or '/' in opr:
        return "Error: Operator must be '+' or '-'."
    elif any(not number.isdigit() for number in top_row) or any(not number.isdigit() for number in bottom_row):
        return 'Error: Numbers must only contain digits.'
    elif any(len(str(number)) > 4 for number in top_row) or any(len(str(number)) > 4 for number in bottom_row):
        return 'Error: Numbers cannot be more than four digits.'
    
    # Calculate max length of operands (either top or bottom) for each problem
    for i in range(len(problems)):
        longest_operand = max(len(top_row[i]), len(bottom_row[i]))  # Get longest length of top and bottom operands
        max_lengths.append(longest_operand)

    for i in range(len(problems)):
        # Right-align top and bottom operands, add space for operator
        top = f"{top_row[i]}".rjust(max_lengths[i] + 2)  
        middle = f"{opr[i]} {bottom_row[i]}".rjust(max_lengths[i] + 2)
        bottom = '-' * (max_lengths[i] + 2)  # Draw line as long as the longest operand

        # Solve the problem
        if opr[i] == '+':
            solved = int(top_row[i]) + int(bottom_row[i])
        else:
            solved = int(top_row[i]) - int(bottom_row[i])
        
        solved = str(solved).rjust(max_lengths[i] + 2)  # Right-align the result

        # Add to respective lists
        ans.append(solved)
        top_str.append(top)
        middle_str.append(middle)
        bottom_str.append(bottom)

    # Arrange the output
    if show_answers:
        arranged = "\n".join([ "    ".join(top_str), "    ".join(middle_str), "    ".join(bottom_str), "    ".join(ans)])
    else:
        arranged = "\n".join([ "    ".join(top_str), "    ".join(middle_str), "    ".join(bottom_str)])

    return arranged

# Test cases
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))  
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))  
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))  
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))  
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))  
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))  
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))  
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))  
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))  
