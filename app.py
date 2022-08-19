#app
from fastapi import FastAPI
app=FastAPI()

#mongo
import motor.motor_asyncio
mongo_url="mongodb://localhost:27017"
mongo_url_client=motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
database=mongo_url_client.atom

#root
@app.get("/")
async def root():
    return {"message":"Welcome to root"}
 
#router
from api import router
app.include_router(router)






        
    
