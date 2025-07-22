FROM jenkins/jenkins:lts

USER root

# Install Docker CLI inside Jenkins
RUN apt-get update -y && \
    apt-get install -y \
        sudo \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg \
        software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    apt-get clean

# Add jenkins to docker group (optional in this case)
RUN getent group docker || groupadd docker && usermod -aG docker jenkins

# 👇 REMOVE or COMMENT OUT this line
# USER jenkins
