#!/usr/bin/env bash
set -euo pipefail

# Kullanım: ./run_mavros.sh [PORT]
# Varsayılan: 14540 (PX4 SITL default UDP portu)
PORT="${1:-14540}"

# ROS 2 ortamı
if [ -f "/opt/ros/humble/setup.bash" ]; then
  source /opt/ros/humble/setup.bash
fi

URL="udp://:${PORT}@"
echo "[MAVROS] starting mavros_node with fcu_url=${URL}"

# Namespace: /mavros
exec ros2 run mavros mavros_node --ros-args \
  -r __ns:=/mavros \
  -p fcu_url:="${URL}" \
  -p fcu_protocol:="v2.0" \
  -p tgt_system:=1 \
  -p tgt_component:=1
