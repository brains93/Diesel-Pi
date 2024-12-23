#!/bin/bash
#!/bin/bash
echo "Check if is root"
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
# Get the current working directory
CWD=$(pwd)
python pip install -r requirements.txt
# Copy the folders to /var/www/
cp -r "$CWD/api" /var/www/
cp -r "$CWD/webapp" /var/www/

# Create a service file for the Flask app
cat <<EOL > /etc/systemd/system/dieselpiapi.service
[Unit]
Description=DieselPi API
After=network.target

[Service]
User=root
WorkingDirectory=/var/www/api
ExecStart=/usr/bin/python -m uvicorn api:app --host 0.0.0.0 --port 8000
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
EOL

# Create a service file for the FastAPI app
cat <<EOL > /etc/systemd/system/dieselpiapp.service
[Unit]
Description=DieselPi frontend
After=network.target

[Service]
User=root
WorkingDirectory=/var/www/webapp
ExecStart=/usr/local/bin/flask --app webapp run --host=0.0.0.0 --port=5000
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd to apply the new service files
systemctl daemon-reload

# Enable and start the Flask app service
systemctl enable dieselpiapp.service
systemctl start dieselpiapp.service

# Enable and start the FastAPI app service
systemctl enable dieselpiapi.service
systemctl start dieselpiapi.service
rm -r ../DieselPi/
echo "Setup complete."