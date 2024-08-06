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
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage("Run Unit Tests") {
            steps {
                sh '''
                source venv/bin/activate
                python manage.py test
                '''
            }
         }
    }
}