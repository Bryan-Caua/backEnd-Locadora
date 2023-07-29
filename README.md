Este projeto é uma aplicação de uma locadora desenvolvida em Django e Python. Ele possui funcionalidades relacionadas à gestão de filmes e usuários, permitindo que os usuários possam alugar filmes disponíveis na locadora.

Instalação dos pacotes de teste
Antes de prosseguir com a instalação e execução do projeto, certifique-se de ter o Python e o gerenciador de pacotes pip instalados em seu sistema.

Verifique se os pacotes pytest, pytest-testdox e pytest-django estão instalados globalmente em seu sistema:
bash
Copy code
pip list
Caso sejam listados o pytest, pytest-testdox e pytest-django em seu ambiente global, utilize os seguintes comandos para desinstalá-los globalmente:
bash
Copy code
pip uninstall pytest
pip uninstall pytest-testdox
pip uninstall pytest-django
Crie e ative seu ambiente virtual:
bash
Copy code
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual no Linux:
source venv/bin/activate

# Ative o ambiente virtual no Windows:
.\venv\Scripts\activate
Instale o pacote pytest-testdox:
bash
Copy code
pip install pytest-testdox pytest-django
Vá até o arquivo pytest.ini e modifique o nome do projeto my_project_name.settings para o nome do seu_projeto.settings (onde se encontra o settings.py).
Rodando os testes
Após seguir os passos de instalação, você poderá rodar os testes no diretório principal do projeto usando o seguinte comando:

bash
Copy code
pytest --testdox -vvs
Rodando os testes de cada tarefa isoladamente
Ao final de cada tarefa do projeto, você poderá executar uma suite de testes direcionada àquela tarefa específica. Lembre-se de sempre estar com o ambiente virtual (venv) ativado.

Rodando testes da Tarefa 1:

bash
Copy code
pytest --testdox -vvs tests/tarefas/t1/
Rodando testes da Tarefa 2:

bash
Copy code
pytest --testdox -vvs tests/tarefas/t2/
Rodando testes da Tarefa 3:

bash
Copy code
pytest --testdox -vvs tests/tarefas/t3/
Rodando testes da Tarefa 4:

bash
Copy code
pytest --testdox -vvs tests/tarefas/t4/
URLs da aplicação
A aplicação possui as seguintes URLs:

/admin/: URL do painel de administração do Django.
/api/: URLs da API para a gestão de filmes e usuários.
/api/movies/: URLs específicas para a gestão de filmes.
/api/users/: URLs específicas para a gestão de usuários.
Personalização e Contribuição
Este projeto foi desenvolvido com base no M5 - Kenzie Buster. Sinta-se à vontade para personalizar a aplicação de acordo com suas necessidades e contribuir com melhorias ou correções de bugs. Se desejar contribuir, abra um pull request com suas alterações.

Agradecimentos
Agradecemos à Kenzie Academy por fornecer a base do projeto M5 - Kenzie Buster. Também agradecemos a todos os colaboradores e desenvolvedores envolvidos no desenvolvimento do Django e seus pacotes relacionados, tornando o processo de criação desta locadora em Django uma experiência incrível.
