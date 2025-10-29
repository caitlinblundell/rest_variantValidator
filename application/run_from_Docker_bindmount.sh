"""
Script to run the Docker container with a bind mount to the repo directory.
"""

#!/bin/bash
docker run -it --rm -v $(pwd)/rest_api:/app -w 
/app my-python-app python app.py