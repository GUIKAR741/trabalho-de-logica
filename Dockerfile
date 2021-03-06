FROM python:3.7

RUN wget https://www.labri.fr/perso/lsimon/downloads/softwares/glucose-syrup-4.1.tgz && \
    tar -xvzf glucose-syrup-4.1.tgz && \
    cd glucose-syrup-4.1/simp && make rs

ENV PATH=$PATH:/glucose-syrup-4.1/simp/

WORKDIR /usr/src/app

CMD [ "/bin/sh" ]