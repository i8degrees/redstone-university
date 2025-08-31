## Appendix B: Glossary

This glossary compiles key terms from the Redstone University curriculum, organized alphabetically. Each term’s definition is followed by a footnote indicating the module where it is introduced.

**7-segment display**
: An arrangement of seven light segments that can be combined to display numbers and some letters. [4]

**Active-Low Logic**
: A design principle where the "active" or "on" state is represented by a LOW (unpowered) signal. [4]

**Adder**
: A digital circuit that performs the addition of numbers. [5]

**Address**
: A unique binary number that specifies a particular location in memory. [11]

**Address Bus**
: A set of parallel wires that carries the address of the memory location to be read from or written to. [11]

**Arithmetic Logic Unit (ALU)**
: The part of a central processing unit (CPU) that carries out arithmetic and logic operations. It is the fundamental building block of a processor. [9]

**Arithmetic Overflow**
: An error condition that occurs when the result of a calculation is too large to be represented by the available number of bits. [6]

**BCD (Binary-Coded Decimal)**
: A method of representing the decimal digits `0`–`9` using a 4-bit binary code. [4]

**Binary**
: A base-2 number system that uses only two symbols, `0` and `1`, to represent information. It is the fundamental language of all digital computers. [1]

**Binary Coded Decimal (BCD)**
: A system that represents each decimal digit (`0`-`9`) with its own dedicated 4-bit binary number. Essential for multi-digit decimal displays. [13]

**Binary-Coded Decimal (BCD)**
: A system that represents each decimal digit (`0`-`9`) with a 4-bit binary number. [5]

**Bit**
: A single "binary digit," which can be either a `0` or a `1`. It is the smallest possible unit of data in computing. [1]

**Bitwise Operation**
: An operation in software that manipulates numbers at the level of their individual bits, rather than their decimal value. [1]

**Boolean Algebra**
: A branch of mathematics for working with true/false values ($1$/$0$), using operators like AND, OR, and NOT. [2]

**Bus (Input Bus)**
: A collection of parallel wires that carry a complete piece of binary information. Our 4-bit input interface creates a 4-bit bus. [1]

**Carry Bit**
: A bit that stores the overflow from a single column of addition, which is then "carried" over to the next column. [6]

**Clock**
: A circuit that generates a steady pulse to synchronize the operations of a computer. [12]

**Combinational Logic**
: A type of digital circuit whose output is purely a function of its present inputs only. [10]

**Comparator**
: A digital circuit that compares two binary numbers and outputs a signal indicating the result of that comparison (e.g., equal, greater than, etc.). [7]

**Composite Gate**
: A logic gate that is constructed by combining primitive gates (e.g., an AND gate built from NOT and OR gates). [2]

**Control Unit**
: The part of the CPU that directs the operation of the processor. It fetches, decodes, and executes instructions by sending control signals to other components. [12]

**Data Bus**
: A set of parallel wires used to transfer data to and from the CPU and memory. [11]

**Decimal**
: The base-10 number system that humans commonly use, with ten unique symbols (`0`-`9`). [1]

**Decoder**
: A circuit that takes a multi-bit binary input and activates a single, corresponding output line. Our decoder acts as an **Identifier**. [4]

**Diode**
: A component that allows a signal to flow in only one direction, preventing back-powering. The Redstone Repeater is our primary diode. [0]

**Diode Matrix**
: A grid of input and output lines where components (like our taps) are placed at intersections to create a programmable logic device, often used as a ROM. [4]

**Double Dabble Algorithm**
: A common algorithm used to convert a binary number to BCD, often implemented sequentially with shift registers and "add-3" modules. Our ROM is a combinational equivalent. [13]

**Encoder**
: A circuit that takes a single active input line and translates it into a multi-bit coded output. Our encoder acts as a **Mapper**. [4]

**Feedback Loop**
: A circuit design where an output from a gate is fed back into its own input path, creating a stateful circuit that can hold a value. [10]

**Fetch-Decode-Execute Cycle**
: The fundamental process of a computer, where it retrieves an instruction from memory, determines its operation, and performs that operation. [12]

**Flag**
: A single bit stored in a status register that holds information about the result of the most recent ALU operation. [7]

**Full Adder**
: A 1-bit circuit that adds three bits ($A$, $B$, and a Carry-In) and produces a Sum and a Carry-Out. [5]

**Functionally Complete**
: A property of a set of logic gates (or a single gate like NAND/NOR) from which any possible Boolean function can be constructed. [3]

**Gated D-Latch**
: A 1-bit memory circuit that copies its Data ($D$) input to its output ($Q$) when the Write Enable ($WE$) signal is active, and holds its state when $WE$ is inactive. [10]

**Hexadecimal**
: A base-16 number system used as a human-friendly representation of binary data. [5]

**Input**
: A component, like a Lever, that allows a user to manually control a circuit. [0]

**Instruction Register (IR)**
: A register in the Control Unit that holds the instruction that is currently being executed or decoded. [12]

**Instruction Set Architecture (ISA)**
: The part of the computer architecture related to programming, including the native data types, instructions, registers, and memory model. [12]

**Interface (Input Interface)**
: A device that allows a user or system to provide information to a machine. Our 4-lever setup is a manual input interface. [1]

**Inverter (NOT Gate)**
: A circuit or component that flips a signal from ON to OFF, or OFF to ON. The Redstone Torch is our primitive inverter. [0]

**Logic Gate**
: A physical device that performs a Boolean logic operation on one or more inputs to produce a single output. [2]

**Modularity**
: The engineering practice of designing a system in independent, interchangeable components. This makes the system easier to design, test, and upgrade. [4]

**Most Significant Bit (MSB)**
: The bit in a binary number with the largest place value, which is used as the sign bit in Two's Complement representation. [7]

**Multiplexer (MUX)**
: A digital circuit that selects one of several input signals and forwards the selected input into a single output line. It acts as a digital switch. [8]

**Negative Flag (N)**
: A status flag that is set to `1` if the result of an operation is negative (i.e., its MSB is `1`), and `0` otherwise. [7]

**Opcode (Operation Code)**
: A set of bits that defines a specific machine language instruction to be performed by the CPU, such as `ADD` or `JUMP`. [9]

**Output**
: A component, like a Redstone Lamp, that displays the result or state of a circuit. [0]

**Power Source**
: A component, like a Redstone Torch or Lever, that outputs a full-strength (`15`) signal. [0]

**Primitive Gate**
: A basic, indivisible logic gate from which more complex gates are built. In our course, these are NOT and OR. [2]

**Program Counter (PC)**
: A register in the Control Unit that holds the memory address of the next instruction to be fetched. [12]

**RAM (Random Access Memory)**
: A form of computer memory that can be read and changed in any order. It is used to store working data and machine code. [11]

**Register**
: A small, extremely fast storage location inside a computer's central processing unit (CPU) that holds data for immediate use.


### Module 1 Conclusion

Fantastic work! You've now mastered the most fundamental concept in all of computing: how information is physically represented in a binary system. You have a working input device, and you've seen how this physical concept directly connects to both real-world hardware and clever software algorithms.

Your input bus is ready to carry these binary signals to the next stage where logic gates will turn them into calculations and decisions. Now that you’ve built your input interface and practiced working with binary, you’re ready to learn how to manipulate these binary signals in Module 2: The Grammar of Circuits. There, we will build our first logic gates, which will process the inputs you’ve set here into meaningful outputs.

The basic building blocks of our computer are about to take shape. Get ready for the world of logic gates and circuits! [1]

**Repeater**
: A component that acts as a signal booster (refreshing signal strength to `15`) and a diode. [0]

**Ripple-Carry Adder**
: A type of multi-bit adder built by chaining Full Adders together, where the carry bit "ripples" from one stage to the next. [5]

**ROM (Read-Only Memory)**
: A type of storage where data is permanently programmed into the hardware's structure. [4]

**Select Line(s)**
: The control input(s) to a MUX that determine which data input is passed to the output. [8]

**Sequential Logic**
: A type of digital circuit whose output depends on the sequence of previous inputs, not just the current ones. It has memory. [10]

**Sign Bit**
: The most significant bit (MSB) in a signed number representation, which indicates whether the number is positive or negative. [6]

**Signal Strength**
: The power level of a Redstone signal, ranging from `15` (full) down to `0` (off). A signal loses `1` strength for every block of dust it travels. [0]

**Simplification**
: The process of using the laws of Boolean algebra to reduce a complex logic expression to a simpler, equivalent one, resulting in a more efficient circuit. [3]

**State**
: The condition of a circuit at a particular time, representing the data it is currently storing. [10]

**Status Register**
: A collection of flag bits within a CPU that stores the status of the processor and information about the outcome of the last operation. [7]

**Strong Power**
: A type of power provided by components like Repeaters or Torches directly to a block. It can activate all adjacent Redstone components, including dust. [0]

**Tap (Repeater/Torch)**
: Our term for a connection that reads a signal from a bus line to control another wire. [4]

**Truth Table**
: A chart showing every possible input combination for a logic circuit and its corresponding output. [2]

**Two's Complement**
: A mathematical operation and binary representation system used by computers to handle negative numbers, allowing for subtraction using addition. [6]

**Universal Gate**
: A logic gate, such as NAND or NOR, that is functionally complete by itself. [3]

**von Neumann Architecture**
: A computer architecture based on the concept of a stored-program computer where instruction data and program data are stored in the same memory.``` [12]

**Weak Power**
: A type of power provided by Redstone Dust to a block. It can activate components like lamps and repeaters, but not adjacent Redstone dust. [0]

**Wire**
: Our term for any component, usually Redstone Dust, that transmits a signal from one point to another. [0]

**Write Enable**
: A control signal that tells a memory module whether to store the data currently on the data bus into the selected address. [11]

**XOR (Exclusive OR)**
: A logic gate that outputs `1` only if its inputs are different. It is fundamental to binary arithmetic and many software algorithms. [3]

**Zero Flag (Z)**
: A status flag that is set to `1` if the result of an operation is zero, and `0` otherwise. It is the primary mechanism for testing equality. [7]


---

[0]: Module 0: The Redstone Toolkit – Orientation Day (Optional)

[1]: Module 1: Speaking in 1s and 0s – The Input Interface

[2]: Module 2: The Grammar of Circuits – Foundational Logic Gates

[3]: Module 3: The Art of Logic – Simplification and Special Gates

[4]: Module 4: From Binary to Pictures: Building a Digital Display

[5]: Module 5: The 4-Bit Adder & The Hexadecimal Upgrade

[6]: Module 6: Advanced Arithmetic – Overflow and Subtraction

[7]: Module 7: Comparators and Status Flags – The Dawn of Decision-Making

[8]: Module 8: The Multiplexer – The Digital Switch

[9]: Module 9: The ALU – The Grand Assembly

[10]: Module 10: The Processor's Scratchpad – Building a Register

[11]: Module 11: Addressable Storage – Building RAM

[12]: Module 12: The Control Unit & Programmable Logic

[13]: Module 13: The "Real World" Display – The Double Dabble Algorithm
