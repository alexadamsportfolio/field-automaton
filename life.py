# Necessary imports
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


# Set up the parameters for the grid
vals = range(256)
decay = 2
threshold = 2.5
globality = 1
liveliness = 128


# Define Gaussian distribution function
def gaussian(x, midpoint, steepness):
    return math.e ** (-steepness * ((x - midpoint) ** 2))


# Return a grid of NxN random values
def randomGrid(N, dist):
    return np.random.choice(vals, N*N, p=dist).reshape(N, N)


# Update function
def update(frameNum, img, grid, N):


    # Copy grid and iterate over every tile
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):


            # Compute total sum of life, weighted by proximity
            total = 0
            for k in range(N):
                for l in range(N):
                    total += float(grid[k, l] / ((math.sqrt((i - k) ** 2 + (j - l) ** 2) ** decay) + 1)) / 256


            # Apply Conway's rules
            newGrid[i, j] = 256 * gaussian(total, threshold, globality)


    # Update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,


# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # Parse arguments
    parser = argparse.ArgumentParser(description="Runs continuous Conway's Game of Life simulation.")


    # Add arguments
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--decay', dest='decay', required=False)
    parser.add_argument('--threshold', dest='threshold', required=False)
    parser.add_argument('--globality', dest='globality', required=False)
    parser.add_argument('--liveliness', dest='liveliness', required=False)
    args = parser.parse_args()


    # Set grid size, interval, decay, threshold, globality, and liveliness
    N = 30
    if args.N and int(args.N) > 8:
        N = int(args.N)
       
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)


    if args.decay:
        global decay
        decay = float(args.decay)


    if args.threshold:
        global threshold
        threshold = float(args.threshold)


    if args.globality:
        global globality
        globality = float(args.globality)


    if args.liveliness:
        global liveliness
        liveliness = int(args.liveliness)


    # Declare value distribution for initial state
    probDist = np.append((np.ones(liveliness) / liveliness), np.zeros(256 - liveliness))


    # Declare grid
    grid = np.array([])


    # Generate an initial state
    grid = randomGrid(N, probDist)


    # Set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ), interval=updateInterval, frames=10, save_count=50)


    # Set output file
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])


    # Show plot
    plt.show()


# Call main
if __name__ == '__main__':
    main()
