I would like to thank the article https://www.geeksforgeeks.org/dsa/conways-game-life-python-implementation/, which provided me with the foundation on which I elaborated the life.py program.

Assuming that all necessary modules have been installed, life.py can be easily run with

```python3 life.py```

However, there are 6 optional parameters that will influence the behavior of the automaton:

- Grid Size: An integer value that establishes the number of cells are in each dimension for the 2d grid. Default is 30.
- Interval: Specifies the interval between iterations in milliseconds. Default is 50.
- Decay: A float value. Prior to being inputted into a distribution function, the state of a given cell is derived from the sum of all cells on the grid, where each cell is weighted by a factor of $\frac{1}{1+\delta^k}$, where $k$ is the Decay parameter, and $\delta$ is the distance in the Euclidean metric between the cells. Default is 2.
- Threshold & Globality: Float values $a$ and $b$ respectively, such that the distribution function mapping the raw sum $\Sigma$ onto the interval $(0,1)$ is $e^{-b(\Sigma-a)^2}$. Defaults are 2.5 and 1 respectively.
- Liveliness: A float value between 0 and 255 that specifies how much "life" the grid is initalized with. Default is 128.

Below is an example of life.py being run with configured parameters:

```python3 life.py --grid-size 50 --interval 1000 --decay 4 --threshold 3 --globality 1.75 --liveliness 200```

And below is an example output of the automaton:

<img width="996" height="534" alt="Screenshot 2025-09-21 4 34 06 PM" src="https://github.com/user-attachments/assets/96e0edff-4f0f-461e-ae14-988c17b09ded" />

There is also a --mov-file parameter that presumably saves the animation to a file, but I've never bothered to test it.
