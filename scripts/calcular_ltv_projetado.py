#!/usr/bin/env python3
"""
Calculador de LTV Projetado com Estratégias de Ascensão

Calcula projeção de Lifetime Value (LTV) considerando múltiplos cenários
de taxa de ascensão e implementação de centros de lucro.

Uso:
    python calcular_ltv_projetado.py \
        --aov-atual 297 \
        --taxa-ascensao 12 \
        --num-degraus 4 \
        --output projecao_ltv.json
"""

import json
import argparse
from typing import List, Dict


CENTROS_LUCRO_INCREMENTOS = {
    "CENTRO 1: Captura com No-Optin": 5,
    "CENTRO 2: Bump de Pré-checkout": 8,
    "CENTRO 3: Remarketing Funcional": 15,  # Recovery
    "CENTRO 4: 4 Order Bumps": 12,
    "CENTRO 5: Upsell de Exit Popup": 7,  # Recovery
    "CENTRO 6-8: Upsells 1, 2, 3": 25,
    "CENTRO 9: Ofertas de Downsell": 10,  # Recovery
    "CENTRO 10: Pág. Obrigado com Soft-Sell": 8,
    "CENTRO 11: Campanhas Abandono Upsell": 6,  # Recovery
    "CENTRO 12: Chat Ao Vivo no Checkout": 5,  # CVR
    "CENTRO 13: Abandono Carrinho por Call": 12,  # Recovery
    "CENTRO 14: Abandono por SMS/Email": 8,  # Recovery
    "CENTRO 15: Call Boas Vindas com Monetização": 15,
    "CENTRO 16: Promoção Boas Vindas Email": 10,
    "CENTRO 17: Promoção Boas Vindas Parte 2": 8,
    "CENTRO 18: Oferta Highticket na Traseira": 30,
    "CENTRO 19: Remarketing de Reconhecimento": 20,  # LTV
    "CENTRO 20: Ofertas Backend Para Leads": 5  # CVR
}

TAXAS_CONVERSAO_BENCHMARKS = {
    "funil_automatico": {
        "webinar": 0.05,  # 5%
        "vsl": 0.03,  # 3%
        "trial": 0.15,  # 15%
        "modulo_proximos_passos": 0.10  # 10%
    },
    "funil_semi_automatico": {
        "call_2_etapas": 0.20,  # 20%
        "call_boas_vindas": 0.15,  # 15%
        "call_entrega_bonus": 0.25  # 25%
    },
    "campanha_manual": {
        "calendario_ascensao": 0.05,  # 5%
        "evento_mensal": 0.08,  # 8%
        "recuperacao_segmentada": 0.12  # 12%
    }
}


def calcular_aov_com_centros(aov_base, centros_implementados):
    """Calcula AOV com implementação de centros de lucro"""

    incremento_total = 0

    for centro, incremento in CENTROS_LUCRO_INCREMENTOS.items():
        if centro in centros_implementados:
            incremento_total += incremento

    # Incremento percentual composto
    multiplicador = 1 + (incremento_total / 100)
    novo_aov = aov_base * multiplicador

    return {
        "aov_original": aov_base,
        "aov_projetado": round(novo_aov, 2),
        "incremento_percentual": round(incremento_total, 1),
        "incremento_absoluto": round(novo_aov - aov_base, 2),
        "multiplicador": round(multiplicador, 2)
    }


def calcular_ltv_simples(aov_primeiro_produto, num_degraus, taxa_ascensao):
    """Calcula LTV básico assumindo taxa constante de ascensão"""

    ltv = aov_primeiro_produto

    # Assumir que cada degrau é 3x o anterior (padrão comum)
    preco_atual = aov_primeiro_produto

    for i in range(1, num_degraus):
        preco_atual *= 3  # Próximo degrau 3x mais caro
        probabilidade_ascender = (taxa_ascensao / 100) ** i
        ltv += preco_atual * probabilidade_ascender

    return round(ltv, 2)


def calcular_ltv_detalhado(escada_valor, taxa_ascensao, taxa_renovacao=0.60):
    """
    Calcula LTV detalhado com escada de valor específica

    escada_valor: lista de dicts com {nome, preco, tipo}
    taxa_ascensao: % de clientes que ascendem por degrau
    taxa_renovacao: % de renovação para produtos de assinatura
    """

    ltv_total = 0
    probabilidade_acumulada = 1.0

    for i, produto in enumerate(escada_valor):
        preco = produto['preco']
        tipo = produto.get('tipo', 'one-time')

        # LTV deste degrau = preço * probabilidade de chegar aqui
        ltv_degrau = preco * probabilidade_acumulada

        # Se for assinatura, multiplicar por LTV de retenção
        if 'assinatura' in tipo.lower() or 'mensal' in tipo.lower():
            # LTV de assinatura = preço_mensal / churn_rate
            # Com 60% renovação, churn = 40%, LTV = preço / 0.4 = 2.5x
            churn_rate = 1 - taxa_renovacao
            multiplicador_assinatura = 1 / churn_rate if churn_rate > 0 else 12  # Max 12 meses
            ltv_degrau *= min(multiplicador_assinatura, 12)  # Cap em 12 meses

        ltv_total += ltv_degrau

        # Atualizar probabilidade para próximo degrau
        if i < len(escada_valor) - 1:
            probabilidade_acumulada *= (taxa_ascensao / 100)

    return {
        "ltv_total": round(ltv_total, 2),
        "multiplicador_primeiro_produto": round(ltv_total / escada_valor[0]['preco'], 2) if escada_valor else 0,
        "detalhes_por_degrau": [
            {
                "degrau": i + 1,
                "nome": p['nome'],
                "preco": p['preco'],
                "tipo": p.get('tipo', 'one-time'),
                "probabilidade_chegar": round((taxa_ascensao / 100) ** i, 4)
            }
            for i, p in enumerate(escada_valor)
        ]
    }


def gerar_cenarios_ltv(aov_base, num_degraus):
    """Gera múltiplos cenários de LTV com diferentes taxas de ascensão"""

    cenarios = {}

    for taxa in [5, 10, 15, 20, 25, 30]:
        ltv = calcular_ltv_simples(aov_base, num_degraus, taxa)
        multiplicador = ltv / aov_base

        cenarios[f"taxa_{taxa}pct"] = {
            "taxa_ascensao": f"{taxa}%",
            "ltv_projetado": ltv,
            "multiplicador": round(multiplicador, 2),
            "viabilidade": avaliar_viabilidade(taxa)
        }

    return cenarios


def avaliar_viabilidade(taxa_ascensao):
    """Avalia quão viável é atingir determinada taxa"""

    if taxa_ascensao <= 10:
        return "REALISTA - Alcançável com funis básicos automáticos"
    elif taxa_ascensao <= 20:
        return "OTIMISTA - Requer funis otimizados + doutrinação forte"
    elif taxa_ascensao <= 30:
        return "AGRESSIVO - Necessita sistema completo + time dedicado"
    else:
        return "EXCEPCIONAL - Raro, requer excelência operacional"


def calcular_roi_implementacao_centros(aov_base, num_clientes_mes, centros_prioritarios):
    """Calcula ROI de implementar centros de lucro"""

    # Assumir 30 dias para implementar
    custo_implementacao = 5000  # Estimativa: dev + copy + design

    # Incremento de AOV
    resultado_aov = calcular_aov_com_centros(aov_base, centros_prioritarios)
    incremento_por_cliente = resultado_aov['incremento_absoluto']

    # Receita adicional mensal
    receita_adicional_mes = incremento_por_cliente * num_clientes_mes

    # Payback
    meses_payback = custo_implementacao / receita_adicional_mes if receita_adicional_mes > 0 else 999

    # ROI 12 meses
    receita_12_meses = receita_adicional_mes * 12
    roi_12_meses = ((receita_12_meses - custo_implementacao) / custo_implementacao) * 100

    return {
        "custo_implementacao_estimado": custo_implementacao,
        "incremento_aov": resultado_aov['incremento_absoluto'],
        "receita_adicional_mensal": round(receita_adicional_mes, 2),
        "receita_adicional_anual": round(receita_12_meses, 2),
        "meses_para_payback": round(meses_payback, 1),
        "roi_12_meses_percentual": round(roi_12_meses, 1)
    }


def gerar_recomendacoes(ltv_atual, ltv_potencial, taxa_ascensao_atual):
    """Gera recomendações baseadas em gaps de LTV"""

    recomendacoes = []

    gap_ltv = ltv_potencial - ltv_atual
    gap_percentual = (gap_ltv / ltv_atual) * 100

    if gap_percentual > 100:
        recomendacoes.append({
            "prioridade": "CRÍTICA",
            "acao": "Implementar funis automáticos de ascensão IMEDIATAMENTE",
            "motivo": f"Você está deixando {gap_percentual:.0f}% de LTV na mesa",
            "impacto": f"Potencial adicional de R$ {gap_ltv:.2f} por cliente"
        })

    if taxa_ascensao_atual < 10:
        recomendacoes.append({
            "prioridade": "ALTA",
            "acao": "Adicionar doutrinação e seeding em produtos atuais",
            "motivo": "Taxa de ascensão abaixo do benchmark (10%)",
            "impacto": "Aumento estimado de 5-10pp na taxa de ascensão"
        })

    if ltv_atual < 1000:
        recomendacoes.append({
            "prioridade": "ALTA",
            "acao": "Criar produto highticket (R$ 3k-10k+)",
            "motivo": "LTV atual muito baixo",
            "impacto": "Mesmo com 5% de ascensão, LTV sobe 50-100%"
        })

    recomendacoes.append({
        "prioridade": "MÉDIA",
        "acao": "Implementar top 5 centros de lucro",
        "motivo": "Quick wins de aumento de AOV",
        "impacto": "AOV +30-50% em 30 dias"
    })

    return recomendacoes


def main():
    parser = argparse.ArgumentParser(
        description="Calculador de LTV Projetado com Estratégias de Ascensão"
    )
    parser.add_argument(
        "--aov-atual",
        type=float,
        required=True,
        help="AOV atual do primeiro produto (ex: 297)"
    )
    parser.add_argument(
        "--taxa-ascensao",
        type=float,
        default=10,
        help="Taxa de ascensão atual em %% (default: 10)"
    )
    parser.add_argument(
        "--num-degraus",
        type=int,
        default=4,
        help="Número de degraus na escada (default: 4)"
    )
    parser.add_argument(
        "--clientes-mes",
        type=int,
        default=100,
        help="Número de novos clientes por mês (default: 100)"
    )
    parser.add_argument(
        "--output",
        default="projecao_ltv.json",
        help="Arquivo de saída (default: projecao_ltv.json)"
    )

    args = parser.parse_args()

    print("💰 Calculando projeção de LTV...\n")

    # Cálculos
    ltv_atual = calcular_ltv_simples(args.aov_atual, args.num_degraus, args.taxa_ascensao)

    cenarios = gerar_cenarios_ltv(args.aov_atual, args.num_degraus)

    # Centros de lucro prioritários (top 5)
    centros_prioritarios = [
        "CENTRO 4: 4 Order Bumps",
        "CENTRO 6-8: Upsells 1, 2, 3",
        "CENTRO 12: Chat Ao Vivo no Checkout",
        "CENTRO 13: Abandono Carrinho por Call",
        "CENTRO 15: Call Boas Vindas com Monetização"
    ]

    aov_com_centros = calcular_aov_com_centros(args.aov_atual, centros_prioritarios)

    roi_centros = calcular_roi_implementacao_centros(
        args.aov_atual,
        args.clientes_mes,
        centros_prioritarios
    )

    # LTV potencial (melhor cenário realista: 20%)
    ltv_potencial = cenarios["taxa_20pct"]["ltv_projetado"]

    recomendacoes = gerar_recomendacoes(ltv_atual, ltv_potencial, args.taxa_ascensao)

    # Estrutura de resultado
    resultado = {
        "metadata": {
            "aov_base": args.aov_atual,
            "taxa_ascensao_atual": args.taxa_ascensao,
            "num_degraus": args.num_degraus,
            "clientes_por_mes": args.clientes_mes
        },
        "ltv_atual": {
            "valor": ltv_atual,
            "multiplicador": round(ltv_atual / args.aov_atual, 2)
        },
        "cenarios_ltv": cenarios,
        "otimizacao_aov": aov_com_centros,
        "roi_implementacao_centros": roi_centros,
        "recomendacoes_priorizadas": recomendacoes,
        "impacto_receita_anual": {
            "receita_atual_ano": round(ltv_atual * args.clientes_mes * 12, 2),
            "receita_potencial_ano_20pct": round(ltv_potencial * args.clientes_mes * 12, 2),
            "receita_potencial_ano_com_centros": round(
                ltv_potencial * aov_com_centros['multiplicador'] * args.clientes_mes * 12,
                2
            ),
            "gap_receita_anual": round(
                (ltv_potencial - ltv_atual) * args.clientes_mes * 12,
                2
            )
        }
    }

    # Salvar
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)

    print(f"✅ Projeção calculada com sucesso!")
    print(f"📄 Salva em: {args.output}\n")

    # Resumo visual
    print("=" * 80)
    print("PROJEÇÃO DE LIFETIME VALUE (LTV)")
    print("=" * 80)

    print(f"\n📊 SITUAÇÃO ATUAL:")
    print(f"   AOV: R$ {args.aov_atual}")
    print(f"   Taxa de ascensão: {args.taxa_ascensao}%")
    print(f"   LTV: R$ {ltv_atual} ({ltv_atual / args.aov_atual:.1f}x o primeiro produto)")

    print(f"\n📈 CENÁRIOS DE LTV:")
    for key, cenario in cenarios.items():
        taxa = cenario['taxa_ascensao']
        ltv = cenario['ltv_projetado']
        mult = cenario['multiplicador']
        viab = cenario['viabilidade']
        print(f"   {taxa:>4}: R$ {ltv:>8.2f} ({mult}x) - {viab}")

    print(f"\n💎 OTIMIZAÇÃO DE AOV (Top 5 Centros de Lucro):")
    print(f"   AOV atual: R$ {aov_com_centros['aov_original']}")
    print(f"   AOV projetado: R$ {aov_com_centros['aov_projetado']}")
    print(f"   Incremento: +{aov_com_centros['incremento_percentual']}% (R$ {aov_com_centros['incremento_absoluto']})")

    print(f"\n💰 ROI DE IMPLEMENTAÇÃO:")
    print(f"   Investimento: R$ {roi_centros['custo_implementacao_estimado']:,.2f}")
    print(f"   Receita adicional/mês: R$ {roi_centros['receita_adicional_mensal']:,.2f}")
    print(f"   Payback: {roi_centros['meses_para_payback']:.1f} meses")
    print(f"   ROI 12 meses: {roi_centros['roi_12_meses_percentual']:.0f}%")

    print(f"\n🎯 IMPACTO ANUAL (com {args.clientes_mes} clientes/mês):")
    impacto = resultado['impacto_receita_anual']
    print(f"   Receita atual: R$ {impacto['receita_atual_ano']:,.2f}/ano")
    print(f"   Potencial (20% ascensão): R$ {impacto['receita_potencial_ano_20pct']:,.2f}/ano")
    print(f"   Potencial (20% + centros): R$ {impacto['receita_potencial_ano_com_centros']:,.2f}/ano")
    print(f"   GAP: R$ {impacto['gap_receita_anual']:,.2f}/ano sendo deixado na mesa")

    print(f"\n🚀 TOP RECOMENDAÇÕES:")
    for i, rec in enumerate(recomendacoes[:3], 1):
        print(f"   {i}. [{rec['prioridade']}] {rec['acao']}")
        print(f"      Impacto: {rec['impacto']}")

    print(f"\n{'=' * 80}")
    print(f"Consulte {args.output} para análise completa detalhada.")
    print("=" * 80)


if __name__ == "__main__":
    main()
