# Skill: Ascensão Automática de Clientes

Sistema completo para criar estratégias de ascensão automática que fazem clientes comprarem mais, mais rápido, mais vezes e por valores maiores.

## Como Instalar (passo a passo)

> Esta skill funciona dentro do **Claude Code** (o Claude que roda no computador). Se você ainda não tem o Claude Code instalado, siga primeiro o tutorial oficial: https://docs.claude.com/claude-code

### Opção 1 — O jeito rápido (copiar e colar no Terminal)

Abra o **Terminal** do seu computador (no Mac: aperte `Cmd + Espaço`, digite "Terminal" e aperte Enter) e cole o bloco abaixo. Ele faz tudo sozinho:

```bash
mkdir -p ~/.claude/skills && \
cd ~/.claude/skills && \
git clone https://github.com/hackersdomarketing/skill-ascensao-automatica.git ascensao-automatica
```

Pronto! A skill já está instalada. Abra o Claude Code e peça para ele "ativar a skill de ascensão automática".

### Opção 2 — Sem usar comandos (baixar como ZIP)

1. Abra este endereço no navegador: https://github.com/hackersdomarketing/skill-ascensao-automatica
2. No canto direito, clique no botão verde escrito **Code**
3. Vai abrir um menuzinho — clique em **Download ZIP**
4. Vai baixar um arquivo chamado `skill-ascensao-automatica-main.zip` na sua pasta Downloads
5. **Descompacte** esse arquivo (clique duas vezes nele) — vai virar uma pasta
6. **Renomeie** essa pasta de `skill-ascensao-automatica-main` para `ascensao-automatica` (sem o "-main" no final)
7. Abra o **Finder** e aperte `Cmd + Shift + G`. Vai aparecer uma caixinha
8. Cole este caminho na caixinha e aperte Enter: `~/.claude/skills/`
   - Se a pasta `skills` não existir, crie uma nova pasta com esse nome exato
9. Arraste a pasta `ascensao-automatica` (a que você renomeou) para dentro de `~/.claude/skills/`

Pronto! A skill está instalada.

### Como confirmar que funcionou

Abra o Claude Code e digite: **"ative a skill de ascensão automática"**

Se o Claude responder reconhecendo a skill e começar a seguir o framework dela, está tudo certo. Se ele não reconhecer, feche o Claude Code e abra de novo — às vezes precisa reiniciar para detectar skills novas.

---

## Quando Usar Esta Skill

Use esta skill quando precisar:

1. Criar funis de ascensão automáticos
2. Desenhar jornadas de cliente que maximizam LTV
3. Criar ofertas irresistíveis para cada degrau da escada de valor
4. Implementar sistemas de doutrinação e seeding
5. Desenvolver calendários de campanhas de ascensão
6. Aumentar taxa de renovação e retenção
7. Criar centros de lucro automatizados

**Palavras-chave para ativar:** ascensão, escada de valor, LTV, funil automático, upsell, cross-sell, monetização, customer journey, doutrinação, seeding

## Estrutura da Skill

```
ascensao-automatica/
├── SKILL.md                           # Framework principal completo
├── README.md                          # Este arquivo
├── references/                        # Conhecimento técnico
│   ├── analise_estrategica.json       # Base de dados estruturada (20 PDFs)
│   ├── GUIA_TATICO_IMPLEMENTACAO.md   # Guia prático detalhado
│   └── RESUMO_EXECUTIVO.md            # Referência rápida
├── scripts/                           # Scripts Python automatizados
│   ├── gerar_estrategia_ascensao.py   # Gera estratégia customizada
│   ├── analisar_escada_valor.py       # Analisa gaps e oportunidades
│   ├── calendario_campanhas.py        # Gera calendário 90 dias
│   └── calcular_ltv_projetado.py      # Calcula projeção de LTV
└── assets/                            # Templates e recursos
    ├── templates/emails/              # Templates de emails prontos
    └── checklists/                    # Checklists de implementação
```

## Como Usar

### 1. Leitura Inicial (15-20 min)

Comece pelo resumo executivo para entender visão geral:

```bash
# Abrir no editor
open references/RESUMO_EXECUTIVO.md
```

### 2. Gerar Estratégia Customizada

Use o script para gerar estratégia específica para seu negócio:

```bash
python scripts/gerar_estrategia_ascensao.py \
  --produto-atual "Curso Frontend R$ 97" \
  --produto-alvo "Mentoria R$ 2997" \
  --avatar "Iniciante em marketing digital" \
  --output minha_estrategia.json
```

**Output:** Estratégia completa com funis automáticos, semi-automáticos e campanhas manuais priorizadas.

### 3. Analisar Sua Escada de Valor

Primeiro, crie arquivo JSON com sua escada:

```json
{
  "nome": "Minha Escada de Valor",
  "produtos": [
    {"nome": "Ebook", "preco": 27, "tipo": "one-time", "formato": "PDF"},
    {"nome": "Curso Online", "preco": 197, "tipo": "one-time", "formato": "vídeos gravados"},
    {"nome": "Assinatura Premium", "preco": 497, "tipo": "assinatura mensal", "formato": "ao vivo + comunidade"},
    {"nome": "Mentoria", "preco": 2997, "tipo": "assinatura mensal", "formato": "acompanhamento direto"}
  ]
}
```

Depois analise:

```bash
python scripts/analisar_escada_valor.py \
  --escada minha_escada.json \
  --output analise_gaps.json
```

**Output:** Relatório com problemas, oportunidades, score de saúde da escada e recomendações priorizadas.

### 4. Criar Calendário de Campanhas

Gere calendário de 90 dias com rotação automática:

```bash
python scripts/calendario_campanhas.py \
  --degraus 4 \
  --inicio 2026-02-01 \
  --semanas 12 \
  --output calendario_90_dias.json
```

**Output:** Calendário semanal detalhado com ações específicas, métricas e checklists.

### 5. Calcular LTV Projetado

Veja impacto financeiro de implementar estratégias:

```bash
python scripts/calcular_ltv_projetado.py \
  --aov-atual 297 \
  --taxa-ascensao 12 \
  --num-degraus 4 \
  --clientes-mes 100 \
  --output projecao_ltv.json
```

**Output:** Múltiplos cenários de LTV, ROI de centros de lucro, impacto anual na receita.

### 6. Usar Templates de Emails

Copie e adapte sequência pronta:

```bash
# Abrir template
open assets/templates/emails/email_sequencia_ascensao_7_dias.md
```

Template inclui 7 emails prontos para adaptar ao seu negócio.

### 7. Seguir Checklist de Implementação

Use checklist para garantir nada é esquecido:

```bash
# Abrir checklist
open assets/checklists/checklist_implementacao_completa.md
```

Checklist cobre 8 fases de implementação completa.

## Fluxo de Trabalho Recomendado

**Semana 1:**
1. Ler RESUMO_EXECUTIVO.md (20 min)
2. Gerar estratégia customizada com script
3. Analisar escada de valor atual
4. Identificar prioridade 1 (maior gap de ascensão)

**Semana 2:**
1. Implementar doutrinação no produto atual (seeding, módulo próximos passos)
2. Criar sequência de emails automática (usar template)
3. Configurar hooks de tráfego interno

**Semana 3-4:**
1. Implementar funil automático prioritário
2. Configurar 5 centros de lucro (quick wins)
3. Testar fluxo completo

**Mês 2:**
1. Monitorar métricas e otimizar
2. Adicionar funil semi-automático se conversão < 10%
3. Começar calendário de campanhas

**Mês 3:**
1. Escalar o que funciona
2. Implementar estratégias de renovação
3. Criar eventos mensais de ascensão

## Exemplos de Uso

### Exemplo 1: E-commerce de Infoprodutos

**Input:**
```bash
python scripts/gerar_estrategia_ascensao.py \
  --produto-atual "Ebook R$ 27" \
  --produto-alvo "Curso Completo R$ 497" \
  --avatar "Empreendedor iniciante"
```

**Output gerado:**
- Gap: 18.4x
- Prioridade 1: Webinar automático (conversão esperada: 5-8%)
- Prioridade 2: Call de 2 etapas (conversão: 15-25%)
- Calendário de 12 semanas com ações semanais

### Exemplo 2: SaaS/Plataforma

**Input:**
```bash
python scripts/gerar_estrategia_ascensao.py \
  --produto-atual "Plano Basic R$ 97/mês" \
  --produto-alvo "Plano Pro R$ 497/mês" \
  --avatar "Usuário ativo há 3 meses"
```

**Output gerado:**
- Gap: 5.1x
- Prioridade 1: Funcionalidades bloqueadas à mostra + trial 7 dias (conversão: 10-15%)
- Prioridade 2: Emails de uso contextual (conversão: 5-8%)
- ROI estimado: 450% em 12 meses

### Exemplo 3: Agência/Serviços

**Input:**
```bash
python scripts/gerar_estrategia_ascensao.py \
  --produto-atual "Consultoria R$ 997/mês" \
  --produto-alvo "Done-For-You R$ 5997/mês" \
  --avatar "Cliente há 6+ meses com bons resultados"
```

**Output gerado:**
- Gap: 6.0x
- Prioridade 1: Demonstração de diferença via mini-documentários (conversão: 10-15%)
- Prioridade 2: Oferta de implementação única → DFY (conversão: 20-30%)
- LTV projetado: R$ 12.450 (12.5x inicial)

## Métricas de Sucesso

### KPIs Principais

| Métrica | Baseline | Meta 30 dias | Meta 90 dias |
|---------|----------|--------------|--------------|
| Taxa de ascensão | Atual | +5pp | +10pp |
| LTV médio | Atual | +30% | +100% |
| AOV com centros de lucro | Atual | +20% | +40% |
| Taxa de renovação (assinaturas) | Atual | +10pp | +20pp |

### Benchmarks por Tipo de Funil

**Funis Automáticos:**
- Webinar automático: 3-8%
- VSL + checkout: 2-5%
- Trial + pitch: 10-20%

**Funis Semi-Automáticos:**
- Call de 2 etapas: 15-25%
- Call de boas-vindas: 10-20%

**Campanhas de Recuperação:**
- Email abandono: 5-12%
- Call abandono: 15-25%
- Campanha periódica: 3-8%

## Recursos Adicionais

### Referências Técnicas

- **analise_estrategica.json**: Base de dados estruturada com todos os conceitos, frameworks, funis e centros de lucro extraídos de 20 PDFs especializados
- **GUIA_TATICO_IMPLEMENTACAO.md**: 30KB de guia prático com exemplos, scripts de email/call, checklists e cronogramas
- **RESUMO_EXECUTIVO.md**: Referência rápida para consulta durante trabalho (glossário, diagramas, regras de ouro)

### Scripts Python

Todos os scripts incluem:
- Ajuda completa (`python script.py --help`)
- Validação de inputs
- Output JSON estruturado
- Resumo visual no terminal
- Exemplos de uso

### Templates

- **email_sequencia_ascensao_7_dias.md**: Sequência completa pronta para adaptar, com variações sugeridas por tipo de produto
- **checklist_implementacao_completa.md**: 8 fases detalhadas cobrindo fundação → métricas → renovação

## Troubleshooting

### "Taxa de ascensão < 5%"

**Causas comuns:**
1. Falta de doutrinação no produto atual
2. Gap de preço muito grande
3. Promessa não adaptada ao avatar do degrau

**Soluções:**
1. Implementar seeding e módulo "Próximos Passos"
2. Criar produto intermediário
3. Revisar copy da página de vendas

### "AOV não aumenta com centros de lucro"

**Causas comuns:**
1. Ofertas não relevantes para avatar
2. Timing incorreto dos upsells
3. Checkout com fricção

**Soluções:**
1. Validar fit produto-cliente
2. Testar ordem dos upsells
3. Simplificar checkout (menos campos)

### "Clientes não renovam"

**Causas comuns:**
1. Baixo consumo do produto
2. Falta de conteúdo novo regular
3. Ausência de comunidade/conexão

**Soluções:**
1. Implementar sistema de consumo programado
2. Liberar conteúdo mensalmente (grava 12, libera 1/mês)
3. Criar eventos exclusivos mensais

## Suporte

Para dúvidas ou sugestões de melhoria da skill:

1. Consulte primeiro o SKILL.md completo
2. Revise exemplos em GUIA_TATICO_IMPLEMENTACAO.md
3. Use RESUMO_EXECUTIVO.md para glossário de termos

## Changelog

**v1.0.0** (2026-01-21)
- Release inicial da skill
- 900+ linhas de framework detalhado
- 4 scripts Python automatizados
- Templates de emails e checklists
- Base de conhecimento extraída de 20 PDFs especializados

---

**Criado por:** Skill Forge
**Baseado em:** 20 PDFs sobre estratégias de ascensão (Rafa Marks)
**Conhecimento total extraído:** 353KB de conteúdo → 86KB estruturado + 900 linhas de framework
