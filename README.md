# Mesh-to-MC-high-fedelty
 convert models into mincraft blocks acuretly

this script can take a .stl file and convert it into a mincraft schematic, its purpese is to allow for smaller converted struchers by using stairs and slabs.
to use it open the the main.py with an ide switch the addres of the moddle to the desired model and run it, a test.schem will be created

curently only supports stone

## Development
### Gui
The gui consists of 3 file:
1. `gui.py`: The class MainWindow, handle the gui and its events.
2. `form.ui`: A ui file for qt. Should be eddited in Qt Designer/Creator.
3. `ui_form.py`: Auto generated python file from `form.ui`, using `pyside6-uic form.ui -o ui_form.py`
