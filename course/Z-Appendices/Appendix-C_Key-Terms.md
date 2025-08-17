<hr class="pagebreak"/>

### Appendix C: Key Terms

**7-Segment Display**
: An arrangement of seven light segments that can be combined to display numbers and some letters.

**Active-Low Logic**
: A design principle where the "active" or "on" state is represented by a LOW (unpowered) signal.

**BCD (Binary-Coded Decimal)**
: A method of representing the decimal digits 0-9 using a 4-bit binary code.

**Binary**
: A base-2 number system that uses only two symbols, 0 and 1, to represent information. It is the fundamental language of all digital computers.

**Bit**
: A single "binary digit," which can be either a 0 or a 1. It is the smallest possible unit of data in computing.

**Bitwise Operation**
: An operation in software that manipulates numbers at the level of their individual bits, rather than their decimal value.

**Boolean Algebra**
: A branch of mathematics for working with true/false values (1/0), using operators like AND, OR, and NOT.

**Bus (Input Bus)**
: A collection of parallel wires that carry a complete piece of binary information. Our 4-bit input interface creates a 4-bit bus.

**Composite Gate**
: A logic gate constructed by combining primitive gates (e.g., an AND gate built from NOT and OR gates).

**Decimal**
: The base-10 number system that humans commonly use, with ten unique symbols (0-9).

**Decoder**
: A circuit that takes a multi-bit binary input and activates a single, corresponding output line. Our decoder acts as an **Identifier**.

**Diode**
: A component that allows a signal to flow in only one direction, preventing back-powering. The Redstone Repeater is our primary diode.

**Diode Matrix**
: A grid of input and output lines where components (like our taps) are placed at intersections to create a programmable logic device, often used as a ROM.

**Encoder**
: A circuit that takes a single active input line and translates it into a multi-bit coded output. Our encoder acts as a **Mapper**.

**Functionally Complete**
: A set of gates from which any Boolean function can be built (e.g., just NAND or just NOR).

**Input**
: A component, like a Lever, that allows a user to manually control a circuit.

**Interface (Input Interface)**
: A device that allows a user or system to provide information to a machine. Our 4-lever setup is a manual input interface.

**Inverter (NOT Gate)**
: A circuit or component that flips a signal from ON to OFF, or OFF to ON. The Redstone Torch is our primitive inverter.

**Logic Gate**
: A physical or virtual device that implements a Boolean operation.

**Modularity**
: The engineering practice of designing a system in independent, interchangeable components. This makes the system easier to design, test, and upgrade.

**Output**
: A component, like a Redstone Lamp, that displays the result or state of a circuit.

**Power Source**
: A component, like a Redstone Torch or Lever, that outputs a full-strength (15) signal.

**Primitive Gate**
: A basic, indivisible logic gate from which more complex gates are built. In our course, these are NOT and OR.

**ROM (Read-Only Memory)**
: A type of storage where data is permanently programmed into the hardware's structure.

**Register**
: A small, extremely fast storage location inside a computer's central processing unit (CPU) that holds data for immediate use.

**Repeater**
: A component that acts as a signal booster (refreshing signal strength to 15) and a diode.

**Signal Strength**
: The power level of a Redstone signal, ranging from 15 (full) down to 0 (off). A signal loses 1 strength for every block of dust it travels.

**Strong Power**
: A type of power provided by components like Repeaters or Torches directly to a block. It can activate all adjacent Redstone components, including dust.

**Tap (Repeater/Torch)**
: Our term for a connection that reads a signal from a bus line to control another wire.

**Truth Table**
: A chart showing all possible input/output combinations for a logic gate or circuit.

**Weak Power**
: A type of power provided by Redstone Dust to a block. It can activate components like lamps and repeaters, but not adjacent Redstone dust.

**Wire**
: Our term for any component, usually Redstone Dust, that transmits a signal from one point to another.

**XOR (Exclusive OR)**
: Outputs 1 if inputs are different; used in both hardware and software for unique logic tricks.
