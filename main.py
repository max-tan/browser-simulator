import time  # Import time module to measure execution time

class BrowserSimulator:
    def __init__(self):
        self.history = []
        self.forward_stack = []

    def navigate(self, action):
        if action == 9999:  # Back
            if len(self.history) > 1:
                self.forward_stack.append(self.history.pop())
                return f"9999 - {self.history[-1]}" if self.history else "9999 - backward stack empty"
            else:
                return "9999 - backward stack empty"
        elif action == 9998:  # Forward
            if self.forward_stack:
                self.history.append(self.forward_stack.pop())
                return f"9998 - {self.history[-1]}"
            else:
                return "9998 - forward stack empty"
        else:  # Website visit
            self.history.append(action)
            self.forward_stack = []
            return f"{action} - {action}"

    def simulate(self, input_file, output_file):
        start_time = time.time()  # Record start time
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            outfile.write(f"Programming Language Used: Python\n")  # Annotate output with language used
            for line in infile:
                action = int(line.strip())
                result = self.navigate(action)
                outfile.write(f"{result}\n")
        end_time = time.time()  # Record end time after simulation
        total_time = end_time - start_time  # Calculate execution time
        print(f"Execution time: {total_time} seconds")  # Print execution time

if __name__ == "__main__":
    simulator = BrowserSimulator()
    simulator.simulate("browser.txt", "output.txt")
