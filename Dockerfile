FROM alpine:latest

# Add dependencies from Alpine
RUN apk add --no-cache gcc
RUN apk add --no-cache g++
RUN apk add --no-cache linux-headers
RUN apk add --no-cache musl-dev
RUN apk add --no-cache python3-dev
RUN apk add --no-cache py3-pip


COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY rootfs /code/

CMD [ "python3", "/code/controlar_rgb.py"]