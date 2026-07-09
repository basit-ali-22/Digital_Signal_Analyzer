# DIGITAL SIGNAL ANALYZER
A VLSI-oriented "Digital Signal Analyzer" project built using Python, Numpy, Pandas and Matplotlib. 
The Digital Signal Analyzer generates digital signals, analyzes their properties and then plots the clock, reset, and data waveforms in the form of graphs.

## Features
- Generates clock signal
- Generates reset signal
- Generate data signal
- Analyze LOW and HIGH counts
- Calculate duty cycle
- Detect rising and falling edges 
- Plots digital waveforms
- Export siignal data to CSV
- Export signal statistics to CSV
- Save waveform as PNG image

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib

## Project Structure
Digital SigNAL Analyzer/
|
|--- main.py
|---signal_generator.py
|---analyzer.py
|---plotter.py
|
|---data/
|    |---signal.csv
|    |---statistics.csv
|
|---images/
|    |---waveform.png
|
|---README.md
|---requirements.txt
|---.gitignore

## How it works

### Step.1 Generate digital signals
- Clock
- Reset
- Data

### Step.2 Visualize all signals using Matplotlib

### Step.3 Analyze each signal
- HIGH count
- LOW count
- Duty cycle
- Rising edges
- Falling edges

### Step.4 Export results
- signal.csv
- statistics.csv
- waveform.png

## Sample Output

### Signal Statistics

+--------+------+-----+------------+--------------+---------------+
| Signal | HIGH | LOW | Duty Cycle | Rising Edges | Falling Edges |
+--------+------+-----+------------+--------------+---------------+
| Clock  |  5   |  5  |    50%     |      5       |       4       |
| Reset  |  4   |  6  |    40%     |      0       |       1       |
|  Data  |  6   |  4  |    60%     |      3       |       2       |
+--------+------+-----+------------+--------------+---------------+

## Project Screenshots 

### Waveform 

~~~~~~

images/waveform.png

