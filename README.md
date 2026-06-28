# ⚔️ RPG Battle Game (Python)

A simple turn-based RPG battle game developed in Python using Object-Oriented Programming (OOP) principles.

## 📖 About the Project

This project simulates a turn-based battle between a hero and an enemy.

The player controls the hero and can choose between a normal attack or a special attack each turn. After the player's action, the enemy automatically attacks until one of the characters runs out of Health Points (HP).

The main purpose of this project is to practice the core concepts of Object-Oriented Programming in Python.

---

## 🚀 Features

- Turn-based battle system
- Hero and enemy classes using inheritance
- Normal attack
- Special attack
- Health Points (HP) system
- Character information display
- Win and lose conditions
- Simple terminal interface

---

## 🏗️ Project Structure

### Character

The base class for all characters in the game.

#### Attributes

- Name
- HP (Health Points)
- Level

#### Methods

- `get_name()`
- `get_hp()`
- `get_level()`
- `show_details()`
- `attack()`
- `come_under_attack()`

---

### Hero

Inherits from the `Character` class.

#### Additional Attribute

- Skill

#### Additional Method

- `special_attack()`

The special attack deals:

```text
Damage = Level × 4
```

---

### Enemy

Inherits from the `Character` class.

#### Additional Attribute

- Type

Example:

- Red

---

### Game

The `Game` class manages the battle flow.

Responsibilities:

1. Create the hero.
2. Create the enemy.
3. Display character information.
4. Ask the player to choose an attack.
5. Execute attacks.
6. End the battle when one character's HP reaches zero.

---

## 🎮 How to Play

Run the Python file:

```bash
python main.py
```

During each turn, choose one of the following options:

```text
1 - Normal Attack
2 - Special Attack
```

- **1** → Perform a normal attack.
- **2** → Perform a special attack.

The battle continues until either the hero or the enemy is defeated.

---

## 💻 Example Output

```text
Starting Battle

Character Details

Name: Link
HP: 200
Level: 5
Skill: Spin Attack

Name: Octorok
HP: 50
Level: 3
Type: Red

Press Enter to attack...

Choose:
1 - Normal Attack
2 - Special Attack
```

---

## 📚 Concepts Practiced

- Object-Oriented Programming (OOP)
- Classes and Objects
- Inheritance
- Encapsulation
- Method Overriding
- Constructors
- Polymorphism
- Game Loop
- User Input Handling

---

## 📂 Suggested Project Structure

```text
project/
│
├── main.py
└── README.md
```

---

## 🔮 Future Improvements

- Experience (XP) system
- Character leveling
- Inventory system
- Healing items
- Multiple enemies
- Character selection
- Critical hits
- Defense mechanics
- Graphical User Interface (GUI)
- Save and load game progress
- Random enemy generation

---

## 👨‍💻 Author

Developed as a practice project to improve Python programming skills and gain hands-on experience with Object-Oriented Programming concepts.