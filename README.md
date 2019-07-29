# evoDots
A simple project using genetic algorithms to make dots towards a goal without being explicitly programmed.

## Installation
>```python
>pip install -r requirements.txt
>```

## Usage
>```python
>python Simulate.py
>```

## Overview
![Demo 1] (res/test1.gif)
![Demo 2] (res/test2.gif)
![Demo 3] (res/test3.gif)

The dots begin from the bottom green circle. They start their lives randomly in the beginning, taking any direction whatsoever. Once the whole population dies, the system runs through calculations to determine the best performing dot in terms of getting closest to the goal. 
That dot is then selected as the "parent" of the next generation, and the dots of the next generation will be copies of that parent with slight mutations. Rinse and repeat until eventually a dot emerges that is able to bypass all the randomly-generated obstacles and find the goal (red dot).

This is an experimental project with no real purpose but the same algorithm can be used in several applications including robotics, automotive, simulations, etc. 