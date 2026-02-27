## Q-Learning (Reinforcement Learning)

Q-Learning is a **model-free reinforcement learning algorithm** used to find the best action an agent should take in a given state to maximize cumulative reward.

Since you're into AI & ML (and already working on optimization ideas like RL-based threshold tuning in your image authenticity project 👀), this concept is very relevant for you.

---

## 1️⃣ What Problem Does Q-Learning Solve?

It solves **sequential decision-making problems**.

Example:

* Robot navigating a maze
* Game-playing AI
* Dynamic pricing
* Threshold optimization
* Resource allocation

---

## 2️⃣ Core Idea

Q-Learning learns a function called:

[
Q(s, a)
]

Where:

* **s** = current state
* **a** = action
* **Q(s,a)** = expected future reward if we take action `a` in state `s`

The goal is to learn the **optimal Q-values**.

---

## 3️⃣ Q-Table Concept

We store values in a table like this:

| State | Action 1 | Action 2 | Action 3 |
| ----- | -------- | -------- | -------- |
| S1    | 0.5      | 1.2      | 0.1      |
| S2    | 0.8      | 0.3      | 1.5      |

The agent chooses the action with the **highest Q-value**.

---

## 4️⃣ Q-Learning Update Formula (Very Important ⭐)

[
Q(s,a) = Q(s,a) + \alpha \left[ r + \gamma \max Q(s',a') - Q(s,a) \right]
]

Where:

* **α (alpha)** = learning rate
* **γ (gamma)** = discount factor
* **r** = reward
* **s'** = next state

### Meaning:

New Q-value =
Old Q-value + Learning rate × (Target − Old value)

---

## 5️⃣ How It Works (Step-by-Step)

1. Initialize Q-table with zeros.
2. Observe current state.
3. Choose action (exploration or exploitation).
4. Take action → get reward.
5. Update Q-value.
6. Repeat until convergence.

---

## 6️⃣ Exploration vs Exploitation

We use **ε-greedy strategy**:

* With probability ε → explore (random action)
* With probability 1−ε → exploit (best known action)

This prevents the agent from getting stuck in a bad policy.

---

## 7️⃣ Simple Python Example (Concept Level)

```python
import numpy as np

# States = 3, Actions = 2
Q = np.zeros((3, 2))

alpha = 0.1
gamma = 0.9

state = 0
action = 1
reward = 10
next_state = 2

Q[state, action] = Q[state, action] + alpha * (
    reward + gamma * np.max(Q[next_state]) - Q[state, action]
)

print(Q)
```

---

## 8️⃣ Visual Example – Grid World

![Image](https://www.mathworks.com/help/examples/rl/win64/BasicGridWorldExample_01.png)

![Image](https://www.researchgate.net/publication/342657550/figure/fig1/AS%3A1111137764556801%401641927295552/Grid-world-example-with-a-sample-trajectory-generated-by-policy-p-The-robot-is-tasked.jpg)

![Image](https://images.sciencebuddies.org/tbAGK1AYoMfYLMZOdXHMDaGICFM%3D/1200x600/-/https/www.sciencebuddies.org/cdn/Files/19813/7/maze-star.png)

![Image](https://miro.medium.com/1%2AABOvAjsEGnfVUP8FYcyp2g.png)

In grid world:

* Agent moves up/down/left/right
* Gets reward when reaching goal
* Learns optimal path

---

## 9️⃣ Advantages

✔ Model-free (no need environment model)
✔ Converges to optimal policy (if explored enough)
✔ Simple to implement

---

## 🔟 Limitations

❌ Large state space → Q-table becomes huge
❌ Not suitable for continuous state space

👉 Solution: **Deep Q-Network (DQN)** (uses neural networks instead of Q-table)

