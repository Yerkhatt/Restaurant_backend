from fastapi import FastAPI, Path, Query
from schema import *

app = FastAPI()



Menu = {}



@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(description="id of item that you want to get", gt=0)):
	return Menu[item_id]

@app.get('/get-all/')
def get_all():
	return Menu

'''@app.get('/get-by-name')
def get_item(name: str ):
	for item_id in Menu:
		if Menu[item_id].name == name:
			return Menu[item_id]
	return {'Data': 'Not found'}'''




@app.post('/create-item/{item_id}')
def create_item(item_id: int,item: Item):
	if item_id in Menu:
		return {'Error':'Item ID already exists!'}
	Menu[item_id] = item
	return Menu[item_id]

@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: UpdateItem):
	if item_id not in Menu:
		return {'Error': 'item ID does not exist'}

	if item.price != None:
		Menu[item_id].price = item.price
		
	if item.calories != None:
		Menu[item_id].calories = item.calories

	if item.origin != None:
		Menu[item_id].origin = item.origin
		
	return Menu[item_id]

@app.delete('/delete-item')
def delete_item(item_id: int = Query(..., description="The ID of the item to delete")):
	if item_id not in Menu:
		return {"Error": "ID does not exist!"}
	
	del Menu[item_id]
	return {"Success": "Item deleted!"}
