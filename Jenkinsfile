pipeline {
    agent any
    environment {
        DOCKERHUB_USERNAME = ''
        DOCKERHUB_TOKEN    = ''
        TF_VAR_docker_host = ''
        TF_VAR_config_path = ''
        TF_VAR_logs_path   = ''
    }
    stages {
        stage('run dagger ci') {
            steps {
                sh '''
                    pip install -r ./dagger/requirements.txt
                    python ./dagger/pipeline.py
                '''
            }
        }
        stage('deploy w/ terraform') {
            steps {
                sh '''
                    cd deploy
                    terraform init
                    terraform apply -auto-approve
                '''
            }
        }
        stage('cleanup') {
            steps {
                sh 'rm deploy/.terraform* deploy/*.tfstate*'
            }
        }
    }
}
