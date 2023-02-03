# Compilador para a linguagem Python

Para baixar e usar o compilador, basta fazer um clone do repositório e executar os seguintes comandos:

-- Para intalar o antlr
* pip3 install antlr4-python3-runtime==4.9.3

-- Para instalar o antlr-denter
* pip install antlr-denter

Para usar o compilador são necessários os seguintes passos:

- Preencher o arquivo _input.jac_ com o programa python que deseja executar, ou criar outro arquivo com a extensão _.jac_

- Executar o arquivo _build.bat_, se você estiver usando windows, ou o arquivo _build.sh_, se você estiver usando linux

- Executar o arquivo _run.bat nomedoarquivo.jac_, se você estiver usando windows ou o arquivo _run.sh nomedoarquivo.jac_, se você estiver usando linux

Obs.: Vale ressaltar que o compilador não consegue compilar características mais avançadas da linguagem python, apenas o básico da linguagem indo até funções recursivas.
