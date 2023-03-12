from django.utils import timezone
# Create your models here.
from django.db import models
from enum import Enum


class Paises(models.TextChoices):
    AFG = 'AFG', 'Afganistán'
    ALB = 'ALB', 'Albania'
    DEU = 'DEU', 'Alemania'
    AND = 'AND', 'Andorra'
    AGO = 'AGO', 'Angola'
    AIA = 'AIA', 'Anguila'
    ATA = 'ATA', 'Antártida'
    ATG = 'ATG', 'Antigua y Barbuda'
    SAU = 'SAU', 'Arabia Saudita'
    DZA = 'DZA', 'Argelia'
    ARG = 'ARG', 'Argentina'
    ARM = 'ARM', 'Armenia'
    ABW = 'ABW', 'Aruba'
    AUS = 'AUS', 'Australia'
    AUT = 'AUT', 'Austria'
    AZE = 'AZE', 'Azerbaiyán'
    BEL = 'BEL', 'Bélgica'
    BHS = 'BHS', 'Bahamas'
    BHR = 'BHR', 'Bahrein'
    BGD = 'BGD', 'Bangladesh'
    BRB = 'BRB', 'Barbados'
    BLZ = 'BLZ', 'Belice'
    BEN = 'BEN', 'Benín'
    BTN = 'BTN', 'Bhután'
    BLR = 'BLR', 'Bielorrusia'
    MMR = 'MMR', 'Birmania'
    BOL = 'BOL', 'Bolivia'
    BIH = 'BIH', 'Bosnia y Herzegovina'
    BWA = 'BWA', 'Botsuana'
    BRA = 'BRA', 'Brasil'
    BRN = 'BRN', 'Brunéi'
    BGR = 'BGR', 'Bulgaria'
    BFA = 'BFA', 'Burkina Faso'
    BDI = 'BDI', 'Burundi'
    CPV = 'CPV', 'Cabo Verde'
    KHM = 'KHM', 'Camboya'
    CMR = 'CMR', 'Camerún'
    CAN = 'CAN', 'Canadá'
    TCD = 'TCD', 'Chad'
    CHL = 'CHL', 'Chile'
    CHN = 'CHN', 'China'
    CYP = 'CYP', 'Chipre'
    VAT = 'VAT', 'Ciudad del Vaticano'
    COL = 'COL', 'Colombia'
    COM = 'COM', 'Comoras'
    COG = 'COG', 'República del Congo'
    COD = 'COD', 'República Democrática del Congo'
    PRK = 'PRK', 'Corea del Norte'
    KOR = 'KOR', 'Corea del Sur'
    CIV = 'CIV', 'Costa de Marfil'
    CRI = 'CRI', 'Costa Rica'
    HRV = 'HRV', 'Croacia'
    CUB = 'CUB', 'Cuba'
    CWU = 'CWU', 'Curazao'
    DNK = 'DNK', 'Dinamarca'
    DMA = 'DMA', 'Dominica'
    ECU = 'ECU', 'Ecuador'
    EGY = 'EGY', 'Egipto'
    SLV = 'SLV', 'El Salvador'
    ARE = 'ARE', 'Emiratos Árabes Unidos'
    ERI = 'ERI', 'Eritrea'
    SVK = 'SVK', 'Eslovaquia'
    SVN = 'SVN', 'Eslovenia'
    ESP = 'ESP', 'España'
    USA = 'USA', 'Estados Unidos de América'
    EST = 'EST', 'Estonia'
    ETH = 'ETH', 'Etiopía'
    PHL = 'PHL', 'Filipinas'
    FIN = 'FIN', 'Finlandia'
    FJI = 'FJI', 'Fiyi'
    FRA = 'FRA', 'Francia'
    GAB = 'GAB', 'Gabón'
    GMB = 'GMB', 'Gambia'
    GEO = 'GEO', 'Georgia'
    GHA = 'GHA', 'Ghana'
    GIB = 'GIB', 'Gibraltar'
    GRD = 'GRD', 'Granada'
    GRC = 'GRC', 'Grecia'
    GRL = 'GRL', 'Groenlandia'
    GLP = 'GLP', 'Guadalupe'
    GUM = 'GUM', 'Guam'
    GTM = 'GTM', 'Guatemala'
    GUF = 'GUF', 'Guayana Francesa'
    GGY = 'GGY', 'Guernsey'
    GIN = 'GIN', 'Guinea'
    GNQ = 'GNQ', 'Guinea Ecuatorial'
    GNB = 'GNB', 'Guinea-Bissau'
    GUY = 'GUY', 'Guyana'
    HTI = 'HTI', 'Haití'
    HND = 'HND', 'Honduras'
    HKG = 'HKG', 'Hong kong'
    HUN = 'HUN', 'Hungría'
    IND = 'IND', 'India'
    IDN = 'IDN', 'Indonesia'
    IRN = 'IRN', 'Irán'
    IRQ = 'IRQ', 'Irak'
    IRL = 'IRL', 'Irlanda'
    BVT = 'BVT', 'Isla Bouvet'
    IMN = 'IMN', 'Isla de Man'
    CXR = 'CXR', 'Isla de Navidad'
    NFK = 'NFK', 'Isla Norfolk'
    ISL = 'ISL', 'Islandia'
    BMU = 'BMU', 'Islas Bermudas'
    CYM = 'CYM', 'Islas Caimán'
    CCK = 'CCK', 'Islas Cocos (Keeling)'
    COK = 'COK', 'Islas Cook'
    ALA = 'ALA', 'Islas de Åland'
    FRO = 'FRO', 'Islas Feroe'
    SGS = 'SGS', 'Islas Georgias del Sur y Sandwich del Sur'
    HMD = 'HMD', 'Islas Heard y McDonald'
    MDV = 'MDV', 'Islas Maldivas'
    FLK = 'FLK', 'Islas Malvinas'
    MNP = 'MNP', 'Islas Marianas del Norte'
    MHL = 'MHL', 'Islas Marshall'
    PCN = 'PCN', 'Islas Pitcairn'
    SLB = 'SLB', 'Islas Salomón'
    TCA = 'TCA', 'Islas Turcas y Caicos'
    UMI = 'UMI', 'Islas Ultramarinas Menores de Estados Unidos'
    VGB = 'VGB', 'Islas Vírgenes Británicas'
    VIR = 'VIR', 'Islas Vírgenes de los Estados Unidos'
    ISR = 'ISR', 'Israel'
    ITA = 'ITA', 'Italia'
    JAM = 'JAM', 'Jamaica'
    JPN = 'JPN', 'Japón'
    JEY = 'JEY', 'Jersey'
    JOR = 'JOR', 'Jordania'
    KAZ = 'KAZ', 'Kazajistán'
    KEN = 'KEN', 'Kenia'
    KGZ = 'KGZ', 'Kirguistán'
    KIR = 'KIR', 'Kiribati'
    KWT = 'KWT', 'Kuwait'
    LBN = 'LBN', 'Líbano'
    LAO = 'LAO', 'Laos'
    LSO = 'LSO', 'Lesoto'
    LVA = 'LVA', 'Letonia'
    LBR = 'LBR', 'Liberia'
    LBY = 'LBY', 'Libia'
    LIE = 'LIE', 'Liechtenstein'
    LTU = 'LTU', 'Lituania'
    LUX = 'LUX', 'Luxemburgo'
    MEX = 'MEX', 'México'
    MCO = 'MCO', 'Mónaco'
    MAC = 'MAC', 'Macao'
    MKD = 'MKD', 'Macedônia'
    MDG = 'MDG', 'Madagascar'
    MYS = 'MYS', 'Malasia'
    MWI = 'MWI', 'Malawi'
    MLI = 'MLI', 'Mali'
    MLT = 'MLT', 'Malta'
    MAR = 'MAR', 'Marruecos'
    MTQ = 'MTQ', 'Martinica'
    MUS = 'MUS', 'Mauricio'
    MRT = 'MRT', 'Mauritania'
    MYT = 'MYT', 'Mayotte'
    FSM = 'FSM', 'Micronesia'
    MDA = 'MDA', 'Moldavia'
    MNG = 'MNG', 'Mongolia'
    MNE = 'MNE', 'Montenegro'
    MSR = 'MSR', 'Montserrat'
    MOZ = 'MOZ', 'Mozambique'
    NAM = 'NAM', 'Namibia'
    NRU = 'NRU', 'Nauru'
    NPL = 'NPL', 'Nepal'
    NIC = 'NIC', 'Nicaragua'
    NER = 'NER', 'Niger'
    NGA = 'NGA', 'Nigeria'
    NIU = 'NIU', 'Niue'
    NOR = 'NOR', 'Noruega'
    NCL = 'NCL', 'Nueva Caledonia'
    NZL = 'NZL', 'Nueva Zelanda'
    OMN = 'OMN', 'Omán'
    NLD = 'NLD', 'Países Bajos'
    PAK = 'PAK', 'Pakistán'
    PLW = 'PLW', 'Palau'
    PSE = 'PSE', 'Palestina'
    PAN = 'PAN', 'Panamá'
    PNG = 'PNG', 'Papúa Nueva Guinea'
    PRY = 'PRY', 'Paraguay'
    PER = 'PER', 'Perú'
    PYF = 'PYF', 'Polinesia Francesa'
    POL = 'POL', 'Polonia'
    PRT = 'PRT', 'Portugal'
    PRI = 'PRI', 'Puerto Rico'
    QAT = 'QAT', 'Qatar'
    GBR = 'GBR', 'Reino Unido'
    CAF = 'CAF', 'República Centroafricana'
    CZE = 'CZE', 'República Checa'
    DOM = 'DOM', 'República Dominicana'
    SSD = 'SSD', 'República de Sudán del Sur'
    REU = 'REU', 'Reunión'
    RWA = 'RWA', 'Ruanda'
    ROU = 'ROU', 'Rumanía'
    RUS = 'RUS', 'Rusia'
    ESH = 'ESH', 'Sahara Occidental'
    WSM = 'WSM', 'Samoa'
    ASM = 'ASM', 'Samoa Americana'
    BLM = 'BLM', 'San Bartolomé'
    KNA = 'KNA', 'San Cristóbal y Nieves'
    SMR = 'SMR', 'San Marino'
    MAF = 'MAF', 'San Martín (Francia)'
    SPM = 'SPM', 'San Pedro y Miquelón'
    VCT = 'VCT', 'San Vicente y las Granadinas'
    SHN = 'SHN', 'Santa Elena'
    LCA = 'LCA', 'Santa Lucía'
    STP = 'STP', 'Santo Tomé y Príncipe'
    SEN = 'SEN', 'Senegal'
    SRB = 'SRB', 'Serbia'
    SYC = 'SYC', 'Seychelles'
    SLE = 'SLE', 'Sierra Leona'
    SGP = 'SGP', 'Singapur'
    SMX = 'SMX', 'Sint Maarten'
    SYR = 'SYR', 'Siria'
    SOM = 'SOM', 'Somalia'
    LKA = 'LKA', 'Sri lanka'
    ZAF = 'ZAF', 'Sudáfrica'
    SDN = 'SDN', 'Sudán'
    SWE = 'SWE', 'Suecia'
    CHE = 'CHE', 'Suiza'
    SUR = 'SUR', 'Surinám'
    SJM = 'SJM', 'Svalbard y Jan Mayen'
    SWZ = 'SWZ', 'Swazilandia'
    TJK = 'TJK', 'Tayikistán'
    THA = 'THA', 'Tailandia'
    TWN = 'TWN', 'Taiwán'
    TZA = 'TZA', 'Tanzania'
    IOT = 'IOT', 'Territorio Británico del Océano Índico'
    ATF = 'ATF', 'Territorios Australes y Antárticas Franceses'
    TLS = 'TLS', 'Timor Oriental'
    TGO = 'TGO', 'Togo'
    TKL = 'TKL', 'Tokelau'
    TON = 'TON', 'Tonga'
    TTO = 'TTO', 'Trinidad y Tobago'
    TUN = 'TUN', 'Tunez'
    TKM = 'TKM', 'Turkmenistán'
    TUR = 'TUR', 'Turquía'
    TUV = 'TUV', 'Tuvalu'
    UKR = 'UKR', 'Ucrania'
    UGA = 'UGA', 'Uganda'
    URY = 'URY', 'Uruguay'
    UZB = 'UZB', 'Uzbekistán'
    VUT = 'VUT', 'Vanuatu'
    VEN = 'VEN', 'Venezuela'
    VNM = 'VNM', 'Vietnam'
    WLF = 'WLF', 'Wallis y Futuna'
    YEM = 'YEM', 'Yemen'
    DJI = 'DJI', 'Yibuti'
    ZMB = 'ZMB', 'Zambia'
    ZWE = 'ZWE', 'Zimbabue'


class Sexo(models.TextChoices):
    HOMBRE = 'HOMBRE', 'HOMBRE'
    MUJER = 'MUJER', 'MUJER'


class TiposIdentificacion(models.TextChoices):
    REGISTRO_CIVIL = 'RC', 'REGISTRO CIVIL'
    TARJETA_IDENTIDAD = 'TI', 'TARJETA IDENTIDAD'
    CEDULA_CIUDADANIA = 'CC', 'CEDULA CIUDADANIA'
    PASAPORTE = 'PA', 'PASAPORTE'
    TARJETA_EXTRANJERIA = 'TE', 'TARJETA_EXTRANJERIA'


class Medico(models.Model):
    tipo_identificacion = models.CharField(max_length=50, choices=TiposIdentificacion.choices,
                                           default=TiposIdentificacion.CEDULA_CIUDADANIA)
    numero_identificacion = models.IntegerField()
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True)
    sexo = models.CharField(max_length=20, choices=Sexo.choices, null=True)
    lugar_nacimiento = models.CharField(max_length=50, choices=Paises.choices, default=Paises.COL)
    lugar_residencia = models.CharField(max_length=30)
    numero_celular = models.CharField(max_length=30)
    numero_registro_profesional = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    clave = models.CharField(max_length=15)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = 'Medicos'
        verbose_name_plural = 'Medicos'
        db_table = 'medicos'
        ordering = ['apellidos', '-nombres']


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, default='', null=True)

    def __str__(self):
        return "{0}".format(self.nombre)

    class Meta:
        verbose_name = 'Especialidades'
        verbose_name_plural = 'Especialidades'
        db_table = 'especialidades'


class MedicoEspecialidad(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT)


class PerfilDermatologico(models.TextChoices):
    FOTOTIPO_I = 'FOTOTIPO I', 'Personas que tienen un color de pelo rubio o pelirrojo, ojos claros, ya sean verdes o azules, y una piel muy pálida o blanca. Suelen quemarse con mucha facilidad durante sus exposiciones al sol y, por ello, son los que más cuidados precisan tomar y quienes deben usar los bloqueador solares con la máxima protección'
    FOTOTIPO_II = 'FOTOTIPO II', 'Personas que tienen un color de pelo rubio o pelirrojo, ojos claros, ya sean verdes o azules, y una piel muy pálida o blanca. Suelen quemarse con mucha facilidad durante sus exposiciones al sol y, por ello, son los que más cuidados precisan tomar y quienes deben usar los bloqueador solares con la máxima protección'
    FOTOTIPO_III = 'FOTOTIPO III', 'Personas que tienen un color de pelo rubio o pelirrojo, ojos claros, ya sean verdes o azules, y una piel muy pálida o blanca. Suelen quemarse con mucha facilidad durante sus exposiciones al sol y, por ello, son los que más cuidados precisan tomar y quienes deben usar los bloqueador solares con la máxima protección'
    FOTOTIPO_IV = 'FOTOTIPO IV', 'Se trata de personas con pelo castaño oscuro, los ojos marrones y la piel, de por sí, morena. No suelen tener problemas para broncearse, y su piel adopta una tonalidad dorada con facilidad. Sólo se queman si están mucho tiempo tomando el sol, pero eso no significa que no tengan que usar protector solar, con una protección normal'
    FOTOTIPO_V = 'FOTOTIPO V', 'Son personas que tienen la piel oscura, al igual que los ojos, el pelo color negro. Se broncean con muchísima facilidad y no es necesario que se expongan mucho al sol para estar morenos. Es muy raro que se quemen, y esto sólo ocurre cuando están expuestos a las radiaciones solares de una manera excesiva. Sin embargo, ellos también necesitan usar protección solar'
    FOTOTIPO_VI = 'FOTOTIPO VI', 'personas de raza negra. Sus pieles son muy oscuras, al igual que su cabello y ojos. Es casi imposible que se quemen, pues tienen una piel muy pigmentada, aunque deben evitar la exposición al sol sin protección, pues las radiaciones, aunque no les produzcan daños externos, también son nocivas'



class Paciente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True)
    lugar_nacimiento = models.CharField(max_length=30)
    edad = models.CharField(max_length=30, null=True)
    sexo = models.CharField(max_length=20, choices=Sexo.choices, null=True)
    lugar_residencia = models.CharField(max_length=30)
    numero_celular = models.IntegerField(null=True)
    correo = models.CharField(max_length=100, null=True)
    clave = models.CharField(max_length=15, null=True)
    perfil_dermatologico = models.CharField(max_length=255, choices=PerfilDermatologico.choices, default=PerfilDermatologico.FOTOTIPO_IV)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = 'Pacientes'
        verbose_name_plural = 'Pacientes'
        db_table = 'pacientes'
        ordering = ['apellidos', '-nombres']


class EstadoCaso(models.TextChoices):
    CREADO = 'CREADO'
    RESERVADO = 'ENREVISION'
    SELECCIONADO = 'SELECCIONADO'
    LIBRE = 'LIBRE'


class CasoMedico(models.Model):
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    paciente = models.ForeignKey(Paciente, related_name="casos_medicos", on_delete=models.CASCADE, null=True)
    medico = models.ForeignKey(Medico, related_name="casos_medicos_medico", on_delete=models.CASCADE, null=True)
    estado = models.CharField(max_length=50, choices=EstadoCaso.choices)
    tipo = models.TextField(max_length=200, null=True)
    forma = models.TextField(max_length=200, null=True)
    numero = models.TextField(max_length=200, null=True)
    distribucion = models.TextField(max_length=200, null=True)
    color = models.TextField(max_length=200, null=True)


    class Meta:
        db_table = 'casosmedicos'

    def __str__(self):
        return '%s: %s' % (self.estado, self.descripcion)

class ImagenDiagnostica(models.Model):
    caso = models.ForeignKey(CasoMedico, related_name="imagenes", on_delete=models.CASCADE)
    url = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'ImagenDiagnostica'
        verbose_name_plural = 'ImagenesDianosticas'
        db_table = 'imagenesdianosticas'

    def __str__(self):
        return '%s' % self.url

class HistoriaClinica(models.Model):
    nombre = models.CharField(max_length=50)


class Interacciones(models.Model):
    nombre = models.CharField(max_length=50)


class Diagnostico(models.Model):
    caso = models.ForeignKey(CasoMedico, related_name="diagnosticos", on_delete=models.CASCADE)
    fecha_diagnostico = models.DateField()
    descripcion = models.TextField()
    fecha_acepta = models.DateField(null=True)

    class Meta:
        verbose_name = 'Diagnosticos'
        verbose_name_plural = 'Diagnosticos'
        db_table = 'diagnosticos'

    def __str__(self):
        return '%s: %s' % (self.fecha_acepta, self.descripcion)

class DiagnosticoExterno(models.Model):
    caso = models.ForeignKey(CasoMedico, related_name="diagnosticosexternos", on_delete=models.CASCADE)
    fecha_diagnostico = models.DateField()
    diagnostico = models.TextField()
    nombre_medico = models.TextField()
    correo = models.TextField()
    recomendaciones = models.TextField()
    ciudadcita = models.TextField()
    fechacitapresencial = models.TextField()
    urlCitaremota = models.TextField()
    class Meta:
        verbose_name = 'Diagnosticosexternos'
        verbose_name_plural = 'Diagnosticosexternos'
        db_table = 'diagnosticosexternos'

    def __str__(self):
        return '%s: %s' % (self.fecha_diagnostico, self.descripcion)


class Tratamiento(models.Model):
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.PROTECT)
    fecha_inicio = models.DateField()
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    detalle = models.TextField()

    class Meta:
        verbose_name = 'Tratamientos'
        verbose_name_plural = 'Tratamientos'
        db_table = 'tratamientos'


class TipoSoporte(models.TextChoices):
    PREGRADO = 'PREGRADO', 'PREGRADO'
    ESPECIALIZACION = 'ESPECIALIZACION','ESPECIALIZACION'
    CERTIFICACION = 'CERTIFICACION','CERTIFICACION'
    SEMINARIO = 'SEMINARIO','SEMINARIO'
    DIPLOMADO = 'DIPLOMADO','DIPLOMADO'

class Soporte(models.Model):
    medico = models.ForeignKey(Medico, related_name="soportes_medico", on_delete=models.CASCADE, null=True)
    tipo_soporte = models.CharField(max_length=50, choices=TipoSoporte.choices,
                                           default=TipoSoporte.PREGRADO)
    institucion_educativa = models.TextField(max_length=150, default='NINGUNA')
    nombre_programa = models.TextField(max_length=150, default='MEDICINA')
    descripcion = models.TextField(max_length=200, null=True)
    graduado = models.BooleanField(default=True)
    fecha_grado = models.DateField(null=True)
    fecha_soporte = models.DateField(null=True)
    validado = models.BooleanField(default=False)
    url = models.TextField(max_length=500, null=True)

    class Meta:
        verbose_name = 'Soportes'
        verbose_name_plural = 'Soportes'
        db_table = 'soportes'

class Seguimiento(models.Model):
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.PROTECT)
    mensaje_paciente = models.TextField()
    fecha_msg_paciente = models.DateField()
    mensaje_medico = models.TextField(max_length=500, null=True)
    fecha_msg_medico = models.DateField(null=True)
    detalle = models.TextField(max_length=500,null=True)

    class Meta:
        verbose_name = 'Seguimientos'
        verbose_name_plural = 'Seguimientos'
        db_table = 'seguimientos'

class ImagenDiagnosticaT(models.Model):
    seguimiento = models.ForeignKey(Seguimiento, null=True, blank=True, on_delete=models.PROTECT)
    url = models.TextField()
    descripcion = models.TextField(max_length=200, null=True)
    fecha_creacion = models.DateField()

    class Meta:
        verbose_name = 'ImagenDiagnosticaT'
        verbose_name_plural = 'ImagenesDianosticasT'
        db_table = 'imagenesdianosticast'
