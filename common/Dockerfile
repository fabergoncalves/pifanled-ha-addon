FROM alpine:latest

ENV PYTHONUNBUFFERED=1

# Add dependencies from Alpine
RUN apk add --no-cache gcc
RUN apk add --no-cache g++
RUN apk add --no-cache linux-headers
RUN apk add --no-cache musl-dev
RUN apk add --no-cache python3-dev
RUN apk add --no-cache py3-pip


ADD /rpiws281x /rpiws281x
RUN pip install /rpiws281x/library/
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY rootfs/* /code/
RUN chmod +x /code/controlar_rgb.py
RUN chmod +x /code/entrypoint.sh

CMD [ "/code/entrypoint.sh"]