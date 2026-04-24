# Checklist Completa de Implementação de Ascensão Automática

Use esta checklist para garantir que todos os elementos essenciais estão implementados.

---

## FASE 1: FUNDAÇÃO (Semana 1-2)

### 1.1 Mapeamento da Escada de Valor

- [ ] Listar todos os produtos/serviços atuais
- [ ] Ordenar por preço (menor → maior)
- [ ] Identificar gaps de preço > 5x
- [ ] Definir próximo produto a criar (se necessário)
- [ ] Mapear evolução do avatar em cada degrau
  - [ ] Degrau 1: Quem ele é? O que deseja? O que teme?
  - [ ] Degrau 2: Quem ele é? O que deseja? O que teme?
  - [ ] Degrau 3: Quem ele é? O que deseja? O que teme?
  - [ ] Degrau 4+: Quem ele é? O que deseja? O que teme?

### 1.2 Definição de "Única Crença" por Transição

- [ ] Frontend → Backend: "Qual crença faz ele PRECISAR do backend?"
- [ ] Backend → Highticket: "Qual crença faz ele PRECISAR do highticket?"
- [ ] Documentar em arquivo acessível ao time

### 1.3 Identificação de "Problema Criado"

Para cada produto, definir:
- [ ] Produto resolve: [PROBLEMA X]
- [ ] Ao resolver X, cria consciência de: [PROBLEMA Y]
- [ ] Próximo produto resolve: [PROBLEMA Y]
- [ ] Validar que a lógica faz sentido (não forçado)

---

## FASE 2: DOUTRINAÇÃO NO PRODUTO ATUAL (Semana 2-3)

### 2.1 Seeding nas Aulas/Conteúdo

- [ ] Revisar 100% do conteúdo atual
- [ ] Identificar 5-10 momentos para inserir seeding
- [ ] Adicionar menções a:
  - [ ] Histórias de alunos do próximo nível
  - [ ] Técnicas/ferramentas que só próximo nível tem acesso
  - [ ] Resultados possíveis com próximo nível
- [ ] Testar que seeding é NATURAL, não forçado

### 2.2 Módulo "Próximos Passos"

- [ ] Criar módulo no final do produto
- [ ] Aula 1: "Seu Próximo Passo Mais Rápido" (mata objeções)
- [ ] Aula 2: "Produto de Ancoragem" (mostra mais caro primeiro)
- [ ] Aula 3: "Pitch do Produto Principal" (VSL ou direto)
- [ ] Seção final: "Outros Produtos" (página embedada)
- [ ] Linkar para checkouts personalizados

### 2.3 Produtos Bloqueados à Mostra

- [ ] Na área de membros, mostrar produtos superiores bloqueados
- [ ] Adicionar ícone de cadeado
- [ ] Ao clicar: modal com vídeo de 30-60s sobre o produto
- [ ] CTA no modal: "Quero ter acesso" → página de vendas

### 2.4 Banners Contextuais

- [ ] Criar 3-5 banners de ascensão
- [ ] Configurar exibição contextual (após X aulas consumidas)
- [ ] Testar em diferentes dispositivos
- [ ] Rastrear cliques em cada banner

---

## FASE 3: FUNIL AUTOMÁTICO PRIORITÁRIO (Semana 3-4)

### 3.1 Escolha do Funil

Baseado no gap de preço e avatar, escolher:
- [ ] Webinar automático (gap médio, educar avatar)
- [ ] VSL + checkout (gap pequeno, venda direta)
- [ ] Trial + doutrinação (gap grande, precisa experimentar)
- [ ] Módulo próximos passos (já implementado na fase 2)
- [ ] Funil de cupom de desconto (mini-workshop → oferta)

### 3.2 Criação de Conteúdo do Funil

- [ ] Escrever roteiro (webinar/VSL/aulas de trial)
- [ ] Gravar vídeo(s) profissionalmente
- [ ] Editar com boa qualidade
- [ ] Adicionar CTA clara em 3+ momentos
- [ ] Testar que áudio está nítido e vídeo fluido

### 3.3 Página de Vendas/Checkout

- [ ] Headline que fala ao desejo do avatar NESTE estágio
- [ ] Promessa clara e tangível
- [ ] 5-10 bullet points de benefícios
- [ ] 3-5 depoimentos de alunos do PRÓXIMO nível
- [ ] FAQ com 5-8 perguntas mais comuns
- [ ] Garantia (7-30 dias)
- [ ] CTA acima da dobra + final da página
- [ ] Checkout otimizado (campos mínimos, confiança)

### 3.4 Sequência de Emails Automática

- [ ] Email 1 (Dia 1): Boas-vindas + valor + bônus
- [ ] Email 2 (Dia 2): Consumo + seeding
- [ ] Email 3 (Dia 4): Problema criado + doutrinação
- [ ] Email 4 (Dia 5): Prova social + caso de estudo
- [ ] Email 5 (Dia 6): Objeções + esperança
- [ ] Email 6 (Dia 7): Pitch direto + oferta
- [ ] Email 7 (Dia 8): Urgência final + FOMO
- [ ] Configurar no autoresponder (timing exato)
- [ ] Testar sequência completa (enviar pra você mesmo)

### 3.5 Hooks de Tráfego Interno

- [ ] IMÃ gratuito + aula de uso (página pós-cadastro vira oferta)
- [ ] Emails de consumo + relacionamento (10 tipos variados)
- [ ] Email "Bônus 2 dias após compra" (iniciar conversa)
- [ ] Email "Você já conversou comigo?" (pós não-compra)
- [ ] Email "Pode me fazer um favor?" (menção ao próximo programa)

---

## FASE 4: IMPLEMENTAÇÃO DE CENTROS DE LUCRO (Semana 4-6)

### 4.1 Quick Wins (Semana 4)

- [ ] CENTRO 4: Adicionar 4 order bumps no checkout
- [ ] CENTRO 6-8: Criar sequência de 3 upsells
- [ ] CENTRO 12: Instalar chat ao vivo no checkout
- [ ] Testar fluxo completo de compra + upsells

### 4.2 Recovery (Semana 5)

- [ ] CENTRO 3: Configurar remarketing funcional (ads)
- [ ] CENTRO 5: Exit popup com oferta de downsell
- [ ] CENTRO 13: Campanha de abandono de carrinho por call
- [ ] CENTRO 14: Abandono por SMS/Email (automático)

### 4.3 Otimização (Semana 6)

- [ ] CENTRO 10: Página de obrigado com soft-sell do próximo
- [ ] CENTRO 15: Call de boas-vindas com pitch de upgrade
- [ ] CENTRO 16-17: Promoção de boas-vindas (2 sequências)
- [ ] Medir incremento de AOV semana a semana

---

## FASE 5: FUNIL SEMI-AUTOMÁTICO (Semana 6-7)

### 5.1 Preparação para Calls

- [ ] Treinar time em script de qualificação
- [ ] Treinar time em script de fechamento
- [ ] Configurar ferramenta de agendamento (Calendly, etc)
- [ ] Criar página de captura para agendar call
- [ ] Testar fluxo: página → agendamento → confirmação

### 5.2 Call de 2 Etapas

- [ ] Etapa 1: Call em grupo (50-100 pessoas)
  - [ ] Roteiro com 60-70% valor + 30-40% pitch
  - [ ] CTA: "Agende call individual se quiser saber mais"
- [ ] Etapa 2: Call individual de fechamento
  - [ ] Script de perguntas (dor, objetivo, objeções)
  - [ ] Script de pitch consultivo
  - [ ] Script de fechamento com opções de pagamento

### 5.3 Follow-Up Pós-Call

- [ ] Email automático 1h após call
- [ ] WhatsApp 24h após (se não fechou)
- [ ] Email 48h após com depoimento
- [ ] Email 72h após: "Última chance antes de fechar turma"

---

## FASE 6: CAMPANHAS DE RECUPERAÇÃO (Semana 8-12)

### 6.1 Segmentação de Base

- [ ] Segmento 1: Comprou há 30 dias, não ascendeu
- [ ] Segmento 2: Comprou há 60 dias, não ascendeu
- [ ] Segmento 3: Comprou há 90+ dias, não ascendeu
- [ ] Segmento 4: Abandonou carrinho do próximo produto
- [ ] Segmento 5: Abriu emails mas nunca clicou

### 6.2 Calendário de Campanhas

- [ ] Semana 1: Automática para Degrau 1
- [ ] Semana 2: Semi-automática para Degrau 2
- [ ] Semana 3: Evento para Degrau 3
- [ ] Semana 4: Recuperação geral (todos os degraus)
- [ ] Repetir ciclo mensalmente
- [ ] Criar documento com planejamento de 90 dias

### 6.3 Evento Mensal de Ascensão

- [ ] Definir tema sexy (resolver problema atual)
- [ ] Criar página de inscrição
- [ ] Sequência de antecipação (3-5 emails)
- [ ] Preparar conteúdo do evento (60 min valor)
- [ ] Preparar pitch (15-20 min)
- [ ] Oferta especial exclusiva para participantes
- [ ] Follow-up pós-evento (replay + urgência 48h)

---

## FASE 7: MÉTRICAS E OTIMIZAÇÃO (Contínuo)

### 7.1 Configuração de Rastreamento

- [ ] Google Analytics configurado corretamente
- [ ] Pixels de conversão (Meta, Google Ads)
- [ ] Eventos customizados:
  - [ ] Clique em oferta de ascensão
  - [ ] Visualização de página de vendas do próximo nível
  - [ ] Início de checkout
  - [ ] Compra concluída
- [ ] Dashboard de métricas (Data Studio, Tableau, etc)

### 7.2 KPIs a Monitorar Semanalmente

- [ ] Taxa de ascensão por degrau (meta: ≥ 10%)
- [ ] Tempo médio para ascender
- [ ] Taxa de abertura de emails (meta: ≥ 25%)
- [ ] Taxa de cliques em emails (meta: ≥ 5%)
- [ ] Taxa de conversão de funis automáticos (meta: 5-12%)
- [ ] Taxa de conversão de calls (meta: 15-25%)
- [ ] AOV por degrau
- [ ] LTV por coorte

### 7.3 Otimização Contínua

- [ ] Revisar métricas toda Segunda
- [ ] Identificar 1 gargalo principal da semana
- [ ] Testar 1 variação (copy, oferta, CTA)
- [ ] Medir impacto após 7-14 dias
- [ ] Documentar aprendizados
- [ ] Escalar o que funciona, eliminar o que não

---

## FASE 8: ESTRATÉGIAS DE RENOVAÇÃO (Mês 3+)

### 8.1 Para Produtos de Assinatura

- [ ] Conteúdo programado mensal:
  - [ ] Gravar 12 treinamentos de uma vez
  - [ ] Liberar 1 por mês automaticamente
  - [ ] Títulos apelativos que geram FOMO
- [ ] Sistema de evolução progressiva:
  - [ ] Ciclo 1: 1 treinamento/mês
  - [ ] Ciclo 2 (renovação): +1 podcast/mês
  - [ ] Ciclo 3 (renovação 2): +1 close friends/mês
- [ ] Gamificação:
  - [ ] Nomenclaturas (Calouro → Veterano → Elite)
  - [ ] Benefícios progressivos por nível
  - [ ] Reconhecimento público

### 8.2 Campanha Longa de Renovação

- [ ] 6 meses antes: Oferta para quem renova agora
- [ ] 5 meses antes: Oferta escalona (menor desconto)
- [ ] 4 meses antes: Oferta escalona
- [ ] 3 meses antes: Oferta escalona
- [ ] 2 meses antes: Urgência aumenta
- [ ] 1 mês antes: Última chance + perda de benefícios

### 8.3 Eventos Exclusivos

- [ ] Evento online mensal só para membros ativos
- [ ] Evento presencial trimestral
- [ ] Calendário visível na área de membros
- [ ] Antecipação constante (quem vai palestrar, spoilers)
- [ ] Pitch de upgrade no final de cada evento

---

## CHECKLIST DE VALIDAÇÃO FINAL

Antes de considerar implementação completa, verificar:

### Produto Pronto para Ascensão?

- [ ] Entrega valor prometido? (NPS ≥ 40)
- [ ] Cria problema novo que próximo resolve?
- [ ] Tem doutrinação embutida? (seeding, histórias)
- [ ] Tem módulo "Próximos Passos"?
- [ ] Tem banners/CTAs para próximo nível?
- [ ] Tem sequência automática pós-compra?
- [ ] Produtos bloqueados à mostra?
- [ ] Apresenta escada completa no início?
- [ ] Hooks de tráfego interno funcionando?
- [ ] Métricas sendo rastreadas?

### Funil de Ascensão Otimizado?

- [ ] É automático ou semi-automático?
- [ ] Promessa adaptada ao avatar do degrau?
- [ ] Formato que cliente não vivenciou ainda?
- [ ] Sequência de doutrinação prévia?
- [ ] Urgência/escassez real?
- [ ] Provas sociais do próximo nível?
- [ ] Checkout personalizado com depoimentos?
- [ ] Chat de dúvidas no checkout?
- [ ] Sequência de abandono de carrinho?
- [ ] Taxa de conversão monitorada?

### Sistema Completo Funcionando?

- [ ] Pelo menos 1 funil automático ativo
- [ ] Taxa de ascensão ≥ 10% em pelo menos 1 transição
- [ ] Sequências de email enviando sem erros
- [ ] Métricas atualizando diariamente
- [ ] Time treinado para calls (se aplicável)
- [ ] Calendário de campanhas dos próximos 90 dias pronto
- [ ] Processo de otimização semanal estabelecido
- [ ] ROI positivo em pelo menos 1 estratégia

---

## PRÓXIMOS 90 DIAS

Após completar implementação base:

**Mês 1:**
- Otimizar funis automáticos existentes
- Começar testes A/B (copy, oferta, CTA)
- Implementar +5 centros de lucro

**Mês 2:**
- Adicionar funil semi-automático se conversão < 10%
- Começar eventos mensais
- Criar sistema de renovação para assinaturas

**Mês 3:**
- Escalar o que funciona (mais tráfego)
- Criar produto intermediário se gap grande
- Implementar sistema de afiliados para clientes

**Meta 90 dias:**
- Taxa de ascensão ≥ 15% em todas as transições
- LTV 3-5x maior que inicial
- Sistema rodando com mínimo de intervenção manual

---

**Use esta checklist como guia vivo. Marque itens conforme completa e revisite mensalmente para garantir que nada foi esquecido.**
