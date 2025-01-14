import turtle
from typing import Tuple

def setup_turtle() -> turtle.Turtle:
    """
    Sets up the turtle graphics environment.
    Returns:
        A configured turtle object for drawing.
    """
    # Create the turtle object.
    # Customize the turtle speed and hide the turtle cursor.
    # Return the turtle object for use in the program.

def draw_triangle(t: turtle.Turtle, vertices: Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float]], color: str) -> None:
    """
    Draws a filled triangle based on the given vertices.
    Args:
        t: The turtle object.
        vertices: A tuple containing three (x, y) coordinates for the triangle's vertices.
        color: The fill color for the triangle.
    """
    # Move the turtle to the first vertex without drawing.
    # Draw lines between the vertices, completing the triangle.
    # Fill the triangle with the given color.

def sierpinski(t: turtle.Turtle, vertices: Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float]], depth: int) -> None:
    """
    Recursively draws the Sierpiński Triangle.
    Args:
        t: The turtle object.
        vertices: A tuple containing three (x, y) coordinates for the current triangle's vertices.
        depth: The remaining depth of recursion.
    """
    # Base case: if depth is 0, draw a single triangle using draw_triangle.
    # Recursive case: Divide the triangle into three smaller triangles.
    # Call sierpinski on each smaller triangle, reducing the depth.

def main() -> None:
    """
    Main function to set up the environment and draw the Sierpiński Triangle.
    """
    # Set up the turtle environment using setup_turtle.
    # Define the initial vertices of the outer triangle.
    # Ask the user for the recursion depth (handle invalid input).
    # Call sierpinski with the turtle, initial vertices, and depth.
    # Keep the turtle graphics window open until the user closes it.

if __name__ == "__main__":
    main()