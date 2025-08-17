## Part II: The Processor Core - Giving Our Machine a Brain

Congratulations on completing Part I! Take a moment to appreciate what you've built. You have a fully functional I/O system: a 4-bit interface to input numbers and a beautiful two-stage display that can show the results. You've mastered the theory of Boolean logic and applied it to a complex, real-world circuit.

But right now, our machine is just a fancy passthrough. It can display a number, but it can't *do* anything with it. It has a mouth and ears, but no brain.

In Part II, we begin to build that brain by focusing on its most critical capability: **arithmetic**.

#### Our Mission for Part II

This part of the course is a multi-stage story of engineering, debugging, and upgrading. We will not just build a component; we will discover its flaws and systematically improve it until it's powerful and reliable.

*   **In Module 4 (The Adder & The \"Decoder\" Bug),** we'll build our first calculating circuit, the adder. We will immediately discover that our amazing display from Part I has a critical limitation.
*   **In Module 5 (The Hexadecimal Upgrade),** we will solve our first bug by teaching our display to speak Hexadecimal, a far more powerful language for our computer.
*   **In Module 6 (The \"Overflow\" Bug & The Carry Bit),** just when we think our system is perfect, we'll push it to its absolute limit and discover a new, more fundamental bug called \"overflow,\" and learn to harness the carry bit to solve it.
*   **In Module 7 (The Subtractor),** we'll complete our arithmetic toolkit. Using a brilliant trick called Two's Complement, we will teach our existing adder how to perform subtraction.

By the end of this Part, you will have built a complete, robust, and versatile **Arithmetic Unit**, capable of handling both addition and subtraction for any 4-bit numbers and displaying their results perfectly. This powerful component will become the cornerstone of our final processor.

Let's get started!
