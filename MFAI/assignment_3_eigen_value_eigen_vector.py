'''characteristic equation is found by  
lambda^3 - trace(A)lambda^2 + ((ae-bd)+ai-cg+(ei-fh))lambda- determinant(A) = 0
the eigen values by bisection method, eigen vectors by cross products of the rows
(after substituting the respective eigen values)'''

# matrix = []

# print("Enter the elements of the 3 x 3 matrix:")

# for i in range(3):
#     row = []
#     for j in range(3):
#         value = float(input(f"Enter [{i},{j}]: "))
#         row.append(value)
#     matrix.append(row)
matrix=[
    [9.066964285714286,-10.076785714285716,-0.726785714285714],
    [-10.076785714285716,159.125,123.05357142857143],
    [-0.726785714285714,123.05357142857143,684.6964285714286]
]


# Displaying the matrix

print("\nMatrix:")

for i in range(3):
    print(matrix[i])




a = matrix[0][0]
b = matrix[0][1]
c = matrix[0][2]

d = matrix[1][0]
e = matrix[1][1]
f = matrix[1][2]

g = matrix[2][0]
h = matrix[2][1]
i = matrix[2][2]


# Finding coefficients of characteristic equation
# |A - lambda I| = 0
#
# lambda^3 - trace(A)lambda^2
# + ((ae-bd)+ai-cg+(ei-fh))lambda
# - determinant(A) = 0


coefficient_lambda2 = -(a + e + i)

coefficient_lambda = (
    a * e +
    a * i +
    e * i -
    b * d -
    c * g -
    f * h
)

determinant = (
    a * e * i +
    b * f * g +
    c * d * h -
    c * e * g -
    b * d * i -
    a * f * h
)

coefficient_constant = -determinant




print("\nCharacteristic Equation:")

print(
    "lambda^3 + (",
    coefficient_lambda2,
    ")lambda^2 + (",
    coefficient_lambda,
    ")lambda + (",
    coefficient_constant,
    ") = 0"
)


# Function to calculate the value of the characteristic equation
# for a particular lambda

def equation(x):
    return (
        x**3 +
        coefficient_lambda2 * x**2 +
        coefficient_lambda * x +
        coefficient_constant
    )


#approx

maximum = max(
    abs(a), abs(b), abs(c),
    abs(d), abs(e), abs(f),
    abs(g), abs(h), abs(i)
)

limit = 3 * maximum + 1


# Finding eigenvalues using scanning and bisection, roots of cubic equation.

eigenvalues = []

step = 0.01
left = -limit
previous_value = equation(left)

while left <= limit and len(eigenvalues) < 3:

    right = left + step
    current_value = equation(right)

    # Check if the function crosses zero
    if previous_value * current_value <= 0:

        low = left
        high = right

        # Bisection method
        for k in range(100):

            middle = (low + high) / 2
            middle_value = equation(middle)

            if abs(middle_value) < 0.00000001:
                break

            if equation(low) * middle_value <= 0:
                high = middle
            else:
                low = middle

        root = (low + high) / 2

        # Avoid storing duplicate roots
        duplicate = False

        for value in eigenvalues:
            if abs(root - value) < 0.001:
                duplicate = True

        if duplicate == False:
            eigenvalues.append(root)

    left = right
    previous_value = current_value



print("\nEigenvalues:")

for value in eigenvalues:
    print(value)
# Finding eigenvectors

print("\nEigenvectors:")

for eigenvalue in eigenvalues:

    # Matrix (A - lambda I)

    r1 = [
        a - eigenvalue,
        b,
        c
    ]

    r2 = [
        d,
        e - eigenvalue,
        f
    ]

    r3 = [
        g,
        h,
        i - eigenvalue
    ]
    '''The eigen vectors r1.v=0||r2.v=0||r3.v=0 so since dot products are equaling zero
    that means they are perpendicular which in turn means their cross-product with each
    other could be zeroes(here we hope to find it with r1xr2=0 or r1xr3=0 if the other fails.) '''
    # Cross product of first two rows

    x = r1[1] * r2[2] - r1[2] * r2[1]
    y = r1[2] * r2[0] - r1[0] * r2[2]
    z = r1[0] * r2[1] - r1[1] * r2[0]

    # If first two rows give zero vector,
    # try rows 1 and 3

    if abs(x) < 0.000001 and abs(y) < 0.000001 and abs(z) < 0.000001:

        x = r1[1] * r3[2] - r1[2] * r3[1]
        y = r1[2] * r3[0] - r1[0] * r3[2]
        z = r1[0] * r3[1] - r1[1] * r3[0]

    print("\nEigenvalue:", eigenvalue)

    print("Eigenvector:")

    print("[", x, ",", y, ",", z, "]")
