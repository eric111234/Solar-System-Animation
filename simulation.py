import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants (approximate orbital radii in AU and orbital periods in years)
planet_data = {
    'Mercury': {'radius': 0.4, 'period': 0.241},
    'Venus': {'radius': 0.7, 'period': 0.615},
    'Earth': {'radius': 1, 'period': 1.000},
    'Mars': {'radius': 1.3, 'period': 1.881},
    'Jupiter': {'radius': 1.6, 'period': 11.86},
    'Saturn': {'radius': 1.8, 'period': 29.46},
    'Uranus': {'radius': 2.1, 'period': 84.02},
    'Neptune': {'radius': 2.7, 'period': 164.8},
}

# General scaling factors for visualization
orbit_scale = 15.0          # Larger orbit scale to space out planets
slowdown_factor = 90       # Increased slowdown for all orbits

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(-60, 60)
ax.set_ylim(-60, 60)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Make the Sun much larger for visibility
sun = plt.Circle((0, 0), 3.5, color='yellow', zorder=10)  # Increase Sun's size
ax.add_patch(sun)

# Initialize planet markers with different sizes
planets = {}
for planet, data in planet_data.items():
    # Scale the orbit and set marker sizes for inner planets to be more visible
    if data['radius'] <= 1.5:  # For inner planets (Mercury to Mars)
        radius = data['radius'] * orbit_scale  # Larger orbit for inner planets
        marker_size = 12  # Larger marker size for inner planets
    else:
        radius = data['radius'] * 20  # Moderate orbit scale for outer planets
        marker_size = 12  # Standard marker size for outer planets

    # Create the plot with adjusted marker size
    planets[planet] = ax.plot([], [], 'o', label=planet, markersize=marker_size)[0]
    planet_data[planet]['radius'] = radius  # Update radius with scaled value

# Labels for the legend
ax.legend()


# Function to initialize the plot
def init():
    for planet in planets.values():
        planet.set_data([], [])
    return list(planets.values())


# Function to animate the plot
def animate(t):

    planet_positions = []

    for planet, data in planet_data.items():
        radius = data['radius']
        period = data['period'] * slowdown_factor  # Slow down the orbit

        # Angle change in radians (orbital speed), slowed down
        angle = 2 * np.pi * (t / period)

        # Calculate planet's position
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)

        # Update planet's position, use a list for coordinates
        planet_positions.append(planets[planet].set_data([x], [y]))

    return planet_positions

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.arange(0, 365, 1), init_func=init, blit=False, interval=30)

# Show the plot
plt.show()
