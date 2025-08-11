import asyncio
import pytest
from candidate_package import control


@pytest.mark.requires_sitl
@pytest.mark.requires_connect
@pytest.mark.timeout(60)
def test_task_1_arm_disarm():
    async def run():
        await control.connect()
        await control.arm_disarm()
    asyncio.get_event_loop().run_until_complete(run())
