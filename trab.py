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
    "alexandre", "anna_beatriz", "bonfim", "daniel_marcio",
    "eurinardo", "filipe_maciel", "nauber", "osvaldo", "josimeire",
    "marcio_costa", "joao_victor", "pablo", "tatiane", "patricia",
    "alex_lima", "gleison", "gastao", "rosineide", "anderson_feitoza",
    "nilde", "anderson_magno", 'rafael_ivo'
]
dias = [
    "segunda", "terca", "quarta", "quinta", "sexta"
]
semestres = {
    '1': [
        "anna_beatriz-intro_es-es",
        "gleison-mat_bas-es",
        "gastao-mat_bas-cc",
        "anderson_magno-pre_calc-cc",
        "josimeire-etica-es",
        "josimeire-etica-cc",
        "marcio_costa-fup-cc",
        "marcio_costa-fup-es",
        "rafael_ivo-intro_cc-cc"
    ],
    '2': [
        "osvaldo-iprs-es",
        "alex_lima-arq_comp-cc",
        "alex_lima-arq_comp-es",
        "eurinardo-lab_prog-cc",
        "eurinardo-lab_prog-es",
        "anderson_feitoza-discreta-cc",
        "anderson_feitoza-discreta-es",
        "tatiane-ed-cc",
        "tatiane-ed-es",
        "gleison-calc1-cc",
    ],
    '3': [
        "rosineide-prob_est-cc",
        "nilde-prob_est-es",
        "pablo-grafos-es",
        "pablo-grafos-cc",
        "joao_victor-poo-cc",
        "nauber-lp-es",
        "rafael_ivo-lp-cc",
        "joao_victor-poo-es",
        "gastao-algebra_linerar-cc",
        "patricia-req_soft-es",
    ],
    '4': [
        "alexandre-logica-cc",
        "alexandre-logica-es",
        "daniel_siqueira-bd-cc",
        "daniel_siqueira-bd-es",
        "nauber-processos_soft-es",
        "marcio_costa-paa-cces",
        "eurinardo-eda-cc",
    ],
    '5': [
        "osvaldo-aps-cces",
        "patricia-ihc-es",
        "patricia-ihc-cc",
        "joao_victor-pds-es",
        "filipe_maciel-redes-cces",
        "alex_lima-so-cc",
        "rafel_ivo-so-es",
        "patricia-eng-soft-cc",
        "osvaldo-gps-es",
        "daniel_siqueira-comp-grafica-cc",
    ],
    '6': [
        "alex_lima-ia-cc",
        "filipe_maciel-web-cc",
        "filipe_maciel-sd-cc",
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

for p in professores:
    # for d in [dias[0], dias[-1]]:
    seg, sex = dias[0], dias[-1]
    for sem in semestres.keys():
        imp = []
        for ij in semestres[sem]:
            if p in ij:
                if not (f"-{p}_{seg}" in imp):
                    imp.append(f"-{p}_{seg}")
                for h in horarios:
                    if not (f"{ij}_{seg}_{h}" in imp):
                        imp.append(f"{ij}_{seg}_{h}")
        if len(imp) > 0:
            print(' '.join(imp))
        imp = []
        for ij in semestres[sem]:
            if p in ij:
                if not (f"-{p}_{sex}" in imp):
                    imp.append(f"-{p}_{sex}")
                for h in horarios:
                    if not (f"{ij}_{sex}_{h}" in imp):
                        imp.append(f"{ij}_{sex}_{h}")
        if len(imp) > 0:
            print(' '.join(imp))

# Limitação de aulas por semana
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
            print(f"-{ij}_segunda_{h} {ij}_quarta_{h}")
            print(f"-{ij}_quarta_{h} {ij}_sexta_{h}")
            print(f"-{ij}_sexta_{h} {ij}_quarta_{h}")
            print(f"-{ij}_quarta_{h} {ij}_segunda_{h}")
            print(f"-{ij}_terca_{h} {ij}_quinta_{h}")
            print(f"-{ij}_quinta_{h} {ij}_terca_{h}")


# Professor não deve da duas disciplinas no mesmo horarios
for p in professores:
    for d1 in dias:
        for h1 in horarios:
            dis = []
            for semestre in semestres.keys():
                for disciplina in semestres[semestre]:
                    for semestre1 in semestres.keys():
                        for disciplina1 in semestres[semestre1]:
                            if p in disciplina and \
                                p in disciplina1 and \
                                    disciplina != disciplina1 and not \
                                    (f"-{disciplina}_{d1}_{h1}" in dis):
                                dis.append(f"-{disciplina}_{d1}_{h1}")
            if len(dis) > 0:
                print(' '.join(dis))


# disciplinas de cces não podem colidir com nenhuma outra do mesmo semestre
for d1 in dias:
    for h1 in horarios:
        for semestre in semestres.keys():
            for disciplina in semestres[semestre]:
                dis = []
                if 'cces' == disciplina.split('-')[-1]:
                    if not (f"-{disciplina}_{d1}_{h1}" in dis):
                        dis.append(f"-{disciplina}_{d1}_{h1}")
                    for disciplina1 in semestres[semestre]:
                        if not (f"-{disciplina1}_{d1}_{h1}" in dis):
                            dis.append(f"-{disciplina1}_{d1}_{h1}")
                if len(dis) > 0:
                    print(' '.join(dis))

# disciplinas de cc não podem colidir com nenhuma outra do mesmo semestre
for d1 in dias:
    for h1 in horarios:
        for semestre in semestres.keys():
            for disciplina in semestres[semestre]:
                dis = []
                if 'cc' == disciplina.split('-')[-1]:
                    if not (f"-{disciplina}_{d1}_{h1}" in dis):
                        dis.append(f"-{disciplina}_{d1}_{h1}")
                    for disciplina1 in semestres[semestre]:
                        if 'cc' == disciplina1.split('-')[-1] and not \
                           (f"-{disciplina1}_{d1}_{h1}" in dis):
                            dis.append(f"-{disciplina1}_{d1}_{h1}")
                if len(dis) > 0:
                    print(' '.join(dis))


# disciplinas de es não podem colidir com nenhuma outra do mesmo semestre
for d1 in dias:
    for h1 in horarios:
        for semestre in semestres.keys():
            for disciplina in semestres[semestre]:
                dis = []
                if 'es' == disciplina.split('-')[-1]:
                    if not (f"-{disciplina}_{d1}_{h1}" in dis):
                        dis.append(f"-{disciplina}_{d1}_{h1}")
                    for disciplina1 in semestres[semestre]:
                        if 'es' == disciplina1.split('-')[-1] \
                           and not (f"-{disciplina1}_{d1}_{h1}" in dis):
                            dis.append(f"-{disciplina1}_{d1}_{h1}")
                if len(dis) > 0:
                    print(' '.join(dis))


system("./converttoCNF")
