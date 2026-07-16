const RECLAMOS_DATA = [
  {
    "id": "r1",
    "categoria": "Limpieza Pública",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "Santiago de Surco",
    "fecha": "2023-06-08",
    "texto": "Reclamo por \"Mejora de barrido\", Santiago de Surco, urb. Higuereta — Av. El Polo cdra. 45, a media cuadra de Av. Ayacucho."
  },
  {
    "id": "r2",
    "categoria": "Limpieza Pública",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "Villa María del Triunfo",
    "fecha": "2023-05-15",
    "texto": "Reclamo por \"Vaciado de tacho de basura\", Villa María del Triunfo, urb. César Vallejo — Av. El Triunfo cdra. 7, a media cuadra de Av. Pachacútec."
  },
  {
    "id": "r3",
    "categoria": "Limpieza Pública",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "Santiago de Surco",
    "fecha": "2023-09-12",
    "texto": "Reclamo por \"Vaciado de contenedor\", Santiago de Surco, urb. Sagitario — Ca. Monte Bello cdra. 45, frente al colegio de la zona."
  },
  {
    "id": "r4",
    "categoria": "Limpieza Pública",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "San Juan de Lurigancho",
    "fecha": "2023-11-24",
    "texto": "Reclamo por \"Punto Verde cerrado en horario de atención\", San Juan de Lurigancho, urb. Bayóvar — Av. El Sol de Zárate 1802."
  },
  {
    "id": "r5",
    "categoria": "Limpieza Pública",
    "tipo": "Denuncia",
    "estado": "Derivado",
    "distrito": "Pachacámac",
    "fecha": "2023-11-28",
    "texto": "Denuncia por \"Irregularidades en la disposición de residuos de establecimientos\", Pachacámac, urb. José Gálvez de Pachacámac — Av. Manchay cdra. 5, a media cuadra de Ca. Los Álamos de Manchay."
  },
  {
    "id": "r6",
    "categoria": "Limpieza Pública",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "San Miguel",
    "fecha": "2023-04-12",
    "texto": "Denuncia por \"Acopio de recuperadores urbanos en espacio público\", San Miguel, urb. Maranga — Av. La Paz cdra. 17, cruce con Av. Universitaria."
  },
  {
    "id": "r7",
    "categoria": "Limpieza Pública",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "San Isidro",
    "fecha": "2023-09-11",
    "texto": "Denuncia por \"Instalación de Campana Verde\", San Isidro, urb. Corpac — Ca. Miguel Dasso cdra. 36, a la altura del grifo."
  },
  {
    "id": "r8",
    "categoria": "Limpieza Pública",
    "tipo": "Denuncia",
    "estado": "En proceso",
    "distrito": "Ate",
    "fecha": "2023-12-15",
    "texto": "Denuncia por \"Vereda sucia por mascotas\", Ate, urb. Valdiviezo — Av. Metropolitana cdra. 44, cruce con Av. Prolongación Javier Prado."
  },
  {
    "id": "r9",
    "categoria": "Limpieza Pública",
    "tipo": "Denuncia",
    "estado": "En proceso",
    "distrito": "Villa El Salvador",
    "fecha": "2023-08-11",
    "texto": "Denuncia por \"Irregularidades en la separación de residuos en origen\", Villa El Salvador, urb. Parque Industrial — Av. El Sol 5672."
  },
  {
    "id": "r10",
    "categoria": "Limpieza Pública",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "Carabayllo",
    "fecha": "2023-06-22",
    "texto": "Denuncia por \"Recuperador urbano acopiando residuos en zona no prevista\", Carabayllo, urb. El Progreso — Av. Camino Real de Carabayllo 42."
  },
  {
    "id": "r11",
    "categoria": "Tránsito/Transporte",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "San Miguel",
    "fecha": "2023-12-06",
    "texto": "Reclamo por \"Problemas con obras de bacheo\", San Miguel, urb. Miramar de San Miguel — Av. La Marina cdra. 11, frente al mercado del barrio."
  },
  {
    "id": "r12",
    "categoria": "Tránsito/Transporte",
    "tipo": "Reclamo",
    "estado": "Ingresado",
    "distrito": "La Molina",
    "fecha": "2023-11-17",
    "texto": "Reclamo por \"Inconvenientes con el retiro/devolución de la bicicleta de BA Ecobici por Tembici\", La Molina, urb. Santa Patricia."
  },
  {
    "id": "r13",
    "categoria": "Tránsito/Transporte",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "Puente Piedra",
    "fecha": "2023-06-03",
    "texto": "Reclamo por \"Mapas y carteles de orientación en estaciones y/o accesos - SUBTE\", Puente Piedra, urb. La Ensenada."
  },
  {
    "id": "r14",
    "categoria": "Tránsito/Transporte",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "Puente Piedra",
    "fecha": "2023-05-24",
    "texto": "Reclamo por \"Medios de pago - SUBTE\", Puente Piedra, urb. Laderas de Chillón."
  },
  {
    "id": "r15",
    "categoria": "Tránsito/Transporte",
    "tipo": "Reclamo",
    "estado": "Ingresado",
    "distrito": "Carabayllo",
    "fecha": "2023-08-30",
    "texto": "Reclamo por \"Restos de obra en vereda que impiden el paso\", Carabayllo, urb. Lucyana — Av. Túpac Amaru 35."
  },
  {
    "id": "r16",
    "categoria": "Tránsito/Transporte",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "Carabayllo",
    "fecha": "2023-11-10",
    "texto": "Reclamo por \"Inconvenientes con el personal - SUBTE\", Carabayllo, urb. El Progreso."
  },
  {
    "id": "r17",
    "categoria": "Tránsito/Transporte",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "Santiago de Surco",
    "fecha": "2023-07-04",
    "texto": "Reclamo por \"Funcionamiento / mantenimiento de escaleras mecánicas - SUBTE\", Santiago de Surco, urb. La Capullana."
  },
  {
    "id": "r18",
    "categoria": "Tránsito/Transporte",
    "tipo": "Reclamo",
    "estado": "Ingresado",
    "distrito": "Los Olivos",
    "fecha": "2023-03-09",
    "texto": "Reclamo por \"Funcionamiento y mantenimiento de ascensores - SUBTE\", Los Olivos, urb. Villa Sol."
  },
  {
    "id": "r19",
    "categoria": "Tránsito/Transporte",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "San Juan de Lurigancho",
    "fecha": "2023-02-09",
    "texto": "Reclamo por \"Altas - bajas temperaturas - SUBTE\", San Juan de Lurigancho, urb. Huáscar — Av. Gran Chimú 3099."
  },
  {
    "id": "r20",
    "categoria": "Tránsito/Transporte",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "San Juan de Lurigancho",
    "fecha": "2023-01-24",
    "texto": "Reclamo por \"Pases y abonos - SUBTE\", San Juan de Lurigancho, urb. Zárate."
  },
  {
    "id": "r21",
    "categoria": "Otros",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "San Martín de Porres",
    "fecha": "2023-11-05",
    "texto": "Reclamo por \"Propuestas para la mejora en trámites\", San Martín de Porres, urb. Infantas — Jr. Huandoy 927."
  },
  {
    "id": "r22",
    "categoria": "Otros",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "San Juan de Lurigancho",
    "fecha": "2023-09-15",
    "texto": "Reclamo por \"Intervención por calle anegada/inundada\", San Juan de Lurigancho, urb. Campoy — Av. Fernando Wiesse 2407."
  },
  {
    "id": "r23",
    "categoria": "Otros",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "Santa Anita",
    "fecha": "2023-05-12",
    "texto": "Reclamo por \"Inconvenientes con la obtención de un turno en Centro de Salud u Hospital Público\", Santa Anita, urb. Cooperativa Universal."
  },
  {
    "id": "r24",
    "categoria": "Otros",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "San Borja",
    "fecha": "2023-01-20",
    "texto": "Reclamo por \"Inconvenientes con trámites\", San Borja, urb. Torres de Limatambo — Av. San Borja Norte 3320."
  },
  {
    "id": "r25",
    "categoria": "Otros",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "Carabayllo",
    "fecha": "2023-11-23",
    "texto": "Reclamo por \"Felicitación/agradecimiento\", Carabayllo, urb. Lucyana — Av. Túpac Amaru 3086."
  },
  {
    "id": "r26",
    "categoria": "Otros",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "San Juan de Miraflores",
    "fecha": "2023-05-12",
    "texto": "Reclamo por \"Inconvenientes con la atención en Centro de Salud u Hospital Público\", San Juan de Miraflores, urb. Pamplona Alta."
  },
  {
    "id": "r27",
    "categoria": "Otros",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "Carabayllo",
    "fecha": "2023-12-09",
    "texto": "Denuncia por \"Ocupación indebida de la vereda/calzada por área gastronómica\", Carabayllo, urb. Lucyana — Av. Camino Real de Carabayllo cdra. 11, a media cuadra de Av. Túpac Amaru."
  },
  {
    "id": "r28",
    "categoria": "Otros",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "Lurín",
    "fecha": "2023-04-23",
    "texto": "Denuncia por \"Obstrucción de calle o vereda por elementos fijos o móviles\", Lurín, urb. Julio C. Tello — Antigua Panamericana Sur cdra. 3, espalda del centro de salud."
  },
  {
    "id": "r29",
    "categoria": "Otros",
    "tipo": "Denuncia",
    "estado": "Derivado",
    "distrito": "Carabayllo",
    "fecha": "2023-03-28",
    "texto": "Denuncia por \"Criaderos de mosquitos\", Carabayllo, urb. El Progreso — Av. Universitaria Norte cdra. 36, al costado del parque zonal."
  },
  {
    "id": "r30",
    "categoria": "Otros",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "Comas",
    "fecha": "2023-05-29",
    "texto": "Denuncia por \"Ocupación indebida por mantero o vendedor ambulante\", Comas, urb. Collique — Av. Universitaria cdra. 5, al costado del parque zonal."
  },
  {
    "id": "r31",
    "categoria": "Áreas Verdes",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "San Luis",
    "fecha": "2023-02-22",
    "texto": "Reclamo por \"Problemas con intervenciones de arbolado\", San Luis, urb. Túpac Amaru de San Luis — Jr. Las Moreras cdra. 39, cerca a la comisaría del sector."
  },
  {
    "id": "r32",
    "categoria": "Áreas Verdes",
    "tipo": "Reclamo",
    "estado": "Cerrado",
    "distrito": "San Martín de Porres",
    "fecha": "2023-02-05",
    "texto": "Reclamo por \"Inconvenientes con las tareas de guardián de plaza\", San Martín de Porres, urb. Santa Luisa."
  },
  {
    "id": "r33",
    "categoria": "Áreas Verdes",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "Chorrillos",
    "fecha": "2023-02-25",
    "texto": "Denuncia por \"Árbol con enfermedades\", Chorrillos, urb. Los Cedros de Villa — Av. Guardia Civil 4681."
  },
  {
    "id": "r34",
    "categoria": "Áreas Verdes",
    "tipo": "Solicitud",
    "estado": "Derivado",
    "distrito": "San Juan de Miraflores",
    "fecha": "2023-12-06",
    "texto": "Solicitud de \"Falta de recolección de restos de poda de arbolado público\", San Juan de Miraflores, urb. María Auxiliadora — Ca. Las Turquesas cdra. 33, frente al colegio de la zona."
  },
  {
    "id": "r35",
    "categoria": "Áreas Verdes",
    "tipo": "Solicitud",
    "estado": "Ingresado",
    "distrito": "El Agustino",
    "fecha": "2023-03-22",
    "texto": "Solicitud de \"Poda de árbol/despeje de luminaria o semáforo\", El Agustino, urb. Santoyo — Jr. Ancash Este cdra. 2, espalda del centro de salud."
  },
  {
    "id": "r36",
    "categoria": "Áreas Verdes",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "Cieneguilla",
    "fecha": "2023-09-11",
    "texto": "Solicitud de \"Extracción de árbol\", Cieneguilla, urb. La Libertad — Ca. Los Eucaliptos cdra. 25, frente al colegio de la zona."
  },
  {
    "id": "r37",
    "categoria": "Áreas Verdes",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "Carabayllo",
    "fecha": "2023-05-02",
    "texto": "Solicitud de \"Plantación de árbol\", Carabayllo, urb. El Progreso — Av. Túpac Amaru 2812."
  },
  {
    "id": "r38",
    "categoria": "Áreas Verdes",
    "tipo": "Solicitud",
    "estado": "Derivado",
    "distrito": "San Martín de Porres",
    "fecha": "2023-01-16",
    "texto": "Solicitud de \"Instalación de bebederos en parque/plaza\", San Martín de Porres, urb. Santa Luisa — Av. Canta Callao 3334."
  },
  {
    "id": "r39",
    "categoria": "Áreas Verdes",
    "tipo": "Solicitud",
    "estado": "En proceso",
    "distrito": "Independencia",
    "fecha": "2023-06-02",
    "texto": "Solicitud de \"Mantenimiento de senderos de parque/plaza\", Independencia, urb. Tahuantinsuyo."
  },
  {
    "id": "r40",
    "categoria": "Áreas Verdes",
    "tipo": "Solicitud",
    "estado": "Ingresado",
    "distrito": "Santa Anita",
    "fecha": "2023-08-23",
    "texto": "Solicitud de \"Instalación de caniles en parque/plaza\", Santa Anita, urb. Viña San Francisco."
  },
  {
    "id": "r41",
    "categoria": "Alumbrado Público",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "Villa María del Triunfo",
    "fecha": "2023-07-27",
    "texto": "Solicitud de \"Mayor iluminación en calle / plaza\", Villa María del Triunfo, urb. San Francisco de la Tablada — Av. Pachacútec cdra. 10, al costado del parque zonal."
  },
  {
    "id": "r42",
    "categoria": "Alumbrado Público",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "Ate",
    "fecha": "2023-07-03",
    "texto": "Solicitud de \"Reparación de luminaria apagada durante la noche\", Ate, urb. Huaycán — Av. La Molina cdra. 40, a la altura del grifo."
  },
  {
    "id": "r43",
    "categoria": "Alumbrado Público",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "Santiago de Surco",
    "fecha": "2023-08-29",
    "texto": "Solicitud de \"Reparación de luminaria por artefacto roto\", Santiago de Surco, urb. Valle Hermoso — Av. Ayacucho cdra. 30, espalda del centro de salud."
  },
  {
    "id": "r44",
    "categoria": "Alumbrado Público",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "Rímac",
    "fecha": "2023-05-08",
    "texto": "Solicitud de \"Reparación de tapa faltante / deteriorada en columna de alumbrado\", Rímac, urb. Villacampa — Av. Alcázar 2230."
  },
  {
    "id": "r45",
    "categoria": "Alumbrado Público",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "San Juan de Lurigancho",
    "fecha": "2023-01-25",
    "texto": "Solicitud de \"Limpieza de artefacto de alumbrado\", San Juan de Lurigancho, urb. Huáscar — Av. Canto Grande 1356."
  },
  {
    "id": "r46",
    "categoria": "Alumbrado Público",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "Los Olivos",
    "fecha": "2023-02-24",
    "texto": "Solicitud de \"Luminaria intermitente\", Los Olivos, urb. Pro — Av. Las Palmeras 6368."
  },
  {
    "id": "r47",
    "categoria": "Alumbrado Público",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "Cercado de Lima",
    "fecha": "2023-10-27",
    "texto": "Solicitud de \"Reparación de luminaria encendida durante el día\", Cercado de Lima, urb. Santa Beatriz — Av. Alfonso Ugarte 2060."
  },
  {
    "id": "r48",
    "categoria": "Alumbrado Público",
    "tipo": "Solicitud",
    "estado": "Ingresado",
    "distrito": "Chorrillos",
    "fecha": "2023-03-30",
    "texto": "Solicitud de \"Reparación de toma de energía de alumbrado público\", Chorrillos, urb. Túpac Amaru — Av. Guardia Civil 1884."
  },
  {
    "id": "r49",
    "categoria": "Alumbrado Público",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "San Martín de Porres",
    "fecha": "2023-06-05",
    "texto": "Solicitud de \"Mayor iluminación en calle / plaza\", San Martín de Porres, urb. Condevilla — Jr. Huandoy cdra. 25, frente al colegio de la zona."
  },
  {
    "id": "r50",
    "categoria": "Alumbrado Público",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "Cercado de Lima",
    "fecha": "2023-04-27",
    "texto": "Solicitud de \"Reparación de luminaria apagada durante la noche\", Cercado de Lima, urb. Palomino — Jr. Camaná cdra. 28, frente a la losa deportiva."
  },
  {
    "id": "r51",
    "categoria": "Seguridad Ciudadana (Serenazgo)",
    "tipo": "Denuncia",
    "estado": "En proceso",
    "distrito": "San Martín de Porres",
    "fecha": "2023-05-26",
    "texto": "Denuncia por \"Cuidacoches (Trapitos)\", San Martín de Porres, urb. Condevilla — Av. Perú cdra. 38, cruce con Av. Canta Callao."
  },
  {
    "id": "r52",
    "categoria": "Seguridad Ciudadana (Serenazgo)",
    "tipo": "Denuncia",
    "estado": "Derivado",
    "distrito": "San Martín de Porres",
    "fecha": "2023-03-31",
    "texto": "Denuncia por \"Denuncia rechazada en Comisaría\", San Martín de Porres, urb. Naranjal — Jr. Huandoy 3378."
  },
  {
    "id": "r53",
    "categoria": "Seguridad Ciudadana (Serenazgo)",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "Ate",
    "fecha": "2023-01-01",
    "texto": "Solicitud de \"Mayor presencia policial\", Ate, urb. Ceres — Av. José Carlos Mariátegui cdra. 14, cerca a la comisaría del sector."
  },
  {
    "id": "r54",
    "categoria": "Seguridad Ciudadana (Serenazgo)",
    "tipo": "Denuncia",
    "estado": "Ingresado",
    "distrito": "Villa El Salvador",
    "fecha": "2023-09-30",
    "texto": "Denuncia por \"Cuidacoches (Trapitos)\", Villa El Salvador, urb. Parque Industrial — Ca. Los Álamos del Sur 3254."
  },
  {
    "id": "r55",
    "categoria": "Seguridad Ciudadana (Serenazgo)",
    "tipo": "Denuncia",
    "estado": "Derivado",
    "distrito": "Independencia",
    "fecha": "2023-01-11",
    "texto": "Denuncia por \"Cuidacoches (Trapitos)\", Independencia, urb. Payet — Av. Los Pinos 1839."
  },
  {
    "id": "r56",
    "categoria": "Seguridad Ciudadana (Serenazgo)",
    "tipo": "Denuncia",
    "estado": "Ingresado",
    "distrito": "Lurigancho-Chosica",
    "fecha": "2023-10-09",
    "texto": "Denuncia por \"Cuidacoches (Trapitos)\", Lurigancho-Chosica, urb. Chosica Centro — Av. Lima Sur 3350."
  },
  {
    "id": "r57",
    "categoria": "Seguridad Ciudadana (Serenazgo)",
    "tipo": "Denuncia",
    "estado": "Ingresado",
    "distrito": "Chorrillos",
    "fecha": "2023-11-16",
    "texto": "Denuncia por \"Cuidacoches (Trapitos)\", Chorrillos, urb. Los Cedros de Villa — Av. Guardia Civil 1138."
  },
  {
    "id": "r58",
    "categoria": "Seguridad Ciudadana (Serenazgo)",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "Los Olivos",
    "fecha": "2023-09-07",
    "texto": "Solicitud de \"Mayor presencia policial\", Los Olivos, urb. El Trébol — Av. Antúnez de Mayolo cdra. 3, a la altura del paradero de Av. Las Palmeras."
  },
  {
    "id": "r59",
    "categoria": "Seguridad Ciudadana (Serenazgo)",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "La Victoria",
    "fecha": "2023-12-04",
    "texto": "Solicitud de \"Mayor presencia policial\", La Victoria, urb. Balconcillo — Jr. Hipólito Unanue cdra. 31, cerca a la comisaría del sector."
  },
  {
    "id": "r60",
    "categoria": "Seguridad Ciudadana (Serenazgo)",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "Villa María del Triunfo",
    "fecha": "2023-10-12",
    "texto": "Solicitud de \"Mayor presencia policial\", Villa María del Triunfo, urb. Nueva Esperanza — Av. Pachacútec cdra. 11, a la altura del paradero de Av. Salvador Allende."
  },
  {
    "id": "r61",
    "categoria": "Ruido/Contaminación sonora",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "San Juan de Lurigancho",
    "fecha": "2023-03-18",
    "texto": "Denuncia por \"Ruidos molestos y vibraciones\", San Juan de Lurigancho, urb. Canto Grande — Jr. Los Amautas cdra. 13, frente al mercado del barrio."
  },
  {
    "id": "r62",
    "categoria": "Ruido/Contaminación sonora",
    "tipo": "Solicitud",
    "estado": "Cerrado",
    "distrito": "Lurigancho-Chosica",
    "fecha": "2023-02-02",
    "texto": "Solicitud de \"Consulta técnica sobre tramites de inscripción en el registro de actividades catalogadas como potencialmente contaminantes por ruidos y vibraciones (RAC)\", Lurigancho-Chosica, urb. Jicamarca — Jr. Arequipa 3239."
  },
  {
    "id": "r63",
    "categoria": "Ruido/Contaminación sonora",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "Comas",
    "fecha": "2023-03-27",
    "texto": "Denuncia por \"Ruidos molestos y vibraciones\", Comas, urb. La Pascana — Av. Micaela Bastidas cdra. 33, a la altura del paradero de Av. Universitaria."
  },
  {
    "id": "r64",
    "categoria": "Ruido/Contaminación sonora",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "Independencia",
    "fecha": "2023-07-27",
    "texto": "Denuncia por \"Ruidos molestos y vibraciones\", Independencia, urb. Payet — Av. Chinchaysuyo cdra. 10, al costado del parque zonal."
  },
  {
    "id": "r65",
    "categoria": "Ruido/Contaminación sonora",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "Los Olivos",
    "fecha": "2023-02-18",
    "texto": "Denuncia por \"Ruidos molestos y vibraciones\", Los Olivos, urb. Pro — Av. Carlos Izaguirre cdra. 10, al costado del parque zonal."
  },
  {
    "id": "r66",
    "categoria": "Ruido/Contaminación sonora",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "Carabayllo",
    "fecha": "2023-05-07",
    "texto": "Denuncia por \"Ruidos molestos y vibraciones\", Carabayllo, urb. El Progreso — Av. Túpac Amaru cdra. 1, a media cuadra de Ca. Los Geranios."
  },
  {
    "id": "r67",
    "categoria": "Ruido/Contaminación sonora",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "Santiago de Surco",
    "fecha": "2023-12-04",
    "texto": "Denuncia por \"Ruidos molestos y vibraciones\", Santiago de Surco, urb. Las Gardenias — Av. Ayacucho cdra. 41, a la altura del grifo."
  },
  {
    "id": "r68",
    "categoria": "Ruido/Contaminación sonora",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "Chorrillos",
    "fecha": "2023-07-23",
    "texto": "Denuncia por \"Ruidos molestos y vibraciones\", Chorrillos, urb. Los Cedros de Villa — Av. Guardia Civil cdra. 7, frente al colegio de la zona."
  },
  {
    "id": "r69",
    "categoria": "Ruido/Contaminación sonora",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "San Isidro",
    "fecha": "2023-02-04",
    "texto": "Denuncia por \"Ruidos molestos y vibraciones\", San Isidro, urb. El Olivar — Av. Dos de Mayo cdra. 4, a la altura del grifo."
  },
  {
    "id": "r70",
    "categoria": "Ruido/Contaminación sonora",
    "tipo": "Denuncia",
    "estado": "Cerrado",
    "distrito": "Villa El Salvador",
    "fecha": "2023-09-24",
    "texto": "Denuncia por \"Ruidos molestos y vibraciones\", Villa El Salvador, urb. Pachacámac VES — Av. Micaela Bastidas 523."
  }
];
