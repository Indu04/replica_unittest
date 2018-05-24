pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'dir'
                bat 'pylint --output-format=parseable --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" --rcfile myconfig.pylintrc src/source_code >lint.log'
                step([
                        $class: 'WarningsPublisher',
                        parserConfigurations: [[
                            parserName: 'Pylint',
                            pattern: 'lint.log']],
                        unstableTotalAll           : '0',
                        usePreviousBuildAsReference: true
                    ])
                bat 'echo "BUILD END"'
            }
        }
    }
}
