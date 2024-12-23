import fastapi
from functions import HeaterControl
import logging
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='/var/log/api.log')

app = fastapi.FastAPI()

class FanSpeed(BaseModel):
    speed: int

heater_control = HeaterControl()
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "You should not be here. Go to /docs to see the API documentation."}

@app.get("/state/")
def get_state():
    status = heater_control.get_state()
    if status[0] == 0:
        return {"message": "heater is on.", "room_temp": status[1], "heater_temp": status[2]}
    else:
        return {f"message": "heater is off.", "room_temp": status[1], "heater_temp": status[2]}

@app.post("/fan/")
def set_fan_speed(fan_speed: FanSpeed):
    speed = fan_speed.speed
    heater_control.set_fan_speed(speed)
    return {"message": "Fan speed set.", "level": speed}

@app.post("/heater/speed")
def set_fan_speed(fan_speed: FanSpeed):
    fan_speed = fan_speed.speed
    heater_control.set_fan_speed(fan_speed)
    pump_speed = heater_control.calculate_pump_speed(fan_speed)
    heater_control.set_pump_speed(pump_speed)

    return {"message": "Fan speed set.", "fan_speed": fan_speed, "pump_speed": pump_speed}


@app.post("/pump/")
def set_pump_speed(speed: int):
    heater_control.set_pump_speed(speed)
    return {"message": "Pump speed set."}

@app.post("/heater/on")
def start_heater():
    heater_control.start_heater()
    return {"message": "Heater started."}

@app.post("/heater/off")
def stop_heater():
    heater_control.stop_heater()
    return {"message": "Heater stopped."}