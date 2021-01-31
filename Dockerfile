FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app/frontend

COPY ./frontend/rollup.config.js ./
COPY ./frontend/package*.json ./

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash
RUN apt install -y nodejs
RUN npm install

COPY ./frontend/src ./src
COPY ./frontend/public ./public

RUN npm run build

WORKDIR /app

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./app /app
