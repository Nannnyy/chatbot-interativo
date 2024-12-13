from models.pergunta import Pergunta

def construirListaPerguntas(dicionario_json):
    perguntas = [Pergunta(
        pergunta['id'],
        pergunta['texto'],
        pergunta['tipo'],
        pergunta['resposta_correta'],
        pergunta.get('opcoes', None)
    ) for pergunta in dicionario_json['perguntas']]

    return perguntas