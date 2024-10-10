from flask import Flask, jsonify
from flask_cors import CORS
import pygame
import random
from nqueens_generator import NQueens_Generator  # Make sure to import your NQueens_Generator class

app = Flask(__name__)
CORS(app)

@app.route('/get_colors')
def get_colors():
    n = random.choice([7,8,9,10])  # Number of rows and columns in the grid
    game = NQueens_Generator(n)
    result = game.get_solver()
    sample_list = game.select_color_sizes()
    color_map = game.color_board(solver=result, color_sizes=sample_list)
    game.paint_board(color_map)
    color_board = game.colored_board

    color_names = [
        "#FFD700", "#008080", "#FF007F", "#BF1B00", "#DFFF00",
        "#0ABAB5", "#E0B0FF", "#E2725B", "#7FFFD4", "#32CD32",
        "#800020", "#FFE5B4", "#D128A1",
    ]
    
    # Convert color names to RGB values (Pygame uses integers in the range 0-255)
    pygame.init()
    rgb_values = {color: pygame.Color(color) for color in color_names}

    def get_color_per_box(color_board, color_names):
        colors = []
        for i in range(color_board.shape[0]):
            for j in range(color_board.shape[1]):
                num = int(color_board[i][j][1:])
                colr = rgb_values[color_names[num]]
                colors.append((colr.r, colr.g, colr.b))
        return colors

    colors = get_color_per_box(color_board, color_names)
    return jsonify(colors)

if __name__ == '__main__':
    app.run(debug=True)