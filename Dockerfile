FROM python:3.10.13-slim

WORKDIR /app

COPY . /app/
RUN pip install --upgrade pip && pip install -r requirments.txt

# Giữ container chạy bằng cách sử dụng lệnh sleep infinity
CMD ["sleep", "infinity"]
