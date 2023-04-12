pipeline {
    agent any
    environment {
        DOCKERHUB_USERNAME = credentials("DOCKERHUB_USERNAME")
        DOCKERHUB_TOKEN    = credentials("DOCKERHUB_TOKEN")
        TF_VAR_docker_host = ''
        TF_VAR_config_path = ''
        TF_VAR_logs_path   = ''
    }
    stages {
        stage('run dagger ci') {
            steps {
                def tag = "";
                if ("${env.BRANCH_NAME}" == "main") {
                    tag = "latest"
                } else {
                    tag = "dev"
                }

                sh '''
                    pip install -r ./dagger/requirements.txt
                    python ./dagger/pipeline.py --tag=$tag
                '''
            }
        }
        stage('deploy w/ terraform') {
            when {
                environment(name: 'BRANCH_NAME', value: 'main')
            }
            steps {
                sh '''
                    cd deploy
                    terraform init
                    terraform apply -auto-approve
                '''
            }
        }
        stage('cleanup') {
            when {
                environment(name: 'BRANCH_NAME', value: 'main')
            }
            steps {
                sh 'rm deploy/.terraform* deploy/*.tfstate*'
            }
        }
    }
}
