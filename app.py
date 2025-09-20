from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/add")

def add(a, b):
    """Add two numbers and return the result."""
    result = float(a) + float(b)
    return {"operation": "add", "a": a, "b": b, "result": result}   

@app.get("/subtract")
def subtract(a, b):
    """Subtract b from a and return the result."""
    result = float(a) - float(b)
    return {"operation": "subtract", "a": a, "b": b, "result": result}

# Main program
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9321)


