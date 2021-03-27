#!/bin/bash
rm *.log
while true; do
    jetforce --hostname biomimetic.me --host  173.255.250.253  --tls-certfile /etc/letsencrypt/live/biomimetic.me/fullchain.pem --tls-keyfile /etc/letsencrypt/live/biomimetic.me/privkey.pem 
done
