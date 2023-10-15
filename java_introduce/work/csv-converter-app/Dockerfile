# Base image
FROM openjdk:11-jre-slim

# Set working directory
WORKDIR /app

# Copy source code
COPY src /app/src
COPY resources /app/resources
COPY test /app/test
COPY README.md /app/README.md

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Add your specific libraries and tools installation here
# For example:
# RUN apt-get install -y <library-package>

# Build the application
RUN javac -d ./out -cp /app/src src/Main.java

# Set entry point
ENTRYPOINT ["java", "-cp", "out", "Main"]
