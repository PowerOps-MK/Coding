# golang:1.17-alpine
FROM golang@sha256:660f138b4477001d65324a51fa158c1b868651b44e43f0953bf062e9f38b72f3

# create a working directory inside the image
WORKDIR /app

# copy Go modules and dependencies to image
COPY go.mod ./

# download Go modules and dependencies
RUN go mod download

# copy directory files i.e all files ending with .go
COPY *.go ./

# compile application
RUN go build -o /godocker
 
# tells Docker that the container listens on specified network ports at runtime
# EXPOSE 8080

# command to be used to execute when the image is used to start a container
CMD [ "/godocker" ]
