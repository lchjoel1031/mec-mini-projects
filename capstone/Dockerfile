FROM python:3.10-slim
COPY ./app.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./hierarchical_level_lgbm_model.pkl /deploy/
COPY ./periodic_level_lgbm_model.pkl /deploy/
COPY ./stochastic_level_lgbm_model.pkl /deploy/
COPY ./transient_level_lgbm_model.pkl /deploy/
WORKDIR /deploy/
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "app.py"]