# Simpleserv
### Primitive Content Server

This repository contains a simple content server built with Python's `http.server` module. The server exposes files from a `/files` directory and provides an additional `/trace` endpoint to display connection details such as the client's IP address, requested path, HTTP version, and more.

## Files Available for Testing

The following test files are included in the `/files` directory:
- `test`
- `test.html`
- `test.svg`
- `test.png`
- `test.jpeg`
- `test.pdf`

You can access these files by navigating to `http://localhost:8080/[filename]` after running the server.

Example:
```
http://<yourhostname>:8080/test.html
```

## `/trace` Endpoint

The `/trace` endpoint returns various connection details, including the client's IP address, request method, and HTTP version. This is useful for inspecting the details of any incoming request.

Access the trace endpoint via:
```
http://<yourhostname>:8080/trace
```

## Running the Server

1. Pull the image:
    ```bash
    docker pull ghcr.io/maximilian-hack/simpleserv:main
    ```
    
2. Run the image:
   ```bash
    docker run -d --rm -p 8080:8080 ghcr.io/maximilian-hack/simpleserv:main
    ```
   

<details>
<summary>Or build the image locally (eg. for arm64)</summary>
    
1. Build the Docker image:
    ```bash
    docker build -t simpleserv .
    ```

2. Run the Docker container:
    ```bash
    docker run -d --rm -p 8080:8080 simpleserv
    ```
    
</details>

<details>
    
<summary>About the flags used</summary>

`-d`: do not attach/show logs

`--rm`: auto remove container when stopped

`-p 8080:8080`: map host port on container port; `[hostport]:8080`

</details>

Once running, the server will host the files from the `/files` folder on port `8080`.

## Volume Mapping

To serve your own files, you can map a folder on your local machine to the `/files` folder inside the container using Docker volume mapping.

Example:
```bash
docker run -p 8080:8080 -v /path/to/your/files:/usr/src/app/files ghcr.io/maximilian-hack/simpleserv:main
```

Replace `/path/to/your/files` with the path to the directory on your machine containing the files you wish to host. All files in that directory will be accessible from the server.

---
©2024 Maximilian Hack
