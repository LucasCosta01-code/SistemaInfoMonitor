# Sistema de Monitoramento de Informações do Sistema

Este projeto consiste em um sistema de monitoramento que coleta e exibe informações detalhadas sobre o sistema em execução. A função `get_system_info()` é responsável por coletar dados como informações do sistema operacional, uso da CPU, memória, disco, rede e, se disponível, informações da GPU.

## Funcionalidades Principais
- Coleta informações do sistema operacional, CPU, memória, disco, rede e GPU.
- Apresenta os dados de forma estruturada e fácil de entender.
- Permite monitorar o desempenho do sistema em tempo real.

## Como Usar
1. Clone o repositório.
2. Instale as dependências necessárias: `tkinter`, `psutil`, `platform`, `GPUtil`.
3. Execute o arquivo `Sistema.py` para visualizar as informações do sistema.

## Detalhes da Implementação
- A função `get_system_info()` coleta informações do sistema e retorna um dicionário com os dados.
- As informações coletadas incluem detalhes do sistema operacional, uso da CPU, memória, disco, rede e, opcionalmente, informações da GPU.
- Os dados são exibidos em uma interface gráfica usando a biblioteca `tkinter`.

## Próximos Passos
- Explore a possibilidade de adicionar mais métricas de sistema.
- Aprimore a interface gráfica para uma melhor experiência do usuário.
- Considere a adição de funcionalidades de exportação ou salvamento de dados.

## Contribuição
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Abra uma issue ou envie um pull request.
