#!/bin/bash
uvicorn falcon_api:app --host 0.0.0.0 --port 8000 --workers 2