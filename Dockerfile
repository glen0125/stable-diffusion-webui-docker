FROM siutin/stable-diffusion-webui-docker:latest-cuda

USER app

WORKDIR /app/stable-diffusion-webui

ENTRYPOINT ["venv/bin/python", "-u", "webui.py", "--api", "--port", "7862"]