# CommerceFlow

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

O CommerceFlow é um sistema de gestão de vendas e estoque que utiliza tecnologias como Apache Spark, PySpark, Databricks, Azure e Terraform para processar e organizar grandes volumes de dados de maneira eficiente. O sistema oferece funcionalidades de controle de inventário, processamento de pedidos e pagamentos, além de realizar a gestão de clientes e entregas, tudo com uma arquitetura escalável e otimizada para grandes volumes de dados.

## Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte implantação para saber como implantar o projeto.

Esta documentação está disponível também no [MkDocks](colocar o link do mkdocks)

## Ferramentas utilizadas 
- [SQL Server](https://www.microsoft.com/sql-server) - Banco de dados relacional para armazenamento de dados.  
- [Python](https://www.python.org/) - Desenvolvimento de scripts de automação.  
- [Terraform](https://www.terraform.io/) - Gerenciamento de infraestrutura como código.  
- [Databricks](https://www.databricks.com/) - Processamento distribuído de dados.  
- [Azure](https://azure.microsoft.com/) - Persistência em Object Storage.
- [Ubuntu](https://ubuntu.com/blog/tag/labs) - Máquina virtual para rodar o Terraform.
- [Power BI](https://powerbi.microsoft.com/) - Visualização e análise de dados.  
- [MkDocs](https://www.mkdocs.org/) - Documentação do projeto.  


## Desenho de Arquitetura

![image](https://github.com/suyane924/TrabalhoFinalEng_Dados/blob/Guna-Me/CommerceFlow/Ferramentas.drawio.png)

## Pré-requisitos

Antes de iniciar, você precisará ter instalado:  
- [Pyhton](python.org)
- [Azure CLI](https://docs.microsoft.com/pt-br/cli/azure/install-azure-cli)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
- [Ubuntu](https://ubuntu.com/download)
- Conta Microsoft Learning (assinatura sandbox)


## Instalação  

### Passo 1: Clonar o repositório  
```bash  
git clone https://github.com/suyane924/TrabalhoFinalEng_Dados.git  
cd seu-repositorio

```

### Passo 2: Configurar ambiente python
```bash  
python -m venv venv  
source venv/bin/activate  # (No Windows: venv\Scripts\activate)  
pip install -r requirements.txt  

```

### Passo 3: Configurar infraestrutura com terraform (após certificar-se de que obtém os pré-requisitos)

- É necessário utilizar uma máquina virtual com o sistema operacional Ubuntu para realizar a configuração, visto que o Terraform será usado para criar a infraestrutura remotamente na Azure.
  
# Configuração do Azure Data Lake e SQL Server com Terraform

## Passos

### 1. Ativar uma Assinatura de Teste

Utilize a assinatura MS Learn Sandbox para limitar o tempo de uso.

### 2. Configuração da Azure CLI

Antes de iniciar, clone o projeto contendo os arquivos `.tf` e abra-o no Visual Studio Code.

#### 2.1 Login na Azure CLI

```sh
az login
```

#### 2.2 Obter o Nome do Grupo de Recursos

```sh
az group list -o table
```

#### 2.2 Obter o Nome do Grupo de Recursos

```sh
az group list -o table
```

### 3. Executar o Terraform

#### 3.1 Inicializar o Terraform

```sh
terraform init
```

#### 3.2 Validar o código nos arquivos .tf

```sh
terraform validate
```

#### 3.3 Ajustar a formatação nos arquivos .tf

```sh
terraform fmt
```

#### 3.4 Criar um plano de execução

```sh
terraform plan
```

#### 3.5 Aplicar o Terraform na nuvem

```sh
terraform apply
```

### 3.6 Verificar o deploy do ADLS e do SQL Server

- Faça login em [Portal Azure](https://portal.azure.com/) e verifique o ADLS e o SQL Server criado.
- Liberar IP no firewall do SQL Server nas configurações de rede.

### Passo 4: Executar pipelines no Databricks
Acesse o workspace configurado e importe os notebooks.
Execute as tarefas conforme o cronograma definido.

### Passo 5: Visualizar os dados com Power BI
Conecte ao Azure Blob Storage para importar os dados processados.
Configure os gráficos e dashboards de acordo com os modelos disponibilizados.

## Implantação 
- Para implantar o projeto em um ambiente ativo, certifique-se de que todas as dependências estejam configuradas, configure as credenciais no arquivo .env, e execute os comandos de inicialização descritos acima.

1. Orquestração de Fluxos de Trabalho com Databricks:
Nossa principal ferramenta para gerenciar os fluxos de trabalho coordenando todas as etapas da pipeline de dados.

2. Criação de Dados Sintéticos com a Biblioteca Faker:
A geração da massa de dados foi realizada com a biblioteca Faker.

3. Armazenamento Persistente no Azure Object Storage:
Para garantir escalabilidade e durabilidade, os dados serão armazenados no Object Storage da Azure.

4. Estrutura de Camadas de Dados:
Landing Zone:
Ingestão e armazenamento dos dados brutos, camada de entrada.

Camada Bronze:
Armazenamento de dados transformados minimamente e enriquecidos com informações adicionais.

Camada Silver:
As informações são padronizadas e salvas no formato Parquet.

Camada Gold:
Dados estruturados em tabelas otimizadas para análise, com a criação de dimensões e fatos adequadas para relatórios.

5. Dashboards Interativos com Power BI:
O Power BI será empregado para a visualização dos dados, permitindo a construção de dashboards dinâmicos que auxiliam na análise e na tomada de decisões.

## Autores

- [Maria Eduarda Monteiro Marcos](https://github.com/Guna-ME) - Configuração Azure, Databricks, script para geração dos dados com faker, automação entre as lands.
- [Gabriel Tarciso Macieiski](https://github.com/GTM016) - Documentação MkDocks.
- [Suyane Bonfanti dos Santos](https://github.com/suyane924) - Geração dos arquivos csv, códigos para processar os dados entre as camadas landing, bronze, silver e gold, diagrama dimensional.


Você também pode ver a lista de todos os [colaboradores](gitHub.com/suyane924/TrabalhoFinalEng_Dados/graphs/contributors) que participaram deste projeto.

## Licença

Este projeto está sob a licença - veja o arquivo [LICENSE](https://github.com/jlsilva01/projeto-ed-satc/blob/main/LICENSE) para detalhes.

## Referências

[CHATGPT](https://chatgpt.com/) [DOCUMENTAÇÃO GITHUB JORGE LUIZ DA SILVA](https://github.com/jlsilva01/engenharia-dados-azure-databricks)


