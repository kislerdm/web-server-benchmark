FROM r-base:3.6.1 AS build

RUN Rscript -e 'remotes::install_github("dselivanov/RestRserve")'

WORKDIR /app

COPY . .

CMD Rscript api.R