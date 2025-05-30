pipeline {
    agent any

    stages {
        stage('Test button page') {
            steps {
                    dir('POM\\tests') {
                        sh 'pytest'
                    }
            }
        }

        stage ('Test like a button page') {
            steps {
                dir('POM\\tests') {
                        sh 'pytest'
                    }
            }
        }

    }
}
