pipeline {
    agent any

    stages {
        stage("COUNTINOUS DOWNLOAD") {
            steps {
                git branch: 'dev', url: 'https://github.com/Mambroise/Invocing_app.git'
            }
        }
        stage("Setup Python Environment") {
            steps {
                sh 'bash -c "python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"'
            }
        }
        stage("Run Unit Tests") {
            steps {
                sh '''
                    bash -c "
                    source venv/bin/activate &&
                    echo 'Current directory before cd:' &&
                    pwd &&
                    cd 'Django project' &&
                    echo 'Current directory after cd:' &&
                    pwd &&
                    python3 manage.py test
                    "
                '''
            }
        }
    }
}
