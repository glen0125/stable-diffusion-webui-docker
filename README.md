## Prepare the directory mapping in your host:
```
mkdir -p /LOCAL-SD && cd /LOCAL-SD
mkdir models outputs
sudo chown 10000:$UID -R models outputs
sudo chmod 775 -R models outputs
```
It is recommended to download [v1-5-pruned-emaonly.safetensors](https://huggingface.co/runwayml/stable-diffusion-v1-5/blob/main/v1-5-pruned-emaonly.safetensors) and place it in the /LOCAL-SD/models/Stable-diffusion directory to improve loading speed.


## Run with api
```
docker run -d --name sdw --gpus all --network host \
  -v $(pwd)/models:/app/stable-diffusion-webui/models \
  -v $(pwd)/outputs:/app/stable-diffusion-webui/outputs \
  --rm aios/stable-diffusion-webui-api
```
This will start a container and listen at http://127.0.0.1:7862. If you want to listen on the address 0.0.0.0, please specify the --listen parameter. If you want to specify a port, please include the --port ${port} parameter. 

e.g.

```
docker run -d --name sdw --gpus all --network host \
  -v $(pwd)/models:/app/stable-diffusion-webui/models \
  -v $(pwd)/outputs:/app/stable-diffusion-webui/outputs \
  --rm aios/stable-diffusion-webui-api --listen --port 7860
```
This will start a container and listen at http://0.0.0.0:7860.

## build
```
docker build -t aios/stable-diffusion-webui-api .
```
