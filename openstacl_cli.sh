#!/bin/bash
sudo apt update
sudo apt install python3-openstackclient

SERVICES=(cinder glance heat neutron nova octavia sahara)

for service in "${SERVICES[@]}"; do
    echo "Установка клиента для $service..."
    apt install "python3-${service}client"
done
