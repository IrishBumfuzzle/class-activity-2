def find_cube_pairs(target):
    solutions = []
    max_num = round(target ** (1/3))  

    for a in range(1, max_num + 1):
        for b in range(a, max_num + 1):
            if a**3 + b**3 == target:
                solutions.append((a, b))
    return solutions

pairs = find_cube_pairs(1729)
print("Valid cube pairs for 1729:")
for a, b in pairs:
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")
"""Submit your response here:  https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u"""

"""
The code has been corrected to ensure that it finds all pairs of integers (a, b) such that a^3 + b^3 = 1729. 
The maximum number is calculated as the cube root of the target value, and the nested loop iterates 
through all possible pairs of integers up to that maximum. 
"""