## Interlude I (A): The Art of Compact Design (Optional)
**note:** This is one potential versin of this interlude. I haven't decided which approach to take yet.

---

### A Note from the Instructor

Congratulations on finishing Module 2! You have mastered the theoretical foundation of our entire computer.

Before we begin our next major project, we have this special, optional section. Think of it as an engineering deep dive. The goal of Module 2 was to build for **clarity**, making our gates large so the logic was easy to trace. This Interlude introduces the art of building for **efficiency**.

We will analyze some common, space-saving designs used by the Redstone community. Understanding them is not required, but it will empower you to make your own builds smaller and faster. This is your first step into true Redstone engineering. From Module 3 onward, we will follow the **Rule of Abstraction**: a gate is defined by its function, not its layout. You are free to use these new designs or the verbose ones from Module 2. As long as it works, it is correct.

---

### Interlude Summary

-   Narrative Beat: You have mastered the language of logic. Now, let's learn the art of the Redstone engineer: how to shrink those textbook examples into sleek components ready for a real machine.
-   Learning Goals:
    -   Understand the engineering trade-offs between a circuit's size, speed, and readability.
    -   Learn common techniques Redstone engineers use to make circuits more compact.
    -   Analyze classic compact gate designs to see these principles in action.
-   Minecraft Artifact: A toolkit of compact logic gate designs.

---

### The Engineering Trade-Off: Size, Speed, and Readability

Every Redstone design is a compromise. When you compact a circuit, you are usually trading **readability** for **efficiency**.

| Factor | Verbose (Educational) Builds | Compact (Practical) Builds |
| :--- | :--- | :--- |
| **Size / Footprint** | Large and sprawling for clarity. | Small and dense to save space. |
| **Speed / Tick Delay**| Often slower due to longer wiring. | Can be faster with shorter signal paths. |
| **Readability** | Very easy to trace and debug. | Can be difficult to read, making errors harder to find. |

> ### Guideline:
> For learning and debugging, verbose is best. For large-scale builds where space is a concern, compact is essential.

---

### Case Studies in Compact Design

Each case study compares the **Verbose Teaching Version** you learned in Module 2 with a **Compact Practical Version** designed for efficiency. Both obey the same truth table, the only difference is the implementation.

---

#### Case Study: The Compact AND Gate

First, recall our verbose AND gate, built from our primitives to be easy to understand.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/main/assets/images/02b_AND-gate-composite_minecraft.png" alt="Verbose AND Gate in Minecraft" width="512px"/><br/><em>Figure: Our easy-to-read, but large, educational AND gate.</em></div><br/>

Now, look at the design below. It performs the exact same logic, but in a much smaller space.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/main/assets/images/02b_AND-gate_minecraft.png" alt="Compact AND Gate in Minecraft" width="512px"/><br/><em>Figure: A classic, space-efficient compact AND gate.</em></div><br/>

#### Logical Deconstruction
This compact build still follows the logic of $A \text{ AND } B$ ($A \land B$), implemented as $\text{NOT } (\text{NOT } A \text{ OR } \text{NOT } B)$ ($\neg(\neg A \lor \neg B)$). The components are just cleverly merged.
-   The two torches on the sides are the first $\text{NOT}$ gates, creating $\text{NOT } A$ ($\neg A$) and $\text{NOT } B$ ($\neg B$).
-   The central Redstone dust on top of the block acts as the $\text{OR}$ gate, collecting the signals from the torches. If either $\neg A$ or $\neg B$ is on, this dust becomes powered.
-   The torch on the back of the central block is the final $\text{NOT}$ gate, inverting the $\text{OR}$ signal to produce the final AND output.

#### Build Steps
1.  Place three solid blocks in a row.
2.  Place input levers on the front of the two outer blocks.
3.  Place a Redstone Torch on the top of each of the two outer blocks. These are your `!A` and `!B` inverters.
4.  Place a single piece of Redstone Dust on top of the central block. This dust will be powered by either of the torches. This is your `OR` gate.
5.  Place a Redstone Torch on the back face of the central block. This is your final inverter.
6.  The output from this final torch is `A AND B`. Connect it to a lamp to test.

---

#### Case Study: The Compact NAND Gate

<div align="center"><img src="./images/NAND-gate-composite_minecraft.png" alt="Verbose NAND Gate in Minecraft" width="512px"/><br/><em>Figure: Our educational NAND gate, built by removing the final inverter from the verbose AND gate.</em></div><br/>

<div align="center"><img src="./images/NAND-gate-compact_minecraft.png" alt="Compact NAND Gate in Minecraft" width="512px"/><br/><em>Figure: A compact NAND gate, created by tapping the output of the compact AND gate before the final inversion.</em></div><br/>

#### Logical Deconstruction
This is the beauty of understanding the logic. A NAND gate is simply $A \text{ NAND } B$ ($\neg(A \land B)$). In our compact AND gate build, the final component is a torch that performs the last inversion. To get a NAND output, we just need to take the signal from *before* that final torch. The signal on the central dust is $\text{NOT } A \text{ OR } \text{NOT } B$ ($\neg A \lor \neg B$), which De Morgan's Law proves is logically identical to $A \text{ NAND } B$.

#### Build Steps
1.  Build the compact AND gate exactly as described above.
2.  Instead of taking the output from the final torch, connect your output wire directly to the Redstone Dust on top of the central block.
3.  This signal is your NAND output. Connect it to a lamp to verify.

---

#### Case Study: The Compact XOR Gate

Recall our large, easy-to-read XOR gate from Module 2.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/main/assets/images/02b_XOR-gate-composite_minecraft.png" alt="Verbose XOR Gate in Minecraft" width="512px"/><br/><em>Figure: Our educational XOR gate, built for clarity.</em></div><br/>

Now, observe a classic compact XOR design. It is much smaller but harder to read at a glance.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/main/assets/images/02b_XOR-gate_minecraft.png" alt="Compact XOR Gate in Minecraft" width="512px"/><br/><em>Figure: A very common and tileable compact XOR gate design.</em></div><br/>

#### Logical Deconstruction
This design is more complex and relies on how torches interact. The logic effectively creates the two conditions for an XOR, $A \text{ XOR } B$ ($A \oplus B$), which is true when $A \text{ AND } \text{NOT } B$ ($A \land \neg B$) or $\text{NOT } A \text{ AND } B$ ($\neg A \land B$) is true, and merges their outputs.
-   The torches on top of the input blocks create $\text{NOT } A$ ($\neg A$) and $\text{NOT } B$ ($\neg B$).
-   The torches on the sides of the output block are each controlled by a combination of a direct input and an inverted input.
-   The final Redstone dust on top acts as an $\text{OR}$ gate, combining the outputs of the side torches.

#### Build Steps
1.  Place two solid blocks for your inputs, side-by-side. Place levers on the front.
2.  Place a third solid block one block away from and between the inputs. This will be your output block.
3.  On the input blocks, place Redstone Dust on top.
4.  On the output block, place Redstone Torches on the two sides facing the input blocks.
5.  On top of the output block, place a piece of Redstone Dust.
6.  Place Redstone Torches on the faces of the input blocks that face the central output block.
7.  The final output is taken from the Redstone Dust on top of the output block. Connect it to a lamp. It will be on only when the inputs differ.

---

#### Case Study: The Compact XNOR Gate

<div align="center"><img src="./images/XNOR-gate-composite_minecraft.png" alt="Verbose XNOR Gate in Minecraft" width="512px"/><br/><em>Figure: The educational XNOR, built by inverting an input to the verbose XOR gate.</em></div><br/>

<div align="center"><img src="./images/XNOR-gate-compact_minecraft.png" alt="Compact XNOR Gate in Minecraft" width="512px"/><br/><em>Figure: A compact XNOR gate, built by simply inverting one input to the compact XOR gate.</em></div><br/>

#### Logical Deconstruction
Just as we learned in Module 2, the simplest way to create an XNOR (equality detector) is to invert one of the inputs to an XOR gate. The logic $A \text{ XNOR } B$ ($A \leftrightarrow B$) is identical to $A \text{ XOR } \text{NOT } B$ ($A \oplus \neg B$). We can apply this exact same principle to our compact build. This is the art of the engineer: modifying an existing component instead of reinventing the wheel.

#### Build Steps
1.  Build the compact XOR gate exactly as described above.
2.  Choose one input, for example, input B.
3.  To invert it, place a Redstone Torch between the lever for B and the input block of the XOR gate.
4.  Now, flipping the B lever will send an inverted signal into the compact XOR circuit. The entire circuit will now behave as an XNOR gate, lighting up only when the two levers are in the same state.

---

### Conclusion: Your Journey Into Optimization

You now know the difference between a circuit designed for teaching and one designed for practical builds. This is a major step in your engineering journey. You understand that compact designs are not magic; they are just clever physical implementations of the same Boolean logic you have already mastered.

From Module 3 onward, we follow the **Rule of Abstraction**:
-   A gate is defined by its **truth table** and interface, not by its internal layout.
-   You are free to use verbose or compact designs as you prefer.

> ### Explore More: The Gate Museum
> In the world download provided for the course, you will find a section labeled "Gate Museum" which showcases these and many other community-tested compact designs for each logic gate. I encourage you to explore, build, and test them to expand your engineering toolkit.
