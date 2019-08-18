FROM r-base:3.6.1 AS build

RUN Rscript -e "install.packages(\"plumber\", repos=\"https://cran.rstudio.com\")"

WORKDIR /app

COPY . .

CMD Rscript api.R