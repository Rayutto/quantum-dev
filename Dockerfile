FROM python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libblas-dev liblapack-dev libatlas-base-dev gfortran \
    libgl1-mesa-glx \
    libxrender1 \
    libxext6 \
    libsm6 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install QuTiP and visualization tools
RUN pip install --no-cache-dir qutip jupyter matplotlib numpy scipy

# Set working directory
WORKDIR /workspace

# Optional: expose port for Jupyter or other web tools
EXPOSE 8888

CMD ["bash"]