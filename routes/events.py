from fastapi import APIRouter, HTTPException, status, Body
from models.events import Event

event_router = APIRouter(
    tags=["Event"]
    )
events = []

@event_router.get("/",response_model=list[Event])
async def retrieve_all_events() -> list[Event]:
    return events

@event_router.get("/{event_id}", response_model=Event)
async def retrieve_event(event_id: int) -> Event:
    for event in events:
        if event.id == event_id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
    
@event_router.post("/new")
async def create_event(event: Event = Body(...)) -> dict:
    if any(e.id == event.id for e in events):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Event with supplied ID already exists"
        )
    
    events.append(event)
    return {
        "message": "Event created successfully",
        "event": event
    }
@event_router.delete("/{event_id}")
async def delete_event(event_id: int) -> dict:
    global events
    events = [event for event in events if event.id != event_id]
    return {
        "message": "Event deleted successfully"
    }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,detail="Event with supplied ID does not exist"
    )
@event_router.delete("/")
async def delete_all_events() -> dict:
    global events
    events.clear()
    return {
        "message": "All events deleted successfully"
    }