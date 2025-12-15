## Overview

Traditionally, John Conway's Game of Life takes place on a discrete 2-dimensional square grid with a boolean value on each cell with the following transformation rules (Gardner, 1970):

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Which, during my junior year of high school, I found to be a specific case of this more general transformation rule for certain metric spaces:

$$\Omega_{n+1}(\nu)=\sigma(\int_\mathcal{M} w(\nu,\mu)\Omega_n(\mu) d\mu) \\quad [\\mathrm{I}]$$

Where $\Omega_{n+1}(\nu)$ is the value on the point $\nu$ during iteration $n+1$; $\sigma: \mathbb{R} \to [0,1]$ (we are making the simplifying assumption that all values of $\Omega$ lie on the interval $[0,1]$); $\mathcal{M}$ is the metric space on which we are integrating; and $w$ is a weight function.

Note that Conway's Game of Life is the case where $\sigma$ is the indicator function for the interval $[2,3]$, $\mathcal{M}$ a 2-dimensional Euclidean lattice, and $w$ the indicator function of the Moore neighborhood (not including the central cell).
The case of interest to me, as approximated by life.py, is the case where $\sigma(x)=e^{-a(x-b)^2}$ (note that the Gaussian distribution likely induces soliton waves), $\mathcal{M}=\mathbb{R}^2$, and $w(\nu,\mu)=\frac{1}{1+\delta(\nu,\mu)^k}$ where $\delta(\nu,\mu)$ is the Euclidean metric, and $a$, $b$, and $k$ are parameters that the user is free to customize. Below is a simulation of this case of interest with life.py where $k=4$, $a=1.5$, and $b=2.5$ (note that this output is noticeably more entropic than the one from the screenshot provided in how-to-run-code.md):

<img width="408" height="405" alt="Screenshot 2025-10-07 7 51 53 PM" src="https://github.com/user-attachments/assets/558fcc6b-04f0-4ad2-af8b-d7efe59b4c80" />

Though the formulation given in $[\\mathrm{I}]$ accomodates for a continuous space domain, there is no obvious continuation of the time domain. I am currently interested in constructing time-parameterized $C^\infty$ homotopies bundling the iterations of the case of interest I have defined in the previous paragraph, as well as more general cases. The harmonic nature of the automaton’s evolution is much more strongly pronounced than in any other I have seen, so the analysis of its frequency domain is of high priority. I have not yet made much progress for automata in the general form of $[\\mathrm{I}]$, since I have been investing most of my time into the single-body-automaton/fish.py automaton, a simpler - albeit non-trivial - case.

Though I came up with field-automaton independently, I should acknowledge that I later discovered that it resembles photonics researcher Dr. Stephan Rafler's "SmoothLife" paper on lattice gases (Rafler, 2011). Nonetheless, there remain significant differences in our approaches, such as Smoothlife using a bounded neighborhood while field-automaton uses an unbounded neighborhood whose weighted integral is finite. Github user duckythescientist has implemented Rafler's model into Python (Murphy, 2018) by using a fast Fourier transform algorithm which would not only prove to be much more computationally efficient, but also illuminate the harmonic phenomena I look to study on such automata.

The emergent phenomena from automata are very valuable for simulations of statistical mechanics and its applications to subjects as diverse as field theories (D'Ariano & Perinotti, 2016), biophysics (Hartl et al., 2025), computational social science (McAlpine et al., 2020), thermodynamics (Ising, 1925), and the Navier-Stokes equations (Xu & Yan, 2021). The application of algorithms from harmonic analysis or persistent de Rham-Hodge Laplacians from manifold topological deep learning would provide indispensable insights into such systems, thereby optimizing the global behaviors that arise from local conditions.

## References

D’Ariano, G. M., & Perinotti, P. (2016). Quantum cellular automata and free quantum field theory. Frontiers of Physics, 12(1). https://doi.org/10.1007/s11467-016-0616-z

Gardner, M. (1970). The fantastic combinations of John Conway’s new solitaire game “life”. Scientific American, 223(4), 120–123.

Hartl, B., Levin, M., & Pio-Lopez, L. (2025). Neural cellular automata: Applications to biology and beyond classical AI. Physics of Life Reviews, 56, 94–108. https://doi.org/10.1016/j.plrev.2025.11.010

Ising, E. (1925). Beitrag zur Theorie des Ferromagnetismus. Zeitschrift Für Physik, 31(1), 253–258. https://doi.org/10.1007/bf02980577

McAlpine, A., Kiss, L., Zimmerman, C., & Chalabi, Z. (2020). Agent-based modeling for migration and modern slavery research: a systematic review. Journal of Computational Social Science, 4(1), 243–332. https://doi.org/10.1007/s42001-020-00076-7

Murphy, S. (2018). GitHub - duckythescientist/SmoothLife: Continuous Domain Game of Life in Python with Numpy. GitHub. https://github.com/duckythescientist/SmoothLife

Rafler, S. (2011). Generalization of Conway’s “Game of Life” to a continuous domain - SmoothLife. ArXiv.org. https://arxiv.org/abs/1111.1567

Xu, W., & Yan, G. (2021). A lattice Boltzmann model for the Navier-Stokes equation. Microprocessors and Microsystems, 104391. https://doi.org/10.1016/j.micpro.2021.104391
