# Comprehensive Lecture Notes: Hashing in Data Structures & Cryptography
**Source:** [Coder Army - Hashing in Data Structure | Zero To Advance Level](https://www.youtube.com/watch?v=TLk7_Ia3rzQ)

---

## 1. Introduction: Why Do We Need Hashing?

### 1.1 Search Time Complexity Across Data Structures
To appreciate hashing, consider the time required to search for an element across standard data structures:

| Data Structure | Unsorted Search | Sorted Search / Best Search |
| :--- | :--- | :--- |
| **Array** | $O(N)$ | $O(\log N)$ (Binary Search) |
| **Linked List** | $O(N)$ | $O(N)$ |
| **Stack / Queue** | $O(N)$ | $O(N)$ |
| **Binary Tree** | $O(N)$ | $O(N)$ |
| **Binary Search Tree (BST)** | $O(N)$ (Skewed / Worst) | $O(\log N)$ (Average) |
| **AVL Tree / Balanced BST** | $O(\log N)$ | $O(\log N)$ |
| **Hash Table (`unordered_map`)** | **$O(1)$ (Average)** | **$O(1)$ (Average)** |

* **Core Goal of Hashing:** Achieve **$O(1)$ average time complexity** for `Insert`, `Delete`, and `Search` operations.

```
  Data Input (Key)  --->  [ Hash Function ]  --->  Index/Bucket  --->  Direct Memory Access O(1)
```

---

## 2. Fundamentals of Hashing

### 2.1 What is a Hash Function?
A mathematical formula that maps an input key (number, string, object) to a fixed range of indices in a hash table.

```
               +-----------------+
  Key (k) ---> |  h(k) = k mod N | ---> Hash Table Index (0 to N-1)
               +-----------------+
```

### 2.2 Two-Step Mapping Process
When dealing with non-integer keys (like strings, custom objects):

```
+-----------+       +---------------+       +------------------+       +------------------+
| Input Key |  -->  |   Hash Code   |  -->  |   Compression    |  -->  | Table Index (0-9)|
| ("Rohit") |       | (Integer / ID)|       |   Function       |       |                  |
+-----------+       +---------------+       +------------------+       +------------------+
                            |                        |
                 (e.g., ASCII summation)       (e.g., Index % N)
```

1. **Hash Code Generation:** Converts arbitrary data types (strings/objects) into an integer representation (e.g., using ASCII values).
2. **Compression Function:** Maps that potentially huge integer into the valid index bounds $[0, N-1]$ using modulo operations (e.g., $\text{Index} = \text{HashCode} \pmod{\text{TableSize}}$).

---

## 3. Hash Collisions & Resolution Strategies

* **Collision Definition:** When two distinct keys produce the exact same index in the hash table ($h(k_1) = h(k_2)$ where $k_1 \neq k_2$).

```
  Key 47  ---> [ mod 10 ] ---> Index 7 \
                                         ---> COLLISION! (Both compete for Index 7)
  Key 97  ---> [ mod 10 ] ---> Index 7 /
```

---

### 3.1 Separate Chaining (Open Hashing)

* **Mechanism:** Each bucket in the table holds a head pointer to a Linked List. Colliding elements are appended/prepended as new nodes in that chain.

```
Index      Hash Table
  0   ---> NULL
  1   ---> NULL
  2   ---> [ 82 ] -> NULL
  3   ---> [ 73 ] -> [ 53 ] -> [ 23 ] -> NULL
  4   ---> NULL
  5   ---> [ 95 ] -> [ 25 ] -> NULL
  6   ---> NULL
  7   ---> [ 97 ] -> [ 47 ] -> NULL
  8   ---> [ 58 ] -> NULL
  9   ---> NULL
```

* **Complexity:**
  * **Insertion:** $O(1)$ (inserting at head).
  * **Search/Delete:** $O(1)$ average; $O(N)$ worst case (when all elements hash to a single bucket).
* **Optimization:** In systems like Java's `HashMap`, long chains switch from linked lists to Red-Black / Balanced Trees to ensure $O(\log N)$ worst-case search.

---

### 3.2 Open Addressing Techniques

In Open Addressing, all elements are stored directly inside the hash table array (no external linked lists). Collisions are resolved by probing for the next available slot.

#### A. Linear Probing
* **Formula:** $h(k, i) = (h(k) + i) \pmod N \quad \text{for } i = 0, 1, 2, \dots$
* **Mechanism:** Checks the next adjacent cell sequentially until an empty slot is found.

```
Target Index: [ 4 ] (Occupied)
Probe i=1  -> [ 5 ] (Occupied)
Probe i=2  -> [ 6 ] (Occupied)
Probe i=3  -> [ 7 ] (Empty -> Store Key Here)
```

* **Flaw — Primary Clustering:** Contiguous blocks of occupied cells form quickly. Any new key hashing into or near this block must traverse the entire cluster, degrading performance toward $O(N)$.

---

#### B. Quadratic Probing
* **Formula:** $h(k, i) = (h(k) + i^2) \pmod N \quad \text{for } i = 0, 1, 2, \dots$
* **Mechanism:** Jumps non-linearly using quadratic offsets ($+1^2, +2^2, +3^2, \dots$) to break up contiguous physical clusters.

```
Target Index: [ 4 ] (Occupied)
Probe i=1 (+1) -> [ 5 ] (Occupied)
Probe i=2 (+4) -> [ 8 ] (Occupied)
Probe i=3 (+9) -> [ (4 + 9) % 10 = 3 ] (Empty -> Store Key Here)
```

* **Flaw — Secondary Clustering:** Keys with the same initial hash index traverse the exact same probe sequence, causing search delays for identical starting points.

---

#### C. Double Hashing
* **Formula:** $h(k, i) = (h_1(k) + i \cdot h_2(k)) \pmod N$
* **Mechanism:** Uses a second hash function $h_2(k)$ to calculate the step size for probing. Different keys starting at the same initial index get different step intervals, completely eliminating secondary clustering.

```
               h1(k) = k mod 5,   h2(k) = k mod 6
   Key 52: Starts at 2 -> Step size = 52 mod 6 = 4 -> Next: (2 + 1*4) % 10 = 6
   Key 87: Starts at 2 -> Step size = 87 mod 6 = 3 -> Next: (2 + 1*3) % 10 = 5
   (Both started at index 2, but probed different directions!)
```

* **Trade-off:** Higher computational overhead due to evaluating two hash functions.

---

## 4. Internal Working of `std::unordered_map` (C++)

### 4.1 Implementation Choice
C++ uses **Separate Chaining** with dynamic resizing.

### 4.2 Load Factor & Dynamic Rehashing
$$\text{Load Factor } (\lambda) = \frac{\text{Total Number of Elements } (N)}{\text{Size of Table } (M)}$$

```
1. Insert Element
        │
2. Update Load Factor: λ = N / M
        │
3. Is λ > Max Load Factor Threshold?
        ├─── YES ───► Double Table Size (M -> 2M)
        │             Rehash & Redistribute All Elements
        └─── NO  ───► Keep Table As-Is
```

* **Amortized Analysis:** Similar to dynamic array (`std::vector`) doubling, rehashing is an expensive $O(N)$ operation that happens infrequently, ensuring an **amortized $O(1)$** cost per insertion.

---

## 5. Hashing in Cryptography & Security

```
+-------------------------------+-----------------------------------+
|      Encryption / Decryption  |       Cryptographic Hashing       |
+-------------------------------+-----------------------------------+
| Two-way process (reversible).  | One-way process (irreversible).   |
| Ciphertext can be decrypted   | Hash cannot produce the original  |
| back to original plaintext.   | plaintext.                        |
+-------------------------------+-----------------------------------+
```

---

### 5.1 Public-Key Cryptography & Digital Signatures
* **Asymmetric Keys:** Every entity has a **Public Key** (shared openly) and a **Private Key** (kept secret).
  * Encrypt with **Public Key** $\rightarrow$ Decrypt only with corresponding **Private Key** (Confidentiality).
  * Encrypt with **Private Key** $\rightarrow$ Verify with corresponding **Public Key** (Authentication / Digital Signature).

```
  Sender (Ram)                     Channel / Internet                  Receiver (Shyam)
[ Plaintext Message ]                                                [ Verify Ram's PubKey ]
        │                                                                      │
[ Sign with Ram's PrivKey ]  ───► [ Signed Message (Z) ] ───► [ Authenticated Identity ]
```

---

### 5.2 Cryptographic Hash Properties (e.g., SHA-256)

```
Arbitrary Length Input  ───────►  [ SHA-256 Engine ]  ───────►  Fixed 256-bit Digest
("A", "Hello", or a 10GB File)                                  (Always 64 Hex Characters)
```

1. **Fixed Output Length:** Any input size maps to a uniform output size (e.g., 256 bits).
2. **One-Way Function:** Computationally impossible to derive the original input from the hash digest.
3. **Avalanche Effect:** Changing even a single bit in the input completely alters the resulting hash output.
4. **Collision Resistance:** Extremely improbable for two distinct inputs to yield the identical hash digest.

---

### 5.3 Password Storage & Salting

* **Vulnerability:** Storing plain hashes allows attackers to use precomputed lookup tables (**Rainbow Tables**) for common passwords.
* **Solution (Salting):** Append a unique, random string (Salt) to the password before hashing.

```
User Password: "password123"
Random Salt:   "x9#kL2@!"
Combined:      "password123x9#kL2@!"  ───►  [ SHA-256 ]  ───►  Stored in Database
```

---

## 6. Quick Summary Sheet

```
+-----------------------+-------------------------+------------------------------------+
| Technique / Concept   | Primary Advantage       | Drawback / Consideration           |
+-----------------------+-------------------------+------------------------------------+
| Separate Chaining     | Simple, graceful growth | Extra pointer memory, cache misses |
| Linear Probing        | Cache friendly          | Primary clustering                 |
| Quadratic Probing     | Reduces linear clusters | Secondary clustering               |
| Double Hashing        | Minimal clustering      | Higher compute per collision       |
| Dynamic Rehashing     | Keeps O(1) avg ops      | Occasional O(N) resize overhead    |
| Salting & Hashing     | Secure credential store | Irreversible by design             |
+-----------------------+-------------------------+------------------------------------+
```