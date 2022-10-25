# Crie e leia códigos QR
  
Módulo para criar e ler códigos QR
  
*Read this in other languages: [English](Manual_QRReadCreate.md), [Portugues](Manual_QRReadCreate.pr.md), [Español](Manual_QRReadCreate.es.md).*
  
![banner](imgs/Banner_QRReadCreate.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  

## Descrição do comando

### ReadQR
  
Lê um código QR a partir de um arquivo PNG
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do QR em PNG|Selecione o arquivo PNG que contém o código QR|C:/Users/usuario/Desktop/arquivo.png|
|Atribuir resultado a variável|Atribui o conteúdo do código qr a uma variável|variável|

### CreateQR
  
Cria um código QR e salva em um arquivo PNG
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho onde a imagem será armazenada|Caminho onde a imagem PNG com o código QR gerado será armazenada|C:/Users/usuario/Desktop/arquivo.png|
|Escreva o texto do QR|Escreva o texto que será convertido em código QR|htps://rocketbot.com|

### Leitor de código de barras
  
Leia um código de barras de um arquivo PNG ou JPG
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo PNG|Caminho do arquivo PNG com o código de barras|C:/Users/usuario/Desktop/arquivo.png|
|Atribuir resultado a variável|Atribui o resultado do código de barras a uma variável|variável|

### Leitor de código de barras PDF417
  
Lê um código de barras PDF417 a partir de um arquivo de imagem. IMPORTANTE: Java deve ser instalado para o utilizar.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo PNG|Caminho do arquivo PNG com o código de barras|C:/Users/usuario/Desktop/arquivo.png|
|Atribuir resultado a variável|Atribui o resultado do código de barras a uma variável|variável|
