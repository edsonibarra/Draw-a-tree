# Tree Drawer

This Python script draws a tree pattern based on the height provided. The pattern uses the word "CAR" and fills the tree with ` ` (space) symbols to create a symmetrical tree shape.

## Usage
Clone the repo
```
git clone https://github.com/edsonibarra/Draw-a-tree.git
```
Move into the repo directory in the terminal
```
cd Draw-a-tree
```
Create the virtual environment
```
python -m venv venv
```
Activate the virtaul environment
Windows
```
venv\Scripts\activate
```
Linux/MacOS
```
source venv/bin/activate
```
Install dependencies
```
pip install -r requirements.txt
```
Execute the script to generete the figure and replace height with the number of rows you want.
```
python draw_tree.py --height <height>
```

### Output
```
   C   
  ACA
 RACAR
CRACARC
```

### Execute the pytest tests
Vorbose mode
```
pytest -v . 
```
Should see something similar like this
![image](https://github.com/user-attachments/assets/e1fcab42-987d-4890-8312-4373b59a69c9)

