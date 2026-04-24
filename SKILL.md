---
name: ascensao-automatica
description: "Sistema completo para criar estratégias de ascensão automática de clientes, fazendo-os comprar mais, mais rápido, mais vezes e por valores maiores. Use quando: (1) Precisar criar funis de ascensão automáticos; (2) Desenhar jornadas de cliente que maximizam LTV; (3) Criar ofertas irresistíveis para cada degrau da escada de valor; (4) Implementar sistemas de doutrinação e seeding; (5) Desenvolver calendários de campanhas de ascensão; (6) Aumentar taxa de renovação e retenção; (7) Criar centros de lucro automatizados. Palavras-chave: ascensão, escada de valor, LTV, funil automático, upsell, cross-sell, monetização, customer journey, doutrinação, seeding."
---

# Ascensão Automática de Clientes

Sistema estratégico completo para desenvolver jornadas de ascensão que fazem clientes comprarem automaticamente mais produtos, mais rápido, mais vezes e por valores maiores, com máxima automação e custo zero.

## Visão Geral

Esta skill combina frameworks comprovados de ascensão (Efeito Alquimia, Método Rafa) com inteligência estratégica para criar sistemas automáticos e semi-automáticos de monetização progressiva. Foco principal: **automação máxima** e **custo zero**.

**Resultado esperado:** Transformar clientes parados em toneladas de dinheiro através de ascensão sistemática e automatizada.

## Referência Rápida de Ativação

| Cenário | Tipo de Estratégia | Prioridade |
|---------|-------------------|------------|
| Cliente acabou de comprar frontend | Ascensão Imediata Automática | ALTA |
| Preciso criar escada de valor | Framework Efeito Alquimia | ALTA |
| Baixa taxa de ascensão | Doutrinação + Seeding | ALTA |
| Clientes não renovam | Estratégias de Renovação | ALTA |
| Preciso recuperar quem não ascendeu | Calendário de Campanhas | MÉDIA |
| Criar ofertas irresistíveis | 7 Tipos de Oferta | ALTA |
| Maximizar AOV do funil | 20 Centros de Lucro | MÉDIA |
| Criar funis backend | Funis Backend Automáticos | ALTA |

## REGRA DE OURO

**Sempre Ascende Primeiro AUTOMÁTICO, Depois SEMI-AUTOMÁTICO, Depois MANUAL**

Sequência de prioridade:
1. ✅ AUTOMÁTICO (máxima prioridade)
2. 🔄 SEMI-AUTOMÁTICO (segunda prioridade)
3. 👤 MANUAL (última prioridade, apenas recuperação)

## Framework Principal: Efeito Alquimia Automatizado

### PASSO 1: Mapear Evolução do Avatar na Escada

**CRÍTICO:** Cada cliente é um AVATAR DIFERENTE em cada degrau da escada.

**Ação:**
```
Para cada degrau, definir:
├─ Quem ele é agora? (estado atual)
├─ O que ele deseja? (baseado no estágio)
├─ O que ele teme? (objeções do estágio)
├─ O que o move? (gatilhos emocionais)
└─ Qual próximo problema natural? (criado ao resolver o atual)
```

**Implementação:**
- Criar mapa mental da evolução do avatar
- Documentar desejos específicos por degrau
- Identificar linguagem e vocabulário de cada estágio

Consultar: `references/analise_estrategica.json` → "psicologia.evolucao_avatar_na_escada"

---

### PASSO 2: Construir Ofertas com Formatos Diferentes

**Objetivo:** Mesmo método, formatos diferentes para aumentar percepção de valor.

**Método Rápido - Criar 5 Produtos de 1 Método:**

1. **FERRAMENTAS DO MÉTODO** (Templates, Scripts, Checklists)
   - Preço: R$ 7 - R$ 97
   - Formato: Download digital, acesso imediato

2. **ASSINATURA CLUBE NÍVEL 1** (Práticas melhoradas)
   - Preço: R$ 47 - R$ 197/mês
   - Formato: Área de membros com atualizações mensais

3. **ASSINATURA NÍVEL 2** (Implementação guiada)
   - Preço: R$ 197 - R$ 497/mês
   - Formato: Treinamento ao vivo + comunidade

4. **EVENTO DO MÉTODO** (Experiência imersiva)
   - Preço: R$ 297 - R$ 1.997
   - Formato: Evento online/presencial trimestral

5. **SERVIÇO NÍVEL 3** (Mentoria/Highticket)
   - Preço: R$ 997 - R$ 10.000+/mês
   - Formato: Acompanhamento direto, calls, suporte

**Os 7 Tipos de Oferta para Ascensão:**

Consultar `references/RESUMO_EXECUTIVO.md` seção "7 Tipos de Oferta"

**Gatilhos Psicológicos de Valor:**
- ✅ Menos trabalho/esforço/tempo
- ✅ Mais fácil/pronto/automático
- ✅ Mais perto do especialista
- ✅ Mais suporte/ajuda/proximidade
- ✅ Novas experiências/status
- ✅ Mais legal/divertido/interessante

---

### PASSO 3: Trocar Formato do Funil

**Regra:** Cada ascensão deve usar um formato de funil que o cliente AINDA NÃO VIVENCIOU.

**Formatos disponíveis:**
- Webinar automático
- VSL (Video Sales Letter)
- Funil de cupom de desconto
- Workshop gratuito + pitch
- Call de 2 etapas
- Trial + doutrinação + VSL
- Evento ao vivo
- Desafio/Maratona
- Mini-curso gratuito
- Quiz/Diagnóstico

**Implementação:**
```python
# Rastrear formatos já usados por cliente
formatos_vivenciados = ["webinar", "vsl"]
proximo_formato = escolher_nao_vivenciado(formatos_vivenciados)
```

---

### PASSO 4: Adaptar Promessa e Abordagem

**Componentes da Promessa por Degrau:**

| Degrau | Foco da Promessa | Ângulo de Curiosidade |
|--------|------------------|----------------------|
| Frontend (R$ 7-97) | Resultado rápido específico | "Como conseguir X sem Y" |
| Backend (R$ 297-997) | Transformação completa | "O sistema que [autoridade] usa" |
| Highticket (R$ 3k-10k+) | Implementação garantida | "Faça comigo, não sozinho" |

**CRÍTICO:** Adaptar headline para:
1. **DESEJO** dele (baseado em quem ele é AGORA)
2. **CURIOSIDADE** dele (baseado em onde ele está AGORA)

**Fórmula de Headline Efetiva:**
```
[RESULTADO DOS SONHOS] + [DE FORMA CONTRADITÓRIA MAS CRÍVEL] + [SEM OBJEÇÃO PRINCIPAL]

Exemplo Frontend: "Como criar vídeos virais em 10 minutos sem aparecer nem saber editar"
Exemplo Backend: "O sistema completo de tráfego que fez meus alunos faturarem 6 dígitos em 90 dias"
Exemplo Highticket: "Implemente comigo: Transforme seu negócio em máquina de vendas em 12 semanas"
```

---

### PASSO 5: Doutrinar para Desejar o Próximo Funil

**Fluxo de Doutrinação Completo:**

**0. DEFINIR A ÚNICA CRENÇA**
```
Pergunta crítica: "Qual é a ÚNICA COISA que se o cliente que comprou este produto CRER,
ele não tem outra opção a não ser comprar de mim?"

Exemplo: "Se ele crer que tráfego sem conversão é dinheiro jogado fora,
ele PRECISA comprar meu produto de funis/copy"
```

**1. CURIOSIDADE CLICKBAIT** (Fisgar atenção)
- Quebra de padrão com manchetes clickbait
- Formato/posicionamento diferente
- Mostrar resultado dos sonhos conquistado de forma contraditória
- CTA: "Quer entender como?"

**2. CONFIANÇA** (Estabelecer autoridade)
- Demonstração de autoridade (resultados, credenciais, provas)
- Vínculo emocional por valores compartilhados

**3. ESPERANÇA** (Mostrar possibilidade)
- Disseminar o próximo problema ao longo do produto
- Promessas claras e tangíveis
- Histórias de alunos diversos (até casos difíceis)
- Livrar de objeções e medos

**4. DESEJO** (Intensificar vontade)
- Motivos pelos quais DEVERIA ter
- Diferenças e vantagens exclusivas
- Benefícios extras gerados
- Aumento de status percebido

**5. HOOKS** (Mover para ação)
- Curiosidade sobre próximo passo
- Resultado dos sonhos deste avatar
- Ângulo narrativo contraditório mas crível
- CTA para ação específica

**Implementação Tática:**

**Seeding nas Aulas:**
- Contar histórias SEMPRE de alunos do próximo nível
- Mostrar prints de resultados de quem está no próximo produto
- Vídeos de depoimento citando benefícios exclusivos do próximo nível
- Mencionar técnicas com nomes que eles não conhecem ainda

**Criar Problema Novo:**
```
REGRA: Resolver o problema atual + Criar consciência do próximo problema

Exemplo:
- Produto atual ensinou: "Como criar vídeo viral"
- Problema criado: "E agora, o que fazer com tanta visualização? Como capturar leads? Como vender?"
- Próximo produto resolve: "Sistema de captura e conversão de tráfego viral"
```

**5 Sub-Passos da Doutrinação:**
1. Gerar consciência do próximo produto (mostrar que existe)
2. Aumentar desejo (seeding, histórias, demonstrações)
3. Aumentar tempo de consumo (sequências, formatos de alto valor)
4. Aumentar percepção de um sub-problema
5. Convidar para funil gratuito que resolve EXATAMENTE esse problema

---

### PASSO 6: Doutrinar PREVIAMENTE para Desejar

**Técnicas de Doutrinação Prévia:**

**A) Produtos Bloqueados à Mostra**
- Área de membros mostra produtos superiores bloqueados
- Cada ícone tem link para funil de vendas
- Gera consciência + curiosidade

**B) Ver Sem Ter Acesso**
```
Estrutura de Demonstração de Diferença:

Assinatura Mensal (R$ 97):
└─ Assiste gravado, sem interação

Assinatura Backend (R$ 497):
├─ Assiste ao vivo no YouTube
└─ Pode perguntar no chat

Assinatura Highend (R$ 3k+):
├─ Assiste no Zoom ao vivo
└─ Pode abrir microfone e ser ajudado diretamente

PSICOLOGIA: Quem está no mensal VÊ as pessoas do backend interagindo,
e se pergunta "Por que eu nunca estou nessas aulas ao vivo?"
```

**C) Emails de Notificação Multi-Nível**
- Um único email informa eventos de TODOS os degraus
- Quem é do frontend vê acontecendo eventos do backend/highticket
- Cria FOMO e desejo de participar

**D) Apresentar a Plataforma Completa Logo no Início**
- Na 1ª ou 2ª aula do frontend, mostrar TODA a escada
- Deixar consciente de para onde ele pode ir
- Gerar desejo de evolução desde o início

---

### PASSO 7: Hooks de Tráfego Interno

**5 Hooks Principais para Fazer Leads Entrarem em Funis:**

**1. IMÃ GRÁTIS + AULA DE USO**
```
Fluxo:
└─ Oferecer lead magnet gratuito via email
└─ Página pós-cadastro vira oferta de produto baixo ticket
└─ Upsell automático
```

**2. EMAILS DE CONSUMO + RELACIONAMENTO**

Sequência de 10 tipos de email:
1. Conteúdo puro no próprio email
2. Conteúdo de podcast/vídeo
3. Gravação de mentoria ao vivo
4. Estudo de caso de aluno
5. Workshop/aula secreta bônus
6. Antecipação de evento
7. Convite para call de bônus
8. Oferta de análise gratuita
9. História de sucesso
10. Venda direta do próximo passo (sequência 7 dias)

**3. BÔNUS 2 DIAS APÓS COMPRA**
```
Timing: 2 dias depois da compra
Mecânica: "Você ganhou um bônus! Chame no direct/WhatsApp para receber"
Objetivo: Iniciar conversa + oportunidade de venda consultiva
```

**4. EMAIL "VOCÊ JÁ CONVERSOU COMIGO?"**
```
Timing: 1 dia depois de não comprar no webinar
Mecânica: Puxar para chamar no direct com palavra-chave específica
Objetivo: Time comercial converte por conversa direta
```

**5. EMAIL "PODE ME FAZER UM FAVOR?"**
```
Timing: Após comprar trip ou frontend
Pergunta: "Você já entrou no [PRÓXIMO PROGRAMA]?"
Psicologia: Muitos nem sabiam que existia
Implementação:
├─ Nome do produto linkado para checkout personalizado
├─ Foto linkada para checkout
└─ Checkout tem: depoimentos, mockup, promessa, bullets, chat de dúvidas
```

---

### PASSO 8: Recuperar Quem Não Ascendeu

**Calendário de Campanhas de Ascensão**

**A) Campanhas Periódicas**
- Mensais: Pequenas ofertas e lembretes
- Bi-mensais: Ofertas médias com urgência
- Trimestrais: Grandes lançamentos e eventos

**B) Ascensões Semanais por Degrau**
```
Planejamento semanal:

Semana 1: Campanha para quem está no Frontend
Semana 2: Campanha para quem está no Backend
Semana 3: Campanha para quem está no Highticket
Semana 4: Campanha de recuperação geral
```

**C) Segmentação Comportamental**
```
Segmentos prioritários:
├─ Comprou mas não consumiu (baixo engajamento)
├─ Consumiu muito mas não ascendeu (alta oportunidade)
├─ Quase comprou próximo nível (carrinho abandonado)
└─ Está há X meses sem ascender (campanha recuperação)
```

Consultar: `references/GUIA_TATICO_IMPLEMENTACAO.md` → "Calendário de 90 Dias"

---

## Tipos de Ascensão e Quando Usar

### 1. Empilhamento de Funil
**O que é:** Empilhar funis em sequência na jornada do cliente

**Quando usar:**
- Cliente acabou de entrar no ecossistema
- Precisa criar jornada linear de valor

**Implementação:**
```
Frontend (Trip R$ 27)
└─ Upsell 1: Assinatura Mensal (R$ 97)
   └─ Upsell 2: Ferramentas (R$ 197)
      └─ Upsell 3: Backend (R$ 497)
```

---

### 2. Ascensão Imediata

**A) Ascensão Interna (Pela área de membros)**
```
Mecanismos automáticos:
├─ Banners clicáveis em aulas
├─ Módulo "Próximos Passos"
├─ Pop-ups de oferta contextual
├─ Produtos bloqueados à mostra (clique = página de vendas)
└─ CTAs em descrições de aulas
```

**B) Ascensão Externa (Pelas mensagens)**
```
Canais:
├─ Email automático pós-compra (sequência de boas-vindas + oferta)
├─ WhatsApp automático (integração com CRM)
├─ SMS (para ofertas urgentes/limitadas)
└─ Notificações push (se tiver app)
```

**CRÍTICO:** Sempre criar sequência automática de 7-14 dias com:
- Dias 1-3: Boas-vindas + entrega de valor
- Dias 4-7: Doutrinação + seeding
- Dias 8-14: Pitch do próximo nível

---

### 3. Calendário de Ascensão

**Para quem:** Recuperar quem ficou para trás e não ascendeu sozinho

**Formatos:**

**A) Campanhas Periódicas**
- **Mensais:** Ofertas pequenas, lembretes de valor
- **Bi-mensais:** Ofertas médias, urgência moderada
- **Trimestrais:** Grandes lançamentos, eventos

**B) Ascensões Semanais por Degrau**
```python
# Exemplo de rotação semanal
calendario = {
    "Semana 1": "Campanha Frontend → Backend",
    "Semana 2": "Campanha Backend → Highticket",
    "Semana 3": "Campanha Highticket → Mastermind",
    "Semana 4": "Recuperação geral + Mini ascensões"
}
```

---

## Funis de Ascensão por Nível

### FUNIS FRONTEND → BACKEND (7 Estratégias Automáticas)

**1. MINI ASCENSÕES EM AULAS**
```
Implementação:
├─ Banners dentro das aulas
├─ CTAs no final de cada módulo
├─ Ofertas de "Itens de Ação Prontos" (R$ 7-37)
└─ Objetivo: Criar hábito de compra (Buying Frenzy)

Produtos ideais:
- Templates prontos (R$ 17)
- Checklists avançadas (R$ 7)
- Scripts de vendas (R$ 27)
- Mini-cursos complementares (R$ 37)
```

**2. WORKSHOP/WEBINAR AUTOMÁTICO**
```
Estrutura:
├─ 40-60 min de conteúdo de alto valor
├─ Pitch para Assinatura Nível 2
├─ Oferta com bônus e urgência
└─ Sequência de follow-up automática

Conversão esperada: 3-8% dos inscritos
```

**3. FUNIL DE CUPOM DE DESCONTO**
```
Mecânica:
├─ Mini-workshop de tema sexy (15-30 min)
├─ Ao final: cupom de desconto para Assinatura 1
├─ Cupom expira em 48-72h
└─ Emails lembrando da expiração

Exemplo de tema: "3 Hacks para [Resultado Específico] que 99% não sabe"
```

**4. CALL OBRIGATÓRIA DE 2 ETAPAS**
```
Etapa 1 (Automática):
└─ Call de liberação de bônus (gravada ou ao vivo em grupo)
   └─ Pitch para Assinatura 2 no final

Etapa 2 (Semi-automática):
└─ Quem se interessou agenda call individual
   └─ Fechamento consultivo para Assinatura 2

Conversão esperada: 15-25% na etapa 2
```

**5. BANNERS DE DÚVIDA SOBRE O TÓPICO**
```html
<!-- Exemplo de banner na área de membros -->
<div class="banner-ascensao">
  <h3>Tem dúvidas sobre [TÓPICO DA AULA]?</h3>
  <p>Na Assinatura 1 você tem suporte direto comigo para tirar TODAS as suas dúvidas.</p>
  <a href="/checkout-assinatura-1">Experimente por 7 dias grátis</a>
</div>
```

**6. ESTUDO DE CASO DE ALUNOS**
```
Implementação:
├─ Vídeo de 10-20 min com aluno de sucesso
├─ Aluno menciona: "Só consegui porque entrei na Assinatura 3 Highticket"
├─ No final: "Quer resultados como esse? Veja como"
└─ CTA para VSL do Highticket

Regra: SEMPRE usar alunos do PRÓXIMO nível, não do nível atual
```

**7. MÓDULO DE PRÓXIMOS PASSOS**
```
Estrutura do módulo:

AULA 1: "Seu Próximo Passo Mais Rápido"
├─ Mata objeções internas/emocionais
└─ Prepara para próximo investimento

AULA 2: "Indicação de Produto de Ancoragem"
├─ Apresenta produto MAIS CARO primeiro (Highticket)
├─ Quando clica, já vê preço exposto
└─ Cria ancoragem de preço

AULA 3: "Pitch para Produto Principal"
├─ VSL ou pitch direto do produto que REALMENTE quer vender (Backend)
├─ Aperta bastante no problema que ele tem AGORA
├─ Joga direto para checkout personalizado

SEÇÃO FINAL: "Outros Produtos que Talvez Te Interessem"
├─ Página embedada com vários produtos
├─ Preços promocionais "só para alunos"
└─ Produtos que alunos deste nível geralmente compram
```

---

### FUNIS BACKEND → HIGHTICKET (11 Estratégias)

**1. WEBINAR AUTOMÁTICO**
- Formato: Webinar evergreen de 60-90 min
- Conversão esperada: 2-5% para Highticket

**2. CALL OBRIGATÓRIA DE 2 ETAPAS**
- Qualificação automática + fechamento consultivo
- Conversão esperada: 20-30% dos qualificados

**3. CALL DE ENTREGA DE BÔNUS**
- Manual, high-touch
- Pitch contextual durante entrega

**4. PÁGINA DE OBRIGADO COM CALL GRATUITA**
```
Regras de pricing por produto backend:

Para Highticket de R$ 10k+:
└─ Somente na pág. de obrigado de quem comprou ≥ R$ 997

Para Highticket de R$ 5k:
└─ Página de obrigado de quem comprou ≥ R$ 497

Para Highticket < R$ 3k:
└─ Pode usar em qualquer página de obrigado (até tripwires)

Follow-up: Emails lembrando da call caso não agende
```

**5. IMERSÃO GRAVADA COM PITCH**
```
Implementação:
├─ Dar de bônus gravação de imersão de 3h
├─ Imersão tinha pitch para mentoria no final
├─ Cliente consome conteúdo + é doutrinado + vê pitch
└─ CTA no final para aplicação/call
```

**6. ESTUDO DE CASO DETALHADO**
```
Estrutura completa:

1. Vídeo estudo de caso (15-30 min)
   ├─ Aluna investiu R$ 5k e faturou R$ 80k
   ├─ Durante vídeo: seeding do próximo produto
   └─ Detalhamento da estratégia dela

2. CTA no final: "Quer ajuda para ter resultado como esse?"
   └─ Joga para VSL de 10 min apresentando método

3. Botão da VSL: popup de captura (email + WhatsApp)
   └─ Joga para aplicação para ligação de apresentação

4. Se preencher mas não aplicar:
   └─ Sequência infinita de emails com outros estudos de caso

5. Ligação de apresentação:
   └─ Perguntas de identificação de dor e problema
   └─ Apresentação do Highticket
```

**7. CALL DE SETUP/BOAS VINDAS**
```
Script da call:

1. BOAS VINDAS
2. PERGUNTA SE ESTÁ ANSIOSO
3. QUAIS SÃO OS PLANOS
4. AJUDA A SE SITUAR NA PLATAFORMA
5. PITCH: "Você sabia que tem versão com acompanhamento?"
6. OFERTA: "Custa X, mas como já pagou Y, paga só o restante"
7. BENEFÍCIOS: Calls, suporte direto, comunidade exclusiva

Conversão esperada: 10-20%
```

**8. INGRESSO PARA EVENTO RECORRENTE**
```
Estrutura do evento:

Tipo: Evento dos alunos a cada 1-3 meses
Duração: 2-3 dias
Acesso: Somente para clientes
Preço para não-clientes: R$ 297

Implementação:
├─ Calendário na área de membros mostrando frequência
├─ Seeding constante (quem vai palestrar, antecipação)
├─ Durante evento: ascensão para Highticket
└─ Pitch no último dia

Passos:
1. Criar nome sexy para o evento
2. Criar promessa clara
3. Antecipação via email + remarketing
4. Trazer convidados/palestrantes especiais
5. Pitch do Highticket no final
```

**9. FUNIL DE CUPOM DE DESCONTO MAIS CARO**
```
Diferencial: Produtos de R$ 297 a R$ 497
Mecânica: Mesma do frontend, mas com ofertas superiores
Objetivo: Ascensão intermediária antes do Highticket
```

**10. MINI ASCENSÕES DENTRO DO BACKEND**
```
Filosofia: Fazer cliente PERMANECER no ciclo de compra (Buying Frenzy)

Produtos: R$ 7, R$ 17, R$ 37
Objetivo real: Manter confiança absoluta na marca

Jogo psicológico:
COMPROU > EXPERIÊNCIA BOA ALÉM DO ESPERADO
COMPROU > EXPERIÊNCIA BOA ALÉM DO ESPERADO
COMPROU > EXPERIÊNCIA BOA ALÉM DO ESPERADO

Resultado: Quando fizer pitch de R$ 997+, ele compra sem pensar
```

**11. CAMPANHA DE ABANDONO DE CARRINHO**
```
Tipos:
├─ Por Email/SMS (automático)
├─ Por Call (semi-automático)
└─ Chat ao vivo no checkout (real-time)

Sequência de email de abandono:
- 1h depois: "Esqueceu algo?"
- 24h depois: "Dúvidas sobre [PRODUTO]?"
- 48h depois: "Bônus especial se finalizar hoje"
- 72h depois: "Última chance - oferta expira"
```

---

### HIGHTICKET → MASTERMIND (3 Formas)

**FORMA 1: Convidados Especiais Grátis**
```
Processo:
1. Analisar mentorados com faturamento ideal para mastermind
2. Convidar como convidados especiais GRÁTIS
3. Envolver, fazer vestir a camisa
4. Integrar com o grupo
5. Dar atenção especial, brindes de boas-vindas
6. Apresentar no palco
7. Fazer TODAS as dinâmicas do evento com eles
8. No final, chamar no canto: "Quer viver mais dessa experiência?"

Conversão esperada: 40-60% dos convidados
```

**FORMA 2: Premiação após Vitória Compartilhada**
```
Processo:
1. Nas calls, perguntar quem teve ótimo resultado
2. Comemorar desesperadamente, forçar todos a aplaudirem
3. Tutores descobrem quem faturou o valor ideal
4. 1 dia depois, chamam no privado
5. "O MENTOR premiou você com uma call exclusiva"
6. Na call, mentor avisa que está na hora de subir pro mastermind
7. Se não conseguir entrar, anotar e levar grátis no próximo evento presencial

CRÍTICO: Ao longo da mentoria TODA, gerar doutrinação para mastermind
```

**FORMA 3: Entrega Presencial com Premiação**
```
Processo:
1. Entrega presencial da mentoria a cada 4 meses
2. No evento, descobrir maiores faturamentos + pessoas com índole que gosta
3. Premiar no palco: "Você ganhou ingresso grátis para próximo encontro da Cúpula"
4. Após participar, fazer pitch da Cúpula

Doutrinação prévia crítica: Mencionar a Cúpula ao longo da mentoria
```

---

## Estratégias de Renovação (Highticket/Assinatura)

**Princípio Central:** Fazer membros CONSUMIREM, USAREM e VOLTAREM constantemente

### 3 Hábitos a Criar

**1. Hábito de Consumo**
- Frequência: Semanal/Quinzenal/Mensal
- Formato: Treinamentos, podcasts, conteúdos exclusivos

**2. Hábito de Usar Sem Possuir**
```
REGRA DE OURO: Fazer eles DEPENDEREM de você para ter o que usam sempre

Exemplo:
├─ Ferramentas que só membros acessam (não podem baixar)
├─ Templates que são atualizados mensalmente (versão antiga fica obsoleta)
├─ Comunidade ativa (perdem acesso ao sair)
└─ Calls recorrentes (perdem continuidade ao cancelar)
```

**3. Hábito de Interação Social**
- Gamificação: Calouros, 2º Ano, 3º Ano
- Pegadinhas de veteranos para novatos
- Eventos exclusivos

---

### Sistema de Conteúdo Programado

**Evolução Progressiva por Ciclo:**

```
PRIMEIRO CICLO (Meses 1-12):
└─ 1 treinamento novo por mês

SEGUNDO CICLO (Renovação 1):
├─ 1 treinamento novo por mês
└─ 1 podcast secreto por mês

TERCEIRO CICLO (Renovação 2):
├─ 1 treinamento novo por mês
├─ 1 podcast secreto por mês
└─ 1 ClosesFriends exclusivo por mês
```

**Implementação:**
```
1. Gravar 12 treinamentos de uma vez (títulos apelativos)
2. Liberar 1 por mês automaticamente
3. Disparar emails cheios de promessas e spoilers
4. Incentivar consumo com avisos múltiplos

Objetivo: Criar ritual mensal de consumo
```

---

### Campanha Longa de Renovação

**Exemplo Ágora Financial:** 26% de renovação na 1ª campanha

**Estrutura:**
```
6 meses antes do vencimento: Começar campanha
├─ Oferta para quem renova em 6 meses: Bônus X + Desconto Y
├─ Oferta para quem renova em 5 meses: Bônus A + Desconto B
├─ Oferta para quem renova em 4 meses: Bônus C + Desconto D
├─ Oferta para quem renova em 3 meses: Bônus E + Desconto F
├─ Oferta para quem renova em 2 meses: Bônus G + Desconto H
└─ Último mês: Urgência máxima, perda de benefícios

Princípio: Campanha longa dá tempo para alta taxa de renovação
```

**Centro de Tudo:**
> "Ter uma OFERTA, uma PROPOSTA DE VALOR e uma VANTAGEM que ele SÓ pode obter com você!"

---

## 20 Centros de Lucro (Maximização de AOV)

Implementar progressivamente para aumentar AOV em até 300%:

```
CENTRO 1: Captura com No-Optin (AOV +5%)
CENTRO 2: Bump de Pré-checkout (AOV +8%)
CENTRO 3: Remarketing Funcional (Recovery +15%)
CENTRO 4: 4 Order Bumps (AOV +12%)
CENTRO 5: Upsell de Exit Popup (Recovery +7%)
CENTRO 6-8: Upsells 1, 2, 3 (AOV +25%)
CENTRO 9: Ofertas de Downsell (Recovery +10%)
CENTRO 10: Pág. Obrigado com Soft-Sell (AOV +8%)
CENTRO 11: Campanhas Abandono Upsell (Recovery +6%)
CENTRO 12: Chat Ao Vivo no Checkout (CVR +5%)
CENTRO 13: Abandono Carrinho por Call (Recovery +12%)
CENTRO 14: Abandono por SMS/Email (Recovery +8%)
CENTRO 15: Call de Boas Vindas com Monetização (AOV +15%)
CENTRO 16: Promoção Boas Vindas Email Direto (AOV +10%)
CENTRO 17: Promoção Boas Vindas Parte 2 (AOV +8%)
CENTRO 18: Oferta Highticket na Traseira (AOV +30%)
CENTRO 19: Remarketing de Reconhecimento (LTV +20%)
CENTRO 20: Ofertas Backend Para Leads (CVR +5%)
```

**Implementação Prioritária:**
1. Semana 1-2: Centros 1, 4, 6, 7 (quick wins)
2. Semana 3-4: Centros 12, 13, 14, 15 (automação)
3. Semana 5-8: Centros 2, 3, 5, 9, 11 (otimização)
4. Mês 3+: Centros 10, 16, 17, 18, 19, 20 (escalabilidade)

Consultar detalhes: `references/GUIA_TATICO_IMPLEMENTACAO.md` → "20 Centros de Lucro"

---

## Geração de Estratégias Customizadas com IA

**CRÍTICO:** Esta skill NÃO deve apenas reproduzir estratégias existentes. Deve CRIAR novas estratégias baseadas nos padrões identificados.

### 8 Padrões Fundamentais Identificados

Use estes padrões para criar estratégias novas:

**1. Sequência Automático → Semi → Manual**
```python
def criar_estrategia_ascensao(produto_atual, produto_alvo):
    # SEMPRE começar por automação
    estrategias = []

    # Nível 1: Automático
    estrategias.append(gerar_funil_automatico(produto_atual, produto_alvo))

    # Nível 2: Semi-automático (se automático < 10% conversão)
    estrategias.append(gerar_funil_semi_automatico(produto_atual, produto_alvo))

    # Nível 3: Manual (recuperação)
    estrategias.append(gerar_campanha_manual_recuperacao(produto_atual, produto_alvo))

    return estrategias
```

**2. Consciência → Desejo → Oferta**
```
Para qualquer produto:
1. Gerar consciência (ele sabe que existe?)
2. Aumentar desejo (ele quer ter?)
3. Fazer oferta (ele pode ter agora?)
```

**3. Resolver Problema → Criar Novo Problema**
```
Regra criativa:
- Produto atual ensina X
- X resolvido cria naturalmente problema Y
- Próximo produto resolve Y

Exercício de criação:
"Se meu produto ensina __________, que novo problema isso cria?"
```

**4. Valor Percebido Diferente Por Degrau**
```
Mesmo método + Formatos diferentes = Percepção de valor diferente

Exercício criativo:
"Quais 5 formatos diferentes eu poderia entregar meu método?"
- Curso gravado
- Ao vivo com Q&A
- Implementação comigo
- Feito para você
- Certificação/Licenciamento
```

**5. Ver Sem Ter Acesso**
```
Princípio psicológico: FOMO de oportunidade perdida

Aplicações criativas:
- Produtos bloqueados visíveis
- Notificações de eventos de outros níveis
- Bastidores do nível superior
- Conversas/comentários de membros superiores visíveis
```

**6. Conexão 360°**
```
5 tipos de conexão para criar:
1. Com a Marca (valores, missão, identidade)
2. Com a Tribo (comunidade, movimento)
3. Com o Expert (proximidade, acesso)
4. Com o Método (resultados, provas)
5. Com a Comunidade (pertencimento, status)

Quanto mais conexões, maior retenção e ascensão
```

**7. Hábito de Uso Sem Posse**
```
Estratégia de dependência:
- Cliente USA mas não POSSUI
- Precisa continuar pagando para continuar tendo acesso
- Exemplos: ferramentas SaaS, comunidade, calls recorrentes

Exercício criativo:
"O que meus clientes podem USAR mas não POSSUIR?"
```

**8. Evolução Progressiva com Status**
```
Gamificação de níveis:
- Nomenclaturas diferentes (Calouro, Veterano, Elite)
- Benefícios progressivos
- Rituais de passagem
- Reconhecimento público

Aumenta: Renovação, ascensão, FOMO
```

---

### Framework de Criação de Novas Estratégias

Quando precisar criar estratégia customizada:

**PASSO 1: Analisar Contexto**
```
Perguntas:
├─ Qual produto atual? (preço, formato, promessa)
├─ Qual produto alvo? (preço, formato, promessa)
├─ Qual gap entre eles? (preço, valor percebido, complexidade)
├─ Qual avatar atual? (estágio, desejos, medos)
└─ Qual comportamento atual? (engajamento, consumo, satisfação)
```

**PASSO 2: Identificar Padrões Aplicáveis**
```python
padroes_aplicaveis = []

if gap_preco > 3x:
    padroes_aplicaveis.append("Consciência → Desejo → Oferta")
    padroes_aplicaveis.append("Ver Sem Ter Acesso")

if engajamento < 30%:
    padroes_aplicaveis.append("Conexão 360°")
    padroes_aplicaveis.append("Hábito de Uso")

if avatar_confuso:
    padroes_aplicaveis.append("Resolver → Criar Problema")

# Sempre aplicar:
padroes_aplicaveis.append("Automático → Semi → Manual")
```

**PASSO 3: Combinar Padrões Criativamente**
```
Exemplo de combinação:

Padrão 1: "Resolver → Criar Problema"
+ Padrão 2: "Ver Sem Ter Acesso"
= NOVA ESTRATÉGIA:

"Produto atual resolve problema X.
No final do produto, mostrar bastidores de aluno resolvendo problema Y
(que foi criado ao resolver X) usando produto superior.
Aluno menciona: 'Só consegui porque tenho acesso a [FERRAMENTA EXCLUSIVA DO NÍVEL SUPERIOR]'.
CTA: 'Quer acesso à mesma ferramenta?'"
```

**PASSO 4: Validar com Checklist**
```
Estratégia criada deve ter:
✅ Componente automático (prioridade)
✅ Gatilho psicológico claro
✅ CTA específico
✅ Mensuração possível
✅ Escalável (não depende 100% de manual)
✅ Alinhado com jornada do avatar
```

---

## Scripts Incluídos

Esta skill inclui scripts automatizados para geração de estratégias:

### 1. `gerar_estrategia_ascensao.py`
Gera estratégia completa baseada em inputs do negócio

**Uso:**
```bash
python scripts/gerar_estrategia_ascensao.py \
  --produto-atual "Curso Frontend R$ 97" \
  --produto-alvo "Mentoria R$ 2997" \
  --avatar "Iniciante em marketing digital" \
  --output estrategia_customizada.json
```

### 2. `analisar_escada_valor.py`
Analisa escada de valor existente e sugere melhorias

**Uso:**
```bash
python scripts/analisar_escada_valor.py \
  --escada escada_valor.json \
  --output analise_gaps.json
```

### 3. `calendario_campanhas.py`
Gera calendário de campanhas de 90 dias

**Uso:**
```bash
python scripts/calendario_campanhas.py \
  --degraus 3 \
  --inicio 2026-02-01 \
  --output calendario_90_dias.json
```

### 4. `calcular_ltv_projetado.py`
Calcula LTV projetado com estratégias de ascensão

**Uso:**
```bash
python scripts/calcular_ltv_projetado.py \
  --aov-atual 297 \
  --taxa-ascensao 12 \
  --num-degraus 4 \
  --output projecao_ltv.json
```

---

## Recursos Incluídos

### References (Referências Técnicas)

| Arquivo | Conteúdo | Quando Usar |
|---------|----------|-------------|
| `analise_estrategica.json` | Base de dados completa extraída dos 20 PDFs | Consulta de frameworks, tipos de funil, centros de lucro |
| `GUIA_TATICO_IMPLEMENTACAO.md` | Guia prático com exemplos, scripts, checklists | Durante implementação, copiar templates e seguir cronogramas |
| `RESUMO_EXECUTIVO.md` | Referência rápida tipo mapa mental | Consulta veloz durante trabalho, glossário de termos |

### Assets (Templates e Recursos)

| Arquivo/Pasta | Conteúdo | Uso |
|---------------|----------|-----|
| `templates/emails/` | 20+ templates de emails de ascensão | Copiar e adaptar para campanhas |
| `templates/funis/` | Estruturas de funis automáticos | Implementação rápida de funis |
| `templates/checkouts/` | Páginas de checkout personalizadas | Otimização de conversão |
| `checklists/` | 3 checklists principais de implementação | Garantir nada é esquecido |

---

## Checklists Rápidas

### ✅ Produto Pronto para Ascensão?

```
□ Produto entrega valor prometido? (Melhor primeiro beijo)
□ Cria problema novo que próximo produto resolve?
□ Tem doutrinação embutida? (Seeding, histórias, provas)
□ Tem módulo "Próximos Passos"?
□ Tem banners/CTAs para próximo nível?
□ Tem sequência automática pós-compra?
□ Tem produtos bloqueados à mostra?
□ Apresenta escada completa no início?
□ Tem hooks de tráfego interno funcionando?
□ Métricas de ascensão estão sendo rastreadas?
```

### ✅ Funil de Ascensão Otimizado?

```
□ É automático ou semi-automático? (não manual)
□ Promessa adaptada ao avatar do degrau?
□ Formato de funil que cliente ainda não vivenciou?
□ Tem sequência de doutrinação prévia?
□ Tem urgência/escassez real?
□ Tem provas sociais do próximo nível?
□ Checkout personalizado com depoimentos?
□ Tem chat de dúvidas no checkout?
□ Tem sequência de abandono de carrinho?
□ Taxa de conversão sendo monitorada?
```

### ✅ Campanha de Recuperação Efetiva?

```
□ Segmentação comportamental aplicada?
□ Múltiplos canais (email, WhatsApp, call)?
□ Ofertas escalonadas por tempo?
□ Urgência real (não fake)?
□ Bônus exclusivos para quem voltou?
□ Reativação de valor antes da venda?
□ Sequência de 7-14 dias montada?
□ Follow-up automático configurado?
□ Taxa de recuperação sendo medida?
□ Aprendizados sendo documentados?
```

---

## Métricas de Sucesso

### KPIs por Degrau

| Métrica | Frontend | Backend | Highticket |
|---------|----------|---------|-----------|
| Taxa de Ascensão | ≥ 10% | ≥ 15% | ≥ 25% |
| Tempo Médio para Ascender | 7-30 dias | 30-90 dias | 90-180 dias |
| Taxa de Renovação | N/A | ≥ 60% | ≥ 70% |
| LTV Médio | 3-5x inicial | 10-20x inicial | 50-200x inicial |

### Benchmarks de Conversão

```
Funis Automáticos:
├─ Webinar automático: 3-8%
├─ VSL + checkout: 2-5%
├─ Trial + pitch: 10-20%
└─ Upsell imediato: 15-30%

Funis Semi-Automáticos:
├─ Call de 2 etapas: 15-25%
├─ Call de boas-vindas: 10-20%
└─ Call de entrega de bônus: 20-35%

Campanhas de Recuperação:
├─ Email abandono carrinho: 5-12%
├─ Call abandono carrinho: 15-25%
└─ Campanha periódica: 3-8%
```

---

## Próximos Passos

Após ativar esta skill, siga o fluxo:

**1. Diagnóstico** (Use script `analisar_escada_valor.py`)
```
├─ Mapeie sua escada de valor atual
├─ Identifique gaps de preço
├─ Analise taxa de ascensão atual por degrau
└─ Liste objeções principais por transição
```

**2. Priorização** (Use a Regra de Ouro)
```
Priorize ascensões AUTOMÁTICAS:
├─ Maior gap de ascensão (mais clientes parados)
├─ Maior impacto em LTV
└─ Menor complexidade de implementação
```

**3. Implementação** (Use `references/GUIA_TATICO_IMPLEMENTACAO.md`)
```
Semana 1-2: Funis automáticos básicos
Semana 3-4: Doutrinação e seeding
Semana 5-8: Campanhas de recuperação
Mês 3+: Otimização e novos centros de lucro
```

**4. Medição** (Use `calcular_ltv_projetado.py`)
```
Rastrear semanalmente:
├─ Taxa de ascensão por degrau
├─ Tempo médio para ascender
├─ LTV por coorte
└─ ROI de cada funil/campanha
```

**5. Otimização** (Ciclo contínuo)
```
A cada 30 dias:
├─ Analisar métricas vs benchmarks
├─ Identificar gargalos
├─ Testar variações (copy, oferta, formato)
└─ Escalar o que funciona
```

---

## Exemplos de Uso

### Exemplo 1: E-commerce de Infoprodutos

**Contexto:**
- Produto atual: Ebook R$ 27
- Produto alvo: Curso completo R$ 497
- Gap: 18x no preço

**Estratégia gerada:**

1. **Ascensão Imediata (Automática)**
```
Página de obrigado do Ebook:
├─ Vídeo de 3 min: "Parabéns! Agora veja os 3 erros que 90% comete"
├─ No vídeo: menciona que curso completo ensina a evitar esses erros
└─ CTA: "Acesse o curso completo com 50% OFF (só nas próximas 24h)"

Resultado esperado: 8-12% de conversão
```

2. **Doutrinação no Ebook (Semi-automática)**
```
Dentro do Ebook:
├─ Capítulo 3: Mencionar "No curso completo eu ensino o framework X"
├─ Capítulo 5: Print de resultado de aluno do curso
├─ Capítulo Final: "Seus próximos passos" com link para webinar gratuito

Webinar automático:
└─ Pitch do curso completo
└─ Conversão esperada: 5-8%
```

3. **Recuperação (Manual)**
```
30 dias depois:
├─ Email: "Você aplicou o que está no Ebook?"
├─ Segmenta: Quem clicou mas não comprou curso
└─ Campanha de 7 dias com case studies + oferta

Conversão esperada: 3-5% dos recuperados
```

---

### Exemplo 2: SaaS/Plataforma

**Contexto:**
- Produto atual: Plano Basic R$ 97/mês
- Produto alvo: Plano Pro R$ 497/mês
- Gap: 5x no preço

**Estratégia gerada:**

1. **Ver Sem Ter Acesso (Automática)**
```
Dentro da plataforma Basic:
├─ Funcionalidades Pro aparecem bloqueadas com ícone de cadeado
├─ Ao clicar: "Esta funcionalidade está disponível no Plano Pro"
├─ Modal mostra: vídeo de 30s demonstrando a funcionalidade
└─ CTA: "Upgrade agora e teste 7 dias grátis"

Resultado esperado: 2-4% de upgrade/mês
```

2. **Emails de Uso (Automática)**
```
Trigger: Quando usuário usa funcionalidade X vezes
├─ Email: "Você está dominando [FUNCIONALIDADE]!"
├─ "Usuários Pro conseguem fazer isso 10x mais rápido com [FEATURE PRO]"
├─ Case study de cliente que fez upgrade
└─ CTA: "Veja como funcionaria para você" → Demo personalizada

Resultado esperado: 5-8% de upgrade
```

3. **Call de Sucesso (Semi-automática)**
```
Trigger: Usuário atingiu milestone importante
├─ Email: "Parabéns! Você atingiu [MILESTONE]"
├─ Oferta de call de 15 min para "otimização estratégica"
├─ Na call: mostrar como Pro aceleraria ainda mais
└─ Oferta especial de upgrade com desconto

Resultado esperado: 25-35% de upgrade dos que fazem call
```

---

### Exemplo 3: Agência/Serviços

**Contexto:**
- Produto atual: Consultoria Básica R$ 997/mês
- Produto alvo: Done-For-You R$ 5.997/mês
- Gap: 6x no preço

**Estratégia gerada:**

1. **Demonstração de Diferença (Automática)**
```
Durante calls de consultoria:
├─ Gravar trechos (com permissão) de implementação bem-sucedida
├─ Criar mini-documentários de 5-10 min
├─ Enviar para todos clientes de Consultoria Básica
├─ No final: "Quer que façamos isso PARA você?"
└─ CTA para aplicação de Done-For-You

Resultado esperado: 10-15% aplica
```

2. **Oferta de Implementação Única (Semi-automática)**
```
Após 3 meses de consultoria:
├─ Email: "Análise gratuita da sua implementação"
├─ Call de análise (30 min)
├─ Mostrar: "Você implementou 40% do que poderia"
├─ Pitch: "Se fizéssemos PARA você, teria 100% em 30 dias"
└─ Oferta de Done-For-You

Resultado esperado: 20-30% dos que fazem call
```

3. **Programa de Resultados Garantidos (Manual)**
```
Clientes com bom fit:
├─ Convite para programa piloto de Resultados Garantidos
├─ Done-For-You com garantia de performance
├─ Investimento maior, risco menor
└─ Pitch exclusivo em call 1-on-1

Resultado esperado: 30-40% dos convidados
```

---

## Quando NÃO Usar Esta Skill

Esta skill é poderosa, mas não é para tudo:

**NÃO use quando:**
- ❌ Produto atual não entrega valor (primeiro beijo ruim) → Corrija o produto antes
- ❌ Não há clareza sobre próximo degrau → Defina escada de valor primeiro
- ❌ Taxa de satisfação < 70% no produto atual → Melhore entrega antes de ascender
- ❌ Churn alto no produto atual → Resolva retenção antes de ascensão
- ❌ Não há diferença clara de valor entre degraus → Redefina posicionamento

**Use primeiro:**
- ✅ Validação de produto-mercado
- ✅ Entrega de valor consistente
- ✅ NPS ≥ 40
- ✅ Churn < 5%/mês (assinaturas) ou satisfação > 80% (one-time)

---

## Avisos Críticos

**CRITICAL:** Nunca sacrifique a qualidade da entrega pelo volume de ascensão. Cliente que ascende sem estar pronto gera churn e destrói reputação.

**CRITICAL:** Doutrinação ≠ Manipulação. Só doutrine para produtos que REALMENTE ajudam o cliente no próximo estágio.

**CRITICAL:** Ascensão forçada (sem preparo do avatar) gera reembolsos, reclamações e destruição de marca. Respeite o timing.

**CRITICAL:** Mini ascensões devem entregar valor REAL. Se forem apenas "dinheiro fácil", destroem confiança para ascensões maiores.

**CRITICAL:** Sempre teste automático ANTES de investir em manual. Regra de Ouro não é opcional.

---

## Conclusão

Esta skill fornece um sistema completo para criar estratégias de ascensão automática de clientes. Combine os frameworks (Efeito Alquimia, Método Rafa), os 8 padrões identificados e os scripts automatizados para gerar estratégias customizadas para qualquer negócio.

**Lembre-se:**
1. Sempre priorize AUTOMAÇÃO
2. Doutrine progressivamente
3. Crie problema novo que próximo produto resolve
4. Meça, otimize, escale
5. Foco em LTV, não apenas em venda única

Para implementação detalhada, consulte `references/GUIA_TATICO_IMPLEMENTACAO.md`.
Para referência rápida, consulte `references/RESUMO_EXECUTIVO.md`.
Para dados estruturados, consulte `references/analise_estrategica.json`.
