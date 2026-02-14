#!/bin/bash

mkdir -p ./mount

rclone mount comp_login: ./mount \
    --vfs-cache-mode writes

# rclone mount comp_login: ./mount \
#     --vfs-cache-mode full \
#     --vfs-write-back 5s \
#     --dir-cache-time 5m \
#     --attr-timeout 5m \
#     --buffer-size 16M

