pipeline{

    agent any

    stages{

        stage("COUNTINOUS DOWNLOAD"){
            steps{
                git branch: 'dev', url: 'https://github.com/Mambroise/Invocing_app.git'
            }
        }
        stage("Setup Python Environment") {
            steps {
                sh '''
                python -m venv venv
                .venv\Scripts\activate
                pip install -r requirements.txt
                '''
            }
        }
        stage("Run Unit Tests") {
            steps {
                sh '''
                .venv\Scripts\activate
                python manage.py test
                '''
            }
        }
    }
}