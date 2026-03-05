from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Warehouse System Online, Bratishka"}

@app.get("/status")
def get_status():
    return {"status": "Operational", "fuel_level": "100%"}

@app.get('/tools')
def get_tools():
    tools_list = ["Wrench", "Hammer", "Screwdriver", "Multimeter"]
    return {'tools': tools_list}