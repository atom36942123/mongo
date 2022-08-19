#router
from fastapi import APIRouter
router=APIRouter(tags=["api"])



#create
from fastapi import Request
from fastapi import Body
@router.post("/create-user")
async def create_user(request:Request,payload:dict=Body(...)):
    response=await database.user.insert_one(payload)
    return {"status":"true","message":"created"}





#read
@router.get("/read-user-all")
async def read_user_all(request:Request):
    user_list=[]
    async for i in database.user.find().limit(3):
        i['_id']=str(i['_id'])
        user_list.routerend(i)
    return user_list

from bson import ObjectId
from fastapi import HTTPException
@router.get("/read-user-single-id/{id}")
async def read_user_single_id(request:Request,id:str):
    response=await database.user.find_one({"_id": ObjectId(id)})
    if response:
        response['_id']=str(response['_id'])
    return response

from fastapi import Request
@router.get("/read-user-single-name/{name}")
async def read_user_single_name(request:Request,name:str):
    response=await database.user.find_one({"name":name})
    if response:
        response['_id']=str(response['_id'])
    return response



    



#update
@router.put("/update-user/{id}")
async def update_user(request:Request,id:str,payload:dict=Body(...)):
    response=await database.user.update_one({"_id":ObjectId(id)},{"$set":payload})
    return response.modified_count






#delete
@router.delete("/delete-user/{id}")
async def delete_user(request:Request,id:str):
    response=await database.user.delete_one({"_id":ObjectId(id)})
    return response.deleted_count
