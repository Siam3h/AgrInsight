FROM python:3

WORKDIR /apis

COPY . /apis/

# Ensure the paths are correct relative to WORKDIR
COPY recommender/data/Crop_recommendation.csv recommender/data/Crop_recommendation.csv
COPY recommender/models/ensemble_model.pkl recommender/models/ensemble_model.pkl

COPY wait-for-it.sh /wait-for-it.sh

RUN chmod +x /wait-for-it.sh

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libssl-dev \
    && apt-get clean

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

ENV DJANGO_SETTINGS_MODULE=api.settings

CMD ["./wait-for-it.sh", "db:3306", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
