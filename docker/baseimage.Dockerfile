FROM python:3.10

ARG USER_ID
ARG GROUP_ID

ARG PACKAGE
ENV PACKAGE=${PACKAGE:-'ml_service-0.3.0-py3-none-any.whl'}

ARG MODEL_FILE_PATH
ENV MODEL_FILE_PATH=${MODEL_FILE_PATH:-'/model/heart_model.pkl'}

ARG DATA_FILE_PATH
ENV DATA_FILE_PATH=${DATA_FILE_PATH:-'/data/heart.csv'}


ADD ../scripts /scripts
ADD ../dist /tmp/dist
RUN pip install /tmp/dist/${PACKAGE} && \
if [ ${USER_ID:-0} -ne 0 ] && [ ${GROUP_ID:-0} -ne 0 ]; then \
    groupadd -g ${GROUP_ID} genmodel &&\
    useradd -l -u ${USER_ID} -g genmodel genmodel \
;fi

USER genmodel
WORKDIR /scripts

