### **Module 1: Speaking in 1s and 0s - The Input Register**

**(Learning Goals:** Understand binary as a system of on/off switches. Build a physical interface to input binary numbers.)

**(Narrative Beat:** "Before we can build a computer, we need a way to talk to it. Our language will be binary, and our keyboard will be a set of simple levers.")

#### **Lesson 1.1: Beyond Ten Fingers - Why Binary?**

Think about how you count. You use ten symbols: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. This is called the **decimal** system, or base-10, likely because humans have ten fingers. When we run out of symbols (after 9), we add another column—the "tens" column—and start over. The number 12 is really "one ten plus two ones."

Computers, however, don't have fingers. They have transistors, which are microscopic electronic switches. A switch can only be in one of two states: **ON** or **OFF**. That's it. There's no in-between. This two-state system is called **binary**, or base-2.

To represent information, we assign a meaning to these states:
*   **OFF = 0**
*   **ON = 1**

Every single piece of information on a computer—this text, your favorite song, a high-resolution video—is ultimately stored as an unimaginably long sequence of these 1s and 0s. Each `1` or `0` is called a **bit**, which is short for "binary digit."

#### **Lesson 1.2: Counting with Switches**

How can we possibly represent a number like 13 using only 1s and 0s? We use the same trick as our decimal system: we use columns. But instead of the ones, tens, and hundreds columns, our binary columns double each time.

*   The first column is the **1s** column (2⁰).
*   The second column is the **2s** column (2¹).
*   The third column is the **4s** column (2²).
*   The fourth column is the **8s** column (2³).
*   ...and so on (16, 32, 64...).

To find the value of a binary number, you just add up the column values for every position that has a `1`.

Let's take the binary number **`1101`**.
*   There's a `1` in the 8s column.
*   There's a `1` in the 4s column.
*   There's a `0` in the 2s column (we ignore it).
*   There's a `1` in the 1s column.

So, `1101` in binary is `8 + 4 + 0 + 1 = 13` in decimal. We've successfully represented the number 13!

#### **Lesson 1.3: The Lab - Building Our 4-Bit Register**

It's time to build. A "register" is a simple piece of computer hardware that holds a single number. Our 4-bit register will be our "keyboard," allowing us to manually input any number from 0 to 15.

**Materials Needed (in Minecraft):**
*   4 standard Blocks (e.g., Stone or Iron)
*   4 Levers
*   4 Signs
*   Redstone Dust

**The Build Process:**
1.  **Find an open, flat area.** This will be our main workbench.
2.  **Place four blocks in a horizontal line,** leaving one empty space between each block for clarity.
3.  **Place one lever on the front face of each block.** A lever is the perfect real-world representation of a bit. Flipped down is `0` (off), and flipped up is `1` (on).
4.  **Label your work.** Place a sign on the block above each lever. From right to left, label them "1", "2", "4", and "8". This helps us remember the value of each bit position. Why right to left? It's convention. In both decimal and binary, the "least significant" bit/digit is on the right.
5.  **Wire the outputs.** Go to the back of the blocks. Place a single piece of Redstone dust on the ground behind each block. When you flip a lever, its corresponding block becomes "powered," which in turn powers the dust behind it. These four parallel lines of Redstone dust are now our **4-bit input bus**. A "bus" is just a term for a collection of wires that carry a related signal.

**Visual Representation (Side View):**
```
   [Sign: "8"]                [Sign: "4"]
 [Lever]--[Block]--<Bus Wire 3>   [Lever]--[Block]--<Bus Wire 2> ...etc
```

**Congratulations!** You have just built a fundamental piece of computer hardware. This register allows us to hold a 4-bit number, which is often called a "nibble."

#### **Lesson 1.4: Drills & Verification**

Let's get comfortable using our new device. The best way to learn is by doing.

*   **Drill 1: Decimal to Binary.**
    *   **Goal:** Represent the number **9**.
    *   **Thought Process:** "How do I make 9? I need an 8. So, I'll flip the '8' lever ON. What's left? 9 - 8 = 1. I need a 1. So I'll flip the '1' lever ON. The '4' and '2' levers stay OFF."
    *   **Result:** The levers should be in the state: `ON, OFF, OFF, ON` which corresponds to the binary number `1001`.

*   **Drill 2: Binary to Decimal.**
    *   **Goal:** What decimal number is represented by the binary `0110`?
    *   **Action:** Go to your register and set the levers: `OFF, ON, ON, OFF`.
    *   **Thought Process:** "Okay, the '8' lever is off. The '4' lever is on. The '2' lever is on. The '1' lever is off. So, the value is 4 + 2 = 6."
    *   **Result:** `0110` is 6.

*   **Challenge Drill:**
    *   What is the largest number you can represent? (Flip all levers ON: `1111` -> `8+4+2+1 = 15`).
    *   What is the smallest number? (Flip all levers OFF: `0000` -> `0`).
    *   Represent your age (if it's 15 or under!).

**Module 1 Conclusion:**
You've now mastered the most fundamental concept: how information is physically represented in a binary system. You have a working input device and an intuitive understanding of binary numbers. But right now, these are just dumb switches connected to wires. In the next module, we will learn the rules of logic that will allow us to start manipulating these signals in intelligent ways.