FROM python:3.8-windowsservercore-1809

RUN pip install Pillow
RUN pip install playsound
RUN pip install pandas

COPY . /

CMD [ "python", "KAKE_Home_School.py" ]