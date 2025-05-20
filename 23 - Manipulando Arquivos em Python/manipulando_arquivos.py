# Introdução a manipulação de arquivos

# Por que precisamos manipular arquivos?
# Os arquivos são essenciais para qualquer tipo de programação, pois fornecem um meio de armazenar e recuperar dados. Através da manipulação de arquivos, podemos persistir os dados além da vida útil de um programaespecífico.

# Conceito de arquivo em informática
# Um arquivo é um container no computador onde as informações são armazenadas em formato digital. Existem dois tipos de arquivos que podemos manipular em Python: arquivos de texto e arquivos binários.

# Abrindo e fechando arquivos

# Por que precisamos manipular arquivos?
# Para manipular arquivos em Python, primeiro precisamos abrilos. Usamos a função 'open()' para isso. Quando terminamos de trabalhar com o arquivo, usamos a função 'close()' para liberar recusos.

# Exemplo

# Abrindo um arquivo
arquivo = open('exemplo.txt', 'r')  # 'r' significa que estamos abrindo o arquivo para leitura

# Lendo o conteúdo do arquivo
conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo

# Fechando o arquivo
arquivo.close()

# Modos de abertura de arquivo
#  Existem diferentes modos para abrir um arquivo, como somente leitura ('r'), gravação ('w') e anexar ('a'). O modo de abertura deve ser escolhido de acordo com a operação que iremos realizar no mesmo.

# Exemplo

file = open('exemplo.txt', 'w')  # Abre o arquivo para escrita (substitui o conteúdo existente)

file.write('Olá, mundo!')  # Escreve no arquivo
file.close()  # Fecha o arquivo

file = open('exemplo.txt', 'a')  # Abre o arquivo para anexar (adiciona ao conteúdo existente)

file.write('\nAdicionando mais uma linha.')  # Adiciona uma nova linha ao arquivo
file.close()  # Fecha o arquivo

file = open('exemplo.txt', 'r')  # Abre o arquivo para leitura
conteudo = file.read()  # Lê o conteúdo do arquivo
file.close()  # Fecha o arquivo

# Lendo de um arquivo

# Introdução
# Python fornece várias maneiras de ler um arquivo. Podemos usar 'read()', 'readline()' ou 'readlines()' dependendo de nossas necessidades.

# Método read:
file = open('exemplo.txt', 'r')  # Abre o arquivo para leitura
conteudo = file.read()  # Lê todo o conteúdo do arquivo
file.close()  # Fecha o arquivo

# Método readline e readlines
# O método 'readline()' lê uma linha por vez, enquanto 'readlines()' retorna uma lista onde cada elemento é uma linha do arquivo.

# Exemplo

file = open('exemplo.txt', 'r')  # Abre o arquivo para leitura
linha = file.readline()  # Lê a primeira linha do arquivo
print(linha)  # Imprime a linha lida
linhas = file.readlines()  # Lê todas as linhas do arquivo e armazena em uma lista
file.close()  # Fecha o arquivo


# Escrevendo em um arquivo

# Introdução
#  Podemos usar 'write()' ou 'writelines()' para escrever em um arquivo. Lembre-se, no entanto, de abrir o arquivo no modo correto.

# Exemplo
file = open('exemplo.txt', 'w')  # Abre o arquivo para escrita (substitui o conteúdo existente)
file.write('Olá, mundo!')  # Escreve no arquivo
file.write('\nAdicionando mais uma linha.')  # Adiciona uma nova linha ao arquivo
file.close()  # Fecha o arquivo

# Gerenciando arquivos e diretórios

# Introdução
# Python também oferece funções para gerenciar arquivos e diretórios. Podemos criar, renomear e excluir arquivos e diretórios usando os módulos 'os' e 'shutil'.

# Exemplo

import os
import shutil

# Criando um diretório
os.mkdir('novo_diretorio')  # Cria um novo diretório chamado 'novo_diretorio'

# Renomeando um arquivo
os.rename('exemplo.txt', 'exemplo_renomeado.txt')  # Renomeia o arquivo 'exemplo.txt' para 'exemplo_renomeado.txt'

# Movendo um arquivo
shutil.move('exemplo_renomeado.txt', 'novo_diretorio/exemplo_renomeado.txt')  # Move o arquivo para o novo diretório

# Excluindo um arquivo
os.remove('novo_diretorio/exemplo_renomeado.txt')  # Remove o arquivo do novo diretório

# Excluindo um diretório
os.rmdir('novo_diretorio')  # Remove o diretório vazio

# Conclusão
# A manipulação de arquivos é uma habilidade essencial em Python. Compreender como abrir, ler, escrever e gerenciar arquivos nos permitirá criar aplicações mais robustas e funcionais. Pratique esses conceitos para se familiarizar com a manipulação de arquivos em Python.

# Tratamento de exceções em manipulação de arquivos

# Introdução
# Tratar erros é uma parte importante da manipulação de arquivos. Python oferece uma variedade de exceções que nos permitem lidar com erros comuns.

# Exceções mais comuns

# FileNotFoundError: Lançada quando o arquivo que está sendo aberto não pode ser encontrado no diretório especificado.

# PermissionError: Lançada quando ocorre uma tentativa de abrir um arquivo sem as permissões adequadas para leitura ou gravação.

# IOError: Lançada quando ocorre um erro geral de E/S (entrada/saída) ao trabalhar com o arquivo, como problemas de permissão, falta de espaço em disco, entre outros.

# UnicodeDecodeError: Lançada quando ocorre um erro ao tentar decodificar os dados de um arquivo de texto usando uma codificação inadequada.

# • UnicodeEncodeError: Lançada quando ocorre um erro ao tentar codificar dados em uma determinada codificação ao gravar em um arquivo de texto.

# • IsADirectoryError: Lançada quando é feita uma tentativa de abrir um diretório em vez de um arquivo de texto.

# Exemplo

try:
    arquivo = open('exemplo.txt', 'r')  # Tenta abrir o arquivo para leitura
    conteudo = arquivo.read()  # Lê o conteúdo do arquivo
except FileNotFoundError:
    print("Arquivo não encontrado.")
except PermissionError:
    print("Permissão negada.")
except Exception as e:
    print("Erro:", e)
finally:
    arquivo.close()

# Exemplo de uso de with
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# O bloco 'with' garante que o arquivo seja fechado automaticamente, mesmo que ocorra um erro durante a leitura.

# Boas práticas na manipulação de arquivos

# Introdução
# Ao manipular arquivos em Python existem algumas boas práticas que podemos seguir, vamos abordar as principais.

# Bloco with
# Use o gerenciamento de contexto (context manager) com a declaração 'with'. O gerenciamento de contexto permite trabalhar com arquivos de forma segura, garantindo que eles sejam fechados corretamente, mesmo em caso de exceções.

# Exemplo

with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Verifique se o arquivo foi aberto com sucesso
#  É recomendado verificar se o arquivo foi aberto corretamente antes de executar operações de leitura ou gravação nele.

# Exemplo

try:
    with open('exemplo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
except PermissionError:
    print("Permissão negada.")  
except Exception as e:
    print("Erro:", e)
finally:
    print("Operação concluída.")

# Use a codificação correta
# Certifique-se de usar a codificação correta ao ler ou gravar arquivos de texto. O argumento 'encoding' da função 'open()' permite especificar a codificação.

# Exemplo

with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Trabalhando com arquivos CSV

# Introdução
#  Vamos aprender sobre arquivos CSV, um formato de arquivo amplamente utilizado para armazenar dados tabulares. CSV é a sigla para 'Comma Separated Values'.

# Lendo arquivos CSV Python fornece um módulo chamado 'csv' para lidar facilmente com arquivos CSV.

# Exemplo

import csv
with open('exemplo.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        print(linha)
# Escrevendo arquivos CSV
# Para escrever em arquivos CSV, usamos o método 'writer()' do módulo 'csv'.
# Exemplo
import csv

with open('exemplo.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['Nome', 'Idade', 'Cidade'])  # Cabeçalho
    escritor_csv.writerow(['João', 25, 'São Paulo'])
    escritor_csv.writerow(['Maria', 30, 'Rio de Janeiro'])
    escritor_csv.writerow(['Pedro', 22, 'Belo Horizonte'])

# Lendo arquivos CSV com pandas
# O pandas é uma biblioteca poderosa para manipulação de dados em Python. Ele fornece funções convenientes para ler e escrever arquivos CSV.

# Exemplo

import pandas as pd
# Lendo um arquivo CSV
df = pd.read_csv('exemplo.csv', encoding='utf-8')
print(df)

# Escrevendo em arquivos CSV Da mesma forma podemos utilizar o módulo 'csv' para escrever em arquivos CSV.

# Exemplo

import csv

with open('exemplo.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['Nome', 'Idade', 'Cidade'])  # Cabeçalho
    escritor_csv.writerow(['João', 25, 'São Paulo'])
    escritor_csv.writerow(['Maria', 30, 'Rio de Janeiro'])
    escritor_csv.writerow(['Pedro', 22, 'Belo Horizonte'])
# Lendo arquivos CSV com pandas

# O pandas é uma biblioteca poderosa para manipulação de dados em Python. Ele fornece funções convenientes para ler e escrever arquivos CSV.

# Exemplo

import pandas as pd

# Lendo um arquivo CSV
df = pd.read_csv('exemplo.csv', encoding='utf-8')
print(df)

# Escrevendo em arquivos CSV
# Da mesma forma podemos utilizar o módulo 'csv' para escrever em arquivos CSV.

# Exemplo

import csv

with open('exemplo.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['Nome', 'Idade', 'Cidade'])  # Cabeçalho
    escritor_csv.writerow(['João', 25, 'São Paulo'])
    escritor_csv.writerow(['Maria', 30, 'Rio de Janeiro'])
    escritor_csv.writerow(['Pedro', 22, 'Belo Horizonte'])

# Lendo arquivos CSV com pandas
# O pandas é uma biblioteca poderosa para manipulação de dados em Python. Ele fornece funções convenientes para ler e escrever arquivos CSV.

# Exemplo

import pandas as pd
# Lendo um arquivo CSV
df = pd.read_csv('exemplo.csv', encoding='utf-8')
print(df)

# Práticas recomendadas
# Usarcsv.reader e csv.writer para manipular arquivos CSV.
# Fazer otratamentocorreto das exceções.
# Ao gravar arquivos CSV definir o argumento newline='' no método'open'.
