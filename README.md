# Coordinate Points Analyzer 📊
A Python program for analyzing and visualizing points on a coordinate plane, defining its position and angle

## Features
- ✅ Determine which quadrant a point belongs to
- ✅ Calculate distance from origin
- ✅ Calculate angle with X-axis
- ✅ Interactive coordinate input
- ✅ Automatic graph scaling
- ✅ Color-coded quadrants

## Installation
### Prerequisites
- Python 3.10 or higher
- pip3

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Sarmatae685/coordinate-analyzer.git
cd coordinate-analyzer
```

2. Create and activate virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the program:
```bash
python3 coordinate_analyzer.py
```

## Example of usage
### Interactive Input
```
==================================================
COORDINATE POINTS ANALYSIS
==================================================

Enter the coordinates of the points.
To complete the entry, leave the field blank and press Enter.


--- Point 1 ---
Enter X coordinate: 1
Enter Y coordinate: 1
✓ Added point: (1, 1)

--- Point 2 ---
Enter X coordinate: -1
Enter Y coordinate: -1
✓ Added point: (-1, -1)

--- Point 3 ---
Enter X coordinate:  [Enter to finish]
...
```
### Console Output
```
==================================================
ANALYSIS RESULTS
==================================================

Point (1.0, 1.0) in I quadrant
Distance from the origin to the point: 1.41
The angle between the X-axis: 45.00°
--------------------------------------------------
Point (-1.0, -1.0) in III quadrant
Distance from the origin to the point: 1.41
The angle between the X-axis: -135.00°
--------------------------------------------------
...
```
### Visualization
![Example](screenshots/example.png)

## Technologies
- `Python 3.10+` (uses pattern matching with match-case)
- `matplotlib` — for graph visualization
- `math` — for trigonometric calculations

## License
MIT License - see [LICENSE](LICENSE) file for details  

## Star⭐
⭐ If you found this helpful, please star the repo!
