#!/usr/bin/env python3
"""
Gerador de Calendário de Campanhas de Ascensão

Gera calendário completo de campanhas de 90 dias com rotação semanal
por degraus e tipos de campanha.

Uso:
    python calendario_campanhas.py \
        --degraus 3 \
        --inicio 2026-02-01 \
        --output calendario_90_dias.json
"""

import json
import argparse
from datetime import datetime, timedelta
from typing import List, Dict


TIPOS_CAMPANHA = {
    "automatica": {
        "nome": "Campanha Automática",
        "descricao": "Funis e sequências 100% automatizadas",
        "frequencia": "Sempre ativa",
        "exemplos": [
            "Webinar automático",
            "Sequência de emails de ascensão",
            "Módulo 'Próximos Passos'",
            "Banners na área de membros"
        ]
    },
    "semi_automatica": {
        "nome": "Campanha Semi-Automática",
        "descricao": "Automação + toque humano",
        "frequencia": "Semanal ou mensal",
        "exemplos": [
            "Calls de boas-vindas",
            "Calls de 2 etapas",
            "Eventos online mensais",
            "Q&A ao vivo com pitch"
        ]
    },
    "recuperacao": {
        "nome": "Campanha de Recuperação",
        "descricao": "Reativar quem não ascendeu",
        "frequencia": "Quinzenal ou mensal",
        "exemplos": [
            "Email de abandono de carrinho",
            "Ofertas especiais para inativos",
            "Ligações de recuperação",
            "Promoções relâmpago"
        ]
    },
    "evento": {
        "nome": "Evento de Ascensão",
        "descricao": "Eventos com pitch estruturado",
        "frequencia": "Mensal ou trimestral",
        "exemplos": [
            "Masterclass ao vivo",
            "Desafio de 3-5 dias",
            "Imersão online",
            "Evento presencial"
        ]
    }
}


def gerar_semanas_calendario(data_inicio, num_semanas=12):
    """Gera lista de semanas a partir da data de início"""
    semanas = []

    for i in range(num_semanas):
        inicio_semana = data_inicio + timedelta(weeks=i)
        fim_semana = inicio_semana + timedelta(days=6)

        semanas.append({
            "numero": i + 1,
            "inicio": inicio_semana.strftime("%Y-%m-%d"),
            "fim": fim_semana.strftime("%Y-%m-%d"),
            "mes": inicio_semana.strftime("%B %Y")
        })

    return semanas


def atribuir_campanhas_por_semana(semanas, num_degraus):
    """Atribui campanhas a cada semana com rotação por degrau"""

    calendario = []

    for semana in semanas:
        num_semana = semana['numero']

        # Rotação de degraus (4 semanas por ciclo completo)
        degrau_foco = ((num_semana - 1) % 4)

        if degrau_foco < num_degraus:
            # Semanas 1-3: Focar em degrau específico
            degrau_nome = f"Degrau {degrau_foco + 1}"
            tipo_campanha = determinar_tipo_campanha(num_semana, degrau_foco)

        else:
            # Semana 4: Recuperação geral
            degrau_nome = "Todos os degraus"
            tipo_campanha = "recuperacao"

        campanha_info = TIPOS_CAMPANHA[tipo_campanha]

        # Gerar ações específicas
        acoes = gerar_acoes_semana(tipo_campanha, degrau_foco if degrau_foco < num_degraus else None, num_semana)

        calendario.append({
            "semana": num_semana,
            "periodo": f"{semana['inicio']} a {semana['fim']}",
            "mes": semana['mes'],
            "degrau_foco": degrau_nome,
            "tipo_campanha": campanha_info['nome'],
            "descricao": campanha_info['descricao'],
            "acoes": acoes,
            "metricas_acompanhar": gerar_metricas(tipo_campanha, degrau_foco if degrau_foco < num_degraus else None)
        })

    return calendario


def determinar_tipo_campanha(num_semana, degrau):
    """Determina tipo de campanha baseado na semana e degrau"""

    # Padrão de rotação
    if num_semana % 4 == 1:
        return "automatica"
    elif num_semana % 4 == 2:
        return "semi_automatica"
    elif num_semana % 4 == 3:
        return "evento"
    else:  # num_semana % 4 == 0
        return "recuperacao"


def gerar_acoes_semana(tipo_campanha, degrau, num_semana):
    """Gera ações específicas para a semana"""

    acoes = {
        "automatica": [
            {
                "dia": "Segunda (Dia 1)",
                "acao": "Ativar sequência de emails de ascensão",
                "detalhe": "5 emails ao longo da semana com histórias, provas e CTA"
            },
            {
                "dia": "Terça (Dia 2)",
                "acao": "Ativar banners de ascensão na área de membros",
                "detalhe": "Banner contextual aparece após consumo de 3+ aulas"
            },
            {
                "dia": "Quarta (Dia 3)",
                "acao": "Remarketing para quem clicou mas não comprou",
                "detalhe": "Audiência custom: clicou em oferta mas não finalizou"
            },
            {
                "dia": "Sexta (Dia 5)",
                "acao": "Email de urgência: 'Últimas 48h para oferta especial'",
                "detalhe": "Bônus exclusivo + desconto que expira domingo"
            },
            {
                "dia": "Domingo (Dia 7)",
                "acao": "Email final: 'Oferta encerra hoje à meia-noite'",
                "detalhe": "Última chance + depoimentos + FAQ"
            }
        ],
        "semi_automatica": [
            {
                "dia": "Segunda (Dia 1)",
                "acao": "Enviar convites para call de boas-vindas/upgrade",
                "detalhe": "Segmentar: clientes ativos há 14+ dias que não ascenderam"
            },
            {
                "dia": "Terça-Quarta (Dias 2-3)",
                "acao": "Realizar calls de 2 etapas - Grupo",
                "detalhe": "Call em grupo (50-100 pessoas) com pitch do upgrade"
            },
            {
                "dia": "Quinta-Sexta (Dias 4-5)",
                "acao": "Calls individuais de fechamento",
                "detalhe": "Quem se interessou na call em grupo agenda individual"
            },
            {
                "dia": "Sábado (Dia 6)",
                "acao": "Follow-up com quem não agendou call",
                "detalhe": "WhatsApp/Email: 'Ficou alguma dúvida? Fale comigo'"
            },
            {
                "dia": "Domingo (Dia 7)",
                "acao": "Análise de resultados e documentação",
                "detalhe": "Taxa de conversão, objeções comuns, melhorias"
            }
        ],
        "evento": [
            {
                "dia": "Segunda (Dia 1)",
                "acao": "Anúncio do evento da semana",
                "detalhe": "Email + post: 'Masterclass GRATUITA na Sexta sobre [TEMA]'"
            },
            {
                "dia": "Terça-Quarta (Dias 2-3)",
                "acao": "Antecipação e inscrições",
                "detalhe": "Emails de buildup: quem vai palestrar, o que vai aprender, spoilers"
            },
            {
                "dia": "Quinta (Dia 4)",
                "acao": "Lembrete 24h antes",
                "detalhe": "Email + WhatsApp: 'Amanhã é o dia! Prepare [X] e [Y]'"
            },
            {
                "dia": "Sexta (Dia 5)",
                "acao": "EVENTO AO VIVO",
                "detalhe": "60-90 min de conteúdo + 15-20 min de pitch do upgrade"
            },
            {
                "dia": "Sábado-Domingo (Dias 6-7)",
                "acao": "Follow-up pós-evento",
                "detalhe": "Replay + oferta especial 48h para quem participou"
            }
        ],
        "recuperacao": [
            {
                "dia": "Segunda (Dia 1)",
                "acao": "Segmentar base que não ascendeu",
                "detalhe": "Criar listas: comprou há 30/60/90+ dias e não ascendeu"
            },
            {
                "dia": "Terça (Dia 2)",
                "acao": "Email de reativação de valor",
                "detalhe": "'Você está aproveitando [BENEFÍCIO X]?' - Sem pitch ainda"
            },
            {
                "dia": "Quarta (Dia 3)",
                "acao": "Email com prova social e resultados",
                "detalhe": "Estudo de caso de quem estava no mesmo degrau e ascendeu"
            },
            {
                "dia": "Quinta (Dia 4)",
                "acao": "Email com oferta exclusiva de recuperação",
                "detalhe": "Desconto + bônus só para quem ainda não ascendeu"
            },
            {
                "dia": "Sexta (Dia 5)",
                "acao": "Ligações para top 20% mais engajados",
                "detalhe": "Call manual: 'Vi que você está ativo, quer acelerar?'"
            },
            {
                "dia": "Sábado-Domingo (Dias 6-7)",
                "acao": "Urgência final + encerramento",
                "detalhe": "Oferta expira domingo + testemunhos de última hora"
            }
        ]
    }

    return acoes.get(tipo_campanha, [])


def gerar_metricas(tipo_campanha, degrau):
    """Gera métricas a acompanhar por tipo de campanha"""

    metricas_base = [
        "Taxa de abertura de emails",
        "Taxa de cliques (CTR)",
        "Visitas à página de vendas",
        "Taxa de conversão",
        "Receita gerada"
    ]

    metricas_especificas = {
        "automatica": [
            "% que abriu ≥ 3 emails da sequência",
            "Taxa de abandono de carrinho",
            "Conversão do remarketing"
        ],
        "semi_automatica": [
            "Taxa de agendamento de calls",
            "Taxa de comparecimento nas calls",
            "Conversão call grupo → call individual",
            "Conversão final call individual"
        ],
        "evento": [
            "Inscritos no evento",
            "Taxa de comparecimento (show-up rate)",
            "Tempo médio de permanência",
            "Conversão durante evento vs pós-evento"
        ],
        "recuperacao": [
            "% da base segmentada que reagiu",
            "Taxa de reativação",
            "Comparação: recuperação vs primeira campanha"
        ]
    }

    return metricas_base + metricas_especificas.get(tipo_campanha, [])


def gerar_resumo_mensal(calendario):
    """Gera resumo agrupado por mês"""

    resumo = {}

    for semana in calendario:
        mes = semana['mes']

        if mes not in resumo:
            resumo[mes] = {
                "semanas": [],
                "tipos_campanha": [],
                "degraus_trabalhados": set()
            }

        resumo[mes]["semanas"].append(semana['semana'])
        resumo[mes]["tipos_campanha"].append(semana['tipo_campanha'])
        resumo[mes]["degraus_trabalhados"].add(semana['degrau_foco'])

    # Converter sets para listas para JSON
    for mes in resumo:
        resumo[mes]["degraus_trabalhados"] = list(resumo[mes]["degraus_trabalhados"])

    return resumo


def gerar_checklist_preparacao():
    """Gera checklist de preparação antes de iniciar campanhas"""

    return {
        "pre_campanha": [
            "✅ Produtos de ascensão criados e precificados",
            "✅ Páginas de vendas otimizadas com depoimentos",
            "✅ Sequências de email escritas e agendadas",
            "✅ Ferramentas configuradas (automação, CRM, agendamento)",
            "✅ Time treinado para calls (se aplicável)",
            "✅ Scripts de call revisados e aprovados",
            "✅ Métricas de rastreamento configuradas",
            "✅ Segmentações de base criadas",
            "✅ Criativos de email/banners aprovados",
            "✅ Testes A/B definidos (copy, oferta, CTA)"
        ],
        "durante_campanha": [
            "📊 Monitorar métricas diariamente",
            "📧 Responder objeções e dúvidas rapidamente",
            "📞 Fazer follow-up com leads quentes",
            "🔧 Otimizar pontos de fricção identificados",
            "📝 Documentar aprendizados e insights"
        ],
        "pos_campanha": [
            "📈 Analisar resultados vs benchmarks",
            "💡 Identificar o que funcionou melhor",
            "🚫 Listar o que não funcionou e por quê",
            "✏️ Iterar copy, oferta ou funil",
            "🗂️ Organizar materiais para próxima campanha"
        ]
    }


def main():
    parser = argparse.ArgumentParser(
        description="Gerador de Calendário de Campanhas de Ascensão"
    )
    parser.add_argument(
        "--degraus",
        type=int,
        default=3,
        help="Número de degraus na escada de valor (default: 3)"
    )
    parser.add_argument(
        "--inicio",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Data de início no formato YYYY-MM-DD (default: hoje)"
    )
    parser.add_argument(
        "--semanas",
        type=int,
        default=12,
        help="Número de semanas a planejar (default: 12)"
    )
    parser.add_argument(
        "--output",
        default="calendario_90_dias.json",
        help="Arquivo de saída (default: calendario_90_dias.json)"
    )

    args = parser.parse_args()

    print("📅 Gerando calendário de campanhas de ascensão...\n")

    # Parse data de início
    data_inicio = datetime.strptime(args.inicio, "%Y-%m-%d")

    # Gerar semanas
    semanas = gerar_semanas_calendario(data_inicio, args.semanas)

    # Atribuir campanhas
    calendario = atribuir_campanhas_por_semana(semanas, args.degraus)

    # Resumo mensal
    resumo_mensal = gerar_resumo_mensal(calendario)

    # Checklist
    checklist = gerar_checklist_preparacao()

    # Estrutura final
    resultado = {
        "metadata": {
            "gerado_em": datetime.now().isoformat(),
            "data_inicio": args.inicio,
            "num_semanas": args.semanas,
            "num_degraus": args.degraus
        },
        "calendario_semanal": calendario,
        "resumo_mensal": resumo_mensal,
        "checklist_preparacao": checklist,
        "legenda_cores": {
            "automatica": "🟢 Verde - Sempre ativa, baixa manutenção",
            "semi_automatica": "🟡 Amarelo - Requer alguma intervenção humana",
            "evento": "🔵 Azul - Alto esforço, alto impacto",
            "recuperacao": "🟠 Laranja - Recuperação de quem não ascendeu"
        }
    }

    # Salvar
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)

    print(f"✅ Calendário gerado com sucesso!")
    print(f"📄 Salvo em: {args.output}\n")

    # Resumo visual
    print("=" * 80)
    print(f"CALENDÁRIO DE {args.semanas} SEMANAS - {args.degraus} DEGRAUS")
    print("=" * 80)

    print(f"\n📊 RESUMO POR MÊS:\n")
    for mes, info in resumo_mensal.items():
        print(f"  {mes}:")
        print(f"    Semanas: {', '.join(map(str, info['semanas']))}")
        print(f"    Campanhas: {len(set(info['tipos_campanha']))} tipos diferentes")
        print(f"    Degraus: {', '.join(info['degraus_trabalhados'])}")
        print()

    print(f"📋 PADRÃO DE ROTAÇÃO SEMANAL:")
    print(f"  Semana 1: Campanha Automática (Degrau 1)")
    print(f"  Semana 2: Campanha Semi-Automática (Degrau 2)")
    print(f"  Semana 3: Evento de Ascensão (Degrau 3)")
    print(f"  Semana 4: Recuperação (Todos os degraus)")
    print(f"  [Repete o ciclo...]")

    print(f"\n🎯 PRÓXIMAS 3 SEMANAS:")
    for semana in calendario[:3]:
        print(f"\n  Semana {semana['semana']} ({semana['periodo']}):")
        print(f"    Tipo: {semana['tipo_campanha']}")
        print(f"    Foco: {semana['degrau_foco']}")
        print(f"    Ações principais:")
        for acao in semana['acoes'][:3]:
            print(f"      • {acao['dia']}: {acao['acao']}")

    print(f"\n{'=' * 80}")
    print(f"Consulte {args.output} para calendário completo detalhado.")
    print("=" * 80)


if __name__ == "__main__":
    main()
