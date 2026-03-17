import graphviz

def generate_architecture():

    dot = graphviz.Digraph()

    dot.node("User","User")
    dot.node("UI","Streamlit UI")
    dot.node("AI","AI Engine")
    dot.node("LLM","Groq LLM")
    dot.node("DB","Database")

    dot.edges([
        ("User","UI"),
        ("UI","AI"),
        ("AI","LLM"),
        ("AI","DB")
    ])

    return dot