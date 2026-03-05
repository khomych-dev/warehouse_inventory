from fastapi import FastAPI

# Створюємо наш "двигун"
app = FastAPI()

# Головний ендпоінт (корінь сайту)
@app.get("/")
def read_root():
    return {"message": "Warehouse System Online, Bratishka"}

# Ендпоінт для перевірки стану
@app.get("/status")
def get_status():
    return {"status": "Operational", "fuel_level": "100%"}

@app.get('/tools')
def get_tools():
    tools_list = ["Wrench", "Hammer", "Screwdriver", "Multimeter"]
    return {'tools': tools_list}