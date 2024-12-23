# Diesel Pi

## Overview

Diesel Pi is a project designed to control a Diesel heater system using a Raspberry Pi. The system includes functionalities power the heater on and off, set the heat level, monitor the heater temp and room temp. The project consists of several components, including a web interface, API, and hardware control functions.

## Video overview 
### Code

<video width="640" height="480" controls>
  <source src="https://youtu.be/jhlhRl0yT9Y" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Hardware
-  video TODO

## TODO
- Add the ability to set a target room temp 
- Add the ability to set a schedule to keep the room at set temps during set times
- Add a low fuel warning
- Make the UI actually nice to look at (may need help here)


## Video Tutorial

Here is a video tutorial on how to set up Diesel Pi:




## Getting Started

#### Software
- Python 3.x
- Flask
- FastAPI
- RPi.GPIO (for Raspberry Pi)

#### Hardware
- Raspbery pi 
- 5v Relay [link ](https://www.amazon.co.uk/DollaTek-Channel-optocoupler-Support-Trigger/dp/B07DJ4NRC1?crid=2LMHPIOX6VJ5E&dib=eyJ2IjoiMSJ9.qtZ0Q_k5Ql7B0ggHLtRrclXCjwLaGcwODm7qtuvlsSOl0f0Dy1nlajZdF92F_pQME-IJHNZau9KaFJy36zwyongoZyFBoDtum7dx6Cqj_M9KozlaTIUuPG2n9mmk0sFyrOd-W0N_17SelmyveXb7u39sGkJKNMlYqrvLTHCnSHQzp_c8j-3J61JQkPWwYsuSqAIk-lQIlF9hf96femxDgT5txTlGmWaIvFTbJsywIKnTnk60vudau0SsrJsvLwKPnDryt2h0LIY9EmNwHx8EzVocIoWmejaSNFNyTzkDseE1fEHAIymVYy9Y5tsAeN3FKCHosuZdOwwohzirNY_CbjNkVOIEB3FskPrR59Cvndx1emEWz0_lChFyJkL0pVijfk7vDk9384Pg_WFqU3jwfuoP-Z2eJ4zMAbh3_wfeL2NNJaUyPFfXExIxf1tSIQi8.XNWSNor-G--sXbUAjxoQnKgX7HQK4sKSozEBaZXzqak&dib_tag=se&keywords=5v+relay&qid=1734906861&sprefix=5v+relay%2Caps%2C148&sr=8-7)
- 5v Solid State Relay [link ](https://www.amazon.co.uk/1-Channel-Trigger-Module-250VAC-Output/dp/B07QS44SYH?crid=2YBIZE5I11H2P&dib=eyJ2IjoiMSJ9.NxmNsIsLuYnvd6rwOAvpszpUiSVkI2ijAYeODiIaFmWWwRlrePaLXOZVOrmVSdOulMdo9947LWbtLldx6CpY70-sly8D4FpddLHpJ1jY5V-8SODJ-f0dTjxicgid6QNrjsrz0kpRdaUcPJ0dgxuUonXEpKyiYHpReSMmcXJdzgWKMoCr_vfG1JGGfferRpuu5_IhA5DiKAnE1w6AOFvwmgFKnSWzZnAxqIVu7IBZwwbRwr0FzYIjct6k2TIpsMplhfdvoSv5WV6ilqmh9bwdIasAsiapbvHjmsTDrvq9ZHNbRJcWMV5X2jZkjXJjSh_YS7_b6u-UZQqZ7BVEerKykdhboNx8m_cibsLTpUckS9RtJb6HQzJoS0EwDr-HMMz05gT8O-Lw9t0AM2s9XaRsNBXwLqFukWDhajtOU-wxm21naSEmxsd9fJpctZMMk0AQ.NDFaGoBbRIs7SgGMd1tAN5Qr9XmR3GkxpW6YRJIkw04&dib_tag=se&keywords=5v+solid+state+relay&nsdOptOutParam=true&qid=1734906840&sprefix=5v+solid+s%2Caps%2C115&sr=8-6)
- PWM Motor controler [link ](https://www.amazon.co.uk/Driver-Controller-Stepper-H-Bridge-suitable/dp/B09T973C76?crid=V1RQZ4NISXPW&dib=eyJ2IjoiMSJ9.5WsPzxYmGKPePHwnhQliPS9FY1DKcGqJ5S7GzJV3qfB9SmoFEgb3nuRwNom6KOgnrfRhHtlYbFeWyEPri--zJ6nHm0WjbIO9kJzJM_zPz4dZT75B-ujt9rfDF06ECPV8KetauhFfML_A627yn-3gvAv01q5fscr7SFeduorr-UZcMY4ZAz-Ijpx77PVDcRCwvd5GEPVfajqSjjEQQC7xmWP4XBf4QgIWR3F0wP60krNe0an-OzhR5CRRXb1l4kGbe__SAfcS-JUFKSdAx70XFpNLYhAF-2lqvwN955rHcUSGPeD5NEJbm-r4GIuwrV2cEC7frkyT_lH_UxWsmoWaU26f5sxwi7aeFSS5ZMjAh25XnKZpyVZpk0d4Oa44HJRSTqi3H7e42oN_ZAsVm7c5wDvCFG48TBlFW7wTZ8hlqor6_vuPvlszB-NIxHWglIMr.AHk2ivxb1XFV17jo3P2myfZM6ZuogE5woHE2bvGJ0Mw&dib_tag=se&keywords=motor+driver&qid=1734906770&sprefix=motor+driver%2Caps%2C100&sr=8-7)
- PSU (only needed if not on battery power) [link](https://www.amazon.co.uk/inShareplus-Universal-Regulated-Switching-Transformer/dp/B088ZQT8TD?dib=eyJ2IjoiMSJ9.P-lKkGBNHKTKRpThhPB4ZjOCihNbDIGP1pkjS98yhopkenlddPtub78g8ja-s7wwC9_Ms-l0MPwtfsBHzzG1qg_gpkIkKTqJa5NMB4por9-ofNY4k2teHkOe178v0m374yTfvwboLgox7AGt_E3lWlGCkx7I9Ao4nS-DTgEJ3MGWIdGu40q9BiugMM-cD0euWB57yc771v6RuB-k-2rgTMjRIb-L1P50xP05IM9obYc.KG6j90Waj1bHICfnTB_hUN6XbdqZjlKTJ6AzaetV4X8&dib_tag=se&keywords=12V%2B10A%2BPower%2BSupply&qid=1734992850&sr=8-4&th=1)

### Wiring 
The hardware should be wired up accordingly (Diagram TODO)
- Relay to pin 23 + 5v
- Solid state relay to pin 24 + 5v
- motor controller to pin 18 + 5v
- The two sensors to pin 7 + 3.3v

### Installation 
Installation is handled by a setup script, clone or curl the repo, run that and it will install the python librarys and setup the two applications as services on the machine.
```
chmod +x ./setup.sh
sudo ./setup.sh
```


## Files
This bit was AI generated. Proper outline is still TODO 
### 1. `index.html`

This file contains the HTML and JavaScript code for the web interface of the heater control dashboard. It provides a user-friendly interface to control the heater, set fan speed, and schedule temperatures for different days of the week.

- **Key Features:**
  - Start, stop, and prime the heater.
  - Adjust the heater level using a slider.
  - Display the current heater and room temperature.
  - Schedule temperatures for different days of the week.

### 2. `webapp.py`

This file contains the Flask application that serves the web interface. It uses Flask-CORS to handle Cross-Origin Resource Sharing (CORS) and renders the `index.html` file.

- **Key Features:**
  - Serves the web interface.
  - Handles CORS to allow cross-origin requests.

### 3. `api.py`

This file contains the FastAPI application that provides the API endpoints for controlling the heater system. It includes endpoints to get the heater state, set fan speed, set pump speed, and start/stop the heater.

- **Key Features:**
  - Provides API endpoints for controlling the heater system.
  - Handles CORS to allow cross-origin requests.
  - Logs API requests and responses.

### 4. `functions.py`

This file contains the hardware control functions for the heater system. It includes functions to set fan speed, activate/deactivate the glowplug, start/stop the pump, and start/stop the heater. It uses threading to handle concurrent operations.

- **Key Features:**
  - Controls the fan speed using PWM.
  - Activates and deactivates the glowplug.
  - Starts and stops the pump using threading.
  - Manages the heater state and transitions.

### 5. `styles.css`

This file contains the CSS styles for the web interface. It is linked in the `index.html` file and provides styling for the dashboard components.

- **Key Features:**
  - Styles the heater control dashboard.
  - Provides a cohesive look and feel for the web interface.



