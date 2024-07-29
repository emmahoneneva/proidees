from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Route definition
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

# Function to run the FastAPI server
def run_fastapi_server():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Run the FastAPI server
if __name__ == "__main__":
    run_fastapi_server()
