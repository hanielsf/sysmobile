TIPO_DE_LOTACAO = (
    ('O01', 'Setor, departamento, estabelecimento ou conjunto de estabelecimentos'
            ' do contribuinte, inclusive administração, no caso de cooperativa de '
            'trabalho, obras próprias de construção civil da Pessoa Jurídica e '
            'dependências do próprio trabalhador (trabalho remoto).'),
    ('O02', 'Obra de Construção Civil (Empreitada Parcial ou Sub-empreitada)'),
    ('003', 'Pessoa Física Tomadora de Serviços prestados mediante cessão '
            'de mão de obra, exceto contratante de cooperativa'),
    ('004', 'Pessoa Jurídica Tomadora de Serviços prestados mediante '
            'cessão de mão de obra, exceto contratante de cooperativa, '
            'nos termos da lei 8.212/1991'),
    ('005', 'Pessoa Jurídica Tomadora de Serviços prestados por cooperados '
            'por intermédio de cooperativa de trabalho, exceto aqueles '
            'prestados a entidade beneficente/isenta'),
    ('006', 'Entidade beneficente/isenta Tomadora de Serviços prestados '
            'por cooperados por intermédio de cooperativa de trabalho'),
    ('007', 'Pessoa Física tomadora de Serviços prestados por Cooperados '
            'por intermédio de Cooperativa de Trabalho'),
    ('008', 'Operador Portuário'),
    ('009', 'Empresa Contratante de Avulsos não portuários por intermédio'
            ' do Sindicato'),
    ('010', 'Embarcação inscrita no Registro Especial Brasileiro (REB)'),
    ('021', 'Classificação da atividade econômica ou obra própria de '
            'construção civil da Pessoa Física'),
    ('024', 'Residência/Outros do Empregador Doméstico'),
    ('090', 'Lotação fora do País'),
)


FUNC_ACUM_CARGOS = (
    ('1', 'Não Acumulável'),
    ('2', 'Profissional da Saúde'),
    ('3', 'Professor'),
    ('4', 'Técnico / Científico'),
)


FUNC_CONT_TEMPO_ESPC = (
    ('1', 'Não'),
    ('2', 'Professor (Infantil, Fundamental e Médio)'),
    ('3', 'Professor de Ensino Superior'),
)


FUNC_CARGO_EXCLUSIVO = (
    ('S', 'Sim'),
    ('N', 'Não')
)


FUNC_SITUACAO_LEI_CARGO = (
    ('1', 'Criação'),
    ('2', 'Extinção'),
    ('3', 'Reestruturação'),
)


TIPO_INSCRICAO = (
    ('J', 'Pessoa Jurídica'),
    ('C', 'CAEPF'),
    ('O', 'CNO'),
)


CLASSIFICACAO_TRIBUTARIA = (
    ('001', 'Empresa enquadrada no regime de tributação Simples Nacional '
            'com tributação previdenciária substituída'),
    ('002', 'Empresa enquadrada no regime de tributação Simples Nacional '
            'com tributação previdenciária não substituída'),
    ('003', 'Empresa enquadrada no regime de tributação Simples Nacional '
            'com tributação previdenciária substituída e não substituída'),
    ('004', 'MEI - Micro Empreendedor Individual'),
    ('006', 'Agroindústria'),
    ('007', 'Produtor Rural Pessoa Jurídica'),
    ('008', 'Consórcio Simplificado de Produtores Rurais'),
    ('009', 'Órgão Gestor de Mão de Obra'),
    ('010', 'Entidade Sindical a que se refere a Lei 12.023/2009'),
    ('011', 'Associação Desportiva que mantém Clube de Futebol Profissional'),
    ('013', 'Banco, caixa econômica, sociedade de crédito, financiamento e '
            'investimento e	demais empresas relacionadas no parágrafo 1o do'
            ' art. 22 da Lei 8.212./91'),
    ('014', 'Sindicatos em geral, exceto aquele classificado no código anterior'),
    ('021', 'Pessoa Física, exceto Segurado Especial'),
    ('022', 'Segurado Especial'),
    ('060', 'Missão Diplomática ou Repartição Consular de carreira estrangeira'),
    ('070', 'Empresa de que trata o Decreto 5.436/2005'),
    ('080', 'Entidade Beneficente/Isenta'),
    ('085', 'Ente Federativo, Orgãos da União, Autarquias e Fundações Públicas'),
    ('099', 'Pessoas Jurídicas em Geral'),
)


CONTAGEM_DIAS_MENSALISTAS = (
    ('M', 'Misto Dias Normais e Extraordinários'),
    ('C', 'Sempre Comercial'),
    ('V', 'Sempre número de dias do Mês'),
)


COOPERATIVA = (
    ('00', 'Não é cooperativa'),
    ('01', 'Cooperativa de Trabalho'),
    ('02', 'Cooperativa de Produção'),
    ('03', 'Outras Cooperativas'),
)


SITUACAO_PJ = (
    ('00', 'Situação Normal'),
    ('01', 'Extinção'),
    ('02', 'Fusão'),
    ('03', 'Cisão'),
    ('04', 'Incorporação'),
)

