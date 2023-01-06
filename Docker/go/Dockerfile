# specify the base image golang:1.19-alpine
FROM golang@sha256:660f138b4477001d65324a51fa158c1b868651b44e43f0953bf062e9f38b72f3

# create a working directory inside the image
WORKDIR /app

# copy directory files i.e all files ending with .go
COPY . .

# download Go modules and dependencies
RUN go mod download

# compile application
RUN go build -v -o server

# command to be used to execute when the image is used to start a container
CMD ["/app/server"]
