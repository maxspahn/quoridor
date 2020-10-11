import matplotlib.pyplot as plt
import numpy as np

# Make a 9x9 grid...
nrows, ncols = 10, 10
image = np.zeros(nrows* ncols)
image = np.zeros(shape = (10, 10))

# Set every other cell to a random number (this would be your data)
print(image)
for i in range(10):
    for j in range(10):
        image[i][j] = (i+j)%2

# Reshape things into a 9x9 grid.
image = image.reshape((nrows, ncols))

row_labels = range(nrows)
col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
plt.matshow(image)
plt.xticks(range(ncols), col_labels)
plt.yticks(range(nrows), row_labels)
player1 = plt.Circle((5, 3), 0.5, color='r', fill=True)
player2 = plt.Circle((1, 9), 0.5, color='b', fill=True)
ax = plt.gca()
ax.add_artist(player1)
ax.add_artist(player2)
plt.show()

sec = input("Press direction")


player1 = plt.Circle((5, 4), 0.5, color='r', fill=True)
ax.add_artist(player1)
plt.show()
