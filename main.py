from fastapi import FastAPI, Path, Query, Depends, HTTPException
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


# Client---------------------------------------------------------------------------
@app.get('/get-client/{client_id}', tags=['Client'])
def get_client(client_id, db: Session=Depends(get_db)):
	client = db.query(models.Client).filter(models.Client.id == client_id).first()
	return client

@app.get('/get-all-clients', tags=['Client'])
def get_all_clients( db: Session=Depends(get_db)):
	client = db.query(models.Client).all()
	return client

@app.post('/add-client', tags=['Client'])
def add_client(request: schemas.Client, db: Session=Depends(get_db)):
	new_client = models.Client(**request.dict())
	db.add(new_client)
	db.commit()
	db.refresh(new_client)
	return new_client

@app.delete('/delete-client/{client_id}', tags=['Client'])
def delete_client(client_id, db: Session=Depends(get_db)):
	db.query(models.Client).filter(models.Client.id == client_id).delete(synchronize_session=False)
	db.commit()
	return 'done'

@app.put('/update-client/{client_id}', tags=['Client'])
def update_client(client_id, request: schemas.Client, db: Session=Depends(get_db)):
	client = db.query(models.Client).filter(models.Client.id == client_id).first()

	if not client:
		raise HTTPException(status_code=404, detail=f'Client with id {client_id} not found')

	for key, value in request.dict().items():
		setattr(client, key, value)

	db.commit()
	return 'updated'


# Manager --------------------------------------------------------------------------------------------------------------

@app.get('/get-manager/{manager_id}', tags=['Manager'])
def get_manager(manager_id, db: Session=Depends(get_db)):
	manager = db.query(models.Manager).filter(models.Manager.id == manager_id).first()
	return manager

@app.get('/get-all-managers', tags=['Manager'])
def get_all_managers( db: Session=Depends(get_db)):
	manager = db.query(models.Manager).all()
	return manager

@app.post('/add-manager', tags=['Manager'])
def add_manager(request: schemas.Manager, db: Session=Depends(get_db)):
	manager = models.Manager(**request.dict())
	db.add(manager)
	db.commit()
	db.refresh(manager)
	return manager

@app.delete('/delete-manager/{manager_id}', tags=['Manager'])
def delete_manager(manager_id, db: Session=Depends(get_db)):
	db.query(models.Manager).filter(models.Manager.id == manager_id).delete(synchronize_session=False)
	db.commit()
	return 'done'

@app.put('/update-manager/{manager_id}', tags=['Manager'])
def update_manager(manager_id, request: schemas.Manager, db: Session=Depends(get_db)):
	manager = db.query(models.Manager).filter(models.Manager.id == manager_id).first()

	if not manager:
		raise HTTPException(status_code=404, detail=f'Manager with id {manager_id} not found')

	for key, value in request.dict().items():
		setattr(manager, key, value)

	db.commit()
	return 'updated'





# Table -----------------------------------------------------------------------------------------------------------------
@app.get('/get-table/{table_id}', tags=['Table'])
def get_table(table_id, db: Session=Depends(get_db)):
	table = db.query(models.Table).filter(models.Table.id == table_id).first()
	return table

@app.get('/get-all-tables', tags=['Table'])
def get_all_table( db: Session=Depends(get_db)):
	table = db.query(models.Table).all()
	return table

@app.post('/add-table', tags=['Table'])
def add_table(request: schemas.Table, db: Session=Depends(get_db)):
	table = models.Table(**request.dict())
	db.add(table)
	db.commit()
	db.refresh(table)
	return table

@app.delete('/delete-table/{table_id}', tags=['Table'])
def delete_table(table_id, db: Session=Depends(get_db)):
	db.query(models.Table).filter(models.Table.id == table_id).delete(synchronize_session=False)
	db.commit()
	return 'done'

@app.put('/update-table/{table_id}', tags=['Table'])
def update_table(table_id, request: schemas.Table, db: Session=Depends(get_db)):
	table = db.query(models.Table).filter(models.Table.id == table_id).first()

	if not table:
		raise HTTPException(status_code=404, detail=f'Table with id {table_id} not found')

	for key, value in request.dict().items():
		setattr(table, key, value)

	db.commit()
	return 'updated'
 



# Table Reservation------------------------------------------------------------------------------------------------------
@app.get('/get-reservation/{reservation_id}', tags=['Table Reservation'])
def get_table(reservation_id, db: Session=Depends(get_db)):
	reservaton = db.query(models.TableReservation).filter(models.TableReservation.id == reservation_id).first()
	return reservaton

@app.get('/get-all-reservations', tags=['Table Reservation'])
def get_all_reservations( db: Session=Depends(get_db)):
	reservations = db.query(models.TableReservation).all()
	return reservations

@app.post('/reserve-table/', tags=['Table Reservation'])
def reserve_table(request: schemas.TableReservation, db: Session=Depends(get_db)):
	reservation = models.TableReservation(**request.dict())
	reservation.reservation_date = datetime.now()
	db.add(reservation)
	db.commit()
	db.refresh(reservation)
	return reservation
	

@app.delete('/delete-reservation/{reservation_id}', tags=['Table Reservation'])
def delete_reservation(reservation_id, db: Session = Depends(get_db)):
    # Check if the reservation exists
    reservation = db.query(models.TableReservation).filter(models.TableReservation.id == reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail=f'Reservation with id {reservation_id} not found')


    # Delete the reservation and detach it from the session
    db.delete(reservation)
    db.commit()
    db.expunge(reservation)
    return 'done'


@app.put('/update-reservation/{reservation_id}', tags=['Table Reservation'])
def update_reservation(reservation_id, request: schemas.TableReservation, db: Session=Depends(get_db)):
	reservation = db.query(models.TableReservation).filter(models.TableReservation.id == reservation_id).first()

	if not reservation:
		raise HTTPException(status_code=404, detail=f'Reservation with id {reservation_id} not found')

	for key, value in request.dict().items():
		setattr(reservation, key, value)

	db.commit()
	return 'updated'






































'''
Menu = {}

@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(description="id of item that you want to get", gt=0)):
	return Menu[item_id]

@app.get('/get-all/')
def get_all():
	return Menu

app.get('/get-by-name')
def get_item(name: str ):
	for item_id in Menu:
		if Menu[item_id].name == name:
			return Menu[item_id]
	return {'Data': 'Not found'}




@app.post('/create-item/{item_id}')
def create_item(item_id: int,item: schemas.Item):
	if item_id in Menu:
		return {'Error':'Item ID already exists!'}
	Menu[item_id] = item
	return Menu[item_id]

@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: schemas.UpdateItem):
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
'''