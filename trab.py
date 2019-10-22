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
disciplinas = [
    "logica-cc", "logica-es", "arq-softw-es", "intro-es-es",
    "qualidade-es", "ppct-cces", "compiladores-cc", 'teoria-cc',
    "lfa-cc", "bd-cc", "bd-es", "comp-grafica-cc", "lab-prog-cc", "lab-prog-es",
    "eda-cc", "web-cc", "sd-cc", "redes-cc", "lp-es", "processos-soft-es", "manutencao-es",
    "iprs-es", "gps-es", "aps-cces", "emp-cces", "etica-es", "etica-cc",
    "paa-cces", "fup-cc", "fup-es", "poo-cc", "poo-es", "vv-es", "pds-es",
    "grafos-es", "grafos-cc", "mat-comp-cc", "ed-cc", "ed-es",
    "req-soft-es", "eng-soft-es", "ihc-es", "ihc-cc", "so-cc", "ia-cc",
    "arq-comp-cc", "arq-comp-es", "mat-bas-es", "calc1-cc", "mat-bas-cc",
    "prob-est-cc", "discreta-cc", "discreta-es", "prob-est-es", "pre-calc-cc"
]
horarios = [
    'h1', 'h2', 'h3', 'h4'
]

for i in professores:
    print(" ".join([f"{i}_{j}" for j in [dias[0], dias[-1]]]))
    print(" ".join([f"-{i}_{j}" for j in [dias[0], dias[-1]]]))

for i in disciplinas:
    for j in dias:
        for k in horarios:
            print(f"{i}_{j}_{k}")

system("./converttoCNF")
