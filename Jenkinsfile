pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'dir'
                bat 'echo "hello"'
                bat 'pylint src/source_code > lint.log'
            }
        }
    }
}
