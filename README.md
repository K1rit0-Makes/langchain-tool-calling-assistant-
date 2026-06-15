# AI-Powered College Assistant

A LangChain Tool Calling Agent developed using Python, Ollama, and Qwen 3.5. The assistant automatically identifies user requests, selects the appropriate tool, executes it, and returns a natural language response.

## Features

### 1. Attendance Calculator
Inputs:
- Total Classes
- Attended Classes

Outputs:
- Attendance Percentage
- Exam Eligibility Status

Rule:
- Attendance ≥ 75% → Eligible for Exam
- Attendance < 75% → Not Eligible for Exam

---

### 2. Result Calculator

Inputs:
- Marks of 5 Subjects

Outputs:
- Average Marks
- Grade
- Pass/Fail Status

Grade Rules:

| Average Marks | Grade |
|--------------|--------|
| ≥ 90 | A |
| 75–89 | B |
| 60–74 | C |
| < 60 | D |

Pass Rule:
- Average ≥ 50 → Pass
- Average < 50 → Fail

---

### 3. Fee Balance Calculator

Inputs:
- Total Course Fee
- Amount Paid

Output:
- Pending Fee Amount

---

### 4. Library Fine Calculator

Input:
- Number of Delayed Days

Output:
- Fine Amount

Rule:

Fine = ₹5 × Delayed Days

---

### 5. Hostel Fee Calculator

Inputs:
- Monthly Hostel Fee
- Number of Months Stayed

Output:
- Total Hostel Fee

---

### 6. Student Information Tool (Bonus)

Input:
- Student ID

Output:
- Student Details retrieved from a Python dictionary

---

## Tech Stack

- Python
- LangChain
- Ollama
- Qwen 3.5
- Tool Calling Agents

## LangChain Components Used

- `@tool`
- `ChatPromptTemplate`
- `create_tool_calling_agent()`
- `AgentExecutor`
- `ChatOllama`
- Tool Calling

## Architecture

```text
User Query
     ↓
LangChain Agent
     ↓
Tool Selection
     ↓
Tool Execution
     ↓
Result Processing
     ↓
Final Response
```

## Example Multi-Tool Query

Input:

```text
I attended 80 classes out of 100.
My marks are 90, 85, 88, 92 and 95.
My course fee is 60000 and I paid 45000.

Provide:
1. Attendance Status
2. Grade
3. Pending Fee
```

Agent Execution:

```text
attendance_calculator
result_calculator
fee_balance_calculator
```

Output:

```text
Attendance Percentage: 80%
Exam Status: Eligible for Exam

Average Marks: 90
Grade: A
Result: Pass

Pending Fee Amount: ₹15000
```

## Screenshots

Execution screenshots for all required test cases are available in the `screen shots` folder.

## Project Objective

The objective of this project is to demonstrate how LangChain Tool Calling Agents can automatically select and execute the correct tools based on natural language user requests without requiring the user to explicitly choose a function.

## Author

S.Y. Krish Vinayaha Samithrej

Department of Mechatronics and Automation
