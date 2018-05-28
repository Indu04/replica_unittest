pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'dir'
                bat 'echo %JOB_NAME%
                bat 'pylint --output-format=parseable --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" --rcfile myconfig.pylintrc src/source_code >lint.log | exit 0'
                bat 'pep8 --config myconfig.pep8  src/source_code >peplint.log | exit 0'
                step([
                        $class: 'WarningsPublisher',
                        parserConfigurations: [[
                            parserName: 'Pylint',
                            pattern: 'lint.log']],
                        unstableTotalAll           : '0',
                        usePreviousBuildAsReference: true
                    ])
                step([
                        $class: 'WarningsPublisher',
                        parserConfigurations: [[
                            parserName: 'Pep8',
                            pattern: 'peplint.log']],
                        unstableTotalAll           : '0',
                        usePreviousBuildAsReference: true
                    ])
                bat 'echo "BUILD END"'
            }
        }
    }
}
