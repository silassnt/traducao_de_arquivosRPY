import re
from deep_translator import GoogleTranslator


tradutor = GoogleTranslator(source='pt', target='en')


arquivo = input("Digite o nome do arquivo .rpy que você quer traduzir: ")

try:
    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Encontra todas as falas entre aspas
    falas = re.findall(r'"(.*?)"', conteudo)

    print(f"\nTotal de falas encontradas: {len(falas)}")
    print("Traduzindo...\n")

    for fala in falas:
        if fala.strip() == "":
            continue
        try:
            traducao = tradutor.translate(fala)
            conteudo = conteudo.replace(f'"{fala}"', f'"{traducao}"')
        except Exception as e:
            print(f"Erro ao traduzir: {fala} -> {e}")

    # Nome do novo arquivo
    novo_arquivo = arquivo.replace(".rpy", "_traduzido.rpy")
    with open(novo_arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"\n✅ Tradução finalizada com sucesso! Arquivo salvo como: {novo_arquivo}")

except FileNotFoundError:
    print("❌ Arquivo não encontrado. Verifique o nome e tente novamente.")


    