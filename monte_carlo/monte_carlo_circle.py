#%%
import random

def monte_carlo_circle_area(radius, num_points=100000):
    """Estimate the area of a circle using the Monte Carlo method.

    Parameters
    ----------
    radius : float
        Radius of the circle. Must be positive.
    num_points : int, optional
        Number of random points to generate. Must be positive.

    Returns
    -------
    float
        Estimated area of the circle.
    """
    if radius <= 0:
        raise ValueError("radius must be positive")
    if num_points <= 0:
        raise ValueError("num_points must be positive")

    inside_circle = 0

    for _ in range(num_points):
        # Generate random (x, y) point within the square enclosing the circle
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)

        # Check if the point lies inside the circle
        if x**2 + y**2 <= radius**2:
            inside_circle += 1

    # Area of the square is (2 * radius)^2
    square_area = (2 * radius) ** 2

    # Ratio of points inside the circle to total points approximates the area ratio
    circle_area = (inside_circle / num_points) * square_area

    return circle_area

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    radius = 1
    estimated_area = []

    for num_points in range(1000, 1000000, 5000):
        estimated_area.append(monte_carlo_circle_area(radius, num_points))
    
    fig, ax = plt.subplots()
    ax.plot(range(1000, 1000000, 5000), estimated_area)
    ax.set_xlabel('Number of Points')
    ax.set_ylabel('Estimated Area of Circle')
    ax.set_title(f'Monte Carlo Circle Area Estimation (Radius = {radius})')
    plt.grid()
    plt.savefig('monte_carlo_circle_area.pdf', bbox_inches='tight')
    plt.show()

# %%
