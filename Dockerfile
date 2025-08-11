FROM osrf/ros:humble-desktop
SHELL ["/bin/bash", "-c"]

# Temel + Gazebo + GStreamer dev + colcon + pytest
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    git build-essential cmake ninja-build wget zip python3-pip \
    python3-pytest python3-colcon-common-extensions \
    gazebo libgazebo-dev libeigen3-dev libopencv-dev libprotobuf-dev protobuf-compiler \
    # GStreamer dev (sitl_gazebo için şart)
    libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
    # runtime yardımcıları
    gstreamer1.0-tools gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
    ros-humble-launch-testing ros-humble-launch-testing-ros \
    iproute2 net-tools && \
    rm -rf /var/lib/apt/lists/*

# Py tarafı
RUN pip3 install --no-cache-dir mavsdk pytest-timeout

# ROS entrypoint
RUN printf '%s\n' '#!/usr/bin/env bash' \
  'source /opt/ros/humble/setup.bash' 'exec "$@"' > /ros_entrypoint.sh && \
  chmod +x /ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]

# PX4 v1.12.3 → /opt (workspace'ten ayrı)
WORKDIR /opt
RUN git clone --depth 1 --branch v1.12.3 https://github.com/PX4/PX4-Autopilot.git
WORKDIR /opt/PX4-Autopilot
RUN pip3 install --no-cache-dir pyros-genmsg empy jinja2
# GCC>=11 uyumluluk fix'i
RUN sed -i 's/math::max(PTHREAD_STACK_MIN, PX4_STACK_ADJUSTED(wq->stacksize))/math::max((size_t)PTHREAD_STACK_MIN, (size_t)PX4_STACK_ADJUSTED(wq->stacksize))/g' \
  platforms/common/px4_work_queue/WorkQueueManager.cpp
# Gazebo plugin'leriyle birlikte derle
RUN make px4_sitl gazebo

# Çalışma alanı (repo buraya mount edilecek)
WORKDIR /ws
