<hr class="pagebreak"/>

## Appendix B: Glossary

This glossary compiles key terms from the Redstone University curriculum, organized alphabetically. Each term’s definition is followed by a footnote indicating the module where it is introduced.

**7-segment display**
: An arrangement of seven light segments that can be combined to display numbers and some letters. [3]

**Active-Low Logic**
: A design principle where the "active" or "on" state is represented by a LOW (unpowered) signal. [3]

**BCD (Binary-Coded Decimal)**
: A method of representing the decimal digits `0`-`9` using a `4`-bit binary code. [3]

**Binary**
: A base-`2` number system that uses only two symbols, `0` and `1`, to represent information. It is the fundamental language of all digital computers. [1]

**Bit**
: A single "binary digit," which can be either a `0` or a `1`. It is the smallest possible unit of data in computing. [1]

**Bitwise Operation**
: An operation in software that manipulates numbers at the level of their individual bits, rather than their decimal value. [1]

**Boolean Algebra**
: A branch of mathematics for working with true/false values (`1`/`0`), using operators like AND, OR, and NOT. [2]

**Bus (Input Bus)**
: A collection of parallel wires that carry a complete piece of binary information. Our `4`-bit input interface creates a `4`-bit bus. [1]

**Composite Gate**
: A logic gate constructed by combining primitive gates (e.g., an AND gate built from NOT and OR gates). [2]

**Decimal**
: The base-`10` number system that humans commonly use, with ten unique symbols (`0`-`9`). [1]

**Decoder**
: A circuit that takes a multi-bit binary input and activates a single, corresponding output line. Our decoder acts as an **Identifier**. [3]

**Diode**
: A component that allows a signal to flow in only one direction, preventing back-powering. The Redstone Repeater is our primary diode. [0]

**Diode Matrix**
: A grid of input and output lines where components (like our taps) are placed at intersections to create a programmable logic device, often used as a ROM. [3]

**Encoder**
: A circuit that takes a single active input line and translates it into a multi-bit coded output. Our encoder acts as a **Mapper**. [3]

**Functionally Complete**
: A set of gates from which any Boolean function can be built (e.g., just NAND or just NOR). [2]

**Input**
: A component, like a Lever, that allows a user to manually control a circuit. [0]

**Interface (Input Interface)**
: A device that allows a user or system to provide information to a machine. Our `4`-lever setup is a manual input interface. [1]

**Inverter (NOT Gate)**
: A circuit or component that flips a signal from ON to OFF, or OFF to ON. The Redstone Torch is our primitive inverter. [0]

**Logic Gate**
: A physical or virtual device that implements a Boolean operation. [2]

**Modularity**
: The engineering practice of designing a system in independent, interchangeable components. This makes the system easier to design, test, and upgrade. [3]

**Output**
: A component, like a Redstone Lamp, that displays the result or state of a circuit. [0]

**Power Source**
: A component, like a Redstone Torch or Lever, that outputs a full-strength (`15`) signal. [0]

**Primitive Gate**
: A basic, indivisible logic gate from which more complex gates are built. In our course, these are NOT and OR. [2]

**Register**
: A small, extremely fast storage location inside a computer's central processing unit (CPU) that holds data for immediate use.


### Module 1 Conclusion

Fantastic work! You've now mastered the most fundamental concept in all of computing: how information is physically represented in a binary system. You have a working input device, and you've seen how this physical concept directly connects to both real-world hardware and clever software algorithms.

Your input bus is ready to carry these binary signals to the next stage where logic gates will turn them into calculations and decisions. Now that you’ve built your input interface and practiced working with binary, you’re ready to learn how to manipulate these binary signals using logic gates in the next module. These gates will process the inputs you’ve set here into meaningful outputs.

The basic building blocks of our computer are about to take shape. Get ready for the world of logic gates and circuits! [1]

**Repeater**
: A component that acts as a signal booster (refreshing signal strength to `15`) and a diode. [0]

**ROM (Read-Only Memory)**
: A type of storage where data is permanently programmed into the hardware's structure. [3]

**Signal Strength**
: The power level of a Redstone signal, ranging from `15` (full) down to `0` (off). A signal loses `1` strength for every block of dust it travels. [0]

**Strong Power**
: A type of power provided by components like Repeaters or Torches directly to a block. It can activate all adjacent Redstone components, including dust. [0]

**Tap (Repeater/Torch)**
: Our term for a connection that reads a signal from a bus line to control another wire. [3]

**Truth Table**
: A chart showing all possible input/output combinations for a logic gate or circuit. [2]

**Weak Power**
: A type of power provided by Redstone Dust to a block. It can activate components like lamps and repeaters, but not adjacent Redstone dust. [0]

**Wire**
: Our term for any component, usually Redstone Dust, that transmits a signal from one point to another. [0]

**XOR (Exclusive OR)**
: Outputs `1` if inputs are different; used in both hardware and software for unique logic tricks. [2]


---

[0]: Module 0: The Redstone Toolkit – Orientation Day (Optional)

[1]: Module 1: Speaking in 1s and 0s – The Input Interface

[2]: Module 2: The Language of Logic – A Deep Dive into Boolean Algebra

[3]: Module 3: From Binary to Pictures - Building a Digital Display
