Though the-math-behind-it.md delineates the mathematics most necessary to the behavior of this project, it would be a shame for a STEM portfolio not to have some mention of my less successful findings - after all, the end is the smallest, and arguably the most trivial, stage in mathematics.
This is a gallery of the surviving minority of my incomplete, if not incorrect, attempts on the field-automaton project; but they are no less interesting.

Let's begin with the first written form of the fundamental equation which describes a massive range of cellular automata - including John Conway's Game of Life and my continuous analogy for it - as is found in the-math-behind-it.md [I]:

![IMG_20251002_101239](https://github.com/user-attachments/assets/4542e068-6436-4791-a4a4-f1815bee8998)

I unwittingly stuck out my tongue, as it was really awkward trying to hold a flimsy notebook that close to the camera on a chromebook, and I thought that the notebook would conceal my face.

Moving on, having an excess of free time in my classes - in this case AP Macroeconomics - I often pursue my mathematical curiosities on the paper of my assignments. 
Though I have neglected my research into field-automaton/life.py in favor of single-body-automaton/fish.py, a simpler case, below is my deepest inquisition into the mathematics of the former:

![434f0853-602a-4439-91a2-7864411c3a79 1280x1280](https://github.com/user-attachments/assets/3172b94a-bb24-4d94-8e75-8d2ad3efcf32)

Starting from the lower right, we can see a transformation rule which resembles [I] from the-math-behind-it.md, with the distribution function $\sigma(x) = e^{-kx^2}$, and the weighting function $w(a,b)=\frac{1}{\delta(a,b)+1}$, where $\delta$ is the metric for $L^p$ spaces, i.e., $\delta(a,b)=|a_x^p+a_y^p-b_x^p-b_y^p|^{1/p}$ (note that life.py computes the Euclidean case where $p = 2$). Moving to the left, we write out our transformation rule explicitly:

$$\Omega_{n+1}(x)=e^{-k(\int \int_{\mathbb{R}^2} \frac{\Omega_n(x)}{|a_x^p+a_y^p-b_x^p-b_y^p|^{1/p}+1} da db)^2}$$

Which takes us to the upper right, where I attempt to identify the support of the spatial frequency domain - as studying the automaton's harmonic behavior has been one of my primary goals for this project - by identifying the frequencies $\xi$ for which the Fourier transform with respect to $x$ is non-vanishing, namely,

$$e^{2\pi i \xi x-k(\int \int_{\mathbb{R}^2} \frac{\Omega_n(x)}{|a_x^p+a_y^p-b_x^p-b_y^p|^{1/p}+1} da db)^2} = 1 \implies$$
$$2\pi i \xi x-k(\int \int_{\mathbb{R}^2} \frac{\Omega_n(x)}{|a_x^p+a_y^p-b_x^p-b_y^p|^{1/p}+1} da db)^2 = 0 \implies$$
$$\xi = \frac{k}{2 \pi i}(\int \int_{\mathbb{R}^2} \frac{\Omega_n(x)}{|a_x^p+a_y^p-b_x^p-b_y^p|^{1/p}+1} da db)^2$$

Except I made an incorrect assumption: I assumed that the amplitude on the frequency domain vanishes if the integrand of the Fourier transform is non-constant, but though this is the case for Fourier series with terms such as $e^{-2 \pi i \xi x}$ where $\xi x$ is an integer, this is not necessarily the case for non-integer values, which poses a kink in my plan to identify the support of the frequency domain.

I would like to conclude this gallery with an image of me at the Texas State Capitol with fish.py and life.py, where I would present my programs to the 89th Texas Legislature for the CS4TX Code @ The Capitol Event.

![41db24d5-d21e-4b9a-b470-6f5384a2ce5c 1280x1280](https://github.com/user-attachments/assets/dc98e21c-02e7-496a-84ac-6c13bd829c53)
