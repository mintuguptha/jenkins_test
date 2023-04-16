pipeline{
	agent any
	environment {
		DOCKERHUB_CREDENTIALS=credentials('mintuguptha-dockerhub')
	}
	stages {
		stage('Build') {
			steps {
				sh 'docker build . -t mintuguptha/flaskapp:v${BUILD_NUMBER}'
			}
		}
		stage('Login') {
			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
		stage('Push') {
			steps {
				sh 'docker push mintuguptha/flaskapp:v${BUILD_NUMBER}'
			}
		}
                stage('Deploy to K8s'){
   			steps{
    				sshagent(['e3810e12-50f9-45a3-9094-9eb6427ecd03'])
    		{
     			sh 'scp -r -o StrictHostKeyChecking=no flask-deploy.yaml root@192.168.45.209:/path'
               script{
      	            try{
       			sh 'sudo ssh root@192.168.45.209 kubectl apply -f /path/flask-deploy.yaml'
		}catch(error)
       			{
		}
    			 }
    			}
   		      }
 		    }	
	}
	post {
		always {
			sh 'docker logout'
		}
	}
}
