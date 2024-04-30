# Browser Simulator

The Browser Simulator is a Python application designed to simulate a user's browsing history, including navigating forward and backward through visited websites. It uses a simple file-based approach for input and output to simulate web browsing actions.

## Features

- Simulates browsing actions such as visiting a new website, going back, and going forward.
- Reads browsing actions from a text file (`browser.txt`) and writes the simulation results to another text file (`output.txt`).
- Calculates and displays the execution time of the simulation.

## How It Works

The simulator uses two main stacks: one for the browsing history and another for the forward history. These are used to track the user's navigation through websites, mimicking the behavior of a web browser's back and forward buttons.

### Actions

- **Visiting a new website:** This action adds the website to the browsing history.
- **Going back (9999):** This action moves the current website from the browsing history to the forward history, simulating a user clicking the back button.
- **Going forward (9998):** This action moves the most recent website from the forward history back to the browsing history, simulating the forward button.

## Input File Format

The input file `browser.txt` should contain one action per line. Actions are represented as follows:

- A positive integer indicates visiting a new website (e.g., `1` for website 1).
- `9999` indicates a "back" action.
- `9998` indicates a "forward" action.

## Output File

The output file `output.txt` contains the results of the browser simulation, detailing which websites were visited, and in what order, after performing all actions from the input file. It includes annotations of backward and forward actions and handles empty stack scenarios gracefully.

## Running the Simulator

To run the simulator, ensure you have Python installed on your system, and follow these steps:

1. Prepare an input file named `browser.txt` in the same directory as the simulator script.
2. Run the simulator with the command `python main.py`.
3. Check the `output.txt` file for the simulation results.

## Requirements

- Python: version 3.10.0 or newer

## Note

This simulator is a simplified version of browsing history and does not simulate actual web browsing or internet access.
