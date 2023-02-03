FROM google/cloud-sdk:emulators

EXPOSE 8085

ADD ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

VOLUME /opt/data

ENTRYPOINT [ "./entrypoint.sh" ]