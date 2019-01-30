pipeline {
    agent any
    environment {
       HOSTS = defineEnvironment() 
    }
    stages {
        stage('Pre-Checks') {
            steps {
                echo 'Pre-Checking...'
                sh 'ansible-playbook pre_checks.yml -i $HOSTS'
            }
        }
        stage('Run Playbooks') {
            steps {
                echo 'Deploying...'
                sh 'ansible-playbook deploy_core.yml -i $HOSTS'
                sh 'ansible-playbook deploy_access.yml -i $HOSTS'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'ansible-playbook run_tests.yml -i $HOSTS'
            }
        }
        stage('Commit back results') {
            steps {
                sh 'python report_spark.py'
                echo 'reporting....'
            }
        }
    }
}

def defineEnvironment() {
    def branchName = "${env.BRANCH_NAME}"
    if (branchName == "development") {
        return 'hosts'
        echo 'Starting Development Pipeline'
    }
    if (branchName == "production") {
        return 'hosts-production'
        echo 'Starting Production Pipeline'
    }
}
