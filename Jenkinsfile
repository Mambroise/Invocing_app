pipeline{

    agent any

    stages{

        stage("COUNTINOUS DOWNLOAD"){
            steps{
                git branch: 'dev', url: 'https://github.com/Mambroise/Invocing_app.git'
            }
        }
        stage("Unit Test"){
            steps{
                sh'mvn test'
            }
        }
    }
}