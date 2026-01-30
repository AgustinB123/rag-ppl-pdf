/*
Script creado por el issue #1460:https://trello.com/c/VyzvCLPI/1460-ingresar-motivo-de-la-accion-tanto-en-alta-baja-como-en-modificaci%C3%B3n-en-abms
La implementacion de este script habilita la posibilidad de agregar observaciones a las modificaciones
hechas en registros de abms que sean supervisados.
*/
ALTER TABLE dbo.TEMPORALES ADD Observacion VARCHAR (200)