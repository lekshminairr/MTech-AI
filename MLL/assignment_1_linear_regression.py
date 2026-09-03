import pandas as pd
import matplotlib.pyplot as plt

# # Load the dataset
# data = pd.read_csv("/content/Salary_dataset.csv")
# Dataset
data = pd.DataFrame({
    "YearsExperience": [
        1.0, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0, 2.1, 2.3, 2.5,
        2.7, 2.9, 3.0, 3.1, 3.3, 3.5, 3.7, 3.9, 4.0, 4.1,
        4.2, 4.4, 4.5, 4.7, 4.9, 5.0, 5.1, 5.3, 5.5, 5.7,
        5.9, 6.0, 6.2, 6.4, 6.6, 6.8, 7.0, 7.1, 7.3, 7.5,
        7.7, 7.9, 8.0, 8.2, 8.4, 8.6, 8.7, 8.9, 9.0, 9.2,
        9.4, 9.5, 9.6, 9.8, 10.0, 10.2, 10.3, 10.5, 10.7, 10.9,
        11.0, 11.2, 11.4, 11.6, 11.8, 12.0, 12.2, 12.4, 12.6, 12.8,
        13.0, 13.2, 13.4, 13.6, 13.8, 14.0, 14.2, 14.4, 14.6, 14.8,
        15.0, 15.2, 15.4, 15.6, 15.8, 16.0, 16.2, 16.4, 16.6, 16.8,
        17.0, 17.2, 17.4, 17.6, 17.8, 18.0, 18.2, 18.4, 18.6, 18.8
    ],

    "Salary": [
        35000, 39344, 46206, 41000, 37732, 42000, 43000, 43526, 39892, 45000,
        48000, 51000, 56643, 60151, 54446, 56000, 57190, 63219, 55795, 56958,
        57082, 61112, 67939, 64000, 66030, 72000, 83089, 81364, 85000, 88000,
        93941, 91739, 95000, 97000, 98274, 101000, 99000, 101303, 105000, 108000,
        110000, 113813, 112000, 113813, 116970, 115000, 118000, 120000, 105583, 119000,
        116970, 120000, 112636, 121000, 122392, 123000, 121873, 125000, 127000, 130000,
        128000, 132000, 134000, 136000, 138000, 140000, 142000, 145000, 147000, 150000,
        148000, 152000, 154000, 157000, 159000, 162000, 160000, 165000, 168000, 170000,
        172000, 175000, 178000, 180000, 183000, 185000, 188000, 190000, 193000, 195000,
        198000, 200000, 203000, 205000, 208000, 210000, 213000, 215000, 218000, 220000
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

L = 0.001
epochs = 1200


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
