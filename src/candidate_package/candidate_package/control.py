"""
Adayın dolduracağı basit API.

Sözleşme:
- connect(): UDP 14540 üzerinden PX4 SITL'e bağlanır, ready döner.
- arm_disarm(): armlar, 2 sn bekler, disarm eder; hata durumlarını raise eder.
- takeoff_land(alt): alt (m) yüksekliğe kalkar, kısa hover, iner; blocking.
"""

async def connect():
    raise NotImplementedError("Implement connect() using MAVSDK System on udp://:14540")

async def arm_disarm():
    raise NotImplementedError("Implement arm then disarm; validate states")

async def takeoff_land(alt: float = 5.0):
    raise NotImplementedError("Implement takeoff to 'alt' meters, hover, and land")
