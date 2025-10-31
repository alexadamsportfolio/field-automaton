Traditionally, John Conway's Game of Life takes place on a discrete 2-dimensional square grid with a boolean value on each cell with the following transformation rules:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Which, during my junior year of high school, I found to be a specific case of this more general transformation rule for certain metric spaces:

$$\Omega_{n+1}(\nu)=\sigma(\int_\mathcal{M} w(\nu,\mu)\Omega_n(\mu) d\mu) \\quad [\\mathrm{I}]$$

Where $\Omega_{n+1}(\nu)$ is the value on the point $\nu$ during iteration $n+1$; $\sigma: \mathbb{R} \to [0,1]$ (we are making the simplifying assumption that all values of $\Omega$ lie on the interval $[0,1]$); $\mathcal{M}$ is the metric space on which we are integrating; and $w$ is a weight function.

Note that Conway's Game of Life is the case where $\sigma$ is the indicator function for the interval $[2,3]$, $\mathcal{M}$ a 2-dimensional Euclidean lattice, and $w$ the indicator function of the Moore neighborhood (not including the central cell).
The case of interest to me, as approximated by life.py, is the case where $\sigma(x)=e^{-a(x-b)^2}$, $\mathcal{M}=\mathbb{R}^2$, and $w(\nu,\mu)=\frac{1}{1+\delta(\nu,\mu)^k}$ where $\delta(\nu,\mu)$ is the Euclidean metric, and $a$, $b$, and $k$ are parameters that the user is free to customize. Below is a simulation of this case of interest with life.py where $k=4$, $a=1.5$, and $b=2.5$ (note that this output is noticeably more entropic than the one from the screenshot provided in how-to-run-code.md):

<img width="408" height="405" alt="Screenshot 2025-10-07 7 51 53 PM" src="https://github.com/user-attachments/assets/558fcc6b-04f0-4ad2-af8b-d7efe59b4c80" />

Though the formulation given in $[\\mathrm{I}]$ accomodates for a continuous space domain, there is no obvious continuation of the time domain. I am currently interested in constructing time-parameterized $C^\infty$ homotopies bundling the iterations of the case of interest I have defined in the previous paragraph, as well as more general cases. The harmonic nature of the automaton’s evolution is much more strongly pronounced than in any other I have seen, so I am very curious about what the frequency domains look like and how they can be used to study the properties of the automaton. I have not yet made much progress for automata in the general form of $[\\mathrm{I}]$, since I have been investing most of my time into the single-body-automaton/fish.py automaton, which is a simpler case where the value of the underlying field at a given point is determined solely by the states of a chosen body and of the given point, rather than by a weighted integration over every point on the space.

The emergent phenomena from such automata are very valuable for simulations of statistical mechanics and its applications to subjects as diverse as field theories, biophysics, thermodynamics, and the Navier-Stokes equations; the horizons for research are very promising.
