FROM ubuntu:latest
LABEL authors="luman"

ENTRYPOINT ["top", "-b"]