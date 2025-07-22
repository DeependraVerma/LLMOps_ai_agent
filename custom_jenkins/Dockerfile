FROM jenkins/jenkins:lts

USER root

# Install sudo and Docker dependencies
RUN apt-get update -y && \
    apt-get install -y sudo apt-transport-https ca-certificates curl gnupg software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    apt-get clean

# Create docker group and add Jenkins user
RUN groupadd -g 998 docker && \
    usermod -aG docker jenkins && \
    chmod 666 /var/run/docker.sock

USER jenkins
