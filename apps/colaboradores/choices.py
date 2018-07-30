TIPO_REGIME_TRABALHISTA = (
    ('CLT', 'Consolidação das Leis do Trabalho'),
    ('RJP', 'Regime Jurídico Próprio'),
)


TIPO_REGIME_PREVIDENCIARIO = (
    ('RGPS', 'Regime Geral da Previdência Social'),
    ('RPPS', 'Regime Próprio de Previdência Social no Brasil'),
    ('RPPE', 'Regime Próprio de Previdência Social no Exterior'),
)


REGIME_DE_JORNADA = (
    ('1', 'Submetidos a Horário de Trabalho'),
    ('2', 'Atividade externa especificada no Inciso I do Art.62 da CTL'),
    ('3', 'Funções especificadas no Inciso II do Art.62 da CTL'),
)


NATUREZA_DA_ATIVIDADE = (
    ('1', 'Trabalho Urbano'),
    ('2', 'Trabalho Rural'),
)


CATEGORIA = (
    ('1', 'Empregado - Geral'),
    ('2', 'Trabalhador Rural por Pequeno Prazo'),
    ('3', 'Empregado - Aprendiz'),
    ('4', 'Empregado - Doméstico'),
    ('5', 'Empregado - contrato a termo firmado nos termos da lei 9601/98'),
    ('6', 'Empregado - contrato por prazo determinado'),
    ('7', 'Empregado - contrato de trabalho intermitente'),
    ('8', 'Servidor Público Titular de Cargo Efetivo'),
    ('9', 'Servidor Público Ocupante de Cargo exclusivo em comissão'),
    ('10', 'Agente Político'),
    ('11', 'Servidor Público indicado para conselho ou órgão representativo'),
    ('12', 'Servidor Público Temporário'),
    ('13', 'Agente Público - Outros'),
    ('14', 'Dirigente Sindical - informações prestadas pelo Sindicato'),
    ('15', 'Trabalhador cedido - informação prestada pelo Cessionário'),
)


VINCULO_COM_OUTRA_EMPRESA = (
    ('1', 'Sem vínculo com outra empresa'),
    ('2', 'Contribuição descontada pelo empregador aqui declarante'),
    ('3', 'Contribuição descontada por outra empresa, valor inferior ao limite'),
    ('4', 'Contribuição descontada por outra empresa, valor total de contribuição'),
)

TIPO_CONTRATO_TRABALHO = (
    ('I', 'Prazo indeterminado'),
    ('D', 'Prazo determinado'),
    ('E', 'Experiência'),
)


TIPO_ADMISSAO = (
    ('A', 'Admissão'),
    ('E', 'Transferência de empresa do mesmo grupo econômico'),
    ('C', 'Transferência de empresa consorciada ou de consórcio'),
    ('S', 'Transferência por motivo de sucessão, incorporação, cisão ou fusão'),
)


INDICATIVO_ADMISSAO = (
    ('N', 'Normal'),
    ('F', 'Decorrente de Ação Fiscal'),
    ('J', 'Decorrente de Decisão Judicial'),
)


UNIDADE_SALARIO = (
    ('M', 'Por Mês'),
    ('H', 'Por Hora'),
    ('D', 'Por Dia'),
    ('S', 'Por Semana'),
    ('Q', 'Por Quinzena'),
    ('T', 'Por Tarefa'),
    ('N', 'Não aplicável'),
)



