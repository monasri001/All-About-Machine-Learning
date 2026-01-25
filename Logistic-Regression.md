## 📊 Logistic Regression 

## 🔍 Definition

**Logistic Regression** is a **supervised machine learning algorithm** used for **classification problems**, where the output is **categorical (mostly binary)**.

👉 Even though it’s called *regression*, it is used for **classification**, not continuous prediction.

---

## 🧠 Core Idea (One Line)

> Logistic Regression predicts the **probability** that an input belongs to a particular class using the **Sigmoid function**.

---

## 📐 Mathematical Model

### Linear Equation

[
z = b_0 + b_1x_1 + b_2x_2 + \dots + b_nx_n
]

### Sigmoid (Logistic) Function

[
\sigma(z) = \frac{1}{1 + e^{-z}}
]

📌 Output range: **0 to 1** (probability)

---

## 🧮 Decision Rule

* If **probability ≥ 0.5 → Class 1**
* If **probability < 0.5 → Class 0**

(Threshold can be changed depending on the problem)

---

## 🧠 How Logistic Regression Works (Step-by-Step)

1️⃣ Take labeled data (X, Y)
2️⃣ Compute linear combination (z)
3️⃣ Apply sigmoid function
4️⃣ Get probability value
5️⃣ Compare with threshold
6️⃣ Classify the output
7️⃣ Update weights using **Gradient Descent**

---

## 📊 Cost Function (Very Important)

### Log Loss / Binary Cross-Entropy

[
J = -\frac{1}{n} \sum [y\log(p) + (1-y)\log(1-p)]
]

🎯 Goal: **Minimize Log Loss**

---

## 📌 Why Not Mean Squared Error?

* Sigmoid makes MSE non-convex
* Log loss ensures **faster and stable convergence**

---

## 🧠 Types of Logistic Regression

### 1️⃣ Binary Logistic Regression

* Two classes (0 / 1)
* Example: Spam / Not Spam

### 2️⃣ Multinomial Logistic Regression

* More than two classes
* Example: Digit classification (0–9)

### 3️⃣ Ordinal Logistic Regression

* Ordered classes
* Example: Low, Medium, High

---

## 📊 Performance Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

---

## 🧪 Real-World Examples

* Email spam detection
* Disease diagnosis (Yes / No)
* Fraud detection
* Customer churn prediction

---

## 📌 Assumptions of Logistic Regression (Exam-Important)

1. Binary or categorical output
2. Independent observations
3. Little or no multicollinearity
4. Linear relationship between features and **log-odds**

---

## ✅ Advantages

✔ Simple & fast
✔ Probabilistic output
✔ Easy to interpret
✔ Works well for linearly separable data

---

## ❌ Disadvantages

❌ Not suitable for non-linear boundaries
❌ Sensitive to outliers
❌ Requires feature scaling

---

## 🧠 One-Line Interview Answer

> **Logistic Regression is a supervised classification algorithm that uses the sigmoid function to predict probabilities and classify data into categories.**



