### **Module 1: Speaking in 1s and 0s - The Input Register**

**(Learning Goals:** Understand binary as a system of on/off switches. Build a physical interface to input binary numbers. Strengthen binary intuition through practice.)

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

#### **Lesson 1.4: Drills & Games - Strengthening Your Binary Intuition**

Let's get comfortable using our new device. Binary can feel strange at first, but practice is the key to making it second nature.

*   **Drill 1: Binary to Decimal.**
    *   **Goal:** What decimal number is represented by the binary `1101`?
    *   **Action:** Go to your register and set the levers: `ON, ON, OFF, ON`.
    *   **Thought Process:** "The '8' lever is on. The '4' lever is on. The '2' lever is off. The '1' lever is on. The value is `8 + 4 + 1 = 13`."

*   **Drill 2: Decimal to Binary (The Greedy Method).**
    *   **Goal:** Represent the number **14**.
    *   **Thought Process:** Start with the biggest bit.
        1.  Is 14 greater than or equal to 8? **Yes.** Flip the '8' lever ON. `14 - 8 = 6` remaining.
        2.  Is 6 greater than or equal to 4? **Yes.** Flip the '4' lever ON. `6 - 4 = 2` remaining.
        3.  Is 2 greater than or equal to 2? **Yes.** Flip the '2' lever ON. `2 - 2 = 0` remaining.
        4.  Is 0 greater than or equal to 1? **No.** Leave the '1' lever OFF.
    *   **Result:** The levers are `ON, ON, ON, OFF`, which is the binary number `1110`.

*   **The Binary Game:** Challenge yourself or a friend. Pick a random number between 0 and 15. See who can set the levers correctly the fastest. This builds muscle memory for the powers of two.

#### **Module 1 Checkpoint**

Let's check our understanding before moving on.

*   **Quiz:**
    1.  What is the largest number a 5-bit register could hold? (Hint: The next bit would be the 16s place).
    2.  What is the decimal value of the binary number `1011`?
    3.  How would you represent the number `5` in binary?

*   **Real-World Connection: CPU Registers**
    > The 4-bit register you just built is a real, albeit simplified, computer component. When you see a computer advertised as having a "64-bit processor," it means its internal registers—the spaces where it does its most immediate work—are 64 bits wide. They are just like your device, but with 64 "levers" instead of 4. This allows them to work with incredibly large numbers in a single step! A 64-bit register can hold a number larger than 18 quintillion.

**Module 1 Conclusion:**
You've now mastered the most fundamental concept: how information is physically represented in a binary system. You have a working input device and have started building an intuitive understanding of binary numbers. But right now, these are just dumb switches connected to wires. In the next module, we will learn the rules of logic that will allow us to start manipulating these signals in intelligent ways.