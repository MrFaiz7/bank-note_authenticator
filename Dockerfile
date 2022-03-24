FROM continuumio/anaconda3
COPY . /usr/app/
WORKDIR /usr/app/
RUN pip install -r requirements.txt

EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]
