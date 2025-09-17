
# PriceWatcher

O PriceWatcher é um scraper de preços que monitora produtos no site Zoom. Ele verifica o preço do produto mais barato, identifica a loja e envia uma notificação via Telegram caso o preço esteja abaixo do desejado.
O projeto foi desenvolvido em Python usando Playwright para automação do navegador.


## Funcionalidades

- Busca produtos no Zoom usando o nome definido em data/products.json.

- Captura: Nome do produto, preço mais baixo, poja que oferece o menor preço,  link para a página do produto  e envia notificações através de um bot no Telegram quando o preço atinge o valor alvo.


## Configuração

1. Crie um bot no Telegram e obtenha:

```bash
  TELEGRAM_TOKEN
  CHAT_ID
```

2. Adicione essas informações no ```notifier.py``` ou como variáveis de ambiente

3. Adicione os produtos que deseja monitorar no arquivo ```data/products.json``` nesse formato

```bash
[
  {"name": "Nome do produto", "target_price": Preço que quer comprar}
]
```
## Rodando localmente

1. Clone o projeto

```markdown
  git clone https://github.com/lima1301lucas/PriceWatcher.git
```

2. Entre no diretório do projeto

```bash
  cd PriceWatcher
```

3. Instale as dependências

```bash
  python -m pip install --upgrade pip
  pip install playwright requests
  playwright install
```

4. Inicie a aplicação

```bash
  python main.py
```
## Stack utilizada

**Back-end:** Python, Playwright

