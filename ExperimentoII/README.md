# MonitorVotador en Busqueda

### Experimento Arquitectura

Este micorservicio se encarga de recibir una solicitud de consulta que a su vez es procesada por tres microservicios de "MonitorVotador" para posteriormente procesar los resultados.

### Ejecución del experimento

1. Se deben crear tres instacias diferentes del servicio de busqueda [Servicio de Busqueda](https://github.com/nicolay-dev-sp/miso-proyecto-final/tree/main/ExperimentoII/Busqueda) con puertos de escucha diferentes, para el ejemplo se utilizaron los puertos: 8100, 8200, 8300
2. Configurar las variables del archivo app.py (urlServiceOne, urlServiceTwo, urlServiceThree) para que coincidan con las url de los tres microservicios ya desplegados
3. Cargar el archivo de ejecución "HTTP Procesar Busqueda.jmx" en jmeter
4. Ejecutar la operación en jmeter con el botón verde

**Nota:** Para evidenciar los cambios en la disponibilidad del experimento usando las tacticas planteadas, se deben configurar las variables voteTactic y retryHU en "True" en el archivo app.py, reiniciar el servidor y lanzar de nuevo la ejecución en jmeter.

### Táctica de detección de errores por votación y camuflaje por reintentos
