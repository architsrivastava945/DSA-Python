# DSA Completion & Mastery Plan — Placement Track
### 1.5–2 hrs/day · Breadth-first completion · Deep Dynamic Programming
*(Resources verified current as of August 2026)*

---

## 0. How to use this document

This is your single source of truth. Don't re-derive strategy mid-way — when in doubt, come back here. Every stage tells you exactly what to learn, what to solve, when to stop, and what's next. The plan assumes **1 study session = 90–120 minutes = 1 day**, and it deliberately does **not** give you hundreds of problems — except for Dynamic Programming, which gets far more depth than everything else on purpose.

**The one rule that fixes your actual problem:** you don't have a discipline problem, you have a *stopping* problem. You don't know when a topic is "done," so you never leave it. Every stage below ends with an explicit **DONE when** checklist. The moment it's true, you move on — even if it feels uncomfortable.

---

## 1. Resource Stack (evaluated, not assumed)

You asked us to evaluate Striver's A2Z Sheet objectively rather than default to it. Verdict, checked against the live resource in 2026:

- **Striver's A2Z DSA Sheet** (hosted on takeuforward.org, ~450 problems across 18 sections, free, with written + video explanations) is still active, well-maintained, and remains one of the most trusted structured DSA resources for Indian placement prep.
- However, **450 problems is too many for your constraint and your goal.** Following it "almost completely" (Option 1) would blow past 1.5–2 hrs/day for months. Using a totally different curriculum (Option 3) would throw away a genuinely good, free, well-explained resource for no reason.

**Decision: Option 2 — use Striver A2Z as the primary *learning* source, but selectively skip and reorder sections.** We use it for concept explanations topic-by-topic, but we curate our own (much smaller) problem set per topic, and we reorder Dynamic Programming to appear earlier than Striver's own sequence (reasoning in Part 4).

| Role | Resource | Why |
|---|---|---|
| **Primary learning source** | Striver's A2Z Sheet (takeuforward.org) | Free, structured, explanations per topic, still active and maintained in 2026 |
| **Primary practice source** | LeetCode | You already use it; best interview-realistic problem format, discussions, and premium company-tag filtering if you upgrade later |
| **Backup explanation source** | NeetCode (YouTube + neetcode.io roadmap) | Use *only* when Striver's explanation doesn't click. Strong, currently-active resource, especially good for alternate DP intuition |
| **DP-specific primary source** | Striver's dedicated DP series | It literally follows the recursion → memoization → tabulation → space-optimization progression you asked for — this is not a coincidence, it's why we pick it |
| **DP-specific backup** | NeetCode DP playlist | Different explanation style when Striver's doesn't land for a specific pattern |

No third practice platform, no course purchases, no resource-hopping. This is the whole stack.

---

## 2. Complete DSA Map & Tiering

| Tier | Topics | Why |
|---|---|---|
| **Tier 1 — MUST KNOW** | Arrays, Strings, Hashing, Two Pointers, Sliding Window, Recursion, Binary Search, Linked Lists, Stack/Queue, Backtracking, Trees, BST, Graph traversal (BFS/DFS), **Dynamic Programming (deep)** | Appear in nearly every assessment/interview at every company tier |
| **Tier 2 — SHOULD KNOW** | Sorting (conceptual), Prefix/Suffix, Monotonic Stack/Queue, Heaps, Greedy, Intervals, Bit Manipulation, Topological Sort, Union-Find | Common at general placement rounds and product companies; less universal than Tier 1 |
| **Tier 3 — GOOD TO KNOW** | Tries, Dijkstra's shortest path, Kruskal's MST, Tree-DP, Graph-DP | Shows up more at product companies and stronger interviews; postponable without risk for service-based/general rounds |
| **Tier 4 — OPTIONAL / DEFER** | Segment Trees/Fenwick Trees, advanced string algorithms (KMP, Z-function, Manacher's, suffix structures), Bellman-Ford, Floyd-Warshall, full Prim's, Tarjan's (bridges/SCCs), Bitmask DP, AVL/Red-Black tree internals | Low ROI for fresher placements; genuinely revisit only if targeting top-tier product companies |

**Dynamic Programming is the one deliberate exception: Tier 1 + deep mastery required**, not the standard "learn → solve a few → move on" treatment given to every other topic.

---

## 3. Dependency-Based Order — and why we break convention

The obvious order (`Arrays → Linked List → Stack → Queue → Trees → Graphs → DP`) is what everyone defaults to, and it's part of why DP gets permanently postponed — it sits at the very end, energy and time run out, and it never gets the depth it needs.

We also don't blindly follow the example ordering `Recursion → Backtracking → Trees/Graphs → Dynamic Programming`. Here's the actual dependency reasoning:

- **DP's real prerequisite is Recursion + Backtracking, not Trees/Graphs.** Backtracking *is* recursion where you explicitly try a choice, recurse, and undo it. DP reuses that exact choice-tree mental model and adds caching. Most interview DP — knapsack, subsequence, string DP, grid DP — needs zero tree/graph knowledge. Only the *advanced* variants (Tree-DP, Graph-DP) need Trees/Graphs, and those are Tier 3.
- **So we place DP's core block immediately after Backtracking — roughly mid-roadmap — not last.** This does three things: it protects DP from the "ran out of time" failure mode, it keeps the choice-tree intuition fresh from Backtracking, and it leaves 5–6 more weeks of "the rest of DSA" during which we schedule spaced DP revision so the knowledge doesn't decay before Phase 2.
- **A short DP capstone returns at the very end of Phase 1**, once Trees and Graphs exist, to cover Tree-DP/Graph-DP lightly and do final unfamiliar-problem consolidation.

Final order: **Arrays/Strings review → Hashing → Recursion → Prefix/Sorting/Binary Search → Bit Manipulation → Linked Lists → Stack/Queue/Monotonic → Backtracking → DYNAMIC PROGRAMMING (core) → Trees/BST → Heaps → Greedy/Intervals → Graphs → Tries → DP Capstone.**

---

## 4. The Fast Completion Plan — Stage by Stage

Each stage below is one unit. 66 total sessions in Phase 1 (roughly 115 hours of study). Timeline math is in the Final Assessment.

### Stage 1 — Arrays, Strings, Two Pointers, Sliding Window *(consolidation)*
**Tier 1 · 3 sessions**
- **Learn:** Not from zero — you're comfortable here. This stage is about *naming* the patterns explicitly (opposite-end two pointers, same-direction two pointers, fixed vs. variable sliding window) and closing 2–3 real gaps.
- **Implement:** the two-pointer template and the variable-sliding-window (expand/contract) template, generalized.
- **Solve (6, must-do):** Two Sum II, 3Sum, Longest Substring Without Repeating Characters, Minimum Window Substring, Container With Most Water, Longest Repeating Character Replacement.
- **DONE when:** you can write both templates from memory in under 2 minutes, and classify a new problem as pointer- vs. window-shaped within 30 seconds.
- **Skip:** re-solving easy array problems you already know. **Don't waste time on:** re-deriving basic traversal complexity.

### Stage 2 — Hashing
**Tier 1 · 3 sessions**
- **Learn:** why hashing turns O(n²) lookups into O(1); collisions/load-factor at a conceptual level only.
- **Implement:** build a frequency counter once by hand (to understand it), then always use `dict`/`Counter` afterward.
- **Solve (6):** Two Sum, Group Anagrams, Top K Frequent Elements, Longest Consecutive Sequence, Subarray Sum Equals K *(prefix-sum + hashmap — an important bridge pattern)*, Valid Sudoku.
- **DONE when:** "count," "seen before," "pair summing to," or "frequency" instantly triggers a hashmap/set reflex.
- **Skip:** implementing a hash table from scratch.

### Stage 3 — Recursion Foundations
**Tier 1 · 4 sessions — critical, everything downstream depends on this**
- **Learn:** define what `f(...)` *means*, in one sentence, before writing any code. Identify the base case. Identify how the problem shrinks. Visualize the recursion tree.
- **Implement:** recursive string/list reversal, factorial/power, subsets of a set (doubles as a Backtracking primer), plain-recursive Fibonacci *(deliberately — it becomes the DP demo later)*.
- **Solve (5):** Reverse Linked List (recursive), Pow(x, n), Subsets (basic), Generate Parentheses, Merge Two Sorted Lists (recursive).
- **DONE when:** for any new recursive problem you can state "`f(...)` means ___" before touching the keyboard, and sketch the recursion tree for a small input on paper.
- **Don't waste time on:** forcing recursion where a simple loop is clearly simpler.

### Stage 4 — Prefix/Suffix, Sorting, Binary Search
**Tier 1/2 · 4 sessions**
- **Learn:** prefix/suffix sums and prefix XOR; sorting — know complexity/stability of common sorts *conceptually*, don't hand-implement them; binary search generalizes from "find a value" to "find the smallest/largest value satisfying a monotonic condition" — this is the single highest-value binary-search idea for interviews.
- **Implement:** standard binary search (careful bounds), a binary-search-on-answer template.
- **Solve (6):** Search in Rotated Sorted Array, Find Minimum in Rotated Sorted Array, Koko Eating Bananas, Capacity To Ship Packages Within D Days, Product of Array Except Self, Kth Largest Element in an Array (sorting application).
- **DONE when:** you recognize "binary search on answer" from a monotonic-feasibility structure, not just from "the array is sorted."
- **Skip:** hand-implementing quicksort/mergesort/heapsort — know their complexity and stability, nothing more, unless a specific interview explicitly asks.

### Stage 5 — Bit Manipulation
**Tier 2 · 2 sessions**
- **Learn:** these are ~8 canonical tricks you learn directly, not derive: AND/OR/XOR/shifts, set/check/clear a bit, XOR-for-uniqueness, power-of-two checks.
- **Solve (4):** Single Number, Number of 1 Bits, Counting Bits, Missing Number.
- **DONE when:** "find the unique/missing element in O(1) space" reflexively suggests XOR.
- **Skip:** bitmask DP and advanced bit tricks — deliberately deferred (Part 14).

### Stage 6 — Linked Lists
**Tier 1 · 4 sessions**
- **Learn:** dummy-node technique for edge cases; fast/slow pointers for cycle detection and midpoint-finding in O(1) space.
- **Implement:** reverse a linked list both iteratively and recursively (ties back to Stage 3), cycle detection, find the middle node.
- **Solve (6):** Reverse Linked List, Linked List Cycle, Middle of the Linked List, Remove Nth Node From End of List, Merge Two Sorted Lists, Reorder List.
- **DONE when:** dummy-node and fast/slow-pointer templates come out automatically.
- **Skip:** full doubly-linked-list API implementation, skip lists, XOR linked lists.

### Stage 7 — Stack, Queue, Monotonic Stack/Queue
**Tier 1/2 · 3 sessions**
- **Learn:** stacks for matching/undo/iterative-DFS, queues for BFS, monotonic stack for "next greater/smaller element" (turns an O(n²) brute force into O(n)), monotonic deque for sliding-window max/min.
- **Implement:** the monotonic-stack template (push while maintaining order, pop-and-resolve).
- **Solve (5):** Valid Parentheses, Min Stack, Daily Temperatures, Next Greater Element I, Sliding Window Maximum.
- **DONE when:** "next greater/smaller" or "span"-flavored problems trigger monotonic stack instinctively.

### Stage 8 — Backtracking
**Tier 1 · 3 sessions**
- **Learn:** the choose → explore → un-choose template, pruning. This is the exact mental model DP reuses next — choice-based recursion, minus the undo, plus caching.
- **Solve (5):** Subsets, Permutations, Combination Sum, Word Search, N-Queens.
- **DONE when:** you can write the choose-explore-unchoose skeleton for a brand-new problem in under 3 minutes.

---

### Stage 9 — DYNAMIC PROGRAMMING (Core Block)
**Tier 1 + DEEP MASTERY · ~19 sessions, ~33 hrs — the one stage where we deliberately abandon the "small problem set" rule**

This is the payoff stage. Every sub-stage below states what concept it teaches, what state/transition it demonstrates, and why it's included.

#### 9a. Foundations: Recursion → DP *(3 sessions)*
Overlapping subproblems, optimal substructure, top-down (memo) vs. bottom-up (tabulation), why both give identical answers, iteration order, space optimization via rolling variables.

**Do this once, on paper and in code — solve one trivial problem four ways.** This transformation, not the problem, is what you're learning:

```python
def climb(n):
    if n <= 2: return n
    return climb(n-1) + climb(n-2)

def climb(n, memo={}):
    if n <= 2: return n
    if n in memo: return memo[n]
    memo[n] = climb(n-1, memo) + climb(n-2, memo)
    return memo[n]

def climb(n):
    if n <= 2: return n
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def climb(n):
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a+b
    return b
```

- **Solve (4, must-do, all easy — purely for the 4-way transformation):** Climbing Stairs, Fibonacci Number, Min Cost Climbing Stairs, N-th Tribonacci Number.
- **DONE when:** you can produce all four versions of any of these from scratch, no lookup.

#### 9b. Take/Not-Take Framework + House Robber Family *(2 sessions)*
**State:** `dp[i]` = best answer considering the first `i` elements. **Concept:** at each step, either take this element or skip it — underlies roughly half of interview DP.
- **Solve (2 must-do, 1 optional):** House Robber (must), House Robber II — circular constraint, forces you to reason about *why* the constraint changes the recurrence (must), Delete and Earn (optional).
- **Prerequisite:** 9a. **DONE when:** given a new 1D array problem with an exclusion/adjacency constraint, you write the recurrence within 5 minutes.

#### 9c. Grid DP *(2 sessions)*
**State:** `dp[i][j]` = best answer to reach cell `(i, j)`. **Concept:** 2D state where transitions come from "which neighbor(s) could I have arrived from."
- **Solve (2 must-do, 1 optional):** Unique Paths (must), Minimum Path Sum (must), Unique Paths II — obstacles (optional).
- **Prerequisite:** 9b. **DONE when:** you can set up the table and transition for any grid-path problem, boundaries included.

#### 9d. Knapsack Family *(4 sessions — highest interview-frequency DP family)*
**State:** `dp[i][capacity]` (space-optimize to `dp[capacity]`). **Concept:** 0/1 knapsack (item used once) vs. unbounded knapsack (item reusable) vs. subset-sum (existence, not optimization) are the *same* transition shape with small changes to reuse rule and iteration direction.
- **Solve, all must-do:** Partition Equal Subset Sum (subset-sum shape), Coin Change (unbounded, minimize), Coin Change II (unbounded, count ways), Target Sum (0/1 knapsack in disguise — derive the transformation yourself before checking a solution).
- **Prerequisite:** 9c. **DONE when:** for any new problem you can decide within 2 minutes whether it's 0/1, unbounded, or subset-sum shaped, and explain why the iteration order differs between 0/1 and unbounded.

#### 9e. Subsequence DP *(3 sessions)*
**State:** LIS teaches "state = sequence ending at index i"; LCS teaches "state = (i, j) across two sequences." **Concept:** the two dominant subsequence-state shapes.
- **Solve (2 must-do, 1 optional):** Longest Increasing Subsequence — O(n²) first; know the O(n log n) binary-search variant exists, don't force-derive it yet (must), Longest Common Subsequence (must), Longest Palindromic Subsequence (optional).
- **Prerequisite:** 9d. **DONE when:** you instantly separate "one sequence, state=index" from "two sequences, state=(i,j)" problems.

#### 9f. String DP *(3 sessions)*
**Concept:** usually reuses LCS's (i,j)-over-two-strings shape, or interval DP's (i,j)-as-a-substring-range shape.
- **Solve (2 must-do, 1 optional):** Edit Distance (must), Longest Palindromic Substring — solve with DP for the state-design reps, know expand-around-center exists as the O(1)-space alternative (must), Distinct Subsequences (optional, harder).
- **Prerequisite:** 9e. **DONE when:** you write `dp[i][j]`'s meaning in one precise sentence before touching transitions.

#### 9g. Multi-State DP *(2 sessions)*
**Concept:** sometimes one dimension isn't enough — state needs an extra flag/dimension (holding stock or not, transactions used so far).
- **Solve, must-do:** Best Time to Buy and Sell Stock II, Best Time to Buy and Sell Stock with Cooldown — derive the extra state dimension yourself before checking a solution.
- **Prerequisite:** 9f. **DONE when:** you recognize when a plain 1D/2D state is insufficient and can name the extra dimension a new problem needs.

**DP Core exit checklist — do not proceed to Stage 10 until every box is true:**
- [ ] Can produce recursion / memo / tabulation / space-optimized versions of a Climbing-Stairs-tier problem from scratch
- [ ] Can classify a new problem as take/not-take, knapsack, subsequence, or string-DP shaped within ~2 minutes
- [ ] Can write a precise one-sentence state definition before writing any code
- [ ] Has solved at least 20 of the problems above independently — not recalled from a video
- [ ] Can explain out loud why memoization and tabulation produce identical answers

---

### Stage 10 — Trees + BST
**Tier 1 · 6 sessions**
- **Learn:** almost every tree problem reduces to "define what the function returns for a subtree, then combine the children's answers."
- **Implement:** all four traversals (recursive + BFS level-order), height, validate BST.
- **Solve (7):** Maximum Depth of Binary Tree, Invert Binary Tree, Diameter of Binary Tree, Validate Binary Search Tree, Lowest Common Ancestor of a Binary Search Tree, Binary Tree Level Order Traversal, Kth Smallest Element in a BST.
- **DONE when:** you write "return value represents ___" before coding, and traversal code no longer needs lookup.
- **Skip:** AVL/Red-Black rotations, splay trees.
- *(Start spaced DP revision from here — see Part 9.)*

### Stage 11 — Heaps / Priority Queues
**Tier 2 · 2 sessions**
- **Learn:** the heap property; `heapq` is min-heap only, negate values for a max-heap; top-K and merge-K patterns.
- **Solve (3 must-do, 1 optional):** Kth Largest Element in an Array, Top K Frequent Elements (revisit via heap), Merge k Sorted Lists, Find Median from Data Stream (optional, two-heaps pattern).
- **DONE when:** "top-K"/"kth largest" triggers heap instinctively, and you know when it beats plain sorting (streaming data).

### Stage 12 — Greedy + Intervals
**Tier 2 · 3 sessions**
- **Learn:** informal exchange-argument intuition (one sentence — not a formal proof) for why a greedy choice is safe; interval merging/scheduling.
- **Solve (4):** Merge Intervals, Non-overlapping Intervals, Jump Game, Meeting Rooms II.
- **DONE when:** you can informally justify why a greedy choice works for a new problem — one sentence is enough at this level.

### Stage 13 — Graphs
**Tier 1 core (BFS/DFS) + Tier 2/3 extensions · 6 sessions**
- **Learn:** graphs are trees without the "no cycle, one parent" guarantee — BFS/DFS templates barely change from Stage 10.
- **Implement:** BFS, DFS, topological sort (Kahn's), Union-Find with union-by-rank + path compression.
- **Solve (6 must-do, 1 optional):** Number of Islands, Clone Graph, Course Schedule, Course Schedule II, Number of Provinces (Union-Find), Network Delay Time (Dijkstra — the *one* shortest-path problem you need), Redundant Connection (optional).
- **DONE when:** you classify a new graph problem as traversal / cycle-ordering / connectivity / shortest-path within a minute, and pick the right tool (BFS, DFS, Union-Find, Dijkstra) correctly.
- **Skip:** Bellman-Ford, Floyd-Warshall, full Prim's, Tarjan's — see Part 14.

### Stage 14 — Tries
**Tier 3 · 1 session**
- **Solve:** Implement Trie (Prefix Tree) — genuinely enough at this tier.
- **DONE when:** you can explain what a trie is for (prefix search, autocomplete) and re-derive the node structure even without memorizing it.

### Stage 15 — DP Capstone: Tree-DP, Graph-DP, Unfamiliar Consolidation
**Tier 1 core / Tier 3 extension · 3 sessions**
- **Learn:** now that Trees/Graphs exist, DP extends onto them — state defined per tree node (post-order combine) or per DAG node (topological order).
- **Solve (must-do):** House Robber III — tree-DP, a direct extension of 9b's take/not-take idea. **(Optional, Tier 3):** Longest Increasing Path in a Matrix — graph-DP/DFS+memo hybrid.
- **Then:** pick 3 problems at random from 9b–9g *without re-reading your notes* and solve them cold, timed, to confirm retention.
- **DONE when:** House Robber III falls in under 15 minutes, and the 3 cold-retention problems are solved without re-deriving from scratch.

**Phase 1 formally ends here.**

---

## 5. Daily Session Structure (90–120 minutes)

There is no fixed split for every topic — new/hard topics need more learning time, familiar patterns need almost none.

| Topic type | Learn | Implement/Setup | Solve | Review mistakes |
|---|---|---|---|---|
| Familiar/comfortable (Stage 1, revision passes) | 5–10 min | — | 60–80 min | 10–15 min |
| Moderately new (Hashing, Linked List, Stack) | 15–20 min | 10–15 min | 50–60 min | 15 min |
| Genuinely new & foundational (Recursion, Trees, Graphs) | 25–35 min | 15–20 min | 40–50 min | 15–20 min |
| DP (9a–9c, learning-heavy) | 30–40 min | 15–20 min | 30–40 min | 15–20 min |
| DP (9d–9g, once the mental model exists) | 10–15 min | — | 60–75 min | 15–20 min |

**DP's daily structure evolves deliberately:** in 9a–9c you spend nearly half the session just *understanding* state/transition design, because that thinking process is the actual skill. By 9d–9g, learning time shrinks and independent problem-solving time grows — you're now applying a mental model, not building one. If by 9d you still need 30+ minutes of "learning" per session, that's a signal to slow down in 9a–9c territory, not push forward.

---

## 6. Exact Completion Criteria — Recap

Every stage above already states its **DONE when** — that *is* Part 7. Two things worth repeating:

1. **The moment DONE-when is true, stop practicing that topic and move on** — even if you feel you could solve "just a few more." That feeling is the exact failure mode this plan exists to prevent.
2. **DP's completion bar is categorically different** and lives in the Stage 9 exit checklist plus Stage 15's capstone criteria — both must be true before you consider DP "complete" for Phase 1 purposes. (Full ability continues developing in Phase 2 — DP is never really "finished," but it moves from foundation-building to refinement.)

---

## 7. Handling Getting Stuck

| Situation | Rule |
|---|---|
| Any problem, first attempt | Work actively for **20–25 minutes** before any outside help. |
| Still stuck after 25 min | Read only the problem's constraints/hints (not a solution) for 5 min, retry for 10 min. |
| Still stuck | Read the editorial or watch a solution — but stop the moment you understand the *approach*, before seeing full code. Close it, then implement independently. |
| After watching any solution | Re-implement it fully from scratch, same day or next day, with nothing open. |
| 3–4 days later | Revisit that same problem cold, no notes, to check real retention. |
| More than 2 "needed the editorial" problems in one session | That's a signal, not bad luck — pause forward progress and consolidate instead of pushing to a 3rd. |

**For DP specifically, diagnose which failure you actually had — they need opposite fixes:**
- **"I couldn't derive the state/transition"** → this is the real DP skill gap. Fix it with *more deliberate derivation practice on paper before coding* — write the state definition and recurrence in words first — not more coding reps.
- **"I derived it fine but couldn't implement it (off-by-one, base-case bug)"** → this is a normal implementation gap, fixed by more coding reps, not more theory.

Conflating these two is exactly how people "practice DP" for months without actually getting better at it.

---

## 8. Revision Strategy

**During normal DSA progression:** revision stays lightweight and never blocks forward motion. Before starting a new stage, spend 5–10 minutes mentally recalling the previous stage's core template — no more. Don't restart a completed topic from scratch.

**DP is the deliberate exception, because DP knowledge decays fastest without reuse.** Once Stage 9 ends and you move into Stages 10–14 (Trees, Heaps, Greedy, Graphs, Tries), insert **one DP problem, pulled cold from Stages 9b–9g, every 3–4 sessions** — timed, no notes. This is not new DP learning; it's retention maintenance, and it's exactly what makes Stage 15's capstone land quickly instead of feeling like starting over.

---

## 9. Phase 2 — After First-Pass Completion

Begin immediately after Stage 15 — don't wait, waiting erodes exactly the freshness Phase 1 built. Structure:

- **Mixed-topic problem sets**, not single-topic grinding — the entire point is pattern recognition without a topic label attached.
- **Timed solving** — simulate assessment/interview time pressure (25–35 min/medium problem).
- **Weak-topic identification loop** — track which patterns you miss under time pressure; route the next few sessions there instead of wherever's comfortable.
- **Mock interviews** — explaining your approach out loud before coding, since that's graded separately from correctness at product companies.
- **DP-specific in Phase 2:** mixed DP problems with the pattern deliberately unlabeled, unfamiliar state-design problems, comparing 2–3 candidate states/transitions before committing to one, and revisiting old DP problems without solutions open.

Run Phase 2 for a minimum of 3–4 weeks before assessments begin, and continue it in parallel with your actual interview cycle for as long as you're applying.

---

## 10. Placement-Track-Specific Guidance

| Track | What matters most | What's usually sufficient | What to postpone |
|---|---|---|---|
| **Service-based companies** | Aptitude + basic-to-medium DSA; CS fundamentals (DBMS/OOP) matter as much as DSA | Tier 1 + light Tier 2 | Graphs beyond BFS/DFS, deep DP rarely tested here specifically |
| **General campus placement rounds** | Speed under time pressure on 2–3 medium problems | Arrays/Hashing/Two-Pointer/Sliding-Window/basic DP/basic Graph cover most of what appears | Tier 3/4 entirely |
| **Startups** | Highly variable — often blends practical coding with DSA | Similar bar to general placement rounds | Formal algorithm depth beyond Tier 2 |
| **Product companies (mid-tier)** | Full Tier 1 + most Tier 2; explaining your approach starts to matter as much as passing tests | This plan's Phase 1, as designed | Most of Tier 4 |
| **Strong/top product companies** | DP depth becomes a real differentiator; optimal complexity expected, not just a working solution | This plan's Phase 1 + extended Phase 2 | Selectively revisit deferred Tier 3/4 items relevant to the specific company |

---

## 11. Pattern Recognition Playbook

| Cue | Technique |
|---|---|
| Contiguous subarray + condition | Sliding Window |
| Sorted array + pair relationship | Two Pointers |
| Frequency/counting | Hashing |
| Repeated min/max extraction | Heap |
| Hierarchy | Tree traversal |
| Prerequisites/dependencies | Topological Sort |
| Shortest path | BFS (unweighted) / Dijkstra (weighted) |
| Overlapping subproblems | Dynamic Programming |
| Intervals | Sort + Greedy merge |
| Next greater/smaller | Monotonic Stack |
| Monotonic search condition ("smallest X such that...") | Binary Search on Answer |
| Choose/take/not-take over a sequence | 1D or Knapsack-family DP |
| Optimization over many possible states | DP |

**Going deeper for DP — the actual thought process, in order, every time:**

1. **What is changing** as the problem progresses (an index? remaining capacity? position on a grid?)
2. **What decisions am I making** at each step?
3. **What information from the past actually affects the future** — this becomes your state.
4. **What should the state represent**, in one precise sentence?
5. **What are my choices** at each state?
6. **What is the transition** — how does one state's answer come from smaller states' answers?
7. **What are the base cases?**
8. **What is the answer state** — which `dp[...]` do I actually return?
9. **Can I reduce the dimensions** — does the transition only need the last 1–2 rows/values, enabling space optimization?
10. **Does this match a known family** (take/not-take, knapsack, subsequence, string-DP, interval)?

This sequence, asked explicitly every time, is what replaces memorizing solutions with actually being able to solve unfamiliar DP problems.

---

## 12. Python for DSA — What You Actually Need

- **list:** index O(1), append O(1) amortized, insert/delete at front O(n), `in` check O(n) — use a set/dict instead if you need O(1) membership.
- **dict/set:** O(1) average insert/lookup/delete — your default tool for frequency and membership.
- **collections.deque:** O(1) append/pop from both ends — use for BFS queues and monotonic-deque patterns. Never use `list.pop(0)` as a queue — that's O(n).
- **heapq:** min-heap only. For a max-heap, negate values on push and pop. `heapify` is O(n); push/pop are O(log n).
- **sorting:** `sorted()`/`list.sort()` are O(n log n), stable. Use `key=` for custom sort; `functools.cmp_to_key` is rarely needed.
- **tuples:** immutable and hashable — use as dict keys or set members (e.g., `visited = set()` of `(row, col)` tuples in grid BFS/DFS).
- **strings:** immutable — repeated concatenation in a loop is O(n²); build with a list and `''.join()` instead.
- **recursion:** Python's default recursion limit (~1000) can bite on deep recursion (skewed trees, long chains). Know `sys.setrecursionlimit` exists; know some deep-recursion problems are cleaner solved iteratively.
- **Handy built-ins:** `enumerate`, `zip`, `itertools.accumulate` (one-line prefix sums), `collections.defaultdict`, `collections.Counter`, `functools.lru_cache` — a real shortcut for memoization, but use it *after* you've hand-written memo dicts a few times, not as a first crutch.

That's the full list. Nothing here should turn into a Python side-quest.

---

## 13. Ignore This For Now

- Segment Trees / Fenwick Trees (BIT)
- Advanced string algorithms: KMP, Z-function, Manacher's, suffix arrays/automaton, Aho-Corasick
- Bellman-Ford, Floyd-Warshall, full Prim's implementation (Kruskal + Dijkstra alone are enough)
- Tarjan's algorithm (articulation points/bridges/SCCs)
- AVL/Red-Black/Splay tree implementation internals
- Bitmask DP *(deferred, not dismissed — revisit only if targeting top-tier product companies later)*
- Advanced number theory/combinatorics (modular exponentiation, matrix exponentiation)
- Computational geometry
- Formal greedy-correctness proofs — one-sentence informal justification is enough at this level

Nothing DP-related is on this list simply for being hard — everything DP-related that matters for placements is inside Stage 9 and Stage 15.

---

## 14. Why People Never Finish DSA — and the Rules That Stop It

| Failure mode | Why it happens | The rule that stops it |
|---|---|---|
| Repeatedly restarting Arrays | It's the most comfortable topic, so it's where people retreat when a new topic feels hard | Stage 1 is capped at 3 sessions with an explicit DONE-when — no re-entry after that |
| Endless LeetCode grinding | No defined stopping point per topic | Every stage has a DONE-when; hitting it means stop, by design |
| Resource hopping | Believing the *next* resource will finally make it click | The 3-resource stack in Part 1 is fixed — the Section 7 "stuck" rules handle the actual problem, not a new course |
| Solving too many similar questions | Confusing repetition with learning | Fixed, small problem counts per stage (except DP, which gets depth *deliberately*, not accidentally) |
| Spending hours on one problem | No time-boxing | The 20–25 minute rule in Part 7, with a hard editorial fallback |
| Avoiding uncomfortable topics | Comfort topics feel like progress | The stage *order* forces Recursion, Linked Lists, Trees, Graphs, and DP on a fixed schedule — not "whenever you feel ready" |
| Postponing Trees/Graphs/DP indefinitely | They're the least familiar and most intimidating | DP is moved *earlier* (Stage 9, not last) specifically to prevent this; Trees/Graphs have fixed slots too |
| Confusing familiarity with mastery | "I've seen this pattern before" ≠ "I can derive it independently" | DONE-when criteria test independent derivation, not recognition |
| Confusing problem count with learning | More problems solved *feels* like more progress | Every stage's problem count is fixed and small (DP excluded) — the ceiling is the point |
| Trying to master everything before moving forward | Perfectionism disguised as thoroughness | "Move on" is stated explicitly at the end of every stage as a required action, not a suggestion |

---

## 15. Master Execution Sheet

| Question | Answer |
|---|---|
| **What do we study?** | The 15-stage map in Part 4 |
| **In what order?** | Arrays review → Hashing → Recursion → Prefix/Sort/Binary Search → Bit Manip → Linked Lists → Stack/Queue → Backtracking → **DP Core** → Trees/BST → Heaps → Greedy/Intervals → Graphs → Tries → **DP Capstone** |
| **How long per stage?** | 1–19 sessions depending on stage (see Part 4 headers); 66 sessions total for Phase 1 |
| **How much per day?** | 90–120 minutes, 1 session, 5–6 sessions/week |
| **What resource?** | Striver A2Z (learn) + LeetCode (practice) + NeetCode (backup/DP intuition) |
| **Which problems?** | The curated lists inside each stage in Part 4 — nothing beyond them required for Phase 1 |
| **When are we done with a topic?** | The stage's own DONE-when criteria, no exceptions |
| **When do we move on?** | Immediately once DONE-when is true |
| **What do we postpone?** | The Part 13 ignore list |
| **How do we handle getting stuck?** | The timers and rules in Part 7 |
| **When does Phase 1 end?** | After Stage 15's capstone — roughly 11–15 weeks in |
| **What does Phase 2 look like?** | Mixed, timed, weak-area-driven practice + mocks (Part 9) |
| **How is DP treated differently?** | ~19 sessions of core depth + spaced revision through Stages 10–14 + a dedicated capstone — roughly 5–6x the investment any other single topic gets |
| **Exact standard before DP is "complete"?** | The Stage 9 exit checklist AND Stage 15's capstone criteria, both true |

---

## 16. Final Honest Assessment

1. **Realistic first-pass timeline:** 66 sessions total. At 6 sessions/week (aggressive but doable), **~11 weeks (~2.5 months)**. At 5 sessions/week with built-in buffer for real life, **~14–15 weeks (~3.5 months)** — this is the **default we'd actually recommend**, because a plan that survives contact with a bad week beats a faster plan that collapses at the first missed day.
2. **How much of DSA this covers at 1.5–2 hrs/day:** essentially all of Tier 1, most of Tier 2, and selected Tier 3 — roughly 90–110 curated problems total (vs. Striver's own ~450). This is by design: full conceptual coverage, not exhaustive problem-count coverage.
3. **Level you can expect to reach:** solid fresher-to-mid interview readiness — comfortable with the large majority of typical placement-round and product-company-medium questions, with DP specifically at a genuinely strong level relative to most fresher peers, who never get this systematic about it.
4. **What will still be weak:** the hardest, rarest DP patterns; graph algorithms beyond BFS/DFS/Dijkstra/Kruskal; advanced string algorithms; segment trees/Fenwick trees. All deliberately deferred, not accidentally missed.
5. **How much deeper DP makes the roadmap:** DP core alone (Stage 9) is roughly 4–6x the session count of any other single topic, and together with the capstone it's close to 30% of total Phase 1 time — an intentional, large investment.
6. **When to begin mixed practice:** immediately after Stage 15, not later — this is stated explicitly to prevent the exact "keep polishing, never transition" pattern that stalls people.
7. **Is this sufficient for fresher placement prep?** Yes — comfortably sufficient for service-based companies, general campus rounds, startups, and most product-company fresher rounds.
8. **What changes for top-tier product companies:** extend Phase 2 substantially (more timed mocks, harder mixed sets, explaining approach out loud), and selectively revisit specific Tier 3/4 items from Part 13 based on the target company's known interview style — plus push DP practice into genuinely unfamiliar, harder territory beyond this plan's core set.
