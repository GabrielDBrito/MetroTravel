

La Agencia de Viajes Metro Travel desea adquirir un programa que le permita  optimizar los costos de los viajes que realizan sus clientes. En este momento, Metro Travel  se especializa en viajes desde el Aeropuerto de Maiquetía hacia las diversas islas del Mar Caribe

Algunos de los destinos requieren que los venezolanos tengan una visa. Para simplificar  el ejercicio, cualquiera que posea una visa aceptable para una de las islas que la  requieren puede ingresar en cualquier otra isla que requiera visa. No se permite empezar el viaje  en un destino que requiere visa si el viajero no la posee. 
Los destinos a contemplar son:

CCS	Caracas		No Requiere Visa	
AUA	Aruba		Requiere Visa	
BON	Bonaire		Requiere Visa	
CUR	Curazao		Requiere Visa	
SXM	San Martín		Requiere Visa	
SDQ	Santo Domingo		Requiere Visa	
SBH	San Bartolomé		No Requiere Visa	
POS	Puerto España (Trinidad)		No Requiere Visa	
BGI	Barbados		No Requiere Visa	
FDF	Fort de France (Martinica)		No Requiere Visa	
PTP	Point a Pitre (Guadalupe)		No Requiere Visa	
PAP	Port Au Prince (Haití)		No Requiere Visa	

Las tarifas en los vuelos existentes se muestran en la tabla que sigue. El monto a pagar  por volar en sentido contrario es el mismo. No interesan los horarios de salida ni llegada … tampoco importa la duración de una escala aburrida en un aeropuerto intermedio … solo se desea minimizar, a opción del usuario:

. El costo del viaje entre 2 puntos
. El número de escalas para un viaje entre 2 puntos

Origen	Destino	Precio del pasaje
CCS	AUA	$ 40,00
CCS	CUR	$ 35,00
CCS	BON	$ 60,00
CCS	SXM	$ 300,00
CCS	PAP	$ 400,00
AUA	CUR	$ 15,00
AUA	BON	$ 15,00
CUR	BON	$ 15,00
CCS	SDQ	$ 180,00
SDQ	SXM	$ 50,00
SXM	SBH	$ 45,00
CCS	POS	$ 150,00
CCS	BGI	$ 180,00
POS	BGI	$ 35,00
POS	SXM	$ 90,00
BGI	SXM	$ 70,00
POS	PTP	$ 80,00
POS	FDF	$ 75,00
PTP	SXM	$ 100,00
PTP	SBH	$ 80,00
CUR	SXM	$ 80,00
AUA	SXM	$ 85,00
PAP	SDQ	$ 30,00
PAP	FDF	$ 55,00

El usuario deberá introducir los códigos del aeropuerto origen y del aeropuerto destino,  y responder si el pasajero tiene visa o no … el programa calculará la ruta más barata o bien la que tenga la menor cantidad de escalas y se la mostrará.

Los datos de destinos y costos deben leerse de archivos planos en disco, no pueden estar  "hard coded" en el programa en Python sino que al empezar a ejecutar el programa se lee del disco duro la tabla de destinos y luego la tabla de tarifas. Habrá serios descuentos en puntos por ignorar esta norma.
