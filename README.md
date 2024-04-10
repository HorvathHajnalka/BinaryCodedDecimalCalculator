### Computer Science Fundamentals Assignment

**Author Information**  
Name: Hajnalka Horváth  
Neptun Code: XXNVW8  
Date: 2022.10.01 - 2022.11.30  

**Overview**  
This Python script is developed as a part of a Computer Science fundamentals assignment. It was my first project at university in my first semester. It reads two numbers from an `input.txt` file, performs arithmetic operations on them (in BCD format), and writes the result to an `output.txt` file. Supported operations include addition, subtraction, multiplication, and division.

**Files**  
- Input: `input.txt`  
- Script: `BCD_calculator.py`  
- Output: `output.txt`  

**Prerequisites**  
Ensure you have Python installed on your machine to execute the script. This code was tested with Python 3.8. No external libraries are required.

**How to Use**  
1. Place the `input.txt` file in the same directory as the script. The input should consist of two numbers and an arithmetic operation symbol (+, -, *, /) formatted as shown below:
   ```
   <number1>
   <operation>
   <number2>
   ```
2. Run the script using the command:
   ```bash
   python BCD_calculator.py
   ```
3. Check the `output.txt` file for results.

**Input Format**  
- The first line should contain the first number.
- The second line should contain one of the arithmetic operation symbols: +, -, *, or /.
- The third line should contain the second number.

**Output Format**  
- The result of the operation will be written to `output.txt` in decimal and hexadecimal format.

**Functionality**  
- **Read Input:** Parses numbers and operation symbol from the input file.
- **BCD Conversion:** Converts decimal numbers to BCD format for processing.
- **Arithmetic Operations:** Performs the specified arithmetic operation on the input numbers in BCD format.
- **Write Output:** Writes the operation result in both decimal and hexadecimal format to the output file.

**Limitations**  
- The script does not handle non-numeric inputs or malformed files gracefully.
- Division by zero will result in an error message being written to the output file.
