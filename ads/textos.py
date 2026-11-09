# -*- coding: utf-8 -*-
H = {
"geral": ["Extreme Odontologia Sinop","Dentista em Sinop","Clínica Odontológica em Sinop","Dra. Luana Alves CRO-MT 11238","Agende pelo WhatsApp","Atendimento com Hora Marcada","Planejamento Digital","10% na Primeira Visita","Jardim Botânico · Sinop MT","Limpeza, Clareamento e Canal","Odontologia de Alto Padrão","Avaliação Completa e Clara","Seg a Sex, das 8h às 18h","Presente de Fim de Ano","Transparência em Cada Etapa"],
"clareamento": ["Clareamento Dental em Sinop","Clareamento Profissional","10% na Primeira Visita","Extreme Odontologia Sinop","Dra. Luana Alves CRO-MT 11238","Consultório ou Supervisionado","Com Proteção da Gengiva","Avaliação Antes de Clarear","Resultado Natural e Seguro","Agende pelo WhatsApp","Jardim Botânico · Sinop MT","Presente de Fim de Ano","Hora Marcada, Sem Espera","Sorriso Mais Claro em Sinop","Clareamento com Acompanhamento"],
"limpeza": ["Limpeza Dental em Sinop","Profilaxia Profissional","10% na Primeira Visita","Extreme Odontologia Sinop","Dra. Luana Alves CRO-MT 11238","Remoção de Tártaro e Manchas","Limpeza com Ultrassom","Gengiva Saudável, Hálito Puro","Agende pelo WhatsApp","Hora Marcada, Sem Espera","Jardim Botânico · Sinop MT","Presente de Fim de Ano","Avaliação Completa Inclusa","Prevenção que Evita Gastos","Seg a Sex, das 8h às 18h"],
"canal": ["Tratamento de Canal em Sinop","Dor de Dente? Agende Hoje","Endodontia em Sinop","Extreme Odontologia Sinop","Dra. Luana Alves CRO-MT 11238","Anestesia Eficiente","Preserve o Seu Dente","10% na Primeira Visita","Agende pelo WhatsApp","Encaixe para Urgência","Técnica Atual e Segura","Jardim Botânico · Sinop MT","Diagnóstico com Radiografia","Hora Marcada, Sem Espera","Presente de Fim de Ano"],
}
D = {
"geral": ["Clínica odontológica de alto padrão em Sinop. Avaliação completa, plano claro, hora certa.",
          "Resp. técnica: Dra. Luana Alves de Andrade, CRO-MT 11238. Rua dos Cedros, 478, Sala 05.",
          "Presente de fim de ano: 10% na 1ª visita em limpeza, clareamento ou canal. Até 31/12/2026.",
          "Limpeza, clareamento, canal, facetas e reabilitação com planejamento digital. Agende já."],
"clareamento": ["Clareamento dental profissional em Sinop, com avaliação prévia e proteção da gengiva.",
          "Resp. técnica: Dra. Luana Alves de Andrade, CRO-MT 11238. Rua dos Cedros, 478, Sala 05.",
          "Presente de fim de ano: 10% na 1ª visita para clareamento dental. Agende até 31/12/2026.",
          "Protocolo de consultório ou supervisionado em casa. Resultado natural. Agende no WhatsApp."],
"limpeza": ["Limpeza dental profissional em Sinop: tártaro, manchas e orientação de higiene. 1 sessão.",
          "Resp. técnica: Dra. Luana Alves de Andrade, CRO-MT 11238. Rua dos Cedros, 478, Sala 05.",
          "Presente de fim de ano: 10% na 1ª visita para limpeza dental. Agende até 31/12/2026.",
          "Ultrassom, polimento e avaliação completa, com hora marcada. Agende pelo WhatsApp."],
"canal": ["Tratamento de canal em Sinop com anestesia eficiente e técnica atual. Saia da dor hoje.",
          "Resp. técnica: Dra. Luana Alves de Andrade, CRO-MT 11238. Rua dos Cedros, 478, Sala 05.",
          "Presente de fim de ano: 10% na 1ª visita para tratamento de canal. Agende até 31/12/2026.",
          "Diagnóstico com radiografia, isolamento absoluto e restauração definitiva. Agende já."],
}
bad=0
for g in H:
    for h in H[g]:
        if len(h)>30: print("H>30",g,len(h),h); bad+=1
    for d in D[g]:
        if len(d)>90: print("D>90",g,len(d),d); bad+=1
    print(g, len(H[g]), "headlines", len(D[g]), "descriptions", "maxH", max(map(len,H[g])), "maxD", max(map(len,D[g])))
print("problemas:",bad)
