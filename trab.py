"""."""
from os import system
from itertools import combinations


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
        "anna_beatriz__intro_es__es",
        "gleison__mat_bas__es",
        "gastao__mat_bas__cc",
        "josimeire__etica__es",
        "josimeire__etica__cc",
        "marcio_costa__fup__cc",
        "marcio_costa__fup__es",
        "rafael_ivo__intro_cc__cc"
    ],
    '2': [
        "osvaldo__iprs__es",
        "alex_lima__arq_comp__cc",
        "alex_lima__arq_comp__es",
        "eurinardo__lab_prog__cc",
        "eurinardo__lab_prog__es",
        "anderson_feitoza__discreta__cc",
        "anderson_feitoza__discreta__es",
        "tatiane__ed__cc",
        "tatiane__ed__es",
        "gleison__calc1__cc",
    ],
    '3': [
        "rosineide__prob_est__cc",
        "nilde__prob_est__es",
        "pablo__grafos__es",
        "pablo__grafos__cc",
        "joao_victor__poo__cc",
        "nauber__lp__es",
        "rafael_ivo__lp__cc",
        "joao_victor__poo__es",
        "gastao__algebra_linerar__cc",
        "patricia__req_soft__es",
    ],
    '4': [
        "alexandre__logica__cc",
        "alexandre__logica__es",
        "daniel_siqueira__bd__cc",
        "daniel_siqueira__bd__es",
        "nauber__processos_soft__es",
        "marcio_costa__paa__cces",
        "eurinardo__eda__cc",
        "osvaldo__aps__cces",
    ],
    '5': [
        "osvaldo__aps__cces",
        "patricia__ihc__es",
        "patricia__ihc__cc",
        "joao_victor__pds__es",
        "filipe_maciel__redes__cces",
        "alex_lima__so__cc",
        "rafel_ivo__so__es",
        "patricia__eng__soft__cc",
        "osvaldo__gps__es",
        "daniel_siqueira__comp__grafica__cc",
    ],
    '6': [
        "alex_lima__ia__cc",
        "filipe_maciel__web__cc",
        "filipe_maciel__sd__cc",
        "anna_beatriz__arq__softw__es",
        "joao_victor__vv__es",
        "anna_beatriz__qualidade__es",
        "bonfim__lfa__cc",
        "nauber__manutencao__es",
        "tatiane__mat__comp__cc",
    ],
    '7': [
        "josimeire__emp__cces",
        "bonfim__compiladores__cc",
        'bonfim__teoria__cc',
    ],
}
dis1cred = {
    '1': [
        "anderson_magno__pre_calc__cc",
    ],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [
        "anna_beatriz__ppct__cces",
    ]
}
horarios = [
    'h1', 'h2', 'h3', 'h4'
]
# semestres = {
#     '1': [
#         "anna_beatriz__intro_es__es",
#     ]
# }

# Professor dar aula segunda ou sexta
for i in professores:
    print(" ".join([f"{i}_{j}" for j in [dias[0], dias[-1]]]))
    print(" ".join([f"-{i}_{j}" for j in [dias[0], dias[-1]]]))

for p in professores:
    seg, sex = dias[0], dias[-1]
    imp = []
    imp2 = []
    for sem in semestres.keys():
        for ij in semestres[sem] + dis1cred[sem]:
            if p in ij:
                if not (f"-{p}_{seg}" in imp):
                    imp.append(f"-{p}_{seg}")
                    imp2.append(f"-{p}_{seg}")
                for h in horarios:
                    if not (f"{ij}_{seg}_{h}" in imp):
                        imp.append(f"{ij}_{seg}_{h}")
                        imp2.append(f"-{ij}_{sex}_{h}")
    if len(imp) > 0:
        print(' '.join(imp))
    # if len(imp2) > 0:
    #     print(' '.join(imp2))
    imp = []
    imp2 = []
    for sem in semestres.keys():
        for ij in semestres[sem] + dis1cred[sem]:
            if p in ij:
                if not (f"-{p}_{sex}" in imp):
                    imp.append(f"-{p}_{sex}")
                    imp2.append(f"-{p}_{sex}")
                for h in horarios:
                    if not (f"{ij}_{sex}_{h}" in imp):
                        imp.append(f"{ij}_{sex}_{h}")
                        imp2.append(f"-{ij}_{seg}_{h}")
    if len(imp) > 0:
        print(' '.join(imp))
    # if len(imp2) > 0:
    #     print(' '.join(imp2))

# Limitação de aulas por semana
for i in semestres.keys():
    for ij in semestres[i] + dis1cred[i]:
        # No minimo uma aula por semana
        for j in dias:
            for k in horarios:
                print(f"{ij}_{j}_{k}", end=" ")
        print()

for i in semestres.keys():
    for ij in semestres[i]:
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
        # Duas Aulas

for i in dis1cred.keys():
    for ij in dis1cred[i]:
        todos = []
        for d1 in dias:
            for h1 in horarios:
                todos.append(f"{ij}_{d1}_{h1}")
        comb = list(combinations(todos, 2))
        # print(comb)
        for i in comb:
            aula = []
            for j in i:
                aula.append("-" + j)
            print(" ".join(aula))

for i in semestres.keys():
    for ij in semestres[i]:
        todos = []
        for d1 in dias:
            for h1 in horarios:
                todos.append(f"{ij}_{d1}_{h1}")
        comb = list(combinations(todos, 3))
        # print(comb)
        for i in comb:
            aula = []
            for j in i:
                aula.append("-" + j)
            print(" ".join(aula))
        # for i in comb:
        #     ll = []
        #     for j in todos:
        #         if j == i[0]:
        #             ll.append("-" + i[0])
        #         elif j == i[1]:
        #             ll.append("-" + i[1])
        #         else:
        #             ll.append(j)
        #     print(' '.join(ll))

# Emparelhamento de aulas
for i in semestres.keys():
    for ij in semestres[i]:
        for h in horarios:
            print(f"-{ij}_segunda_{h} {ij}_quarta_{h}")
            print(f"-{ij}_quarta_{h} {ij}_segunda_{h} {ij}_sexta_{h}")
            print(f"-{ij}_sexta_{h} {ij}_quarta_{h}")
            # print(f"-{ij}_quarta_{h} {ij}_segunda_{h}")
            print(f"-{ij}_terca_{h} {ij}_quinta_{h}")
            print(f"-{ij}_quinta_{h} {ij}_terca_{h}")


# Professor não deve da duas disciplinas no mesmo horarios
# Combinar cada disciplina de cada professor duas a duas
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
                for i in list(combinations(dis, 2)):
                    print(' '.join(i))


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
                    for i in list(combinations(dis, 2)):
                        print(' '.join(i))

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
                    for i in list(combinations(dis, 2)):
                        print(' '.join(i))


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
                    for i in list(combinations(dis, 2)):
                        print(' '.join(i))


system("./converttoCNF")
