### Prelude: The Redstone Toolkit (Optional)


**TODO:** create this module

*   **Keep it Focused:** The goal is not to teach all of Minecraft. It's to provide a "Minimum Viable Knowledge" guide. We should cover:
    1.  **The Absolute Basics:** What is a block? How do you place and break one?
    2.  **The Core Components:** A visual guide to each key component used in the course.
        *   **Redstone Dust:** How it transmits power, its 15-block limit.
        *   **Redstone Torch:** How it provides power and, crucially, how it *inverts* a signal when placed on the side of a powered block.
        *   **Lever/Button:** The basic input switches.
        *   **Redstone Lamp:** The basic output indicator.
        *   **Redstone Repeater:** Its two primary functions—extending a signal past 15 blocks and acting as a one-way diode.
    3.  **Powering Blocks:** The concept of "strong" vs. "weak" power, and how a powered block can activate adjacent components.






---
Alright — I’ll design **visual callouts and diagrams** for Module 0 so they match your Module 1 & 2 style.
We’ll mirror your existing pattern:

* **Minecraft Screenshot** (clear pseudo-isometric view)
* **CircuitVerse Diagram** (only where it adds clarity — some basics like “placing a block” don’t need it)
* **Caption explaining function**
* **Consistent figure numbering and labels**

Here’s how I’d structure the visuals for Module 0:

---

## **Lesson 0.2: The Core Redstone Components**

**Figure 0.1 – Redstone Dust**
*(Minecraft screenshot: 15-block line of dust, fading from bright red to dull brown at the far end)*
Caption: *Redstone Dust carries power up to 15 blocks before the signal fades completely.*

---

**Figure 0.2 – Redstone Torch**
*(Minecraft screenshot: torch on the side of a block powering dust; second image torch on top powering a lamp)*
Caption: *A Redstone Torch can provide constant power and acts as an inverter when placed on the side of a powered block.*

---

**Figure 0.3 – Lever**
*(Minecraft screenshot: lever on a solid block powering a lamp)*
Caption: *A lever outputs power as long as it’s flipped up. Perfect for stable binary inputs.*

---

**Figure 0.4 – Button**
*(Minecraft screenshot: stone button on block powering a lamp for a short pulse)*
Caption: *Buttons send a momentary signal before automatically resetting.*

---

**Figure 0.5 – Redstone Lamp**
*(Minecraft screenshot: lamp off, lamp on)*
Caption: *Redstone Lamps are our go-to visual output indicator.*

---

**Figure 0.6 – Redstone Repeater**
*(Minecraft screenshot: repeater in line with dust — first image shows faint dust before repeater, bright dust after)*
Caption: *Repeaters restore power to full strength and act as one-way diodes to prevent backflow.*

---

**Figure 0.7 – Solid Block**
*(Minecraft screenshot: dust powering a block, block powering adjacent lamp)*
Caption: *Solid blocks can carry power through themselves to components on their sides.*

---

## **Lesson 0.3: Understanding Power in Minecraft**

**Figure 0.8 – Strong vs Weak Power**
*(Minecraft screenshot: strong power lighting dust directly; weak power only lighting torch on side)*
Caption: *Strong power can activate dust and components directly; weak power can only power certain things, like a torch mounted on the side.*

---

**Figure 0.9 – Signal Range with Repeater**
*(Minecraft screenshot: dust line with repeater mid-way, signal bright again after repeater)*
Caption: *After 15 blocks, a Redstone signal dies. A repeater boosts it back to full strength.*

---

## **Lesson 0.4: Building Your First Mini-Circuit**

**Figure 0.10 – Mini-Circuit (Basic)**
*(Minecraft screenshot: lever → dust → lamp)*
Caption: *A basic input → wire → output circuit. Every build in this course builds on this same structure.*

---

**Figure 0.11 – Mini-Circuit (Inverted)**
*(Minecraft screenshot: lever → block with torch on opposite side → lamp)*
Caption: *Adding a torch inverts the signal — the lamp is on when the lever is off.*

---

**CircuitVerse Supplement**
For Module 0, CircuitVerse diagrams are only needed for:

* Figure 0.9 equivalent (signal range as conceptual wiring diagram)
* Figure 0.10/0.11 equivalent (simple input-output schematic with inverter)

---

**Stylistic Notes for Consistency**

* Match **Module 1’s pseudo-isometric screenshot style** (slightly angled, elevated view so dust connectivity is visible).
* Use **same caption formatting** — italics for explanation, bold for emphasis where needed.
* Use **consistent naming** (“Figure 0.x – \[Component Name]”) so references in text are clean.
* For CircuitVerse, keep diagrams minimalist — only components relevant to the example, clearly labeled A, B, Y when appropriate.

---

If you want, I can go one step further and **make you a ready-to-use shot list + camera commands** so you or someone else can capture every figure with the same framing and clarity, just like your later modules. That would make assembling Module 0 lightning fast.

Do you want me to prepare that shot list?
