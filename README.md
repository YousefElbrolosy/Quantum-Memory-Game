# Quantum-Memory-Game
This is a quantum version of the classic Memory card game using IBM Qiskit and PyGame. This game is based on James Weaver's quantum-circuit-pygame package: https://github.com/JavaFXpert/quantum-circuit-pygame. </br>
This interactive and fun memory game is designed to challenge your memory skills by asking you to match pairs of cards from a grid. Test your memory and concentration as you try to remember the positions of various cards and match them to clear the board.

## Table of Contents

- [Features](#features)
- [Gameplay](#gameplay)
- [Getting Started](#getting-started)
- [How to Play](#how-to-play)
- [Contributing](#contributing)

## Features

- Engaging and challenging memory game.
- Control the grid using a Quantum Circuit Grid that simulates real Quantum Computers
- Score tracking to measure your progress.
- Intuitive and user-friendly interface.

## Gameplay

Check out the [gameplay](https://m.youtube.com/watch?v=r27UGgq0eik&t=42s)

## Getting Started

Follow these steps to get the Memory Game up and running on your local machine:

1. Clone the repository:

   ```bash
   git clone https://github.com/YousefElbrolosy/Quantum-Memory-Game.git
   ```
2. Download [qiskit](https://qiskit.org/documentation/stable/0.24/install.html), [pygame](https://pypi.org/project/pygame/),[numpy](https://numpy.org/install/) and [sympy](https://docs.sympy.org/latest/install.html)

That's it! You're ready to enjoy the Memory Game.

## How to Play
1. Place quantum gates on the circuit grid to select the row.
2. Repeat the process to select a column.
3. Flip the a card to reveal its symbol.
4. Flip a second card to see if it matches the first one.
5. If the cards match, they be removed and you will earn points. If not, they will be flipped back.
6. Continue selecting pairs of cards until all matches are found.
7. The game is complete when all pairs are matched.
8. If you flipped two matching cards using a circuit that generated entanglement you earn 10 points!
9. Note that: when playing with noise the card you selected may not be the one that will flip because noise is introduced into the system.
  a. In order to remove that noise you need to perform error mitigation
  b. error mitigation is unlocked when you reach 15 points.


## Contributing

If you'd like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

Thank you for checking out the Memory Game project! Have fun testing and improving your memory skills. If you encounter any issues or have suggestions, feel free to open an issue or contribute to the project. Happy playing!

