pipeline {
    agent any

    environment {
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_PORT = '587'
        EMAIL_USE_TLS = 'True'
        EMAIL_HOST_USER = 'maurice.ambroise79@gmail.com'
        EMAIL_HOST_PASSWORD = 'achw grjw fxad dfgh'
        OTP_VALIDITY_DURATION = '90'
        INACTIVITY_TIMEOUT_MINUTES = '30'
    }

    stages {
        stage("Continuous Download") {
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
