pipeline {
    agent any  // Specifies that the pipeline can run on any available agent (node)

    stages {
        stage('Build') {
            steps {
                echo 'Building the project....'
                // Add your build steps here
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests....'
                // Add your test steps here
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application....'
                // Add your deployment steps here
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! Notifying stakeholders...'
            // Add notification steps for successful build
        }
        failure {
            echo 'Pipeline failed! Sending notification...'
            // Add notification steps for failed build
        }
    }
}
