FROM --platform=linux/x86_64 golang:1.16.5-alpine
ENV CGO_ENABLED 0
RUN apk update && \
    apk add git && \
    go env -w GO111MODULE=on &&\
    # TODO: これらのモジュールは開発用なので本番ではインストールしない
    go get -u github.com/cosmtrek/air && \
    go install honnef.co/go/tools/cmd/staticcheck@latest
WORKDIR /backend
