# Um conversor dos textos do jogo Guilty Gear Strive de formato txt para json
## Objetivo: Codificar o .uexp e transformá-lo em um arquivo json separando os 'headers' e os 'texts'
### Ações:
1. O programa lê o arquivo 'REDGame.uexp' contido nos arquivos do jogo [Documentação para gerar o arquivo](https://docs.google.com/document/d/1KVPcYy4iekH2sEvgmECg9hPEfvFHvzjSKCMXkVMCXVE/edit?pli=1)
2. Separa cada 'header' e cada 'text'
3. Traduz os texts de EN-US para PT-BR
3. Gera o objeto 'Entries' contendo cada objeto 'header' e 'text'
4. Por fim, cria o arquivo json contendo os valores traduzidos

