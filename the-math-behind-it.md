Traditionally, John Conway's Game of Life takes place on a discrete 2-dimensional square grid with a boolean value on each cell with the following transformation rules:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Which I found to be a specific case of this more general transformation rule for certain metric spaces:

$$\Omega_{n+1}(\nu)=\sigma(\int_\mathcal{M} w(\nu,\mu)\Omega_n(\mu) d\mu)  [\\mathrm{I}]$$

Where $\Omega_{n+1}(\nu)$ is the value on the point $\nu$ during iteration $n+1$; $\sigma: \mathbb{R} \to [0,1]$ (we are making the simplifying assumption that all values of $\Omega$ lie on the interval $[0,1]$); $\mathcal{M}$ is the metric space on which we are integrating; and $w$ is a weight function.

Note that Conway's Game of Life is the case where $\sigma$ is the indicator function for the interval $[2,3]$, $\mathcal{M}$ a 2-dimensional Euclidean lattice, and $w$ the indicator function of the Moore neighborhood (not including the central cell).
The case of interest to me, as approximated by life.py, the case where $\sigma(x)=e^{-a(x-b)^2}$, $\mathcal{M}=\mathbb{R}^2$, and $w(\nu,\mu)=\frac{1}{1+\delta(\nu,\mu)^k}$ where $\delta(\nu,\mu)$ is the Euclidean metric, and $a$, $b$, and $k$ are parameters that the user is free to customize.

Though the formulation given in $[\\mathrm{I}]$ accomodates for a continuous space domain, there is no obvious continuation of the time domain. I am currently interested in constructing an n-parameterized $C^\infty$ homotopy connecting the iterations of the case of interest I have defined in the previous paragraph, as well as more general cases. I am also curious what harmonic phenomena arise on these spaces, and I have noticed that there is an unfortunate lack of research into the harmonic analysis of cellular automata despite it being a very promising field. I have not yet made much progress for cellular automata such as those in the form of $[\\mathrm{I}]$, since I have been investing most of my time into the single-body-automaton/fish.py automaton, which is a simpler case where the value of the underlying field at a given point is determined solely by the states of a chosen body and of the given point, rather than by a weighted integration over every point on the space.
