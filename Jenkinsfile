pipeline {
    agent any

    environment {
        DOCKER_HOST = 'tcp://192.168.59.209:4243'
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-cred')
    }

    stages {
        stage('GIT SCM') {
            steps {
                script {
                 git 'https://github.com/mintuguptha/jenkins_test.git'
                }
            }
        }
        stage('Build Docker') {
            steps {
                script {
                sh 'docker build . -t mintuguptha/flaskrepo:v${BUILD_NUMBER}'
                }
            }
        }
        stage('Dcoker Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Docker Push') {
            steps {
                script {
                    sh 'docker push mintuguptha/flaskrepo:v${BUILD_NUMBER}'
                    sh 'docker rmi mintuguptha/flaskrepo:v${BUILD_NUMBER}'
                }
            }
        }
        stage('kubernetes Deploy') {
            agent {
                kubernetes {
                    label 'jenkins'
                    defaultContainer 'jnlp'
                }
            }
            steps{
                sh 'curl -LO "https://dl.k8s.io/release/v1.28.0/bin/linux/amd64/kubectl"'
                sh 'chmod u+x ./kubectl'
                sh 'kubectl set image deployment/flask-deploy flaskapp=mintuguptha/flaskrepo:v${BUILD_NUMBER} --record'
            }
        }
        
    }
}
