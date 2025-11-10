
# Problem Solving Principles & Architecture Guidelines

This document defines the foundational principles, design philosophies, and coding standards for solving algorithmic problems and building modular systems. It is intended to guide developers and LLMs toward producing elegant, efficient, and extensible solutions.

---

## 1. SOLID Design Principles

- **Single Responsibility**: Each class or function must encapsulate one well-defined responsibility.
- **Open/Closed**: Modules should be open for extension but closed for modification.
- **Liskov Substitution**: Subtypes must be substitutable without altering correctness.
- **Interface Segregation**: Clients should not be forced to depend on unused methods.
- **Dependency Inversion**: High-level modules must depend on abstractions, not concrete implementations.

---

## 2. Clean Architecture

- Separate **core logic** from orchestration, I/O, and configuration.
- Use **strategy patterns** to isolate algorithmic variants.
- Keep interfaces **thin**, implementations **swappable**, and dependencies **minimal**.
- Avoid tight coupling and favor **composition over inheritance**.

---

## 3. Efficiency & Elegance

- Prioritize **optimal time and space complexity**.
- Use **intention-revealing names** and avoid cleverness that obscures clarity.
- Prefer **built-in constructs**, **list comprehensions**, and **generators** where appropriate.
- Avoid redundant computation and unnecessary memory allocation.

---

## 4. Extensibility & Testability

- Design solutions that can handle **variants and edge cases** gracefully.
- Avoid hardcoded values; use **configurable parameters** and **dependency injection**.
- Structure code to support **unit testing**, **benchmarking**, and **debugging**.
- Ensure logic is **modular**, **reusable**, and **traceable**.

---

## 5. Developer Experience

- Treat each problem as a **mini-system**, not a one-off script.
- Use **docstrings**, **type hints**, and **comments** to document intent and behavior.
- Structure files and folders for **discoverability**, **readability**, and **reuse**.
- Follow **PEP8**, **DRY**, **KISS**, and **YAGNI** principles.
- Avoid premature optimization; focus on clarity and correctness first.

---

## 6. Code Structure Template

```python
from typing import Protocol, List

class StrategyInterface(Protocol):
    def solve(self, input_data: Any) -> Any: ...

class ConcreteStrategy:
    def solve(self, input_data: Any) -> Any:
        # Core logic here
        pass

class Solution:
    def __init__(self, strategy: StrategyInterface = ConcreteStrategy()) -> None:
        self.strategy = strategy

    def entry_point(self, input_data: Any) -> Any:
        return self.strategy.solve(input_data)
```

---

## 7. Pseudocode Convention

- Use **clear, step-by-step logic**.
- Avoid language-specific syntax.
- Highlight **loop invariants**, **conditions**, and **edge handling**.
- Reflect the same modularity and clarity as the final code.

---

## 8. File Naming & Organization

- Use format: `LC<problem_number>_<problem_slug>.py`
- Organize by topic: `array_string/`, `dp/`, `graphs/`, etc.
- Include `README.md` in each folder with problem summaries and strategy notes.



#### Example Project Structure

```bash
LeetCode75/
├── array_string/
│   ├── LC1768_merge_strings_alternately.py
│   ├── LC238_product_except_self.py
│   ├── LC151_reverse_words.py
│   ├── LC605_can_place_flowers.py
│   └── README.md
├── dp/
│   └── README.md
├── graphs/
│   └── README.md
├── heap/
│   └── README.md
└── README.md
```

---

## 9. Philosophy

We build systems that are:

- **Modular**: Each component is replaceable and independently testable.
- **Resilient**: Handles edge cases and failures gracefully.
- **Elegant**: Minimal, expressive, and intention-driven.
- **Extensible**: Designed to evolve without breaking existing behavior.

---

This document is the grounding reference for all problem-solving workflows. Any developer or LLM using this guide is expected to produce solutions that are **production-grade**, **architecturally sound**, and **developer-friendly**.


