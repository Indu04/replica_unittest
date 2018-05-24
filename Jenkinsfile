pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'dir'
                bat 'pylint src/source_code > lint.log'
                bat 'echo "BUILD END"
            }
        }
    }
}
