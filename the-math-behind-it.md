Traditionally, John Conway's Game of Life takes place on a discrete 2-dimensional square grid with a boolean value on each cell with the following transformation rules:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Which I found to be a specific case of this more general transformation rule for certain metric spaces:

$$\Omega_{n+1}(\nu)=\sigma(\int_\mathcal{M} w(\nu,\mu)\Omega_n(\mu) d\mu)$$

Where $\Omega_{n+1}(\nu)$ is the value on the point $\nu$ during iteration $n+1$; $\sigma: \mathbb{R} \to [0,1]$ (we are making the simplifying assumption that all values of $\Omega$ lie on the interval $[0,1]$); $\mathcal{M}$ is the metric space on which we are integrating; and $w$ is a weight function.

Note that Conway's Game of Life is the case where $\sigma$ is the indicator function for the interval $[2,3]$, $\mathcal{M}$ a 2-dimensional Euclidean lattice, and $w$ the indicator function of the Moore neighborhood (not including the central cell).
