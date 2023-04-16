pipeline{
	agent any
	environment {
		DOCKERHUB_CREDENTIALS=credentials('mintuguptha-dockerhub')
	}
	stages {
		stage('Build') {
			steps {
				sh 'docker build . -t mintuguptha/flaskapp:${BUILD_NUMBER}'
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
    				sshagent(['jenkins_key_kubectl'])
    		{
     			sh 'scp -r -o StrictHostKeyChecking=no flask-deploy.yaml master-VirtualBox@192.168.45.209:/path'
               script{
      	            try{
       			sh 'ssh username@102.10.16.23 kubectl apply -f /path/node-deployment.yaml'
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
