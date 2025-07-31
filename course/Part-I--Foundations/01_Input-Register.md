### Module 1: Speaking in 1s and 0s – The Input Register

---

#### Module Summary

- **Narrative Beat:** Before we can build a computer, we need a way to talk to it. Our language will be binary, and our keyboard will be a set of simple levers.
- **Learning Goals:**
  - Understand binary as a system of on/off switches.
  - Build a physical interface to input binary numbers.
  - Strengthen binary intuition through practice.
- **Lesson Overview:**
    - Lesson 1.1: The Theory – Why Computers Use Binary
    - Lesson 1.2: The Lab – Building and Using Our 4-Bit Register
    - Lesson 1.3: Drills & Games – Strengthening Your Binary Intuition
    - Lesson 1.4: Module 1 Checkpoint
- **Minecraft Artifact:** A working 4-bit input register (keyboard) for binary numbers.

---

#### Module Introduction

Welcome to your first day at Redstone University!

Our grand adventure is to build a complete, working computer from scratch. But like any great construction project, we must begin by laying a solid foundation. The very first thing we need is a way to communicate with our machine. We need a way to give it information.

In this first module, we're going to build our computer's "keyboard." It won't have letters like a normal keyboard. Instead, it will have a set of simple switches that let us speak the computer's one and only native language: `binary`.

Let's get started.

---

#### Lesson 1.1: The Theory – Why Computers Use Binary

Think about how you count. You probably use ten symbols: `0, 1, 2, 3, 4, 5, 6, 7, 8, 9`. This is the **decimal** (base-10) system. It feels natural to us, likely because humans evolved with ten fingers. When we get past `9`, we don't invent a new symbol; we just add a new column to the left, the "tens" column, and start over. The number `12` is really just our way of saying "one ten, plus two ones."

Computers are different. They don't have fingers. Deep down, they are made of billions of microscopic electronic switches called transistors. A switch is a very simple device. It can only ever be in one of two states: **ON** or **OFF**. There is no "halfway on."

This simple, two-state system is the foundation of all modern computing. We call it **binary** (base-2). To represent any piece of information, we just assign a meaning to these two states:

- `OFF = 0`
- `ON = 1`

That's it! Every single thing your computer does, from displaying this text, to playing a song, to running a complex game, is ultimately just a massive, coordinated manipulation of these simple `1`s and `0`s. Each individual `1` or `0` is called a **bit** (short for "binary digit").

So, how can we possibly represent a big number like `13` with just `1`s and `0`s? We use the same trick as our decimal system: we use columns with different values. But instead of ones, tens, and hundreds, our binary columns simply double each time.

| Bit Position | 3   | 2   | 1   | 0   |
|--------------|-----|-----|-----|-----|
| Power of 2   | 2³  | 2²  | 2¹  | 2⁰  |
| Place Value  | 8   | 4   | 2   | 1   |
| Binary       | 1   | 1   | 0   | 1   |

- **Bit Position:** The rightmost bit is position 0, then 1, 2, and so on to the left.
- **Power of 2:** Each position represents a power of two.
- **Place Value:** The actual value for each bit.
- **Binary:** The value of each bit for the number `1101`.


To figure out the value of a binary number, you just add up the values of the columns where there is a `1` (or an "ON" switch).

For example, the binary number `1101`:
- Is there a `1` in the `8`s place? **Yes.**
- Is there a `1` in the `4`s place? **Yes.**
- Is there a `1` in the `2`s place? **No.**
- Is there a `1` in the `1`s place? **Yes.**

So, the value is `8 + 4 + 1 = 13`. We've just translated from the computer's language back to ours!

---

#### Lesson 1.2: The Lab – Building and Using Our 4-Bit Register

It's time to stop talking and start building. A **register** is a fundamental piece of computer hardware that holds a single piece of data. Our 4-bit register will be our simple keyboard, allowing us to manually input any number from `0` to `15`.

##### Materials Needed

- 4 standard building blocks<sup>*</sup>
- 4 Levers
- 4 Signs
- A few pieces of Redstone Dust

<sup>*You can use any solid block, but for the input register, I recommend a redstone lamp. It doubles as a visual indicator of the current state of each bit.</sup>

##### The Build Guide

1. Find a nice open, flat area on our campus. This is your personal workbench.
2. Place **four Redstone Lamps** or **four solid blocks** in a horizontal line with one space between to prevent their redstone dust from merging.
3. On the front face of each block, place one **Lever**. A lever is the perfect physical bit! When it's flipped down, it's `0`. When it's flipped up, it's `1`.
4. Now, let's label our work so we don't get confused. Place a **Sign** on the very top of the block. From **right to left**, label them `1`, `2`, `4`, and `8`. We go right-to-left because, just like in the number `12`, the least valuable digit (the `2`) is on the right. See the schematic, screenshot, or diagram for clarity if needed.
5. Finally, let's wire it up. Go around to the back of your four blocks to the opposite side that you placed the lever. Place a piece or two of **Redstone Dust** on the ground directly behind each one. When you flip a lever, its block becomes powered, which sends a signal to the dust. These four parallel lines of dust are now your official **4-bit input bus**. A "bus" is just the fancy engineering term for a bundle of wires that carry a complete piece of information.

---

##### Minecraft Register Example

<div align="center"><img src="assets/images/01_register_minecraft.png" alt="Minecraft Register" width="512px"/><br/><em>Figure: The register in Minecraft, set to `0110` (binary for 6). The levers are flipped to represent the bits, and the dust is connected to the back. Using redstone lamps makes it easy to see the current state of each bit.</em></div></br></br>

---

##### CircuitVerse Register Example

[View on CircuitVerse](https://circuitverse.org/simulator/edit/redstone-university)

<div align="center"><img src="assets/images/01_register_circuitverse.png" alt="CircuitVerse Register" width="512px"/><br/><em>Figure: The same 4-bit register, built in CircuitVerse. It is also set to `0110` (6 in decimal).</em></div></br></br>

While it has a few stylistic differences, the concept is exactly the same as our Minecraft build. It's a register that holds a 4-bit binary number.

---

Don't worry, we will be building more interesting circuits very soon. We will be using this register to input numbers into our computer throughout the entire course, so while it might not be impressive looking, it is a crucial part of our computer's architecture.

---

#### Lesson 1.3: Drills & Games – Strengthening Your Binary Intuition

Let's get a feel for our new device. Binary feels weird at first, but it will become second nature with just a little practice.

> **Takeaway:** Practicing with your register will make binary numbers feel as natural as decimal. The more you play, the faster you'll get!

##### Drill 1: Binary to Decimal

- **Goal:** What decimal number is `1011`?
- **Action:** Go to your register and set the levers: `ON, OFF, ON, ON`.
- **Calculation:** `8 + 0 + 2 + 1 = 11`. So, `1011` is `11`.

##### Drill 2: Decimal to Binary (The "Greedy" Method)

- **Goal:** Let's represent the number `6`.
- **Thought Process:** Always start with your biggest bit and work your way down.
    1. Is `6` greater than or equal to `8`? **No.** Leave the `8` lever OFF.
    2. Is `6` greater than or equal to `4`? **Yes.** Flip the `4` lever ON. We have `6 - 4 = 2` left to account for.
    3. Is `2` greater than or equal to `2`? **Yes.** Flip the `2` lever ON. We have `2 - 2 = 0` left.
    4. Is `0` greater than or equal to `1`? **No.** Leave the `1` lever OFF.
- **Result:** The levers are `OFF, ON, ON, OFF`, which is the binary number `0110`.

##### The Binary Game

This is a great way to build speed. Pick a random number between `0` and `15` and see how quickly you can represent it on your register. This will burn the powers of two (`1`, `2`, `4`, `8`) into your memory.

---

#### Lesson 1.4: Module 1 Checkpoint

Let's check our understanding before moving on.

> **Takeaway:** If you can answer these questions, you’re ready to move on to the next big idea: logic!

##### Quiz

1. What is the largest number a `5`-bit register could hold? (Hint: The next bit would be the `16`s place).
2. What is the decimal value of the binary number `1100`?
3. How would you represent the number `10` in binary?

##### Real-World Connection: CPU Registers

The `4`-bit register you just built is a real, albeit simplified, computer component. When you see a computer advertised as having a "64-bit processor", it means its internal registers (the spaces inside the chip where it does its most immediate work) are `64` bits wide. They are just like your device, but with `64` "levers" instead of just `4`. This allows them to work with incredibly large numbers in a single step! A `64`-bit register can hold a number larger than `18` quintillion.

In real CPUs, these registers are used to store numbers, addresses, and even instructions. When you write code in assembly language, you are often moving values directly in and out of these registers. Each bit in a register is like a physical wire or lever that can be `ON` or `OFF`, just like your Minecraft build.

##### Software Connection (LeetCode): Counting Bits

How does a programmer "look at" the individual bits you just set with your levers? They use bitwise operations! This is a sneak peek of what we'll learn in Module 2, but it's too cool not to share.

A classic LeetCode problem is **"Number of 1 Bits"**: count how many `1`s are in a number's binary representation. Programmers solve this by checking each "wire" of the number one by one.

```python
def countSetBits(n):
    count = 0
    while n > 0:
        # The '& 1' checks if the last bit is a 1
        if (n & 1) == 1:
            count += 1
        # The '>>= 1' shifts all bits one place to the right
        n >>= 1
    return count

# The binary for 13 is 1101
print(countSetBits(13)) # Output: 3
```

**Software Analogy:** In most programming languages, you can use bitwise operators to manipulate numbers at the binary level. For example, in Python, `n & 1` checks the lowest bit, and `n >>= 1` shifts all bits to the right. This is just like flipping levers and reading wires in your register!

**Extra:** Registers are the foundation for fast calculations in CPUs, and bitwise tricks are used everywhere in high-performance code, cryptography, and even graphics.

---

### Module 1 Conclusion

Fantastic work! You've now mastered the most fundamental concept in all of computing: how information is physically stored in a binary system. You have a working input device, and you've seen how this physical concept directly connects to both real-world hardware and clever software algorithms.

**What's next:** Right now, these are just dumb switches connected to wires. In the next module, we will learn the rules of logic that will allow us to start manipulating these signals and make our machine think.
