from fastapi import FastAPI
app = FastAPI()

richest_people_List = {
    "Elon Musk": "280 Billion USD",
    "Jeff Bezos": "200 Billion USD",
    "Bill Gates": "150 Billion USD",
    "Mark Zukerberg": "100 Billion USD",
    "Shell": "20 Billion USD"
}

@app.get("/richest_people") #info.org
def riches_people():
    return richest_people_List