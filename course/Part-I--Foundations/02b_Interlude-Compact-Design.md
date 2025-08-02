### Interlude I: The Art of Compact Design (Optional)

**A Note from the Instructor:**

Congratulations on finishing Module 2! You've mastered the theoretical foundation of our entire computer.

Before we begin our next major project in Module 3, we have this special, optional section. Think of it as an engineering deep-dive. The goal of Module 2 was to build for **clarity**. This Interlude introduces the art of building for **efficiency**.

You can read it now to prepare for the builds ahead, or you can skip it and come back anytime. In the course we will be using the abstract representation of our logic gates and how you implement them is completely up to you. That's the beauty of black box abstractions, we only care that it provides the interface that is defined in the spec, we don't care HOW it was implemented as long as it works.

---

#### Interlude Summary

-   **Narrative Beat:** You’ve mastered the language of logic. Now, let's learn the art of the Redstone engineer: how to shrink those textbook examples into sleek components ready for a real machine.
-   **Learning Goals:**
    -   Understand the engineering trade-offs between a circuit's size, speed, and readability.
    -   Learn common techniques Redstone engineers use to make circuits more compact.
    -   Analyze a classic compact AND gate design to see these principles in action.
-   **Minecraft Artifact:** A compact version of the AND gate, built and understood.

---

#### **Introduction**

The circuits you built in Module 2 were designed with one goal: **clarity**. They are large and easy to trace so you can see how Boolean logic translates directly into physical blocks.

But when you need to build dozens of gates for a complex component, space becomes a precious resource. This is where engineering comes in. In this appendix, we will explore the philosophy of **compact design**, optimizing our circuits for size and speed.

---

#### The Engineering Trade-Off: Size, Speed, and Readability

In Redstone, every design choice is a trade-off. When compacting a circuit, you are usually trading **readability** for **efficiency**.

| Factor | Verbose (Educational) Builds | Compact (Practical) Builds |
| :--- | :--- | :--- |
| **Size / Footprint** | Large and sprawling. | Small and dense. Aims to fit the most logic in the smallest area. |
| **Speed / Tick Delay** | Often slower due to more components. | Can be significantly faster by minimizing the signal path. |
| **Readability** | Very easy to read and debug. | Often difficult to read, making it very challenging to find mistakes. |

Your goal is to find the right balance. For learning, verbose is best. For practical builds, compact is essential.

---

#### Case Study: The Compact AND Gate

Let's put this into practice by analyzing one of the most classic compact designs in Minecraft. First, recall our verbose AND gate, built to be easy to understand.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02b_AND-gate-composite_minecraft.png" alt="Verbose AND Gate in Minecraft" width="512px"/><br/><em>Figure: Our easy-to-read, but large, educational AND gate.</em></div></br></br>

Now, look at the design below. It performs the exact same logic, but in much smaller space. If we remove the lamps we are using to visual input then it is even more compact!

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02b_AND-gate_minecraft.png" alt="Compact AND Gate in Minecraft" width="512px"/><br/><em>Figure: A classic, space-efficient compact AND gate.</em></div></br></br>



    Let's see how this works. It's still `!(!A OR !B)`, but the components are cleverly merged.

    1.  Place two redstone lamps with a lever on the front of each for inputs `A` and `B`.
    2.  Place redstone dust directly behind each lamp.
    3.  Directly behind the redstone place a solid block.
    4.  Place a torch directly on top of each of the solid blocks to negate both `A` and `B` (`!A` and `!B`).
    5.  Between these two blocks place another solid block. For clarity, it can help to make this a different color from the other two solid blocks. I use red for all solid blocks with a torch on the backside, so it is red in the screenshot above.
    6.  Place redstone on top of the middle block which will serve as our OR gate (`!A OR !B`).
    7.  On the backside of this middle block, place a redstone torch to negate the signal `(!(!A OR !B))`.
    8.  Directly in front of the torch on the backside of the middle block, place your redstone lamp for output `Y`.>

---

#### Case Study: The Compact NAND Gate

**TODO**: include the composite and compact figures for NAND


  **TODO:** Explain to the user that they apply the same process that we did in module 2... Negate the final output of the compact AND gate of their choice..



#### Case Study: The Compact XOR Gate
    Let's look back at our XOR Gate design from module 2...*TODO*: recall xor build from module 2

    <div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02b_AND-gate-composite_minecraft.png" alt="Verbose AND Gate in Minecraft" width="512px"/><br/><em>Figure: Our easy-to-read, but large, educational AND gate.</em></div></br></br>

    *TODO*: Introduce compact version

    <div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02b_XOR-gate_minecraft.png" alt="Compact XOR Gate in Minecraft" width="512px"/><br/><em>Figure: A compact XOR gate built in Minecraft. The output is on only when the two inputs are different.</em></div></br></br>

  **The Build:**

    2.  Build the compact version:
        1.  This more efficient layout uses the same principles but in a smaller space.
        2.  Inputs A and B power blocks that have torches on three sides, creating a complex interaction of NOT and AND-like logic.
        3.  The final output is taken from the torch at the front. It will only be ON if the inputs are different.
        4.  Connect to an output lamp for `Y`.

    3.  Test all four combinations from the truth table (`0,0`, `0,1`, `1,0`, `1,1`).
    4.  **Verification:** The output is `1` only when inputs differ.

#### Case Study: The Compact XNOR Gate

**TODO**: include the composite and compact figures for XNOR

**The Build:**

**TODO**: Add build instructions








#### Conclusion: Your Journey Into Optimization

You now understand the crucial difference between a circuit designed for learning and one designed for practice. This is the first step toward thinking like an engineer.

You do not need to memorize compact designs to complete this course. The verbose builds will work just fine. However, understanding *why* compact designs exist will make you a much better builder.

**Explore More in the World Download!**
**TODO:** Put together a world showcasing a wide variety of compact logic gate designs and tricks.

This case study is just the beginning. To help you on your journey, the Module 2 world download includes a "Gate Museum" showcasing many different community-tested designs for each logic gate. I encourage you to explore them and use the principles you learned here to understand how they work.
