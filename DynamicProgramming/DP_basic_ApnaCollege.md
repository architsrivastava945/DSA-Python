# Complete Dynamic Programming | DP Series - Lecture 1
**Source:** [Apna College - Complete Dynamic Programming | DP Series - Lecture 1](https://youtu.be/uBA8DkCBdco?si=mZpSu-sZoT05ULJT)

---

## 1. Introduction to Dynamic Programming (DP)

* **Definition:** Dynamic Programming is an optimization technique applied to recursive algorithms. It avoids redundant computations by storing intermediate subproblem results in a temporary data structure.
* **"Optimized Recursion":** Reduces time complexity from **Exponential ($O(2^N)$)** down to **Linear ($O(N)$)** or **Polynomial** time by eliminating repeated subtree calculations.
* **Core Philosophy:** *“Those who cannot remember the past are condemned to repeat it.”*

```
                 [ Recursive Problem ]
                           │
       ┌───────────────────┴───────────────────┐
       ▼                                       ▼
  Has Overlapping Subproblems?        Has Optimal Substructure?
       │                                       │
       └───────────────────┬───────────────────┘
                           ▼
                  [ Apply DP: O(N) ]
```

---

## 2. When Can We Apply DP? (Core Conditions)

A problem **must satisfy both** conditions to be solvable via Dynamic Programming:

### 2.1 Overlapping Subproblems
* The same smaller subproblems are computed repeatedly across different recursive branches.
* Typically occurs when recursive steps have multiple choices/branches (e.g., Grid paths with Top/Bottom/Left/Right choices, $n-1$ & $n-2$ calls).

### 2.2 Optimal Substructure
* The optimal solution of the main problem can be constructed directly by combining the optimal solutions of its subproblems.
* Example: To find $F(n)$, combine optimal results of $F(n-1)$ and $F(n-2)$.

```
+------------------------------------+------------------------------------+
| DP Applicable (Satisfies Both)     | DP NOT Applicable                  |
+------------------------------------+------------------------------------+
| • Fibonacci Numbers                | • Sum of 1 to N Numbers            |
| • 0/1 Knapsack                     |   (Single branch, no overlapping)  |
| • Longest Common Subsequence (LCS) | • Merge Sort / Quick Sort          |
| • Matrix Chain Multiplication      |   (Divide & conquer, no overlap)   |
+------------------------------------+------------------------------------+
```

---

## 3. The Motivating Example: Fibonacci Sequence

* **Recurrence Relation:** $F(n) = F(n-1) + F(n-2)$ with base cases $F(0) = 0$, $F(1) = 1$.

### 3.1 Standard Recursion (Brute Force)
* **Time Complexity:** $O(2^N)$ (Exponential)
* **Space Complexity:** $O(N)$ (Auxiliary call stack)

```
                       F(5)
                     /      \
                F(4)          F(3)  <-- Duplicate Call
               /    \        /    \
            F(3)    F(2)   F(2)   F(1)
           /   \    /  \   /  \
         F(2) F(1) F(1) F(0) F(1) F(0)
         /  \
       F(1) F(0)
```
*Notice:* $F(3)$ is computed twice, $F(2)$ is computed 3 times.

---

## 4. Approaches to Dynamic Programming

```
                      Dynamic Programming
                               │
       ┌───────────────────────┴───────────────────────┐
       ▼                                               ▼
1. Memoization (Top-Down)                      2. Tabulation (Bottom-Up)
   • Recursion + Memory (Array/Vector)            • Iteration (Loops) + Table
   • Starts from Big Problem (N) -> Base Cases    • Starts from Base Cases (0,1) -> N
```

---

### 4.1 Memoization (Top-Down Approach)

* **Concept:** Keep the recursive structure intact, but pass a lookup table (e.g., array/vector initialized to `-1`). Before executing a recursive call, check if the value already exists.

#### Algorithm Flowchart
```
                Call F_memo(n)
                      │
               Is n <= 1? ─── YES ───► Return n
                      │ NO
             Is dp[n] != -1? ─── YES ───► Return dp[n]
                      │ NO
           Compute: ans = F(n-1) + F(n-2)
                      │
                 dp[n] = ans
                      │
                  Return ans
```

#### Pruned Recursion Tree (Linearized)
```
         F(5)
        /    \
      F(4)    F(3) [O(1) lookup from dp[3] - No deeper branch!]
     /    \
   F(3)   F(2) [O(1) lookup from dp[2]]
  /    \
F(2)   F(1)
```

* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(N)$ (DP Array) + $O(N)$ (Recursion Call Stack)

---

### 4.2 Tabulation (Bottom-Up Approach)

* **Concept:** Eliminate recursion entirely. Construct solutions iteratively from smallest base cases up to target $N$.

#### 3 Steps of Tabulation
1. **Define the Data Structure:** Choose 1D/2D array and assign precise meaning to `dp[i]`.
2. **Initialize Base Cases:** Fill the smallest known answers (e.g., `dp[0] = 0`, `dp[1] = 1`).
3. **Iterate from Small to Big:** Build up the solution using transitions (e.g., loop from `i = 2` to `N`).

```
Index:    0    1    2    3    4    5
dp[]:   [ 0 ][ 1 ][ 1 ][ 2 ][ 3 ][ 5 ]
          ▲    ▲    ▲
      Base Cases    └── dp[2] = dp[1] + dp[0]
```

* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(N)$ (DP Array only, **0 recursion stack overhead**)

---

## 5. Memoization vs. Tabulation Comparison

| Feature | Memoization (Top-Down) | Tabulation (Bottom-Up) |
| :--- | :--- | :--- |
| **Paradigm** | Recursion + Memory | Iteration (Loops) + Table |
| **Direction** | Large problem $\rightarrow$ Small subproblems | Smallest base cases $\rightarrow$ Target state |
| **Intuition** | Natural extension of brute force recursion | Requires visualizing state transitions |
| **Stack Overhead**| Has recursion call stack ($O(N)$) | **No stack overhead** |
| **Risk** | Risk of Stack Overflow for deep recursion | Safe from Stack Overflow |
| **State Evaluation**| Evaluates only **reachable** states | Evaluates all table states systematically |

---

## 6. Core DP Patterns Roadmap

Mastering DP relies on understanding patterns rather than memorizing questions.

```
+───────────────────────────+─────────────────────────────────────────────────────────+
| DP Pattern                | Standard Problems & Variations                          |
+───────────────────────────+─────────────────────────────────────────────────────────+
| 1. 1D DP                  | Fibonacci, Climbing Stairs, House Robber, Frog Jump     |
| 2. 0/1 & Unbounded Knapsack| 0/1 Knapsack, Subset Sum, Equal Partition, Rod Cutting |
| 3. Longest Common Subseq. | LCS, Longest Increasing Subseq (LIS), Edit Distance    |
| 4. Grid DP                | Unique Paths, Min Path Sum, Cherry Pickup               |
| 5. Matrix Chain (MCM)     | Matrix Chain Multiplication, Burst Balloons             |
| 6. Catalan Numbers        | Unique BSTs, Mountain Ranges, Parentheses Combinations  |
+───────────────────────────+─────────────────────────────────────────────────────────+
```

---

## 7. Key Takeaways & Interview Strategy

* **Start with Memoization:** In initial practice (first 10–15 problems), write standard recursion, then add memoization.
* **Shift to Tabulation:** Convert memoized solutions to iterative tabulation to save recursion stack memory and prevent stack overflow in Online Assessments (OAs).
* **Pattern Recognition:** Map new unseen problems to known core templates (1D DP, Knapsack, LCS, Grid, MCM).

---
---

# DP 2. Climbing Stairs | 1D Dynamic Programming
**Source:** [Shradha Khapra - DP 2. Climbing Stairs | 1D Dynamic Programming](https://youtu.be/3GzA0mz6wp0?si=36FyghaEKkxw9ryM)

---

## 1. Problem Statement & Intuition

* **Problem (LeetCode 70):** You are climbing a staircase that has $n$ steps. You are standing at ground level ($0$) and want to reach step $n$.
* **Allowed Moves:** At each step, you can climb either **1 step** or **2 steps**.
* **Objective:** Find the total number of **distinct ways** to reach the top ($n$-th step).

```
                      [ Step n ]  <-- Target Top
                         /   \
            (Take 1 step)     (Take 2 steps)
               /                 \
       [ Step n-1 ]          [ Step n-2 ]
```

---

### 1.1 Base Cases Walkthrough
* **$n = 1$ Stair:**
  * Ways: `(1)` $\rightarrow$ **1 distinct way**
* **$n = 2$ Stairs:**
  * Ways: `(1 + 1)`, `(2)` $\rightarrow$ **2 distinct ways**
* **$n = 3$ Stairs:**
  * Ways: `(1 + 1 + 1)`, `(1 + 2)`, `(2 + 1)` $\rightarrow$ **3 distinct ways**
* **$n = 4$ Stairs:**
  * From Step $0$, take 1 step $\rightarrow$ remaining problem is $n=3$ ($3$ ways)
  * From Step $0$, take 2 steps $\rightarrow$ remaining problem is $n=2$ ($2$ ways)
  * Total ways = $3 + 2 =$ **5 distinct ways** (`1+1+1+1`, `1+1+2`, `1+2+1`, `2+1+1`, `2+2`)

---

## 2. Dynamic Programming Characteristics

```
                             Climbing Stairs
                                    │
           ┌────────────────────────┴────────────────────────┐
           ▼                                                 ▼
1. Overlapping Subproblems                        2. Optimal Substructure
   • F(3), F(2) computed repeatedly                 • Ways(n) = Ways(n-1) + Ways(n-2)
   • Multiple recursive branch choices               • Optimal solution derived from
     (1-step vs 2-step)                                optimal sub-solutions
```

* **Recurrence Relation:**
  $$\text{Ways}(n) = \text{Ways}(n-1) + \text{Ways}(n-2)$$
* **Direct 1D DP Variation:** The mathematical sequence is identical to the **Fibonacci sequence** with shifted base cases ($F(1)=1, F(2)=2$).

---

## 3. Solution Approaches

```
                      Solution Approaches
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
1. Plain Recursion      2. Memoization (Top-Down) 3. Tabulation (Bottom-Up)
   • O(2^N) Time           • O(N) Time              • O(N) Time
   • O(N) Stack Space      • O(N) Auxiliary Space   • O(1) Space (Optimized)
```

---

### 3.1 Approach 1: Plain Recursion (Brute Force)

```
                            F(4)
                          /      \
                      F(3)        F(2)  <-- Repeated Computation
                     /    \      /    \
                  F(2)   F(1)  F(1)   F(0)
                  /  \
                F(1) F(0)
```

* **C++ Code:**
```cpp
int climbStairs(int n) {
    if (n == 1 || n == 2) return n;
    return climbStairs(n - 1) + climbStairs(n - 2);
}
```
* **Time Complexity:** $O(2^N)$ (Exponential)
* **Space Complexity:** $O(N)$ (Recursion stack depth)

---

### 3.2 Approach 2: Memoization (Top-Down DP)

* **Mechanism:** Initialize a lookup table (`vector<int> dp(n + 1, -1)`). Before recurring, check if `dp[n] != -1`.

```
                    Call helper(n, dp)
                            │
                  Is n <= 2? ─── YES ───► Return n
                            │ NO
                Is dp[n] != -1? ─── YES ───► Return dp[n]
                            │ NO
             Compute: dp[n] = helper(n-1) + helper(n-2)
                            │
                       Return dp[n]
```

* **C++ Code:**
```cpp
int helper(int n, vector<int>& dp) {
    if (n == 1 || n == 2) return n;
    if (dp[n] != -1) return dp[n];
    return dp[n] = helper(n - 1, dp) + helper(n - 2, dp);
}

int climbStairs(int n) {
    vector<int> dp(n + 1, -1);
    return helper(n, dp);
}
```
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(N)$ (DP vector) + $O(N)$ (Recursion stack)

---

### 3.3 Approach 3: Tabulation (Bottom-Up DP)

* **3-Step Framework:**
  1. **Define Table & Meaning:** `dp[i]` represents total distinct ways to climb $i$ stairs.
  2. **Initialize Base Values:** `dp[1] = 1`, `dp[2] = 2`.
  3. **Iterate Bottom-Up:** Loop from $i = 3$ to $n$, filling `dp[i] = dp[i-1] + dp[i-2]`.

```
Index (i):    1    2    3    4    5
dp[i]:      [ 1 ][ 2 ][ 3 ][ 5 ][ 8 ]
              ▲    ▲    ▲
          Base Cases    └── dp[3] = dp[2] + dp[1]
```

* **C++ Code:**
```cpp
int climbStairs(int n) {
    if (n == 1 || n == 2) return n;
    vector<int> dp(n + 1);
    dp[1] = 1;
    dp[2] = 2;
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}
```
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(N)$ (No recursion call stack overhead)

---

### 3.4 Approach 4: Space-Optimized Tabulation (Most Optimal)

* **Observation:** To compute `dp[i]`, we only need the immediate two previous states (`dp[i-1]` and `dp[i-2]`). We can replace the whole $O(N)$ array with two variables.

```
       prev2 (n-2)       prev1 (n-1)         result
          [ 1 ]    +        [ 2 ]     --->   [ 3 ]
                     │                  │
         prev2 <─────┘      prev1 <─────┘  (Shift for next iteration)
```

* **C++ Code:**
```cpp
int climbStairs(int n) {
    if (n == 1 || n == 2) return n;
    int prev2 = 1; // Represents n = 1
    int prev1 = 2; // Represents n = 2
    int result = prev1;
    
    for (int i = 3; i <= n; i++) {
        result = prev1 + prev2;
        prev2 = prev1;
        prev1 = result;
    }
    return result;
}
```
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(1)$ (Constant Space)

---

## 4. Complexity & Trade-Off Summary

| Approach | Time Complexity | Space Complexity | Stack Overflow Risk | Recommended For |
| :--- | :--- | :--- | :--- | :--- |
| **Recursion** | $O(2^N)$ | $O(N)$ | High | Conceptual understanding |
| **Memoization** | $O(N)$ | $O(N) + O(N)$ (Stack) | Moderate | Quick prototype from recursion |
| **Tabulation** | $O(N)$ | $O(N)$ | **None** | Online Assessments (OAs) |
| **Space Optimized** | **$O(N)$** | **$O(1)$** | **None** | **Production & Coding Interviews** |