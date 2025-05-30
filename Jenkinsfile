pipeline {
    agent any

    stages {
        stage('Test button page') {
            steps {
                    dir('POM\\tests') {
                        sh 'pytest -f test_button_page.py'
                    }
            }
        }

        stage ('Test like a button page') {
            steps {
                dir('POM\\tests') {
                        sh 'pytest -f test_like_a_button_page.py'
                    }
            }
        }

    }
}
