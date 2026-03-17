import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key="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")

def ask_ai(prompt):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content


def review_code(code,language):

    prompt=f"""
Review this {language} code.

Find bugs, performance issues and improvements.

Code:
{code}
"""
    return ask_ai(prompt)


def explain_code(code):

    prompt=f"""
Explain the code line by line.

Code:
{code}
"""
    return ask_ai(prompt)


def debug_code(code):

    prompt=f"""
Debug this code and explain the issue.

Code:
{code}
"""
    return ask_ai(prompt)


def security_scan(code):

    prompt=f"""
Check this code for vulnerabilities like SQL injection,
unsafe input and hardcoded passwords.

Code:
{code}
"""
    return ask_ai(prompt)


def complexity(code):

    prompt=f"""
Analyze time complexity and space complexity.

Code:
{code}
"""
    return ask_ai(prompt)


def convert_code(code,target):

    prompt=f"""
Convert the following code to {target}.

Code:
{code}
"""
    return ask_ai(prompt)


def generate_tests(code):

    prompt=f"""
Generate unit tests for the following code.

Code:
{code}
"""
    return ask_ai(prompt)


def auto_fix(code):

    prompt=f"""
Rewrite this code fixing bugs and optimizing it.

Code:
{code}
"""
    return ask_ai(prompt)
def bug_heatmap(code):

    lines = code.split("\n")

    heatmap = []

    for i,line in enumerate(lines):

        score = 1

        if "for" in line:
            score = 3

        if "while" in line:
            score = 4

        if "eval" in line:
            score = 5

        heatmap.append(score)

    return heatmap
def complexity_analysis(code):

    prompt = f"""
Analyze the following code.

Provide:
1. Time complexity
2. Space complexity
3. Optimization suggestions

Code:
{code}
"""

    return ask_ai(prompt)