# Project Euler: Largest Palindrome Product

A highly optimised Python solution for [Project Euler Problem 4](https://projecteuler.net/problem=4): *"Find the largest palindrome made from the product of two 3-digit numbers."*

## 🚀 Overview
This project demonstrates algorithmic optimisation by refactoring a standard numerical problem to minimise execution time. While a naive brute-force approach checks every possible product pair, this solution implements mathematical pruning to significantly reduce the search space.

## ⚙️ Technical Approach

### 1. Dynamic Search Pruning (Early Termination)
**The Concept:** Avoid checking products that are mathematically guaranteed to be smaller than the current best candidate.
**The Implementation:**
The algorithm tracks the `max_palindrome` found so far. If the product of the current loop indices drops below this maximum, the inner loop terminates immediately.
* **Result:** This prevents unnecessary CPU cycles on lower-bound numbers, focusing resources only on high-value candidates.

### 2. Symmetry Optimisation (Commutativity)
**The Concept:** Multiplication is commutative ($A \times B = B \times A$).
**The Implementation:**
The inner loop starts from the current value of the outer loop index (`j = i`).
* **Result:** This eliminates redundant calculations (e.g., calculating $999 \times 998$ but skipping $998 \times 999$), effectively halving the number of iterations required.

## ⏱️ Performance
* **Language:** Python 3.x
* **Complexity:** improved significantly over standard $O(N^2)$ via aggressive pruning.
* **Outcome:** Delivers the correct solution with minimal latency compared to a full exhaustive search.

## 💻 Usage
Run the script directly from the terminal:

```bash
python3 solution.py
