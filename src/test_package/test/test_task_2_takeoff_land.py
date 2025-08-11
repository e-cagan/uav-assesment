import asyncio
import pytest
from candidate_package import control


@pytest.mark.requires_sitl
@pytest.mark.requires_connect
@pytest.mark.timeout(120)
@pytest.mark.parametrize("alt", [3.0, 5.0])
def test_task_2_takeoff_land(alt):
    async def run():
        await control.connect()
        await control.takeoff_land(alt)
    asyncio.get_event_loop().run_until_complete(run())
