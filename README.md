## Prepare the directory mapping in your host:
```
mkdir -p /MY-DATA-DIR && cd /MY-DATA-DIR
mkdir models outputs
sudo chown 10000:$UID -R models outputs
sudo chmod 775 -R models outputs
```
It is recommended to download [v1-5-pruned-emaonly.safetensors](https://huggingface.co/runwayml/stable-diffusion-v1-5/blob/main/v1-5-pruned-emaonly.safetensors) and place it in the /MY-DATA-DIR/models/Stable-diffusion directory to improve loading speed.


## Run with CUDA
```
docker run -d --name sdw --gpus all --network host \
  -v $(pwd)/models:/app/stable-diffusion-webui/models \
  -v $(pwd)/outputs:/app/stable-diffusion-webui/outputs \
  --rm aios/stable-diffusion-webui-api
```

## build
```
docker build -t aios/stable-diffusion-webui-api .
```
