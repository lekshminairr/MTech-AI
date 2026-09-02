# reading number of datapoints in the order (x, y, z)
rows = input("Enter the number of rows/data points: ")
n = int(rows)

matrix = []

for i in range(n):
    x = float(input(f"Enter x {i+1}: "))
    y = float(input(f"Enter y {i+1}: "))
    z = float(input(f"Enter z {i+1}: "))
    matrix.append([x, y, z])

# checking if n > 1 to avoid division by zero at later point (n-1)
if n < 2:
    print("\nError: Enter at least two datapoints")
else:
    sum_x = 0.0
    sum_y = 0.0
    sum_z = 0.0

    # summation of x, y and z to find average
    for i in range(n):
        sum_x += matrix[i][0]
        sum_y += matrix[i][1]
        sum_z += matrix[i][2]

    average_x = sum_x / n
    average_y = sum_y / n
    average_z = sum_z / n

    sum_sq_x = 0.0
    sum_sq_y = 0.0
    sum_sq_z = 0.0

    sum_xy = 0.0
    sum_xz = 0.0
    sum_yz = 0.0

    # finding X, Y, Z and their products
    for i in range(n):
        diff_x = matrix[i][0] - average_x
        diff_y = matrix[i][1] - average_y
        diff_z = matrix[i][2] - average_z

        sum_sq_x += diff_x * diff_x
        sum_sq_y += diff_y * diff_y
        sum_sq_z += diff_z * diff_z

        sum_xy += diff_x * diff_y
        sum_xz += diff_x * diff_z
        sum_yz += diff_y * diff_z

    # finding components of the covariance matrix
    var_x = sum_sq_x / (n - 1)
    var_y = sum_sq_y / (n - 1)
    var_z = sum_sq_z / (n - 1)

    cov_xy = sum_xy / (n - 1)
    cov_xz = sum_xz / (n - 1)
    cov_yz = sum_yz / (n - 1)

    # covariance matrix
    cov_matrix = [
        [var_x, cov_xy, cov_xz],
        [cov_xy, var_y, cov_yz],
        [cov_xz, cov_yz, var_z]
    ]

    print("\nCovariance matrix:")

    for row in cov_matrix:
        print(row)