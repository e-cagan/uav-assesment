import os
import socket
import pytest


def _port_open(host="127.0.0.1", port=14540, timeout=0.2) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(timeout)
    try:
        s.sendto(b"", (host, port))
        return True
    except Exception:
        return False
    finally:
        s.close()


def _sitl_up() -> bool:
    return os.path.exists("/tmp/sitl.log") and _port_open()


def pytest_runtest_setup(item):
    # Uçuş testleri SITL ister
    if "requires_sitl" in item.keywords and not _sitl_up():
        pytest.skip("SITL not running; start with ./run_sitl.sh")

    # Bağlantı isteyen testlerde:
    # - CI ortamında (CI=true) asla xfail yapma -> gerçek sonuç dönsün
    # - Lokal ortamda FORCE_RUN=1 verilmişse yine çalıştır
    # - Aksi halde lokalde iskelet için xfail ver
    if "requires_connect" in item.keywords:
        in_ci = os.getenv("CI", "").lower() in ("1", "true", "yes")
        force_run = os.getenv("FORCE_RUN", "0") == "1"
        if not in_ci and not force_run:
            pytest.xfail("connect() not implemented yet (skeleton)")
