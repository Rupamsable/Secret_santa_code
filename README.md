# Secret_santa_code
I have done secret santa code using python.

1. Employee Class: Represents each employee with their name, email, and assigned secret child.
2. SecretSantaAssigner Class: Handles the logic for assigning secret children while ensuring constraints.
3. FileHandler Class: Reads input files and writes output CSV.
4. Main Function:
    Reads employee and previous assignment data.
    Runs the assignment process.
    Writes the new assignments to an output file.
5. Error Handling:
    Handle invalid CSV format, missing fields, or empty files.
6. Input Parsing: Read the employee data from a CSV file.
7. Validation & Constraints Handling:
    Ensure every employee gets exactly one secret child.
    Avoid self-assignments.
    Avoid repeating last year's assignments.
8. Random Assignment Algorithm:
    Use a shuffled list to distribute secret children.
    If constraints are violated, retry until a valid assignment is found.
