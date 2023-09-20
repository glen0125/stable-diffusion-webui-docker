FROM siutin/stable-diffusion-webui-docker:latest-cuda

USER app

WORKDIR /app/stable-diffusion-webui

CMD ["venv/bin/python", "-u", "webui.py", "--listen", "--port", "7862", "--api"]