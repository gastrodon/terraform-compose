#!/usr/bin/env python3
from multiprocessing import Process, freeze_support

import app
import commands  # noqa

if __name__ == "__main__":
    freeze_support()
    Process(target=app.app).start()