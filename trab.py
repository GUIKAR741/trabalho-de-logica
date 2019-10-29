"""."""
from os import system


def escreve_arquivo(*args, **kwargs):
    """."""
    with open("entrada.txt", "a+") as arq:
        if "file" in kwargs.keys():
            del kwargs['file']
        print_original(*args, file=arq, **kwargs)


open("entrada.txt", "w").close()
print_original = print
print = escreve_arquivo

professores = [
    "alexandre", "anna-beatriz", "bonfim", "daniel-marcio",
    "eurinardo", "filipe-maciel", "nauber", "osvaldo", "josimeire",
    "marcio-costa", "joao-victor", "pablo", "tatiane", "patricia",
    "alex-lima", "gleison", "gastao", "rosineide", "anderson-feitoza",
    "nilde", "anderson-magno"
]
dias = [
    "segunda", "terca", "quarta", "quinta", "sexta"
]
semestres = {
    '1': [
        "anna_beatriz-intro-es-es",
        "gleison-mat-bas-es",
        "gastao-mat-bas-cc",
        "anderson_magno-pre-calc-cc",
        "josimeire-etica-es",
        "josimeire-etica-cc",
        "marcio-fup-cc",
        "marcio-fup-es"
    ],
    '2': [
        "osvaldo-iprs-es",
        "alex-arq-comp-cc",
        "alex-arq-comp-es",
        "eurinardo-lab-prog-cc",
        "eurinardo-lab-prog-es",
        "anderson_feitoza-discreta-cc",
        "anderson_feitoza-discreta-es",
        "tatiane-ed-cc",
        "tatiane-ed-es",
        "gleison-calc1-cc",
    ],
    '3': [
        "rosineide-prob-est-cc",
        "nilde-prob-est-es",
        "pablo-grafos-es",
        "pablo-grafos-cc",
        "joao_victor-poo-cc",
        "nauber-lp-es",
        "joao_victor-poo-es",
        "gastao-algebra-linerar-cc",
        "patricia-req-soft-es",
    ],
    '4': [
        "alexandre_logica-cc",
        "alexandre_logica-es",
        "daniel_siqueira-bd-cc",
        "daniel_siqueira-bd-es",
        "nauber-processos-soft-es",
        "marcio-paa-cces",
        "eurinardo-eda-cc",
    ],
    '5': [
        "osvaldo-aps-cces",
        "patricia-ihc-es",
        "patricia-ihc-cc",
        "joao_victor-pds-es",
        "filipe-redes-cc",
        "alex-so-cc",
        "patricia-eng-soft-es",
        "osvaldo-gps-es",
        "daniel_siqueira-comp-grafica-cc",
    ],
    '6': [
        "alex-ia-cc",
        "filipe-web-cc",
        "filipe-sd-cc",
        "anna_beatriz-arq-softw-es",
        "joao_victor-vv-es",
        "anna_beatriz-qualidade-es",
        "bonfim-lfa-cc",
        "nauber-manutencao-es",
        "tatiane-mat-comp-cc",
    ],
    '7': [
        "anna_beatriz-ppct-cces",
        "josimeire-emp-cces",
        "bonfim-compiladores-cc",
        'bonfim-teoria-cc',
    ],
}
horarios = [
    'h1', 'h2', 'h3', 'h4'
]

# Professor dar aula segunda ou sexta
for i in professores:
    print(" ".join([f"{i}_{j}" for j in [dias[0], dias[-1]]]))
    print(" ".join([f"-{i}_{j}" for j in [dias[0], dias[-1]]]))

for i in professores:
    for sem in semestres.keys():
        for ij in semestres[sem]:
            if i in ij:
                for d in [dias[0], dias[-1]]:
                    print(f"-{i}_{d}", end=' ')
                    for h in horarios:
                        print(f"{ij}_{d}_{h}", end=' ')
                    print()

for i in semestres.keys():
    for ij in semestres[i]:
        # No minimo uma aula por semana
        for j in dias:
            for k in horarios:
                print(f"{ij}_{j}_{k}", end=" ")
        print()
        # Duas Aulas por semana
        for d1 in dias:
            for h1 in horarios:
                for d2 in dias:
                    for h2 in horarios:
                        if d1 == d2 and h1 == h2:
                            print(f"-{ij}_{d2}_{h2}", end=" ")
                        else:
                            print(f"{ij}_{d2}_{h2}", end=" ")
                print()

# Emparelhamento de aulas
for i in semestres.keys():
    for ij in semestres[i]:
        for h in horarios:
            # for d in dias:
            print(f"-{ij}_segunda_{h} {ij}_quarta_{h}")
            print(f"-{ij}_quarta_{h} {ij}_sexta_{h}")
            print(f"-{ij}_sexta_{h} {ij}_quarta_{h}")
            print(f"-{ij}_quarta_{h} {ij}_segunda_{h}")
            print(f"-{ij}_terca_{h} {ij}_quinta_{h}")
            print(f"-{ij}_quinta_{h} {ij}_terca_{h}")
            # print(f"-{ij}_segunda_{h} {ij}_quarta_{h}")


system("./converttoCNF")
