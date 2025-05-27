# Dot Art Project - Turtle Graph 🎨

This project is a simple yet colorful graphical program that generates a 10x10 grid of colored dots using Python's Turtle graphics. Inspired by Damien Hirst’s dot paintings, the goal was to practice graphical programming, working with RGB color formats, and experimenting with coordinate manipulation in 2D space.

## 🔍 What I Learned

Through this project, I gained practical experience in:

- 🐢 **Turtle Graphics**: Using the Turtle module to draw on screen and create visual patterns.
- 🎨 **Colorgram**: Although not used in the final script, I explored the `colorgram` module to extract colors from images.
- 🎲 **Randomization**: Using the `random` module to select random colors from a list for each dot.
- 🧠 **Coordinate Logic**: Managing movement and positioning using Cartesian coordinates.
- 🧹 **Code Organization**: Structuring simple drawing logic inside loops for pattern generation.
- 🖼️ **RGB Color Mode**: Setting the screen color mode to 255 and using RGB tuples for dot coloring.

## 💻 Technologies Used

- **Python 3**
- **Turtle** (for drawing)
- **colorgram.py** (optional: for extracting colors from images)
- **random** (for selecting colors)

## 🚀 How It Works

- The Turtle starts from the bottom-left of the screen and draws a row of 10 colored dots.
- After completing a row, it moves up and starts a new row, repeating this 10 times.
- Each dot is 20 pixels wide, and dots are spaced 50 pixels apart both vertically and horizontally.
- The colors are randomly chosen from a predefined list of RGB values.

## 📦 Setup Instructions

1. Install Python 3 if you haven't already.
2. Install dependencies:
   ```bash
   pip install colorgram.py Pillow
