
import time
import sys
from obswebsocket import obsws, requests  # noqa: E402

client = obsws("localhost", 4455, "DragonsBreath5")
client.connect()
