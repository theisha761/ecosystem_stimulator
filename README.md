# Ecosystem Simulation using Object-Oriented Programming (Python)

## Overview

This project is a Python-based ecosystem simulation designed to demonstrate the core principles of Object-Oriented Programming (OOP). The simulation models different organisms living in habitats, interacting with one another through growth, hunting, aging, and survival.

The project was built as a learning exercise to practice abstraction, inheritance, polymorphism, encapsulation, and multiple inheritance in a realistic scenario.

---

## Features

* Multiple habitats (Forest, Ocean, etc.)
* Plants and animals as different organism types
* Animal hunting behavior based on prey preferences
* Speed-based hunting success
* Plant growth and energy accumulation
* Aging of organisms over time
* Automatic removal of dead organisms
* Population tracking by species
* Support for aquatic and terrestrial organisms

---

## OOP Concepts Demonstrated

### 1. Abstraction

The `Organism` abstract base class defines the common structure and behavior shared by all living organisms.

### 2. Encapsulation

Attributes such as health, energy, age, and alive status are stored as private variables and accessed through getter/setter methods.

### 3. Inheritance

Specialized classes inherit from more general classes:

* Organism

  * Plant

    * Tree
    * Grass
  * Animal

    * Tiger
    * Deer
    * Bear
    * Fish

### 4. Polymorphism

Methods such as `eat()`, `grow()`, `make_sound()`, and `reproduce()` behave differently depending on the organism type.

### 5. Multiple Inheritance

The `AquaticMammal` class demonstrates multiple inheritance by combining behavior from multiple parent classes.

---

## Project Structure

```text
ecosystem/
│
├── organm.py      # Abstract Organism class
├── pln.py         # Plant, Tree, Grass
├── ani.py         # Animal hierarchy
├── aqua.py        # Aquatic and aquatic mammal classes
├── habi.py        # Habitat management
├── eco.py         # Ecosystem simulation engine
├── main.py        # Program entry point
└── README.md
```

---

## Simulation Workflow

For each simulated day:

1. Every organism ages.
2. Plants grow and gain energy.
3. Animals attempt to hunt prey.
4. Dead organisms are removed from habitats.
5. Population counts are updated.
6. Habitat status is displayed.

---

## Example Organisms

### Animals

* Tiger
* Deer
* Bear
* Dolphin

### Plants

* Tree
* Grass

---

## Sample Output

```text
Day 1

Habitat: Forest
Tree: 2
Grass: 1
Tiger: 1
Deer: 1
Bear: 1

Habitat: Ocean
Dolphin: 1
```

---

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project folder.

```bash
cd ecosystem
```

3. Run the simulation.

```bash
python main.py
```

---

## Learning Outcomes

Through this project I practiced:

* Object-Oriented Design
* Class Hierarchies
* Abstract Base Classes
* Method Overriding
* Multiple Inheritance
* Encapsulation
* Simulation Modeling
* Python Project Organization

---

## Future Improvements

* Reproduction mechanics
* Randomized ecosystem events
* Food scarcity and resource management
* Migration between habitats
* Graphical visualization of populations
* Data persistence and statistics tracking

---

## Author

Developed as a Python OOP learning project to explore ecosystem modeling and software design principles.
