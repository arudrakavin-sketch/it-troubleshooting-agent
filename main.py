
from typing import TypedDict
from langgraph.graph import StateGraph
import ollama

print("IT Troubleshooting Agent Started")

class TroubleshootingState(TypedDict):
    problem: str
    category:str
    diagnosis: str
    logs: list[str]
    solution: str
    validation: str



def troubleshoot(state: TroubleshootingState):
    problem = state["problem"]

    return {
        "diagnosis": f"Analyzing problem: {problem}",
        "logs": ["Troubleshooting started"]
    }

def diagnose(state: TroubleshootingState):
    problem = state["problem"]
    category = state["category"]
    

    return {
    "diagnosis": f"Possible {category} issue with: {problem}"
}

def categorize(state: TroubleshootingState):
    problem = state["problem"]
    problem_lower = problem.lower()

    if "wifi" in problem_lower or "internet" in problem_lower:
        category = "Network"
    elif "printer" in problem_lower:
        category = "Printer"
    elif "windows" in problem_lower:
        category = "Windows"
    elif any(word in problem_lower for word in ["sound", "hardware", "keyboard", "mouse", "display", "screen", "monitor"]):
        category = "Hardware"
    elif "software" in problem_lower or "application" in problem_lower:
        category = "Software"
    else:
        category = "Other"
    return {
        "category": category
    }

def resolve(state: TroubleshootingState):
    problem = state["problem"]
    diagnosis = state["diagnosis"]

    try:
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": f"""
You are an IT troubleshooting expert.

User problem: {problem}
Diagnosis: {diagnosis}

Give a clear and practical solution.
Provide the solution as simple numbered steps.
"""
                }
            ]
        )

        solution = response["message"]["content"]

    except Exception as e:
        solution = f"Unable to generate AI solution. Error: {e}"

    return {
        "solution": solution
    }

def validate(state: TroubleshootingState):
    solution = state["solution"]

    if not solution.strip():
        validation = "Solution validation failed: Empty solution."

    elif "step" not in solution.lower():
        validation = "Solution validation failed: No troubleshooting steps found."

    else:
        validation = "Solution validated successfully."

    return {
        "validation": validation
    }

graph = StateGraph(TroubleshootingState)

graph.add_node("troubleshoot", troubleshoot)

graph.add_node("diagnose", diagnose)

graph.add_node("categorize", categorize)

graph.add_node("resolve", resolve)

graph.add_node("validate", validate)

graph.add_edge("troubleshoot", "categorize")

graph.add_edge("categorize", "diagnose")

graph.add_edge("diagnose", "resolve")

graph.add_edge("resolve", "validate")

graph.set_entry_point("troubleshoot")

graph.set_finish_point("validate")

app = graph.compile()
problem = input("Enter your IT problem: ")

if not problem.strip():
    print("Please enter a valid IT problem.")
    exit()
if len(problem.split()) < 2:
    print("Please describe your IT problem clearly.")
    exit()
it_keywords = [
    "wifi", "internet", "printer", "windows",
    "laptop", "computer", "keyboard", "mouse",
    "software", "application", "email", "outlook",
    "network"
]


result = app.invoke({
    "problem": problem,
    "category": "",
    "diagnosis": "",
    "logs": [],
    "solution": "",
    "validation": ""
})
print("\n--- IT Troubleshooting Result ---")
print(f"Problem: {result['problem']}")
print(f"Category: {result['category']}")
print(f"Diagnosis: {result['diagnosis']}")
print("\nSolution:")
print(result["solution"])
print(f"\nValidation: {result['validation']}")