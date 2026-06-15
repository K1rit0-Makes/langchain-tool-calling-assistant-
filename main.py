from langchain.tools import tool
from langchain.agents import (
    AgentExecutor,
    create_tool_calling_agent
)
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


# =====================================
# TOOL 1 - ATTENDANCE
# =====================================

@tool
def attendance_calculator(
    total_classes: int,
    attended_classes: int
):
    """Calculate attendance percentage and exam eligibility."""

    percentage = (
        attended_classes / total_classes
    ) * 100

    status = (
        "Eligible for Exam"
        if percentage >= 75
        else "Not Eligible for Exam"
    )

    return (
        f"Attendance Percentage: {percentage:.2f}%\n"
        f"Exam Status: {status}"
    )


# =====================================
# TOOL 2 - RESULT
# =====================================

@tool
def result_calculator(
    mark1: float,
    mark2: float,
    mark3: float,
    mark4: float,
    mark5: float
):
    """Calculate average marks, grade and pass/fail status."""

    average = (
        mark1 +
        mark2 +
        mark3 +
        mark4 +
        mark5
    ) / 5

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    status = (
        "Pass"
        if average >= 50
        else "Fail"
    )

    return (
        f"Average Marks: {average:.2f}\n"
        f"Grade: {grade}\n"
        f"Result: {status}"
    )


# =====================================
# TOOL 3 - FEE BALANCE
# =====================================

@tool
def fee_balance_calculator(
    total_fee: float,
    amount_paid: float
):
    """Calculate pending fee amount."""

    pending = total_fee - amount_paid

    return (
        f"Pending Fee Amount: ₹{pending:.2f}"
    )


# =====================================
# TOOL 4 - LIBRARY FINE
# =====================================

@tool
def library_fine_calculator(
    delayed_days: int
):
    """Calculate library fine amount."""

    fine = delayed_days * 5

    return (
        f"Library Fine Amount: ₹{fine}"
    )


# =====================================
# TOOL 5 - HOSTEL FEE
# =====================================

@tool
def hostel_fee_calculator(
    monthly_fee: float,
    months_stayed: int
):
    """Calculate total hostel fee."""

    total = monthly_fee * months_stayed

    return (
        f"Total Hostel Fee: ₹{total:.2f}"
    )


# =====================================
# BONUS TOOL
# =====================================

students = {
    "101": {
        "name": "Kirito",
        "department": "Mechatronics"
    },
    "102": {
        "name": "Akhil",
        "department": "CSE"
    }
}


@tool
def student_information(
    student_id: str
):
    """Retrieve student details using student ID."""

    if student_id in students:
        return str(students[student_id])

    return "Student not found."


# =====================================
# TOOLS
# =====================================

tools = [
    attendance_calculator,
    result_calculator,
    fee_balance_calculator,
    library_fine_calculator,
    hostel_fee_calculator,
    student_information
]


# =====================================
# MODEL
# =====================================

llm = ChatOllama(
    model="qwen3.5:latest",
    temperature=0
)


# =====================================
# PROMPT
# =====================================

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI College Assistant.

Always use tools whenever calculations are required.

Use one or more tools if needed.

Return clear answers.
"""
        ),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ]
)


# =====================================
# AGENT
# =====================================

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)


# =====================================
# EXECUTOR
# =====================================

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


# =====================================
# TEST QUERY
# =====================================

response = agent_executor.invoke(
    {
        "input": """
Hostel fee is 6000 per month and I stayed for 5 months. Calculate my hostel fee.N
"""
    }
)
print("\nFINAL ANSWER:\n")
print(response["output"])