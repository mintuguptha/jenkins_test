pipeline{
	agent any
	environment {
		DOCKERHUB_CREDENTIALS=credentials('mintuguptha-dockerhub')
	}
	stages {
		stage('Build') {
			steps {
				sh 'docker build . -t mintuguptha/flaskapp:v1'
			}
		}
		stage('Login') {
			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
		stage('Push') {
			steps {
				sh 'docker push mintuguptha/flaskapp:v1'
			}
		}
	}
	post {
		always {
			sh 'docker logout'
		}
	}
}
