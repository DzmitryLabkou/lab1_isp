FROM python:3.8

ENV TARGET /home/dima/4_sem/lab1_isp

WORKDIR "${TARGET}"

COPY rec_fib.py "${TARGET}"

COPY requirements.txt "${TARGET}"

RUN set -ex \
	pip3 install --no-cache-dir -r requirements.txt \
	&& rm requirements.txt 

CMD ["python", "rec_fib.py"]
