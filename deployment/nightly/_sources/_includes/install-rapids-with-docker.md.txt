There are a selection of methods you can use to install RAPIDS which you can see via the [RAPIDS release selector](https://docs.rapids.ai/install#selector).

For this example we are going to run the RAPIDS Docker container so we need to know the name of the most recent container.
On the release selector choose **Docker** in the **Method** column.

Then copy the commands shown:

```bash
docker pull rapidsai/rapidsai-core:22.12-cuda11.5-runtime-ubuntu20.04-py3.9
docker run --gpus all --rm -it \
    --shm-size=1g --ulimit memlock=-1 \
    -p 8888:8888 -p 8787:8787 -p 8786:8786 \
    rapidsai/rapidsai-core:22.12-cuda11.5-runtime-ubuntu20.04-py3.9
```
