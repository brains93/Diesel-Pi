import RPi.GPIO as GPIO
import threading
import time
import queue
import logging
from w1thermsensor import W1ThermSensor

class HeaterControl:
    def __init__(self):
        self.stop_event = threading.Event()
        self.value_queue = queue.Queue()
        self.pump_running = None  # Make pump_running an instance variable
        self.sensors = W1ThermSensor.get_available_sensors()
        # Pin definitions
        self.motor_pwm_pin = 18  # PWM pin for motor speed control
        self.relay1_pin = 23     # Pin for glowplug relay
        self.relay2_pin = 24     # Pin for pump solid state relay
        self.sensor1 = self.sensors[0]
        self.sensor2 = self.sensors[1]

        # GPIO setup
        GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
        GPIO.setup(self.motor_pwm_pin, GPIO.OUT)
        GPIO.setup(self.relay1_pin, GPIO.OUT)
        GPIO.setup(self.relay2_pin, GPIO.OUT)

        # Initialize PWM for motor control
        self.motor_pwm = GPIO.PWM(self.motor_pwm_pin, 25000)  # Set frequency to 25kHz
        self.motor_pwm.stop()  


    # Function to set motor speed (0 to 100)
    def set_fan_speed(self, speed: int):
        if 0 <= speed <= 100:
            logging.info(f"Setting fan speed to: {speed}")
            self.motor_pwm.ChangeDutyCycle(speed)
        else:
            raise ValueError("Speed must be between 0 and 100")

    # Function to activate relay 1
    def activate_glowplug(self):
        logging.info("Activating glowplug.")
        GPIO.output(self.relay1_pin, GPIO.HIGH)

    # Function to deactivate relay 1
    def deactivate_glowplug(self):
        logging.info("Deactivating glowplug.")
        GPIO.output(self.relay1_pin, GPIO.LOW)

    # Function to set pump speed
    def set_pump_speed(self, speed: int):
        logging.info(f"Setting pump speed to: {speed}")
        self.value_queue.put(speed)
        return 0

    # Function to calculate pump speed based on fan speed
    def calculate_pump_speed(self, fan_speed: int):
        max_pump_speed = 1.0  # seconds at 10% fan speed
        min_pump_speed = 0.1  # seconds at 100% fan speed
        pump_speed = max_pump_speed - ((fan_speed - 10) / 90) * (max_pump_speed - min_pump_speed)
        return pump_speed

    # Function to deactivate relay 2
    def stop_pump(self):
        logging.info("Stopping pump.")
        self.stop_event.set()
        return 0

    # Function to get the state of the heater
    def get_state(self):
        room_temp = self.sensor1.get_temperature()
        heater_temp = self.sensor1.get_temperature()
        if self.pump_running is None or not self.pump_running.is_alive():
            return 1, room_temp, heater_temp
        else:
            return 0, room_temp, heater_temp
        
    # Function to get the temperature from the DS18B20 sensor
    def get_temperature(self, sensor_number: int) -> float:
            """
            Get the temperature from the specified DS18B20 sensor.
            :param sensor_number: The sensor number (1 or 2).
            :return: The temperature in Celsius.
            """
            if sensor_number == 1:
                temperature = self.sensor1.get_temperature()
            elif sensor_number == 2:
                temperature = self.sensor2.get_temperature()
            else:
                raise ValueError("Invalid sensor number. Use 1 or 2.")
            temperature_s = f"{temperature:.1f}"
            logging.info(f"Temperature read from DS18B20 sensor {sensor_number}: {temperature}°C")
            return temperature_s
    
    # Function to start the heater
    def start_heater(self):
        logging.info("Starting heater.")
        if self.pump_running is None or not self.pump_running.is_alive():
            self.start_fan() 
            self.activate_glowplug()
            self.set_fan_speed(50)  # Example speed
            time.sleep(30)  # should be 30 sec
            self.start_pump(1)
            time.sleep(10)  # should be 10 sec
            self.deactivate_glowplug()
        else:
            logging.info("Heater already running.")

    # Function to stop the heater
    def stop_heater(self):
        if self.pump_running is None or not self.pump_running.is_alive():
            logging.info("Heater already stopped.")
        else:
            self.stop_pump()
            self.set_fan_speed(100)
            # This is to cool the heater down after operation
            time.sleep(30)
            self.stop_fan()
            logging.info("Heater stopped.")

    def start_fan(self):
        self.motor_pwm.start(0)

    def stop_fan(self):
        self.motor_pwm.stop()

    def pump(self):
        try:
            while not self.stop_event.is_set():
                logging.debug(self.stop_event)
                try:
                    speed = self.value_queue.get(timeout=0.1)
                    logging.info(f"Received new value: {speed}")
                except queue.Empty:
                    logging.debug("No new value received.")
                    GPIO.output(self.relay2_pin, GPIO.HIGH)
                    time.sleep(0.1)
                    GPIO.output(self.relay2_pin, GPIO.LOW)
                    logging.debug(f"pump pulsing for {speed} seconds.")
                    time.sleep(speed)
        finally:
            GPIO.output(self.relay2_pin, GPIO.LOW)
            logging.info("Pump stopped.")

    def start_pump(self, speed: int):
        logging.info("Starting pump.")
        if self.pump_running is None or not self.pump_running.is_alive():
            self.stop_event.clear()
            self.value_queue.put(speed)
            logging.info("Starting pump thread.")
            self.pump_running = threading.Thread(target=self.pump)
            self.pump_running.start()
            logging.info("Pump started.")
            return self.pump_running
        else:
            logging.info("Pump already running.")
            return self.pump_running

# Example usage
if __name__ == "__main__":
    heater_control = HeaterControl()
    try:
        heater_control.start_heater()
        time.sleep(10)  # Run for 10 seconds
        heater_control.stop_heater()
    finally:
        GPIO.cleanup()  # Clean up GPIO settings
