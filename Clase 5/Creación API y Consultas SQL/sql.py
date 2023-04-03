selectPersona="select * from persona ORDER BY id_persona"

consulta1=str("select hospital.nombre as NOMBRE, hospital.direccion as DIRECCION, count(*) as CANTIDAD\n"+
"from defuncion left join hospital on\n"+
"defuncion.id_hospital=hospital.id_hospital\n"+
"group by hospital.nombre, hospital.direccion\n"+
"order by cantidad desc")