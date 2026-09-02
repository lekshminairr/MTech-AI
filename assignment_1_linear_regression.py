import pandas as pd
import matplotlib.pyplot as plt

# # Load the dataset
# data = pd.read_csv("/content/Salary_dataset.csv")
# Dataset
data = pd.DataFrame({
    "YearsExperience": [
        1.2, 1.4, 1.6, 2.1, 2.3,
        3.0, 3.1, 3.3, 3.7, 3.9,
        4.0, 4.1, 4.2, 4.4, 4.5,
        4.9, 5.1, 5.3, 5.9, 6.0,
        6.8, 7.1, 7.9, 8.2, 8.7,
        9.0, 9.5, 9.6, 10.3, 10.5
    ],

    "Salary": [
        39344, 46206, 37732, 43526, 39892,
        56643, 60151, 54446, 57190, 63219,
        55795, 56958, 57082, 61112, 67939,
        66030, 83089, 81364, 93941, 91739,
        98274, 101303, 113813, 113813, 116970,
        105583, 116970, 112636, 122392, 121873
    ]
})

# Remove the unnecessary index column
data = data[["YearsExperience", "Salary"]]


def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].YearsExperience
        y = points.iloc[i].Salary

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L

    return m, b



m = 0
b = 0

L = 0.01
epochs = 1000


# Gradient Descent
for i in range(epochs):
    m, b = gradient_descent(m, b, data, L)
    if(i%100==0):
        print(f"Epoch: {i} /1000 completed")


print("Slope (m):", m)
print("Intercept (b):", b)


# Plot the data points
plt.scatter(
    data.YearsExperience,
    data.Salary,
    color="black"
)

# Plot regression line
plt.plot(
    data.YearsExperience,
    [m * x + b for x in data.YearsExperience],
    color="red"
)

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression using Gradient Descent")
plt.show()