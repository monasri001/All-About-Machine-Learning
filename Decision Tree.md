## 🌳 Decision Tree (Complete, Clear & Exam-Ready)

## 🔍 Definition

**Decision Tree** is a **supervised machine learning algorithm** used for **classification and regression** that makes decisions by **splitting data into branches** based on feature conditions, forming a **tree-like structure**.

👉 It works exactly like **human decision-making** (if–else logic).

---

## 🧠 Core Idea (One Line)

> A Decision Tree splits data step-by-step using rules until it reaches a final decision (leaf).

---

## 🌳 Structure of a Decision Tree

* **Root Node** – first split (most important feature)
* **Decision Node** – internal node with a condition
* **Branch** – outcome of a condition
* **Leaf Node** – final prediction

---

## 🧠 How Decision Tree Works (Step-by-Step)

1️⃣ Select the **best feature** to split the data
2️⃣ Split data based on a condition
3️⃣ Repeat splitting for child nodes
4️⃣ Stop when:

* All samples belong to one class, or
* Maximum depth is reached
  5️⃣ Leaf node gives final output

---

## 📊 How Does It Choose the Best Split?

### 🔹 1. Entropy (Information Gain)

#### Entropy

[
Entropy = -\sum p \log_2(p)
]

* Measures **impurity**
* 0 → pure node

#### Information Gain

[
IG = Entropy(parent) - \sum Entropy(children)
]

✔ Feature with **highest Information Gain** is chosen

---

### 🔹 2. Gini Index

[
Gini = 1 - \sum p^2
]

* Used in **CART** trees
* Lower Gini → better split

---

## 📘 Types of Decision Trees

### 1️⃣ Classification Tree

* Output: Category
* Example: Pass / Fail, Spam / Not Spam

### 2️⃣ Regression Tree

* Output: Continuous value
* Example: House price prediction

---

## 🧪 Example

**Loan Approval**

```
Is Income > 5L?
 ├─ Yes → Is Credit Score good?
 │     ├─ Yes → Approve
 │     └─ No → Reject
 └─ No → Reject
```

---

## 📌 Stopping Criteria

* Maximum tree depth
* Minimum samples per leaf
* No improvement in split

---

## ⚠️ Overfitting Problem

Decision Trees can **memorize training data**.

### 🔧 Solutions:

* Pruning
* Limiting depth
* Minimum samples per split

---

## 📊 Performance Metrics

* Accuracy
* Precision / Recall
* RMSE (for regression)

---

## ✅ Advantages

✔ Easy to understand & visualize
✔ No feature scaling needed
✔ Handles both numerical & categorical data
✔ Non-linear relationships supported

---

## ❌ Disadvantages

❌ Overfitting
❌ Unstable (small data change → big tree change)
❌ Lower accuracy compared to ensemble models

---

## 🧠 One-Line Interview Answer

> **Decision Tree is a supervised learning algorithm that makes predictions by recursively splitting data based on feature conditions using a tree-like structure.**

