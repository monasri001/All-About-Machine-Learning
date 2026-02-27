## 14️⃣ Policy Learning (Introduction)

Since you just saw **Q-Learning (value-based method)**, now let’s move to the second major family in Reinforcement Learning:

> 🔥 **Policy-Based Methods (Policy Learning)**

This is very important for advanced AI systems — especially if you're thinking about research-level AI or adaptive systems (like your threshold optimization idea 👀).

---

# 1️⃣ What is a Policy?

A **policy** tells the agent what action to take in each state.

It is written as:

[
\pi(a|s)
]

Meaning:

* Probability of taking action **a** given state **s**

So instead of learning Q-values,
👉 we directly learn the **policy function**.

---

# 2️⃣ Value-Based vs Policy-Based

| Q-Learning                       | Policy Learning                   |    |
| -------------------------------- | --------------------------------- | -- |
| Learns Q(s,a)                    | Learns π(a                        | s) |
| Then picks best action           | Directly outputs action           |    |
| Works well for discrete problems | Works well for continuous actions |    |
| Uses Q-table / Q-network         | Uses neural network policy        |    |

---

# 3️⃣ Why Do We Need Policy Learning?

Q-learning struggles when:

* Action space is continuous (e.g., steering angle 23.5°)
* Very large state space
* Probabilistic decision making required
* Robotics control
* Advanced AI agents

Policy learning handles these better.

---

# 4️⃣ Types of Policies

### 1️⃣ Deterministic Policy

[
a = \pi(s)
]

One fixed action for each state.

---

### 2️⃣ Stochastic Policy

[
\pi(a|s)
]

Outputs probability distribution over actions.

Example:

* 70% move left
* 20% move right
* 10% stay

This is common in modern RL.

---

# 5️⃣ How Policy Learning Works

We define:

* Policy network (neural network)
* Reward function
* Objective: maximize expected reward

Goal:

[
\max_\theta J(\theta)
]

Where:

* θ = policy parameters
* J(θ) = expected cumulative reward

---

# 6️⃣ Policy Gradient (Basic Idea)

We update parameters in direction:

[
\theta = \theta + \alpha \nabla J(\theta)
]

We push policy to increase probability of actions that gave high rewards.

---

# 7️⃣ Visual Intuition

![Image](https://lilianweng.github.io/posts/2018-04-08-policy-gradient/A3C_vs_A2C.png)

![Image](https://www.researchgate.net/publication/360910430/figure/fig1/AS%3A11431281080452861%401661307888574/Deep-reinforcement-learning-scheme-A-deep-neural-network-learns-the-policy.png)

![Image](https://www.tutorialspoint.com/machine_learning/images/actor_critic_method.jpg)

![Image](https://miro.medium.com/0%2APhUWeSkXpKxG0rLZ.png)

Instead of learning Q-table:

* Neural network outputs action probabilities
* Agent samples action
* Reward updates network weights

---

# 8️⃣ Popular Policy-Based Algorithms

* REINFORCE
* Actor-Critic
* PPO (Proximal Policy Optimization)
* A3C
* TRPO

These are used in:

* Robotics
* Self-driving cars
* Large-scale AI agents
* Game AI (AlphaGo style systems)

---

# 9️⃣ Advantages

✔ Handles continuous actions
✔ More stable in complex environments
✔ Better convergence in large state spaces

---

# 🔟 Limitations

❌ High variance
❌ Needs careful tuning
❌ Slower to converge sometimes

