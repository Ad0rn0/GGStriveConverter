import json
from deep_translator import GoogleTranslator
from tqdm import tqdm

# Carregar o conteúdo do arquivo
file_path = 'C:\Code\TradutorGGStrive\entext.txt'

# Inicializar listas para headers e textos
headers = []
texts = []

# Ler o arquivo e separar headers e textos
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        if i % 2 == 0:
            headers.append(line.strip().replace('\n', ''))
        else:
            texts.append(line.strip().replace('\n', ''))

# Traduzir textos para português com barra de progresso
translator = GoogleTranslator(source='en', target='pt')
translated_texts = []

for text in tqdm(texts, desc="Translating texts"):
    translated_texts.append(translator.translate(text))

# Criar a estrutura JSON
json_data = {
    "Entries": [
        {"header": header, "text": translated_text}
        for header, translated_text in zip(headers, translated_texts)
    ]
}

# Salvar como arquivo JSON
json_file_path = 'C:\Code\TradutorGGStrive\dist\TextoTraduzido.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print(f'Arquivo JSON traduzido salvo em {json_file_path}')

# Pausar a execução para manter a janela do console aberta
input("Pressione Enter para sair...")
