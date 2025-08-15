### **Module 11: The Heartbeat & Conductor - Automating the Machine (Enhanced Edition)**

**(Learning Goals:** Understand the role of a clock signal in synchronizing a computer's operations. Build a controllable clock. Learn how a Program Counter automatically steps through instructions. Combine all previous modules into a single, automated system that executes a simple, hard-coded program.)

**(Narrative Beat:** "We've built all the organs of our computer: a processor to think, memory to remember, and inputs/outputs to communicate. But it's not alive yet. It waits for us to flip every switch. In this module, we will give our machine two final things: a **heartbeat** to provide a steady rhythm, and a **conductor** to direct the orchestra of components. It's time to take our hands off the levers and watch our creation run on its own.")

---

#### **Lesson 11.1: The Need for a Heartbeat - The Clock**

So far, our computer only does something when we change an input. A real computer works continuously. It executes one instruction, then the next, then the next, in a perfectly synchronized dance. What drives this rhythm? A **clock**.

A computer clock is not like a wall clock; it doesn't tell time. It's a circuit that produces a steady, oscillating signal: `1, 0, 1, 0, 1, 0...`. This regular pulse is sent to all major components of the CPU. Each time the clock signal goes from low to high (a "rising edge"), every component knows it's time to perform its next step. The speed of this clock determines the speed of the processor, measured in Hertz (Hz), or cycles per second. A 3 GHz processor has a clock that pulses 3 billion times every second.

**The Lab: Building a Controllable, Adjustable Clock**
1.  **The Concept: The Repeater Loop.** The simplest clock in Minecraft is a loop of Redstone Repeaters. A signal will chase itself around the loop forever.
2.  **The Build:**
    *   Create a small loop of Redstone dust.
    *   Place several Redstone Repeaters in the loop, all facing the same direction. The more repeaters you add, or the more you increase their delay (by right-clicking them), the slower the clock will be.
    *   To start the clock, you need to introduce a short pulse (e.g., from a quickly-flicked lever or a button).
3.  **Adding Control:** We need to be able to start and stop our computer. We'll add an AND gate to our clock's output. One input to the AND gate is the oscillating clock signal. The other input is a new master lever labeled **"RUN/HALT"**. The final output of the AND gate is our official **System Clock Bus**, which will only pulse when the RUN lever is ON.

**(A clear ASCII schematic of a start/stop repeater-loop clock would be provided here).**

---

#### **Lesson 11.2: The Conductor - The Program Counter**

If the clock is the heartbeat, who tells the orchestra which note to play on each beat? That's the job of the **Program Counter (PC)**.

The Program Counter is just a special-purpose register whose only job is to hold the memory address of the *next instruction* to be executed. On every tick of the clock, two things happen:
1.  The computer performs the instruction pointed to by the PC.
2.  The PC **increments** by one, so it points to the *next* instruction for the next clock cycle.

**The Lab: Building a 2-bit Counter**
To keep things simple, our computer will only have 4 instructions (at addresses 0, 1, 2, and 3). Therefore, we only need a 2-bit Program Counter.

A counter is just an adder whose output is fed back into one of its own inputs.
1.  **The Build:**
    *   Take a 2-bit Adder circuit (a smaller version of our Module 4 adder).
    *   Take a 2-bit Memory Register (a smaller version of our Module 7 register).
    *   The input to the adder is the current value from the memory register, and the number `1` (hard-wired).
    *   The output of the adder feeds back into the data input of the memory register.
    *   The "Write Enable" line of the memory register is connected to our **System Clock Bus**.
2.  **The Result:** On every clock pulse, the register "stores" the result of `(itself + 1)`. It will automatically cycle: `00 -> 01 -> 10 -> 11 -> 00 -> ...`.

---

#### **Lesson 11.3: The Program - Hard-Coding Our Instructions (ROM)**

Our computer needs a program to run. A program is just a sequence of instructions stored in memory. For our simple machine, we will "hard-code" the program into a ROM, just like our Display Encoder from Module 3.

This ROM will be an **Instruction Decoder**. Its "address" input will be the 2-bit output from our Program Counter. Its outputs will be all the control signals needed to operate our computer (like the "SELECT" levers for the ALU and the "STORE" lever for the memory).

**Our Simple Program:**
*   **Address 00 (Step 0):** `LOAD A` - Take the number from Input Register A and prepare it for the ALU.
*   **Address 01 (Step 1):** `LOAD B` - Take the number from Input Register B and prepare it for the ALU.
*   **Address 10 (Step 2):** `ADD` - Tell the ALU to perform the ADD operation.
*   **Address 11 (Step 3):** `STORE` - Take the result from the ALU and store it in our Memory Register.

The student will build a decoder matrix (like the display one) that translates the PC's output (`00`, `01`, `10`, `11`) into the correct Redstone signals to control the ALU and memory.

---

#### **Lesson 11.4: The Grand Assembly & The First Automated Run**

This is the final, exhilarating step. We are connecting everything together.
1.  The **System Clock** connects to the Program Counter.
2.  The **Program Counter** connects to the Instruction Decoder (our Program ROM).
3.  The **Instruction Decoder**'s output control lines connect to all the components:
    *   The ALU's MUX selector.
    *   The Memory Register's "STORE" (Write Enable) line.
    *   (In a more complex computer, it would also control which registers are read from/written to).
4.  The output of the Memory Register is permanently wired to our Hex Display.

**The Experiment - The First Boot-up:**
1.  Set Input Register A to `0101` (5).
2.  Set Input Register B to `0110` (6).
3.  Ensure the Program Counter is reset to `00`.
4.  Flip the master **"RUN/HALT"** switch to RUN.
5.  **Watch:**
    *   **Tick 1:** The PC is `00`. The instruction `LOAD A` runs. Nothing much seems to happen yet. The PC increments to `01`.
    *   **Tick 2:** The PC is `01`. The instruction `LOAD B` runs. The PC increments to `10`.
    *   **Tick 3:** The PC is `10`. The instruction `ADD` runs. The ALU calculates `5+6` and its output becomes `1011`. The PC increments to `11`.
    *   **Tick 4:** The PC is `11`. The instruction `STORE` runs. The `1011` from the ALU is written into the Memory Register. Instantly, the Hex Display, which is connected to the memory, flashes the letter `B`. The PC increments back to `00`.
6.  Flip the **"RUN/HALT"** switch to HALT.

**The Payoff:** You didn't touch a thing after starting it. The machine, on its own, followed a sequence of steps and produced the correct result. You have officially built a computer.

---

#### **Module 22 Checkpoint**

*   **Quiz:**
    1.  What is the purpose of the system clock? (To synchronize operations).
    2.  What is the job of the Program Counter? (To hold the address of the next instruction).
    3.  In our final assembly, what component tells the ALU *which* operation (ADD, AND, etc.) to perform? (The Instruction Decoder/Program ROM).

*   **Real-World Connection: The Fetch-Decode-Execute Cycle**
    > The four steps your computer just ran are a simplified version of the **Fetch-Decode-Execute cycle** that is the basis of all modern computing. A real CPU "fetches" an instruction from memory (using the Program Counter), "decodes" it to understand what to do (using its instruction decoder), and then "executes" the instruction (by activating the ALU, memory, etc.). Your machine does this in a very literal, physical way.

**Module 11 Conclusion:**
This is the moment of triumph. You have taken a collection of disparate parts and breathed life into them with a clock and a program. You've built a system that can execute a sequence of commands without human intervention. While simple, it is a true computer. In our final "Post-Graduate" module, we'll return to a problem we left behind to see how we could make our machine's output even more human-friendly.
