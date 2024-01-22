# Polideuces 01 - Começando

>[Access this guide in english / Acesse este guia em inglês](/docs/en-1-getting-started.md)

## Table of Contents

1. [Configurando](#configurando)
	- [Configure o Raspbberry Pi](#configure-o-raspberry-pi)
	- [Configures sua Máquina](#configure-sua-máquina)
2. [Construindo o Robô](#construindo-o-robo)
	- [Lista de Componentes](#lista-de-componentes)
	- [Juntando Tudo](#juntando-tudo)
3. [Executando o Código do Robô](#executando-o-código-do-robô)

## Configurando

>Muitos dos links desse guia enviam para páginas em inglês, mas você pode usar a [extensão do Google Translate](https://chromewebstore.google.com/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb?pli=1) para o Chrome pra que a página seja traduida automaticamente.

### Configure o Raspberry Pi

1. Cadastre-se gratuitamente para obter uma [conta Viam](https://www.viam.com/).

2. Configure seu Raspberry Pi seguindo o [guia de configuração da Viam](https://docs.viam.com/get-started/installation/prepare/rpi-setup/)
	- Se for usar uma placa diferente, procure seguir o [guia de configuração da Viam para sua placa específica](https://docs.viam.com/), se houver suporte.

3. Se você ainda não fez isso após o guia de configuração do Viam, acesse a [aplicação da Viam](https://app.viam.com/) e adicione uma nova máquina fornecendo um nome no campo "New machine"  e clicando em "Add machine".
	- Na aba "Setup", selecione `Linux (Aarch64)` ou `Linux (x86_64)` para a arquitetura apropriada para o seu computador. Os Raspberry Pi são `Linux (Aarch64)`, mas você pode confirmar isso executando `uname -m`.
	- Siga as etapas mostradas na aba "Setup" para instalar o `viam-server` no seu Raspberry Pi e aguarde a confirmação de que o seu computador foi conectado com sucesso.
	- Por padrão, o `viam-server` iniciará automaticamente quando o sistema for inicializado, mas você pode [alterar esse comportamento](https://docs.viam.com/get-started/installation/manage/) se desejar.

4. Na [aplicação da Viam](https://app.viam.com/), selecione seu robô recém criado e navegue até a guia "Config". Selecione o modo "Raw JSON" e copie e cole o conteúdo de `src/polideuces/configs/polideuces-01.json` lá.
	- Sinta-se livre para alterar quaisquer detalhes das configurações conforme achar necessário. Apenas tome cuidado para alterá-lo também em sua eletrônica e no arquivo `src/polideuces/configs/polideuces-01.json` para que os scripts possam funcionar corretamente.

### Configure sua Máquina

>Certifique-se de que tem o Python 3 com `pip` e `virtualenv` instalados em sua máquina. Você pode saber mais em:
>- [Baixar Python - Python.org](https://www.python.org/downloads/)
>- [Guia de instalação e configuração do Python 3 – Real Python](https://realpython.com/installing-python/)

1. Clone ou baixe este repositório com:

```
git clone git@github.com:EEmery/polideuces-01.git
```

Ou, se preferir, você pode clicar no botão verde "Código" no canto superior direito e selecionar "Baixar ZIP".

2. Em seu terminal, navegue até a raiz da pasta do repositório, crie um novo ambiente e ative-o com:

```
python3 -m venv .venv && source .venv/bin/activate
```

3. Instale as dependências com:

```
python3 -m pip install -r requirements/prod.txt
```

4. Adicione as credenciais ao seu robô no repositório criando um arquivo chamado `credentials.json` em `src/polideuces/secrets/`. O arquivo `credentials.json` deve ser parecido com isto:

```
{
     "name": "nome-do-seu-robô",
     "address": "endereço-do-seu-robô",
     "credential": "sua-credencial"
}
```

Você pode encontrar o endereço do robô na aba "Code sample" da [aplicação da Viam](https://app.viam.com/robots) do seu robô. Ele se parecerá com:

```python
async def connect():
    opts = RobotClient.Options.with_api_key(
	  # Replace "<API-KEY>" (including brackets) with your machine's api key
      api_key='<API-KEY>',
	  # Replace "<API-KEY-ID>" (including brackets) with your machine's api key id
      api_key_id='<API-KEY-ID>'
    )
    return await RobotClient.at_address('endereço-do-seu-robô', opts)
```

Você pode encontrar a credencial na sua [página de robôs na aplicação da Viam](https://app.viam.com/robots). Haverá uma área no final chamada "Secret Keys". Se não houver, clique no botão "Generate key". Copie e cole em seu arquivo `credentials.json`.

>AVISO: Nunca compartilhe ou publique suas credenciais on-line.

## Construindo o Robô

### Lista de componentes

Considere a lista de componentes abaixo como uma sugestão de peças necessárias, mas fique à vontade para alterá-las conforme achar necessário. Apenas certifique-se de atualizar o código e as conexões eletrônicas conforme necessário.

**Atuadores**
- 2 motores Hobby DC com engrenagens de redução e rodas
- 1 driver de motor DC - L298N

**Sensores**
- 1x Webcam - Logitech C270 720p / 30fps HD Webcam com microfone interno
- 1x Acelerômetro - ADLX345
- 1x Sensor de distância - LV Maxsonar EZ

**Cérebros**
- Raspberry Pi 3 Modelo B
- Jumpers de fio de vários tamanhos (principalmente fêmea para fêmea e macho para fêmea)
- Um controle que se conecte ao computado - No meu caso usarei um controle de xbox

**Fornecimento de energia**
- 4 baterias 18265
- 1 suporte para baterias 18265
- 1x conversor redutor DC-DC - Mini560 (7-20V a 5V) step-down
- 1x conversor aumentador DC-DC - MT3608 (2V-9V a 5V) step-up
- 1x interruptor

**Estrutura**
- Parafusos e porcas M2.5
     - De tamanhos variados, mas principalmente de 4 mm a 10 mm
- Parafusos e porcas M3
	- Somente para conexão dos motores DC ao chassi, deve ter no mínimo 23 mm de comprimento
- Peças impressas em 3D:
     - 1x [Esqueleto](/models/Skeleton.stl)
     - 1x [Pé de apoio](/models/Third%20feet.stl)
     - 1x [Suporte de bateria](/models/Battery%20Holder.stl)
     - 1x [Suporte de sensores](/models/Sensors%20Array.stl) (se você decidir imprimir as peças opcionais, o suporte de sensores se tornará desnecessário)
- Peças impressas em 3D opcionais:
     - 1x [Shell - Máscara](/models/Shell%20-%20Mask.stl)
     - 1x [Shell - Parte Superior](/models/Shell%20-%20Top.stl)
     - 2x [Shell - Lado esquerdo](/models/Shell%20-%20Left%20Side.stl) (você pode espelhar o arquivo STL antes de imprimir para obter o lado direito)
     - 2x [Shell - Proteção da roda](/models/Shell%20-%20Wheel%20Cap.stl)
- Você também pode conferir o [Projeto no Onshape](https://cad.onshape.com/documents/57eca4cfdd989f9be606e886/w/89188582492a65a69131f629/e/66d103aafa7007a6db980672?renderMode=0&uiState=659c2bd2daef49 5b2a084473) para copiar e modificar todas as peças do seu jeito.

### Juntando tudo

>Você pode acompanhar a montagem em vídeo:
- [ ] TODO: Adicionar link ao vídeo

**Conexões Eletrônicas**

A fiação completa dos componentes eletrônicos deve ser semelhante a:

![esquemas eletrônicos](/docs/images/electronics-schematic.png)

### Executando o Código do Robô

Para executar o código do robô, certifique-se de que:
- Seu controle de xbox está ligado e conectado ao seu computador
- O robô está ligado e conectado à internet

Depois, basta executar:

```
$python3 src/polideuces/remote_control.py
```
