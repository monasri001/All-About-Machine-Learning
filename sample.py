from sklearn.linear_model import LinearRegression
model = LinearRegression().fit([[1],[2],[3]], [2,4,6])
print(model.predict([[4]]))
