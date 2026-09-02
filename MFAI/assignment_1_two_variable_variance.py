#reading number of datapoints in the order (ht,wt)
rows=input("Enter the number of rows/data points")
n=int(rows)
matrix=[]
for i in range(n):
    ht=float(input(f"Enter height{i+1}:"))
    wt=float(input(f"Enter weight{i+1}:"))
    matrix.append([ht,wt])
#checking if n>1 to avoid division by zero at later point(n-1) and logically too
if n<2:
    print("\n Error enter atleast two datapoints:")
else:
    sum_ht=0.0
    sum_wt=0.0
#summation of height and weight to find average
    for i in range(n):
        sum_ht +=matrix[i][0]
        sum_wt +=matrix[i][1]
    average_ht=sum_ht/n
    average_wt=sum_wt/n
    sum_sq_ht=0.0
    sum_sq_wt=0.0
    sum_hw=0.0
#finding X, Y and XY
    for i in range(n):
        diff_ht=matrix[i][0]-average_ht
        diff_wt=matrix[i][1]-average_wt
        sum_sq_ht +=diff_ht*diff_ht
        sum_sq_wt +=diff_wt*diff_wt
        sum_hw +=diff_ht*diff_wt
#finding compomnents of the variance matrix.[[X^2/(n-1),XY/(n-1)],[XY/(n-1),Y^2/(n-1)]]
    var_ht=sum_sq_ht/(n-1)
    var_wt=sum_sq_wt/(n-1)
    cov_hw=sum_hw/(n-1)
    cov_matrix=[[var_ht,cov_hw],[cov_hw,var_wt]]
    print("covariance matrix:")
    for row in cov_matrix:
        print(row)
    
