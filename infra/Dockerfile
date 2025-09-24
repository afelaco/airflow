# ---- Dockerfile for Apache Airflow ----

# Define build arguments for Airflow and Python versions
ARG AIRFLOW_VERSION
ARG PYTHON_VERSION

# ---- Base image ----
# Use the official slim Apache Airflow image with specified versions of Airflow and Python
FROM apache/airflow:slim-${AIRFLOW_VERSION}-python${PYTHON_VERSION}

# ---- Build stage ----
# Set wheel file argument
ARG WHEEL_FILE

# Switch to root user to install system-wide dependencies during the build process
USER root

# Copy the wheel into a temporary location
COPY dist/${WHEEL_FILE} /tmp/

# Install the wheel and remove the file afterwards
RUN uv pip install /tmp/${WHEEL_FILE} && rm /tmp/${WHEEL_FILE}

# ---- Runtime ----
# Switch back to the airflow user for security purposes during runtime
USER airflow