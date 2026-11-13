# -*- coding: utf-8 -*-
# Segundo anuncio (RSA) de cada grupo, com tema diferente do primeiro. Criado em 13/11/2026.
# Regras: titulos <=30, descricoes <=90; descricao da RT fixada na posicao 1 (art. 43 do CEO);
# sem preco, sem "gratis", sem promessa de resultado.
RT = "Resp. técnica: Dra. Luana Alves de Andrade, CRO-MT 11238. Rua dos Cedros, 478, Sala 05."
H = {
"geral": ["Dentista com Hora Certa","Extreme Odontologia Sinop","Dra. Luana Alves CRO-MT 11238","Sua 1ª Consulta sem Pressa","Plano de Tratamento Explicado","Consultório no Jardim Botânico","Agende pelo WhatsApp","Atendimento Individual","Avaliação Antes de Tratar","Você Entende Cada Etapa","Clínica Reservada em Sinop","10% na Primeira Visita","Cuidado do Início ao Fim","Seg a Sex, das 8h às 18h","Marque Sua Avaliação"],
"clareamento": ["Clareamento com Moldeira","Moldeira Feita Sob Medida","Clareamento Dental em Sinop","Extreme Odontologia Sinop","Dra. Luana Alves CRO-MT 11238","Clareie em Casa com Supervisão","Moldeira Feita na Clínica","Gel Clareador Profissional","Acompanhamento da Dentista","Avaliação Antes de Clarear","10% na Primeira Visita","Agende pelo WhatsApp","Sorriso Mais Claro, Natural","Clareamento Supervisionado","Jardim Botânico · Sinop MT"],
"limpeza": ["Check-up e Limpeza Dental","Limpeza Dental em Sinop","Faz Mais de 6 Meses?","Extreme Odontologia Sinop","Dra. Luana Alves CRO-MT 11238","Previna Cárie e Gengivite","Tártaro Não Sai com Escova","Limpeza e Avaliação Completa","Gengiva Sangrando? Avalie","Agende pelo WhatsApp","10% na Primeira Visita","Hora Marcada em Sinop","Orientação de Higiene","Cuidado Preventivo","Jardim Botânico · Sinop MT"],
"canal": ["Canal para Preservar o Dente","Tratamento de Canal em Sinop","Extreme Odontologia Sinop","Dra. Luana Alves CRO-MT 11238","Dor ao Morder ou à Noite?","Canal com Anestesia Eficiente","Antes de Extrair, Avalie","Sensível ao Quente e ao Frio?","Diagnóstico Antes de Tratar","Explicamos Cada Etapa","Agende pelo WhatsApp","10% na Primeira Visita","Endodontia com Hora Marcada","Dente Escurecido? Avalie","Jardim Botânico · Sinop MT"],
}
D = {
"geral": [RT,"Primeira consulta com tempo para ouvir você: avaliação completa e plano bem explicado.","Consultório reservado no Jardim Botânico, em Sinop. Atendimento individual e hora marcada.","Presente de fim de ano: 10% na 1ª visita em limpeza, clareamento ou canal. Até 31/12/2026."],
"clareamento": [RT,"Clareamento supervisionado: moldeira individual feita na clínica e gel profissional.","Avaliação da cor, da gengiva e das restaurações antes de começar. Agende pelo WhatsApp.","Presente de fim de ano: 10% na 1ª visita para clareamento dental. Agende até 31/12/2026."],
"limpeza": [RT,"Faz mais de 6 meses da última limpeza? Agende avaliação e profilaxia com hora marcada.","Remoção de tártaro, polimento e orientação de escovação e fio dental para o seu caso.","Presente de fim de ano: 10% na 1ª visita para limpeza dental. Agende até 31/12/2026."],
"canal": [RT,"O canal trata a dor e busca preservar o dente natural. Avaliação com radiografia.","Dor ao morder, à noite ou sensibilidade que não passa? Agende uma avaliação em Sinop.","Presente de fim de ano: 10% na 1ª visita para tratamento de canal. Agende até 31/12/2026."],
}
if __name__ == "__main__":
    bad = 0
    for g in H:
        assert len(H[g]) == 15 and len(D[g]) == 4 and len(set(H[g])) == 15
        for h in H[g]:
            if len(h) > 30: print("H>30", g, len(h), h); bad += 1
        for d in D[g]:
            if len(d) > 90: print("D>90", g, len(d), d); bad += 1
        print(g, "maxH", max(map(len, H[g])), "maxD", max(map(len, D[g])))
    print("problemas:", bad)
