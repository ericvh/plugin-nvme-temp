FROM waggle/plugin-base:1.1.1-base
COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r /app/requirements.txt
RUN apt-get update && apt-get install smartmontools && apt-get clean 
COPY . /app/
WORKDIR /app
ENTRYPOINT ["python3", "/app/main.py"]
