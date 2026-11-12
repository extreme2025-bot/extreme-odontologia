# Extreme Odontologia — site e campanha Google Ads

_Atualizado em 09/11/2026, 07:30. Fonte: trabalho feito na sessão com Rafael; itens marcados **[validado]** foram conferidos na fonte; **[pendente]** depende de ação do Rafael._

## Identidade e dados oficiais **[validado no cartão CNPJ e no Instagram]**
- Razão social: EXTREME ODONTOLOGIA LTDA · CNPJ 54.410.614/0001-70 · aberta em 20/03/2024 · EPP · CNAE 86.30-5-04
- Endereço: Rua dos Cedros, 478 – Sala 05 – Jardim Botânico – Sinop/MT – CEP 78556-046
- Responsável técnica: Dra. Luana Alves de Andrade – cirurgiã-dentista – CRO-MT 11238 (grafia "Alves", conforme Instagram)
- WhatsApp: (66) 99664-1307 · Instagram: @extreme_odontologia · Horário: seg–sex, 8h–18h
- Inscrição de pessoa jurídica no CRO-MT: **não localizada** na busca pública do CFO (0 resultados para "EXTREME ODONTOLOGIA" em MT). **[pendente]** confirmar/regularizar — ver riscos.

## Site institucional (GitHub Pages) **[validado – no ar]**
- URL: **https://www.extremeodonto.com.br/** (desde 09/11/2026, a pedido do Rafael o endereço principal é com `www`; `extremeodonto.com.br` sem www redireciona 301 para o www; http → https forçado; o endereço antigo extreme2025-bot.github.io/extreme-odontologia/ redireciona para o novo).
- Repositório: github.com/extreme2025-bot/extreme-odontologia (branch `main`, raiz, `.nojekyll`); gerador `build.py` (Python) no próprio repo.
- Páginas: Home · Tratamentos (índice + Limpeza, Clareamento, Canal) · Dúvidas (12 FAQs) · Artigos (3) · Contato (mapa, WhatsApp, Instagram, horários) · 404 · sitemap.xml · robots.txt.
- SEO: títulos/descrições por página, JSON-LD `Dentist` (endereço, geo, horários, telefone, RT), `FAQPage` e `Article`, Open Graph, embeds do Instagram e do Google Maps.
- Identidade visual: verde-escuro + dourado (do logo do Instagram), fontes Cormorant Garamond + Inter. Imagens: capturas de posts institucionais do Instagram (Rafael pode enviar fotos originais/logo em alta para substituir).
- Rodapé legal em todas as páginas: razão social, CNPJ, RT com CRO, aviso "informativo, não substitui avaliação". Sem preços (vedado pelo CEO, art. 44).
- **Domínio próprio: extremeodonto.com.br** **[validado]** — registrado no Registro.br em 08/11/2026 (ticket 32589910), titular Rafael (CPF), 5 anos, vence **08/11/2031**, R$ 184 (Pix). DNS hospedado no próprio Registro.br (modo avançado): 4 registros A → 185.199.108/109/110/111.153 (GitHub Pages) e CNAME `www` → extreme2025-bot.github.io. Publicação da zona pelo Registro.br levou ~3 h (saída ~01:30 de 09/11). Arquivo `CNAME` no repositório = `www.extremeodonto.com.br` (GitHub Pages redireciona o apex para o www automaticamente); `build.py` usa https://www.extremeodonto.com.br por padrão (canônicas, sitemap, robots, JSON-LD).
- extremeodontologia.com.br (nome completo) estava em processo de liberação no Registro.br — opcional tentar depois, só por proteção de marca.
- 09/11 06:30–07:30 **[validado]**: "Enforce HTTPS" ativo no GitHub Pages. URLs finais no Google Ads apontando para **https://www.extremeodonto.com.br/…**: 4 anúncios (edição em lote "Localizar e substituir" em URL final), 4 sitelinks e a promoção — reenviados para análise. Ocorrência: o anúncio de **Clareamento** foi reprovado por "Destino não correspondente" porque o robô do Google visitou a página durante a troca de endereço (redirecionamento transitório); página conferida estável (AdsBot → 200 direto no www); contestação aberta pelo Rafael em 09/11 (motivo: alterações feitas para obedecer à política). **[pendente]** confirmar aprovação do anúncio de Clareamento antes/depois de 10/11; se negar de novo, editar e salvar o anúncio para forçar nova revisão.

## Promoção vigente
- "Presente de fim de ano": 10% na primeira visita em limpeza, clareamento ou tratamento de canal, até 31/12/2026. Comunicada como percentual, sem valores em reais. Sem brinde, sorteio ou vale (vedados).

## Campanha Google Ads (conta 619-856-4076)
- Nome: **Extreme Odonto | Pesquisa Local Sinop** · ID 24441119250 · Rede de Pesquisa apenas (sem parceiros/Display).
- Orçamento R$ 20/dia · Maximizar cliques com CPC máx. R$ 7,00 · raio 10 km da Rua dos Cedros, 478 · Seg–Sex 07h–21h · início 10/11/2026.
- Grupos e palavras-chave:
  - **Dentista Sinop** — "dentista sinop", [dentista em sinop], "dentista em sinop", "dentista perto de mim", "clínica odontológica sinop", "clinica odontologica", "consultório odontológico", "dentista particular", "odontologia sinop", "melhor dentista em sinop", "dentista jardim botânico", "dentista perto"
  - **Clareamento** — clareamento dental, clareamento dental profissional, clareamento dental sinop, clareamento de dentes, clareamento dentário, clareamento a laser, clarear os dentes e variações
  - **Limpeza** — limpeza dental, limpeza dental sinop, profilaxia dental, limpeza de tártaro, remoção de tártaro, limpeza nos dentes e variações
  - **Canal e dor de dente** — tratamento de canal, canal no dente, tratamento de canal sinop, endodontia, endodontista, dentista canal, dor de dente dentista e variações
- Anúncios: 1 RSA por grupo, 15 títulos + 4 descrições, URL final específica por grupo (home / clareamento / limpeza / canal), caminhos de exibição por grupo. Descrição com identificação da RT ("Resp. técnica: Dra. Luana Alves de Andrade, CRO-MT 11238…") **fixada na posição 1** em todos os anúncios — exigência do art. 43 do CEO.
- Textos completos: `ads/textos.py` no repositório local da sessão (todos ≤30/≤90 caracteres).
- Publicada em 08/11/2026 (status "Pendente" até o início em 10/11; anúncios e recursos "Em análise").
- Feito após a publicação (08/11): 65 negativas no nível da campanha (`ads/negativas.txt`); 4 sitelinks (Clareamento Dental, Limpeza Dental, Tratamento de Canal, Como Chegar); 4 frases de destaque (Hora marcada; Planejamento digital; Agendamento por WhatsApp; Seg a sex, 8h às 18h); recurso de chamada 66 99664-1307; recurso de promoção "10% de desconto em Primeira visita" (exibe "até 31 de dez.", programado para encerrar em 31/12/2026, com termos: primeira visita de novos pacientes, limpeza/clareamento/canal, sujeito a avaliação, não cumulativo); recurso de local **desativado no nível da campanha** (a conta herdava o endereço da Extreme Truck, BR-163).
- Negativas que podem precisar de ajuste se a clínica atender esses casos: aparelho/ortodontia/invisalign, infantil/criança/odontopediatria, convênios (unimed, amil, odontoprev, bradesco, "plano odontológico") e termos de preço (preço, valor, quanto custa).

## Regras do CFO/CEO aplicadas **[validado por pesquisa; fontes citadas na conversa]**
- Art. 43: anúncio e site identificam nome e CRO da RT (feito). Falta o número de inscrição da PJ no CRO — depende de registro.
- Art. 44: sem preços, sem "grátis", sem modalidade de pagamento (cumprido).
- Resolução CFO-271/2025 (CADE): descontos/programas de desconto deixaram de ser vedados; desconto percentual é defensável, mas ainda zona cinzenta — manter linguagem sóbria, sem "promoção relâmpago", sem brinde/sorteio.
- Antes e depois: só nos termos da CFO-196/2019 — não usar nos anúncios.

## Riscos e pendências
1. **Registro da PJ no CRO-MT não localizado** — fiscalização pode autuar a clínica e a RT. Confirmar com a Dra. Luana/contador; se não houver, registrar a empresa no CRO-MT antes de escalar mídia.
2. **Verificação do anunciante no Google Ads** (prazo de 30 dias após o aviso) — se não concluída, a conta inteira pausa (Altezza inclusa).
3. **Verificação do Perfil da Empresa no Google (Maps)** — chamado aberto por Rafael; não bloqueia o Ads.
4. **Domínio próprio** — concluído em 09/11 (extremeodonto.com.br, HTTPS forçado, Ads apontando para o domínio novo). Renovação em 08/11/2031, no CPF do Rafael (conta Registro.br RMAOL25).
5. Opcional: rastrear cliques no WhatsApp como conversão (tag no site) para otimizar depois.

## Conversões e medição (12/11/2026)
- Metas da campanha no Google Ads: **específicas da campanha** — Leads de chamada, Contatos (chamadas a partir de anúncios) e Ver rota. Antes usava o padrão da conta (e-commerce da Extreme Truck).
- Ação de conversão criada: **"WhatsApp - Extreme Odonto (site)"** — categoria Contato (site), contagem "Uma", valor padrão R$ 1,00, envio `AW-10880997164/_hWmCJPtq7cdEKyuu8Qo`.
- No site: a tag do Google (`AW-10880997164`) entra em todas as páginas pelo `build.py` (constante `GTAG`, dentro de `head()`), com personalização de anúncios desligada (`allow_ad_personalization_signals: false`) e sem o envio de remarketing no carregamento da página (`send_page_view: false`). Um único ouvinte de clique dispara a conversão em qualquer link `wa.me`/`api.whatsapp.com`. O rodapé legal avisa do uso da tag.
- Não há banner de consentimento de cookies. Se o jurídico pedir, o ponto de alteração é a constante `GTAG`.
- Só conta como conversão no Ads o clique no WhatsApp de quem chegou por um anúncio; clique de visita orgânica não entra.
