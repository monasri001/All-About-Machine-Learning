## 📘 Types of Machine Learning – **Detailed Definitions**

## 1️⃣ Supervised Learning

### 🔍 Definition

**Supervised Learning** is a type of machine learning where the model is trained using **labeled data**, meaning **each input has a known correct output**.
The model learns a mapping between **input (X)** and **output (Y)** and uses it to predict outputs for new data.

📌 *“Supervised” means a teacher (label) is available.*

---

### 🧠 How it works

* Data contains **features + target label**
* Model compares its prediction with actual output
* Error is calculated and minimized during training

---

### 📊 Types of Supervised Learning

#### a) **Regression**

* Output is a **continuous value**
* Examples:

  * House price prediction
  * Salary estimation
* Algorithms:

  * Linear Regression
  * Polynomial Regression
  * Random Forest Regressor

#### b) **Classification**

* Output is a **category or class**
* Examples:

  * Spam / Not Spam
  * Fraud / Not Fraud
* Algorithms:

  * Logistic Regression
  * Decision Tree
  * SVM
  * KNN
  * Naive Bayes

---

### ✅ Advantages

* High accuracy
* Easy to evaluate
* Clear learning objective

### ❌ Disadvantages

* Requires large labeled datasets
* Labeling is time-consuming and costly

---

## 2️⃣ Unsupervised Learning

### 🔍 Definition

**Unsupervised Learning** is a type of machine learning where the model is trained on **unlabeled data**.
The model **discovers hidden patterns, structures, or relationships** on its own.

📌 *No correct answers are given.*

---

### 🧠 How it works

* Data contains only inputs
* Model groups or organizes data based on similarity
* No direct feedback on correctness

---

### 📊 Types of Unsupervised Learning

#### a) **Clustering**

* Groups similar data points together
* Examples:

  * Customer segmentation
  * Image grouping
* Algorithms:

  * K-Means
  * DBSCAN
  * Hierarchical Clustering

#### b) **Association Rule Learning**

* Finds relationships between variables
* Example:

  * Market basket analysis (Milk → Bread)
* Algorithms:

  * Apriori
  * FP-Growth

#### c) **Dimensionality Reduction**

* Reduces number of features while keeping important information
* Examples:

  * Data visualization
  * Noise reduction
* Algorithms:

  * PCA
  * LDA
  * t-SNE

---

### ✅ Advantages

* No need for labeled data
* Finds hidden patterns
* Useful for exploratory analysis

### ❌ Disadvantages

* Results may be hard to interpret
* No clear accuracy metric

---

## 3️⃣ Semi-Supervised Learning

### 🔍 Definition

**Semi-Supervised Learning** uses a **small amount of labeled data** and a **large amount of unlabeled data** to train the model.
It combines the strengths of supervised and unsupervised learning.

📌 Useful when labeling data is expensive.

---

### 🧠 How it works

* Train initial model with labeled data
* Use model to label unlabeled data
* Retrain model with expanded dataset

---

### 🧪 Examples

* Medical image classification
* Speech recognition
* Web page classification

---

### ✅ Advantages

* Better accuracy than unsupervised learning
* Less labeling cost
* Efficient for real-world problems

### ❌ Disadvantages

* Risk of incorrect pseudo-labels
* More complex implementation

---

## 4️⃣ Reinforcement Learning

### 🔍 Definition

**Reinforcement Learning (RL)** is a type of machine learning where an **agent learns by interacting with an environment** and receiving **rewards or penalties** for actions.

📌 Learning is based on **trial and error**.

---

### 🧠 Key Elements

* **Agent** – learner or decision maker
* **Environment** – world where agent acts
* **Action** – decision taken
* **Reward** – feedback (positive or negative)
* **Policy** – strategy to choose actions

---

### 🧪 Examples

* Game-playing AI (Chess, Go)
* Robotics
* Autonomous vehicles
* Recommendation systems (dynamic)

---

### ✅ Advantages

* No labeled data needed
* Learns optimal strategies
* Suitable for dynamic environments

### ❌ Disadvantages

* Requires large training time
* Computationally expensive
* Hard to design reward function

---

## 🆚 Summary Table

| Type            | Data Label   | Output  | Example             |
| --------------- | ------------ | ------- | ------------------- |
| Supervised      | Labeled      | Known   | Spam detection      |
| Unsupervised    | Unlabeled    | Unknown | Customer clustering |
| Semi-supervised | Few labels   | Known   | Medical diagnosis   |
| Reinforcement   | Reward-based | Action  | Game AI             |

