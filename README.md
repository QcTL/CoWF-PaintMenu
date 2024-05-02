# Paint Menu

This is a simple Pygame application that allows you to create and edit grids of tiles/sprites. You can select tiles from a tileset, paint them onto a grid, and save the resulting grid configuration to a text file.
![Homes4Cheap](https://github.com/QcTL/CoWF-PaintMenu/assets/71326643/eed094de-bdc1-46d2-8259-9a8d9f0381ad)

## Features

- **Tile Selection**: Choose from a selection of tiles/sprites to paint onto the grid.
- **Grid Editing**: Paint selected tiles onto a grid and modify them as desired.
- **Export Functionality**: Save the edited grid configuration to a text file for later use.

## Requirements

- Python 3.x
- Pygame library

## Usage

1. Make sure you have Python 3.x installed on your system.
2. Install the Pygame library using `pip install pygame`.
3. Run the `tile_painter.py` script.
4. Use the following controls:
   - **Left Mouse Button**: Paint selected tile onto the grid.
   - **Right Mouse Button**: Erase tile from the grid.
   - **'A' Key**: Cycle forward through the tile selection.
   - **'S' Key**: Cycle backward through the tile selection.
5. Once you're done editing, close the window to automatically save the grid configuration to `output.txt`.

## Additional Notes

- The tileset used in this project should be named `tileset.png` and placed in the `tileset` directory relative to the script.
- The tileset should contain individual tiles/sprites organized in a grid format.
- The grid size is set to 20x25 tiles by default, but this can be modified in the script.
