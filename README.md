# Desenhar com Azimutes/Rumos e distâncias no CAD.

## Objetivo 
Desenvolvi este programa com o objetivo de testar e aprimorar minhas habilidades com python, e tambem desenhar com azimutes e distâncias de maneira mais fácil.

## Descrição
Basicamente a função dele é permitir que o usuário digite informações contidas em certidões de matrícula, memoriais descritivos, ou mapas e formata-las para serem importadas como um script no Autocad ou outro software CAD que permita essa operação também.

O software trabalha com somente com bibliotecas nativas do python, mas em sistemas linux pode ser necessário instalar o tkinter a parte.

## Aparência e usabilidade

O software possui uma usabilidade simples, em um primeiro momento permitindo o usuário escolher qual tipo de script deseja digitar, está informação costuma ser explícita nos documentos:


![image](https://user-images.githubusercontent.com/49497668/139566505-9b1a81e7-42b4-4c7c-8c2b-34da7c24834d.png)


Ao escolher ele é direcionado a janela para digitar as informações, o usuário pode escolher a pasta e o nome do arquivo de script de deseja criar, se não escolher o script é criado na pasta do software com um nome genérico.

Foi feito pensado em softwares em português então se o usuário escolher um script em rumo e digita orientações o NE ou NW automaticamente ele é preenchido no script como NL e NO.

![image](https://user-images.githubusercontent.com/49497668/139566644-c311382f-c32f-4189-a437-ad468cfa0827.png)
![image](https://user-images.githubusercontent.com/49497668/139566916-4e34daed-bfc8-4612-8efb-f2205fea8f96.png)

Ao terminar de digitar todas as orientações o usuário clica em concluir e o software faz o tratamento final para permitir a importação.


>Todo software de CAD tem sua própria maneira de ser configurado para receber scripts, e diferente para azimutes e distâncias, é importante fazer a configuração correta.
>Este software formata o script para sair com duas casas decimais para distância e segundos.





