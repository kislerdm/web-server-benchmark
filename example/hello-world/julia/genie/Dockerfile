FROM julia:1.1.1

RUN julia -e 'using Pkg; Pkg.add("Genie")'

COPY . .

CMD julia api.jl