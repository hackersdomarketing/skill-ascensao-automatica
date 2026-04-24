#!/usr/bin/env python3
"""
Gerador de Estratégias de Ascensão Automática

Gera estratégias completas de ascensão baseadas em inputs do negócio,
aplicando os 8 padrões fundamentais identificados.

Uso:
    python gerar_estrategia_ascensao.py \
        --produto-atual "Curso Frontend R$ 97" \
        --produto-alvo "Mentoria R$ 2997" \
        --avatar "Iniciante em marketing digital" \
        --output estrategia_customizada.json
"""

import json
import argparse
from datetime import datetime, timedelta
import re

# Padrões fundamentais de ascensão
PADROES = {
    "automatico_semi_manual": {
        "nome": "Sequência Automático → Semi → Manual",
        "aplicacao": "Sempre tentar primeiro automação, depois semi-automação, por último manual"
    },
    "consciencia_desejo_oferta": {
        "nome": "Consciência → Desejo → Oferta",
        "aplicacao": "1. Gerar consciência, 2. Aumentar desejo, 3. Fazer oferta"
    },
    "resolver_criar_problema": {
        "nome": "Resolver Problema → Criar Novo Problema",
        "aplicacao": "Cada produto resolve problema mas cria consciência de novo problema"
    },
    "valor_percebido_diferente": {
        "nome": "Valor Percebido Diferente Por Degrau",
        "aplicacao": "Mesmo método, formatos diferentes"
    },
    "ver_sem_ter_acesso": {
        "nome": "Ver Sem Ter Acesso",
        "aplicacao": "Fazer pessoas verem o que não tem acesso"
    },
    "conexao_360": {
        "nome": "Conexão 360°",
        "aplicacao": "Marca + Tribo + Expert + Método + Comunidade"
    },
    "habito_uso_sem_posse": {
        "nome": "Hábito de Uso Sem Posse",
        "aplicacao": "Cliente usa mas não possui, depende de você"
    },
    "evolucao_status": {
        "nome": "Evolução Progressiva Com Status",
        "aplicacao": "Níveis com nomenclaturas e benefícios progressivos"
    }
}

FUNIS_AUTOMATICOS = [
    {
        "nome": "FUNIL DE CUPOM DE DESCONTO",
        "descricao": "Mini-workshop + cupom com urgência",
        "conversao_esperada": "5-12%",
        "tempo_implementacao": "3-5 dias"
    },
    {
        "nome": "WEBINAR AUTOMÁTICO",
        "descricao": "Webinar evergreen 60-90 min",
        "conversao_esperada": "3-8%",
        "tempo_implementacao": "7-14 dias"
    },
    {
        "nome": "VSL + CHECKOUT PERSONALIZADO",
        "descricao": "Video Sales Letter + checkout otimizado",
        "conversao_esperada": "2-5%",
        "tempo_implementacao": "5-7 dias"
    },
    {
        "nome": "TRIAL + DOUTRINAÇÃO + VSL",
        "descricao": "Trial gratuito + sequência de doutrinação + pitch",
        "conversao_esperada": "10-20%",
        "tempo_implementacao": "10-14 dias"
    },
    {
        "nome": "MÓDULO PRÓXIMOS PASSOS",
        "descricao": "Módulo integrado no produto atual com pitch",
        "conversao_esperada": "8-15%",
        "tempo_implementacao": "5-10 dias"
    }
]

FUNIS_SEMI_AUTOMATICOS = [
    {
        "nome": "CALL DE 2 ETAPAS",
        "descricao": "Call em grupo + call individual de fechamento",
        "conversao_esperada": "15-25%",
        "tempo_implementacao": "3-5 dias"
    },
    {
        "nome": "CALL DE BOAS VINDAS COM PITCH",
        "descricao": "Onboarding call com apresentação de upgrade",
        "conversao_esperada": "10-20%",
        "tempo_implementacao": "2-3 dias"
    },
    {
        "nome": "CALL DE ENTREGA DE BÔNUS",
        "descricao": "Entrega de bônus exclusivo com pitch contextual",
        "conversao_esperada": "20-35%",
        "tempo_implementacao": "5-7 dias"
    }
]

CAMPANHAS_MANUAIS = [
    {
        "nome": "CALENDÁRIO DE ASCENSÃO POR DEGRAU",
        "descricao": "Campanhas semanais segmentadas por nível",
        "conversao_esperada": "3-8%",
        "tempo_implementacao": "7-14 dias"
    },
    {
        "nome": "EVENTO MENSAL DE ASCENSÃO",
        "descricao": "Evento online mensal com pitch de upgrade",
        "conversao_esperada": "5-10%",
        "tempo_implementacao": "14-30 dias"
    },
    {
        "nome": "CAMPANHA DE RECUPERAÇÃO SEGMENTADA",
        "descricao": "Recuperação manual de leads qualificados",
        "conversao_esperada": "8-15%",
        "tempo_implementacao": "7-10 dias"
    }
]


def extrair_preco(texto):
    """Extrai valor numérico de string com preço"""
    match = re.search(r'R?\$?\s*(\d+[\.,]?\d*)', texto)
    if match:
        return float(match.group(1).replace(',', '.'))
    return 0


def calcular_gap_preco(produto_atual, produto_alvo):
    """Calcula gap de preço entre produtos"""
    preco_atual = extrair_preco(produto_atual)
    preco_alvo = extrair_preco(produto_alvo)

    if preco_atual > 0:
        return preco_alvo / preco_atual
    return 0


def identificar_padroes_aplicaveis(gap_preco, avatar):
    """Identifica quais padrões aplicar baseado em contexto"""
    padroes_aplicaveis = []

    # Sempre aplicar automático → semi → manual
    padroes_aplicaveis.append("automatico_semi_manual")

    # Gap grande de preço: consciência e desejo antes da oferta
    if gap_preco > 5:
        padroes_aplicaveis.append("consciencia_desejo_oferta")
        padroes_aplicaveis.append("ver_sem_ter_acesso")

    # Avatar iniciante: conexão 360°
    if "iniciante" in avatar.lower() or "começ" in avatar.lower():
        padroes_aplicaveis.append("conexao_360")

    # Sempre criar problema novo
    padroes_aplicaveis.append("resolver_criar_problema")

    # Sempre diferenciar valor percebido
    padroes_aplicaveis.append("valor_percebido_diferente")

    return padroes_aplicaveis


def gerar_funil_automatico(produto_atual, produto_alvo, gap_preco):
    """Seleciona melhor funil automático baseado em contexto"""
    if gap_preco < 3:
        # Gap pequeno: upsell direto
        return FUNIS_AUTOMATICOS[4]  # Módulo Próximos Passos
    elif gap_preco < 10:
        # Gap médio: webinar ou VSL
        return FUNIS_AUTOMATICOS[1]  # Webinar Automático
    else:
        # Gap grande: trial + doutrinação
        return FUNIS_AUTOMATICOS[3]  # Trial + Doutrinação


def gerar_sequencia_doutrinacao(produto_atual, produto_alvo):
    """Gera sequência de doutrinação progressiva"""
    return {
        "0_unica_crenca": {
            "pergunta": f"Qual é a ÚNICA COISA que se o cliente que comprou '{produto_atual}' CRER, ele não tem outra opção a não ser comprar '{produto_alvo}'?",
            "exemplo": "Se ele crer que [CRENÇA], ele PRECISA ter [PRODUTO ALVO]"
        },
        "1_curiosidade": {
            "mecanismos": [
                "Quebra de padrão com manchetes clickbait",
                "Formato/posicionamento diferente",
                "Mostrar resultado dos sonhos de forma contraditória",
                "CTA: 'Quer entender como?'"
            ]
        },
        "2_confianca": {
            "taticas": [
                "Demonstrar autoridade (resultados, credenciais)",
                "Criar vínculo emocional por valores compartilhados"
            ]
        },
        "3_esperanca": {
            "taticas": [
                "Disseminar próximo problema ao longo do produto",
                "Promessas claras e tangíveis",
                "Histórias de alunos do próximo nível",
                "Livrar de objeções e medos"
            ]
        },
        "4_desejo": {
            "taticas": [
                "Motivos pelos quais DEVERIA ter",
                "Diferenças e vantagens exclusivas",
                "Benefícios extras gerados",
                "Aumento de status percebido"
            ]
        },
        "5_hooks": {
            "taticas": [
                "Curiosidade sobre próximo passo",
                "Resultado dos sonhos deste avatar",
                "Ângulo narrativo contraditório mas crível",
                "CTA para ação específica"
            ]
        }
    }


def gerar_problema_criado(produto_atual):
    """Sugere problemas que são criados ao resolver o atual"""
    return {
        "principio": "Ao resolver o problema prometido no produto atual, um novo problema natural emerge",
        "exercicio": f"Se '{produto_atual}' ensina __________, que novo problema isso cria?",
        "exemplos": [
            {
                "produto_ensina": "Como criar vídeo viral",
                "problema_criado": "O que fazer com tanta visualização? Como capturar leads e converter?",
                "proximo_produto_resolve": "Sistema de captura e conversão de tráfego viral"
            },
            {
                "produto_ensina": "Como gerar tráfego orgânico",
                "problema_criado": "Como converter esse tráfego em vendas sem funil estruturado?",
                "proximo_produto_resolve": "Funil completo de conversão com copy e ofertas"
            },
            {
                "produto_ensina": "Como fazer primeira venda online",
                "problema_criado": "Como escalar vendas sem depender só de esforço manual?",
                "proximo_produto_resolve": "Sistema de vendas automatizado"
            }
        ],
        "implementacao": "Disseminar esse novo problema AO LONGO do produto atual, não apenas no final"
    }


def gerar_calendario_implementacao(funil_auto, funil_semi, campanha_manual):
    """Gera cronograma de implementação"""
    hoje = datetime.now()

    calendario = {
        "fase_1_automatico": {
            "inicio": hoje.strftime("%Y-%m-%d"),
            "fim": (hoje + timedelta(days=14)).strftime("%Y-%m-%d"),
            "funil": funil_auto["nome"],
            "tarefas": [
                "Criar estrutura do funil",
                "Produzir conteúdo/vídeos",
                "Configurar automações",
                "Testar fluxo completo",
                "Ativar tráfego"
            ]
        },
        "fase_2_semi_automatico": {
            "inicio": (hoje + timedelta(days=14)).strftime("%Y-%m-%d"),
            "fim": (hoje + timedelta(days=21)).strftime("%Y-%m-%d"),
            "funil": funil_semi["nome"],
            "tarefas": [
                "Treinar time para calls",
                "Criar scripts de call",
                "Configurar agendamento",
                "Teste piloto com 10-20 clientes",
                "Ativar para todos"
            ],
            "nota": "Só ativar SE funil automático tiver conversão < 10%"
        },
        "fase_3_manual": {
            "inicio": (hoje + timedelta(days=30)).strftime("%Y-%m-%d"),
            "fim": (hoje + timedelta(days=60)).strftime("%Y-%m-%d"),
            "campanha": campanha_manual["nome"],
            "tarefas": [
                "Segmentar base que não ascendeu",
                "Criar sequências de recuperação",
                "Desenvolver ofertas especiais",
                "Executar campanhas semanais",
                "Medir e otimizar"
            ],
            "nota": "Para recuperar quem não ascendeu pelos automáticos"
        }
    }

    return calendario


def gerar_estrategia_completa(produto_atual, produto_alvo, avatar):
    """Gera estratégia completa de ascensão"""

    # Análise de contexto
    gap_preco = calcular_gap_preco(produto_atual, produto_alvo)
    padroes_aplicaveis = identificar_padroes_aplicaveis(gap_preco, avatar)

    # Seleção de funis
    funil_automatico = gerar_funil_automatico(produto_atual, produto_alvo, gap_preco)
    funil_semi = FUNIS_SEMI_AUTOMATICOS[0]  # Call de 2 etapas como padrão
    campanha_manual = CAMPANHAS_MANUAIS[0]  # Calendário por degrau

    # Construção da estratégia
    estrategia = {
        "metadata": {
            "gerado_em": datetime.now().isoformat(),
            "produto_atual": produto_atual,
            "produto_alvo": produto_alvo,
            "avatar": avatar,
            "gap_preco": f"{gap_preco:.1f}x"
        },
        "analise_contexto": {
            "gap_preco_calculado": gap_preco,
            "interpretacao": (
                "Gap pequeno (< 3x)" if gap_preco < 3 else
                "Gap médio (3-10x)" if gap_preco < 10 else
                "Gap grande (> 10x)"
            ),
            "padroes_identificados": [
                {
                    "padrao": padrao,
                    "nome": PADROES[padrao]["nome"],
                    "aplicacao": PADROES[padrao]["aplicacao"]
                }
                for padrao in padroes_aplicaveis
            ]
        },
        "estrategia_nivel_1_automatico": {
            "prioridade": "ALTA - Implementar PRIMEIRO",
            "funil": funil_automatico,
            "sequencia_doutrinacao": gerar_sequencia_doutrinacao(produto_atual, produto_alvo),
            "problema_criado": gerar_problema_criado(produto_atual),
            "hooks_trafego_interno": [
                "Emails de consumo + relacionamento (sequência 14 dias)",
                "Banners dentro do produto atual",
                "Módulo 'Próximos Passos' integrado",
                "Produtos bloqueados à mostra na área de membros",
                "Email 'Pode me fazer um favor?' (2 dias após compra)"
            ]
        },
        "estrategia_nivel_2_semi_automatico": {
            "prioridade": "MÉDIA - Usar SE automático < 10% conversão",
            "funil": funil_semi,
            "quando_ativar": "Após 30 dias do automático, se conversão < 10%",
            "recursos_necessarios": [
                "Time treinado para calls",
                "Scripts de qualificação e fechamento",
                "Sistema de agendamento (Calendly, etc)",
                "CRM para rastreamento"
            ]
        },
        "estrategia_nivel_3_manual": {
            "prioridade": "BAIXA - Apenas para RECUPERAÇÃO",
            "campanha": campanha_manual,
            "quando_ativar": "Após 60-90 dias, para recuperar quem não ascendeu",
            "segmentacao": [
                "Comprou produto atual mas não ascendeu",
                "Alta taxa de consumo mas sem compra",
                "Abandonou carrinho do produto alvo",
                "Está há 90+ dias sem ascender"
            ]
        },
        "cronograma_implementacao": gerar_calendario_implementacao(
            funil_automatico, funil_semi, campanha_manual
        ),
        "metricas_sucesso": {
            "kpis_monitorar": [
                "Taxa de ascensão mensal (meta: ≥ 10%)",
                "Tempo médio para ascender (acompanhar tendência)",
                "Conversão do funil automático (meta: 5-12%)",
                "Conversão do funil semi (meta: 15-25%)",
                "Taxa de recuperação manual (meta: 3-8%)",
                "LTV incremental por estratégia"
            ],
            "benchmarks": {
                "funil_automatico": funil_automatico["conversao_esperada"],
                "funil_semi_automatico": funil_semi["conversao_esperada"],
                "campanha_manual": campanha_manual["conversao_esperada"]
            }
        },
        "proximos_passos": {
            "semana_1": [
                "Revisar estratégia completa com time",
                "Priorizar funil automático",
                "Definir 'única crença' para doutrinação",
                "Mapear problema criado ao resolver atual"
            ],
            "semana_2": [
                f"Implementar {funil_automatico['nome']}",
                "Criar sequência de doutrinação",
                "Configurar hooks de tráfego interno",
                "Preparar métricas de rastreamento"
            ],
            "semana_3_4": [
                "Ativar funil automático",
                "Monitorar conversões diariamente",
                "Coletar feedback qualitativo",
                "Otimizar pontos de fricção"
            ],
            "mes_2": [
                "Avaliar performance do automático",
                "Se conversão < 10%, preparar funil semi-automático",
                "Começar segmentação para campanhas manuais",
                "Documentar aprendizados"
            ]
        }
    }

    return estrategia


def main():
    parser = argparse.ArgumentParser(
        description="Gerador de Estratégias de Ascensão Automática"
    )
    parser.add_argument(
        "--produto-atual",
        required=True,
        help="Produto atual do cliente (ex: 'Curso Frontend R$ 97')"
    )
    parser.add_argument(
        "--produto-alvo",
        required=True,
        help="Produto para o qual quer ascender (ex: 'Mentoria R$ 2997')"
    )
    parser.add_argument(
        "--avatar",
        required=True,
        help="Descrição do avatar (ex: 'Iniciante em marketing digital')"
    )
    parser.add_argument(
        "--output",
        default="estrategia_ascensao.json",
        help="Arquivo de saída (default: estrategia_ascensao.json)"
    )

    args = parser.parse_args()

    print("🚀 Gerando estratégia de ascensão automática...\n")

    estrategia = gerar_estrategia_completa(
        args.produto_atual,
        args.produto_alvo,
        args.avatar
    )

    # Salvar JSON
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(estrategia, f, ensure_ascii=False, indent=2)

    print(f"✅ Estratégia gerada com sucesso!")
    print(f"📄 Salva em: {args.output}\n")

    # Resumo executivo
    print("=" * 80)
    print("RESUMO EXECUTIVO DA ESTRATÉGIA")
    print("=" * 80)

    print(f"\n📊 ANÁLISE:")
    print(f"   Gap de preço: {estrategia['metadata']['gap_preco']}")
    print(f"   Interpretação: {estrategia['analise_contexto']['interpretacao']}")

    print(f"\n🎯 PRIORIDADE 1 - AUTOMÁTICO:")
    print(f"   Funil: {estrategia['estrategia_nivel_1_automatico']['funil']['nome']}")
    print(f"   Conversão esperada: {estrategia['estrategia_nivel_1_automatico']['funil']['conversao_esperada']}")
    print(f"   Tempo impl.: {estrategia['estrategia_nivel_1_automatico']['funil']['tempo_implementacao']}")

    print(f"\n🔄 PRIORIDADE 2 - SEMI-AUTOMÁTICO:")
    print(f"   Funil: {estrategia['estrategia_nivel_2_semi_automatico']['funil']['nome']}")
    print(f"   Quando: {estrategia['estrategia_nivel_2_semi_automatico']['quando_ativar']}")

    print(f"\n👤 PRIORIDADE 3 - MANUAL:")
    print(f"   Campanha: {estrategia['estrategia_nivel_3_manual']['campanha']['nome']}")
    print(f"   Quando: {estrategia['estrategia_nivel_3_manual']['quando_ativar']}")

    print(f"\n📅 PRÓXIMOS PASSOS:")
    for passo in estrategia['proximos_passos']['semana_1'][:3]:
        print(f"   • {passo}")

    print(f"\n{'=' * 80}")
    print(f"Consulte o arquivo {args.output} para estratégia completa detalhada.")
    print("=" * 80)


if __name__ == "__main__":
    main()
