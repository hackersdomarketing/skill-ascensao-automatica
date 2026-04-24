#!/usr/bin/env python3
"""
Analisador de Escada de Valor

Analisa escada de valor existente e sugere melhorias baseadas em gaps,
oportunidades de ascensão e otimização de LTV.

Uso:
    python analisar_escada_valor.py \
        --escada escada_valor.json \
        --output analise_gaps.json
"""

import json
import argparse
from typing import List, Dict
import statistics


def calcular_gap_percentual(preco_atual, preco_proximo):
    """Calcula gap percentual entre dois preços"""
    if preco_atual > 0:
        return ((preco_proximo - preco_atual) / preco_atual) * 100
    return 0


def calcular_gap_multiplicador(preco_atual, preco_proximo):
    """Calcula quantas vezes o próximo é maior que o atual"""
    if preco_atual > 0:
        return preco_proximo / preco_atual
    return 0


def identificar_problemas_escada(produtos):
    """Identifica problemas estruturais na escada de valor"""
    problemas = []

    # Verificar se há produtos
    if len(produtos) < 2:
        problemas.append({
            "tipo": "CRÍTICO",
            "problema": "Escada muito curta",
            "descricao": "Menos de 2 produtos. Recomendado: 4-6 produtos para maximizar LTV",
            "impacto": "Perda de 70-80% do potencial de LTV",
            "acao": "Criar produtos intermediários usando método de 5 produtos de 1 método"
        })
        return problemas

    # Verificar gaps de preço
    for i in range(len(produtos) - 1):
        atual = produtos[i]
        proximo = produtos[i + 1]

        gap = calcular_gap_multiplicador(atual['preco'], proximo['preco'])

        if gap > 10:
            problemas.append({
                "tipo": "ALTO",
                "problema": f"Gap muito grande entre {atual['nome']} e {proximo['nome']}",
                "descricao": f"Gap de {gap:.1f}x (R$ {atual['preco']} → R$ {proximo['preco']})",
                "impacto": "Taxa de ascensão < 3% esperada. Clientes não conseguem 'saltar' gap",
                "acao": f"Criar produto intermediário de R$ {int(atual['preco'] * 3)}-{int(proximo['preco'] / 3)}"
            })

        elif gap < 1.5:
            problemas.append({
                "tipo": "MÉDIO",
                "problema": f"Gap muito pequeno entre {atual['nome']} e {proximo['nome']}",
                "descricao": f"Gap de apenas {gap:.1f}x (R$ {atual['preco']} → R$ {proximo['preco']})",
                "impacto": "Valor percebido insuficiente para justificar upgrade",
                "acao": "Aumentar diferenciação de valor ou consolidar produtos similares"
            })

    # Verificar diversidade de formatos
    formatos = [p.get('formato', 'não especificado') for p in produtos]
    formatos_unicos = len(set(formatos))

    if formatos_unicos < len(produtos) * 0.7:
        problemas.append({
            "tipo": "MÉDIO",
            "problema": "Pouca diversidade de formatos",
            "descricao": f"Apenas {formatos_unicos} formatos diferentes em {len(produtos)} produtos",
            "impacto": "Clientes não percebem diferença suficiente entre degraus",
            "acao": "Variar formatos: gravado, ao vivo, implementação, feito-para-você, etc"
        })

    # Verificar se há produto entry-level (< R$ 100)
    tem_entry = any(p['preco'] < 100 for p in produtos)
    if not tem_entry:
        problemas.append({
            "tipo": "ALTO",
            "problema": "Ausência de produto entry-level",
            "descricao": "Nenhum produto abaixo de R$ 100",
            "impacto": "Barreira de entrada alta, perda de novos clientes",
            "acao": "Criar tripwire de R$ 7-97 para capturar leads frios"
        })

    # Verificar se há highticket (> R$ 3000)
    tem_highticket = any(p['preco'] > 3000 for p in produtos)
    if not tem_highticket:
        problemas.append({
            "tipo": "MÉDIO",
            "problema": "Ausência de produto highticket",
            "descricao": "Nenhum produto acima de R$ 3.000",
            "impacto": "LTV limitado a clientes de baixo/médio ticket",
            "acao": "Criar mentoria/implementação de R$ 3k-10k+ para top 10% dos clientes"
        })

    return problemas


def identificar_oportunidades(produtos):
    """Identifica oportunidades de otimização"""
    oportunidades = []

    # Sugerir produto intermediário se gap grande
    for i in range(len(produtos) - 1):
        atual = produtos[i]
        proximo = produtos[i + 1]
        gap = calcular_gap_multiplicador(atual['preco'], proximo['preco'])

        if gap > 5:
            preco_sugerido = int((atual['preco'] + proximo['preco']) / 2)

            oportunidades.append({
                "tipo": "NOVO PRODUTO",
                "titulo": f"Produto intermediário entre {atual['nome']} e {proximo['nome']}",
                "descricao": f"Gap atual de {gap:.1f}x é grande demais",
                "sugestao": {
                    "preco_sugerido": preco_sugerido,
                    "formato_sugerido": "Diferente dos dois adjacentes",
                    "exemplos": [
                        f"Assinatura de R$ {preco_sugerido}/mês com calls mensais",
                        f"Evento trimestral de R$ {preco_sugerido}",
                        f"Implementação guiada de R$ {preco_sugerido}"
                    ]
                },
                "impacto_estimado": f"Aumento de 15-25% na taxa de ascensão entre esses degraus"
            })

    # Sugerir mini ascensões dentro de produtos
    for produto in produtos:
        if produto['preco'] > 97:
            oportunidades.append({
                "tipo": "MINI ASCENSÕES",
                "titulo": f"Adicionar mini ascensões dentro de '{produto['nome']}'",
                "descricao": "Produtos de R$ 7-37 para criar hábito de compra (Buying Frenzy)",
                "sugestao": {
                    "produtos_sugeridos": [
                        f"Templates prontos: R$ 17",
                        f"Checklists avançadas: R$ 7",
                        f"Scripts personalizados: R$ 27",
                        f"Mini-cursos complementares: R$ 37"
                    ]
                },
                "impacto_estimado": "Aumento de 5-10% no AOV + melhora na confiança para ascensões maiores"
            })

    # Sugerir centros de lucro por produto
    for i, produto in enumerate(produtos):
        if i == 0:  # Primeiro produto
            oportunidades.append({
                "tipo": "CENTROS DE LUCRO",
                "titulo": f"Otimizar funil de '{produto['nome']}'",
                "descricao": "Implementar centros de lucro para maximizar AOV",
                "sugestao": {
                    "centros_prioritarios": [
                        "4 Order Bumps (AOV +12%)",
                        "Upsells 1, 2, 3 (AOV +25%)",
                        "Exit popup (Recovery +7%)",
                        "Chat ao vivo no checkout (CVR +5%)"
                    ]
                },
                "impacto_estimado": f"AOV atual R$ {produto['preco']} → R$ {int(produto['preco'] * 1.4)} (+40%)"
            })

    # Sugerir estratégia de renovação para assinaturas
    assinaturas = [p for p in produtos if 'assinatura' in p.get('tipo', '').lower() or 'mensal' in p['nome'].lower()]
    if assinaturas:
        oportunidades.append({
            "tipo": "RENOVAÇÃO",
            "titulo": "Implementar sistema de renovação para assinaturas",
            "descricao": f"{len(assinaturas)} produto(s) de assinatura identificado(s)",
            "sugestao": {
                "taticas": [
                    "Conteúdo programado mensal (grava 12, libera 1/mês)",
                    "Campanha longa de renovação (6 meses antes)",
                    "Gamificação de níveis (Calouro → Veterano → Elite)",
                    "Eventos exclusivos mensais/trimestrais"
                ]
            },
            "impacto_estimado": "Taxa de renovação de 40-50% → 70-80%"
        })

    return oportunidades


def calcular_ltv_potencial(produtos, taxa_ascensao_media=0.10):
    """Calcula LTV potencial baseado na escada"""
    if not produtos:
        return 0

    # Ordenar por preço
    produtos_ordenados = sorted(produtos, key=lambda x: x['preco'])

    ltv_atual = produtos_ordenados[0]['preco']  # Assumir que começam no primeiro
    ltv_potencial = produtos_ordenados[0]['preco']

    for i in range(1, len(produtos_ordenados)):
        # Cada degrau tem chance de ascensão
        ltv_potencial += produtos_ordenados[i]['preco'] * (taxa_ascensao_media ** i)

    return {
        "ltv_minimo": produtos_ordenados[0]['preco'],
        "ltv_potencial_10pct": round(ltv_potencial, 2),
        "ltv_potencial_20pct": round(calcular_ltv_com_taxa(produtos_ordenados, 0.20), 2),
        "ltv_potencial_30pct": round(calcular_ltv_com_taxa(produtos_ordenados, 0.30), 2),
        "multiplicador_10pct": round(ltv_potencial / produtos_ordenados[0]['preco'], 2)
    }


def calcular_ltv_com_taxa(produtos, taxa):
    """Calcula LTV com taxa específica de ascensão"""
    ltv = produtos[0]['preco']
    for i in range(1, len(produtos)):
        ltv += produtos[i]['preco'] * (taxa ** i)
    return ltv


def gerar_recomendacoes_priorizadas(problemas, oportunidades):
    """Gera lista priorizada de ações"""
    recomendacoes = []

    # Problemas críticos primeiro
    criticos = [p for p in problemas if p['tipo'] == 'CRÍTICO']
    for problema in criticos:
        recomendacoes.append({
            "prioridade": "CRÍTICA",
            "acao": problema['acao'],
            "motivo": problema['descricao'],
            "impacto": problema['impacto']
        })

    # Problemas altos
    altos = [p for p in problemas if p['tipo'] == 'ALTO']
    for problema in altos:
        recomendacoes.append({
            "prioridade": "ALTA",
            "acao": problema['acao'],
            "motivo": problema['descricao'],
            "impacto": problema['impacto']
        })

    # Oportunidades de novos produtos
    novos_produtos = [o for o in oportunidades if o['tipo'] == 'NOVO PRODUTO']
    for oportunidade in novos_produtos[:2]:  # Top 2
        recomendacoes.append({
            "prioridade": "ALTA",
            "acao": oportunidade['titulo'],
            "motivo": oportunidade['descricao'],
            "impacto": oportunidade['impacto_estimado']
        })

    # Centros de lucro
    centros = [o for o in oportunidades if o['tipo'] == 'CENTROS DE LUCRO']
    if centros:
        recomendacoes.append({
            "prioridade": "MÉDIA",
            "acao": centros[0]['titulo'],
            "motivo": "Quick win de aumento de AOV",
            "impacto": centros[0]['impacto_estimado']
        })

    return recomendacoes


def analisar_escada_valor(escada):
    """Análise completa da escada de valor"""

    produtos = escada.get('produtos', [])

    # Ordenar produtos por preço
    produtos_ordenados = sorted(produtos, key=lambda x: x['preco'])

    # Análises
    problemas = identificar_problemas_escada(produtos_ordenados)
    oportunidades = identificar_oportunidades(produtos_ordenados)
    ltv = calcular_ltv_potencial(produtos_ordenados)
    recomendacoes = gerar_recomendacoes_priorizadas(problemas, oportunidades)

    # Estatísticas
    precos = [p['preco'] for p in produtos_ordenados]
    stats = {
        "num_produtos": len(produtos),
        "preco_minimo": min(precos) if precos else 0,
        "preco_maximo": max(precos) if precos else 0,
        "preco_mediano": statistics.median(precos) if precos else 0,
        "gap_medio": statistics.mean([
            calcular_gap_multiplicador(produtos_ordenados[i]['preco'], produtos_ordenados[i+1]['preco'])
            for i in range(len(produtos_ordenados) - 1)
        ]) if len(produtos_ordenados) > 1 else 0
    }

    analise = {
        "metadata": {
            "escada_analisada": escada.get('nome', 'Sem nome'),
            "num_produtos": len(produtos)
        },
        "estatisticas": stats,
        "produtos_ordenados": [
            {
                "posicao": i + 1,
                "nome": p['nome'],
                "preco": p['preco'],
                "tipo": p.get('tipo', 'não especificado'),
                "formato": p.get('formato', 'não especificado'),
                "gap_para_proximo": (
                    f"{calcular_gap_multiplicador(p['preco'], produtos_ordenados[i+1]['preco']):.1f}x"
                    if i < len(produtos_ordenados) - 1 else "N/A (último degrau)"
                )
            }
            for i, p in enumerate(produtos_ordenados)
        ],
        "problemas_identificados": problemas,
        "oportunidades_identificadas": oportunidades,
        "ltv_potencial": ltv,
        "recomendacoes_priorizadas": recomendacoes,
        "score_saude_escada": calcular_score_saude(produtos_ordenados, problemas)
    }

    return analise


def calcular_score_saude(produtos, problemas):
    """Calcula score de saúde da escada (0-100)"""
    score = 100

    # Penalidades por problemas
    for problema in problemas:
        if problema['tipo'] == 'CRÍTICO':
            score -= 30
        elif problema['tipo'] == 'ALTO':
            score -= 15
        elif problema['tipo'] == 'MÉDIO':
            score -= 5

    # Bônus por boas práticas
    if len(produtos) >= 4:
        score += 10  # Escada com tamanho adequado

    if any(p['preco'] < 100 for p in produtos):
        score += 5  # Tem entry-level

    if any(p['preco'] > 3000 for p in produtos):
        score += 5  # Tem highticket

    # Gaps equilibrados
    gaps_ruins = sum(1 for p in problemas if 'Gap' in p.get('problema', ''))
    if gaps_ruins == 0:
        score += 10

    return max(0, min(100, score))


def main():
    parser = argparse.ArgumentParser(
        description="Analisador de Escada de Valor"
    )
    parser.add_argument(
        "--escada",
        required=True,
        help="Arquivo JSON com escada de valor"
    )
    parser.add_argument(
        "--output",
        default="analise_gaps.json",
        help="Arquivo de saída (default: analise_gaps.json)"
    )

    args = parser.parse_args()

    print("📊 Analisando escada de valor...\n")

    # Carregar escada
    with open(args.escada, 'r', encoding='utf-8') as f:
        escada = json.load(f)

    # Analisar
    analise = analisar_escada_valor(escada)

    # Salvar
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(analise, f, ensure_ascii=False, indent=2)

    print(f"✅ Análise concluída!")
    print(f"📄 Salva em: {args.output}\n")

    # Resumo visual
    print("=" * 80)
    print("RESUMO DA ANÁLISE")
    print("=" * 80)

    score = analise['score_saude_escada']
    print(f"\n🏥 SCORE DE SAÚDE DA ESCADA: {score}/100")

    if score >= 80:
        print("   Status: ✅ EXCELENTE - Escada bem estruturada")
    elif score >= 60:
        print("   Status: ⚠️  BOA - Algumas melhorias recomendadas")
    elif score >= 40:
        print("   Status: ⚠️  REGULAR - Várias otimizações necessárias")
    else:
        print("   Status: ❌ CRÍTICA - Reestruturação urgente necessária")

    print(f"\n📈 ESTATÍSTICAS:")
    stats = analise['estatisticas']
    print(f"   Produtos: {stats['num_produtos']}")
    print(f"   Preço mínimo: R$ {stats['preco_minimo']}")
    print(f"   Preço máximo: R$ {stats['preco_maximo']}")
    print(f"   Gap médio: {stats['gap_medio']:.1f}x")

    print(f"\n💰 LTV POTENCIAL:")
    ltv = analise['ltv_potencial']
    print(f"   Com 10% ascensão: R$ {ltv['ltv_potencial_10pct']} ({ltv['multiplicador_10pct']}x inicial)")
    print(f"   Com 20% ascensão: R$ {ltv['ltv_potencial_20pct']}")
    print(f"   Com 30% ascensão: R$ {ltv['ltv_potencial_30pct']}")

    print(f"\n🚨 PROBLEMAS IDENTIFICADOS: {len(analise['problemas_identificados'])}")
    for problema in analise['problemas_identificados'][:3]:
        print(f"   [{problema['tipo']}] {problema['problema']}")

    print(f"\n💡 OPORTUNIDADES IDENTIFICADAS: {len(analise['oportunidades_identificadas'])}")
    for oportunidade in analise['oportunidades_identificadas'][:3]:
        print(f"   [{oportunidade['tipo']}] {oportunidade['titulo']}")

    print(f"\n🎯 TOP 5 RECOMENDAÇÕES:")
    for i, rec in enumerate(analise['recomendacoes_priorizadas'][:5], 1):
        print(f"   {i}. [{rec['prioridade']}] {rec['acao']}")

    print(f"\n{'=' * 80}")
    print(f"Consulte {args.output} para análise detalhada completa.")
    print("=" * 80)


if __name__ == "__main__":
    main()
