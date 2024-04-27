# Comex Case

## Descrição
O projeto tem como objetivo gerar uma base com as informações de NCM e Município, de forma a gerar o máximo de cobertura possível com esses dados.
Para execução do projeto, foi necessário pesquisar sobre o assunto para agregar mais conhecimento, como exemplo: [NCM Receita](https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/classificacao-fiscal-de-mercadorias/ncm).

## Pré-requisitos
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git);
- [docker](https://docs.docker.com/engine/install/ubuntu/).

## Instruções
- Clonar o repositório do projeto:
```sh
git clone https://github.com/Maxmattos/comex-analise
```

- Builds, (re)creates, starts, e attaches ao container:
```sh
sudo docker compose -f ./comex-analise/docker-compose.yml up
```

## Output esperado
Seguida as instruções, deve-se constar, dentro do diretório `./finalDataSet`, um arquivo com o seguinte título `final_data.csv`. Este representa um dataset com o percentual de cobertura na relação de NCM por Município.

## Conclusão pessoal
É possível concluir, que caso a % de um tipo de NCM seja muito alta para um Município, até mesmo 100%, indica que aquele produto é o principal de importação para aquela cidade.

## Tecnologias
No desenvolvimento do projeto, fez-se uso das seguintes tecnologias:

<a href="https://www.python.org/" title="Python">
    <img align="middle" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" height="30" width="40" style="max-width: 100%;">
</a>

<a href="https://git-scm.com/" title="Git">
    <img align="middle" src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" height="30" width="40" style="max-width: 100%;">
</a>


<a href="https://www.docker.com/" title="Docker">
    <img align="middle" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" height="30" width="40" style="max-width: 100%;">
</a>

<a href="https://www.linux.org/" title="Linux">
    <img align="middle" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" height="30" width="40" style="max-width: 100%;">
</a>

<a href="https://github.com/" title="GitHub">
    <img align="middle" src="https://github.com/devicons/devicon/blob/master/icons/github/github-original.svg" alt="github" height="30" width="40" style="max-width: 100%;">
</a>