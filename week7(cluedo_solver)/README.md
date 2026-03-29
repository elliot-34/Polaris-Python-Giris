# Cluedo Solver
I tried to code a small **knowledge-based agent** inspired by CS50's *Intro to AI* logic lecture.  
It solves a simplified **Cluedo game** by reasoning about suspects, weapons, and rooms using logical elimination.

**How to play:**  
- Run the script: `python cluedo_solver.py`  
- Enter the cards you hold or a sentence with suspect/room/weapon info  
- The program will update its guesses and eventually find the killer, room, and weapon.

**Dependencies:**  
- Python 3  
- [SymPy](https://www.sympy.org) (`pip install sympy`)
