'''
Finding the inverse using the equation A^-1=adj(A)/det(A)
'''
matrix = []

print("Enter the elements of the 3 x 3 matrix:")

for i in range(3):
    row = []
    for j in range(3):
        value = float(input(f"Enter [{i},{j}]: "))
        row.append(value)
    matrix.append(row)




print("\n Input matrix:")

for row in matrix:
    print(row)


'''
a b c
d e f
g h i
'''


a = matrix[0][0]
b = matrix[0][1]
c = matrix[0][2]

d = matrix[1][0]
e = matrix[1][1]
f = matrix[1][2]

g = matrix[2][0]
h = matrix[2][1]
i = matrix[2][2]




determinant = (
    a * (e * i - f * h)
    - b * (d * i - f * g)
    + c * (d * h - e * g)
)


# if det=0 then there no inverse since division by zero is not possible 

if determinant == 0:

    print("\nInverse does not exist.")

else:

    # Finding adjoint matrix (remove the row and column of the respective element.)

    adjoint = [
        [e*i - f*h, c*h - b*i, b*f - c*e],
        [f*g - d*i, a*i - c*g, c*d - a*f],
        [d*h - e*g, b*g - a*h, a*e - b*d]
    ]


    # Dividing adjoint by determinant

    inverse = []

    for row in adjoint:

        new_row = []

        for value in row:
            new_row.append(value / determinant)

        inverse.append(new_row)



    print("\nInverse matrix:")

    for row in inverse:
        print(row)