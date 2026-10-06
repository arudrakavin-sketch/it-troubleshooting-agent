# IT Troubleshooting Agent

An AI-powered IT Troubleshooting Agent built with Python, LangGraph, Ollama, and Llama 3.2.

## Overview

This project accepts an IT-related problem from the user, categorizes the issue, generates a possible diagnosis, uses a local Llama 3.2 model to generate practical troubleshooting steps, and validates the generated solution.

The application runs locally using Ollama, so no paid LLM API is required.

## Architecture

User Problem
↓
Troubleshoot
↓
Categorize
↓
Diagnose
↓
Resolve with Llama 3.2
↓
Validate
↓
Final Result

## Tech Stack

- Python
- LangGraph
- Ollama
- Llama 3.2 (3B)
- TypedDict
- PowerShell
- VS Code / Antigravity

## Features

- IT problem input validation
- Automatic problem categorization
- Diagnosis generation
- Local LLM integration
- AI-generated troubleshooting steps
- Error handling
- Solution validation
- Clean user-friendly output
- No paid API required

## Supported Categories

- Network
- Printer
- Windows
- Hardware
- Software
- Other

## Example

Input:

~~~text
printer is not working
~~~

The agent:

1. Categorizes the issue as Printer
2. Generates a possible diagnosis
3. Sends the problem and diagnosis to Llama 3.2
4. Generates practical troubleshooting steps
5. Validates the generated solution

## Project Structure

~~~text
it-troubleshooting-agent/
│
├── .venv/
├── .gitignore
├── app.py
├── main.py
└── README.md
~~~

## How to Run

### 1. Install Ollama

Install Ollama and make sure the Llama 3.2 model is available.

~~~bash
ollama pull llama3.2:3b
~~~

### 2. Install Python dependencies

~~~bash
py -m pip install langgraph ollama
~~~

### 3. Run the application

~~~bash
py main.py
~~~

### 4. Enter an IT problem

Example:

~~~text
wifi is not working
~~~

## LLM Flow

The application uses:

~~~text
Python
   ↓
Ollama
   ↓
Llama 3.2
   ↓
AI Troubleshooting Solution
~~~

## Error Handling

The application uses exception handling around the Ollama API call to prevent the application from crashing when an AI generation error occurs.

## Validation

The generated solution is checked before the final result is displayed.

## Project Goal

The goal of this project is to demonstrate practical implementation of an AI agent workflow using Python, LangGraph, and a locally running Large Language Model.

## Future Improvements

- Add more IT categories
- Add log/file analysis
- Add system diagnostic tools
- Improve solution validation
- Add a web interface
- Add conversation memory