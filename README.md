# Project Euler: Largest Palindrome Product

A highly optimised Python solution for [Project Euler Problem 4](https://projecteuler.net/problem=4): *"Find the largest palindrome made from the product of two 3-digit numbers."*

## 🚀 Overview
This project demonstrates algorithmic optimisation by refactoring a standard numerical problem to minimise execution time. While a naive brute-force approach checks every possible product pair, this solution implements mathematical pruning to significantly reduce the search space.

## ⚙️ Technical Approach

### 1. Dynamic Search Pruning (Early Termination)
**The Concept:** Avoid checking products that are mathematically guaranteed to be smaller than the current best candidate.
**The Implementation:**
The algorithm tracks the `largest_palindrome` found so far. Since the inner loop decrements `j`, if the current product `i * j` is smaller than the best found, all subsequent iterations for that `i` will also be smaller.
* **Result:** The inner loop terminates immediately, preventing unnecessary CPU cycles on lower-bound numbers.

### 2. Symmetry Optimisation (Commutativity)
**The Concept:** Multiplication is commutative ($A \times B = B \times A$).
**The Implementation:**
The inner loop starts from the current value of the outer loop index (`j = i`) rather than resetting to the maximum.
* **Result:** This eliminates redundant calculations (e.g., calculating $999 \times 998$ but skipping $998 \times 999$), effectively halving the total iteration count.

## ⏱️ Performance
* **Language:** Python 3.x
* **Complexity:** Preserves $O(N^2)$ worst-case complexity but achieves a massive reduction in **average execution time** via aggressive pruning.
* **Outcome:** Delivers the correct solution with minimal latency compared to a full exhaustive search.

## 💻 Usage
Run the script directly from the terminal:

```bash
python3 Largest_Palindrome_Product.py
