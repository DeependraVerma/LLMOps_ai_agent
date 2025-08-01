pipeline{
    agent any

    environment {
        SONAR_PROJECT_KEY = 'LLMOPS'
		SONAR_SCANNER_HOME = tool 'sonarqube'
        AWS_REGION = 'us-west-2'
        ECR_REPO = 'my-repo'
        IMAGE_TAG = 'latest'
	}

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/DeependraVerma/LLMOps_ai_agent.git']])                }
            }
        }

    stage('SonarQube Analysis'){
			steps {
				withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')]) {
    					
					withSonarQubeEnv('SonarQube') {
    						sh """
						${SONAR_SCANNER_HOME}/bin/sonar-scanner \
						-Dsonar.projectKey=${SONAR_PROJECT_KEY} \
						-Dsonar.sources=. \
						-Dsonar.host.url=http://sonarqube-dind:9000 \
						-Dsonar.login=${SONAR_TOKEN}
						"""
					}
				}
			}
		}

    stage('Build and Push Docker Image to ECR') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-credentials']]) {
                    script {
                        def accountId = sh(script: "aws sts get-caller-identity --query Account --output text", returnStdout: true).trim()
                        def ecrUrl = "${accountId}.dkr.ecr.${env.AWS_REGION}.amazonaws.com/${env.ECR_REPO}"

                        sh """
                        aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ecrUrl}
                        docker build -t ${env.ECR_REPO}:${IMAGE_TAG} .
                        docker tag ${env.ECR_REPO}:${IMAGE_TAG} ${ecrUrl}:${IMAGE_TAG}
                        docker push ${ecrUrl}:${IMAGE_TAG}
                        """
                    }
                }
            }
        }

        stage('Deploy to ECS Fargate') {
    steps {
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-credentials']]) {
            script {
                sh """
                aws ecs update-service \
                  --cluster multi-ai-agent \
                  --service multi-ai-agent-def-service-nwfzbxwg  \
                  --force-new-deployment \
                  --region ${AWS_REGION}
                """
                }
            }
        }
     }
        
    }
}