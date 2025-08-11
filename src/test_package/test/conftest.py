import asyncio
import pytest
from candidate_package import control

def _connect_implemented() -> bool:
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(control.connect())
        return True
    except NotImplementedError:
        return False
    except Exception:
        # connect implement edilmiş ama runtime hata veriyor olabilir
        return True

def pytest_runtest_setup(item):
    if 'requires_connect' in item.keywords:
        if not _connect_implemented():
            pytest.skip("connect() not implemented yet; skipping dependent task")
