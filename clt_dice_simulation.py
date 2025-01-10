import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Probabilities for the biased die
probabilities = [0.3, 0.15, 0.05, 0.05, 0.15, 0.3]
faces = np.array([1, 2, 3, 4, 5, 6])

# Create a gradient color map
colors = LinearSegmentedColormap.from_list('gradient', ['orangered', 'deepskyblue'], N=6)

# Bar chart to visualize the biased die
plt.figure(figsize=(4, 4))
bars = plt.bar(faces, probabilities, color=[colors(i/5) for i in range(6)])

plt.xticks(faces, color='white', fontsize=10)
plt.yticks(color='white', fontsize=10)
plt.ylim(0, 0.31)

plt.title('Distribution of the Biased Die', color='white', fontsize=16)
plt.xlabel('Die Face', color='white', fontsize=12)
plt.ylabel('Probability', color='white', fontsize=12)

# Set dark background
plt.gca().set_facecolor('black') 
plt.gcf().set_facecolor('black') 

# Number of dice in each simulation
num_dice_list = [2, 5, 15, 20]

# Create the figure and subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8), facecolor='black')
fig.suptitle('Sum of Dice Simulations', color='white', fontsize=20)

# Iterate through the dice counts and plot the histograms
for ax, num_dice in zip(axes.flatten(), num_dice_list):
    # Simulate rolling biased dice
    np.random.seed(100)
    rolls = np.random.choice(faces, size=(3000, num_dice), p=probabilities)
    sums = rolls.sum(axis=1)
    
    # Create a gradient color map for the histogram
    unique_sums = np.unique(sums)
    colors = LinearSegmentedColormap.from_list('gradient', ['orangered', 'deepskyblue'], N=len(unique_sums))
    
    # Plot the histogram
    counts, bins, patches = ax.hist(sums, bins=np.arange(num_dice, num_dice * 6 + 2) - 0.5, rwidth=0.8)
    
    # Apply gradient to the histogram bars
    for i, patch in enumerate(patches):
        patch.set_facecolor(colors(i / len(patches)))
    
    # Customize the subplot
    ax.set_title(f'Sum of {num_dice} Dice', color='white', fontsize=14)
    # ax.set_xticks(range(num_dice, num_dice * 6 + 1))
    ax.tick_params(axis='x', colors='white', labelsize=10)
    ax.tick_params(axis='y', colors='white', labelsize=10)
    ax.set_facecolor('black')

# Adjust layout and show the plot
plt.tight_layout(rect=[0, 0, 1, .95])
plt.show()