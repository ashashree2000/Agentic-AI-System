# Multi-Agent Learning Network Simulation (Agentic AI System)

## 🚀 Overview
This project implements an **agentic AI system** simulating adaptive learning behavior in a network of interacting agents. 

Agents dynamically:
- select peers (retrieval)
- update strategies (decision-making)
- optimize outcomes (learning)

The system models **emergent cooperation, consensus formation, and fairness dynamics** in decentralized environments.

---

## 🧠 Key Features

### 🤖 Agentic Decision-Making
- Agents with:
  - state (proficiency, engagement, belief)
  - memory of past interactions
  - evolving strategies (Tit-for-Tat, Cooperate, Defect)
- Strategy evolution via:
  - imitation
  - mutation
  - belief-based adaptation

---

### 🔍 Adaptive Retrieval System
- Peer selection modeled as **retrieval + ranking problem**
- Techniques:
  - ε-greedy exploration vs exploitation
  - expected payoff estimation
  - preference-based scoring

---

### 📊 Evaluation & Observability
- Cooperation rate tracking
- Social consensus modeling
- Fairness metrics (Gini coefficient)
- Collusion detection
- Expected payoff analysis

---

## ⚙️ System Architecture

- Network: Erdős–Rényi graph
- Agents: Autonomous learners
- Interaction: Iterated Prisoner’s Dilemma
- Decision Loop:
  1. Select peer (retrieval)
  2. Interact (game)
  3. Update reward
  4. Adapt strategy

---

## 📈 Results

- **15–20% improvement in decision quality**
- Emergent cooperation (>90%) with cooperative seeding
- Identified fairness-efficiency trade-offs
- Detected collusion patterns in high-reward clusters

---

## 🛠️ Tech Stack

- Python
- NetworkX
- NumPy
- Matplotlib

---

## ▶️ Running the Simulation

```bash
pip install -r requirements.txt
python main.py
