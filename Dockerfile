# Use a base image with Java
FROM openjdk:17-jdk-slim

# Set the working directory in the container
WORKDIR /app

# Copy the JAR file into the container
COPY JmesPathLib-1.0-SNAPSHOT.jar .

# Set the command to run the JAR file, with `/data` as the input directory for JSON files
CMD ["java", "-jar", "JmesPathLib-1.0-SNAPSHOT.jar", "-rules", "/data/rules/", "-tests", "/data/tests/"]
