# AWS_Lambda_liikennetiedote

AWS:n Lambda -palvelussa [1] pyörivä ajastettu (3 min välein?) yksinkertainen Python-scripti
(käytetty AWs:n Boto3-kirjastoa), joka tutkailee valtatie 9:n tiesensorin tietoja keskinopeudesta (viimeisin 5 min)
ja lähettää SES-palvelun avulla (Simple Email Service [2]) sähköpostiin ilmoituksen alhaisista nopeuksista (raja esim. 50 km/h).

Huom. Öisin ilmoituksia tulee tavallista useammin, tämä saattaa johtua siitä, että sensorin kohdalla 
kaikki autot (joita vain muutamia 5 min sisään) hidastavat rampille mennessä. Tällöin myös keskinopeus 
näkyy alhaisena, ja saa ilmoituksen lähtemään [Paras teoria mitä keksin].

Toimiakseen scripti vaatii (sen lisäksi että se ladataan AWS Lambdaan):
    > Ajastuksen
    > SES:n asettamisen toimintakuntoon (mm. vahvistettu sähköposti lähettäjäksi)
Paikallisesti:
    > AWS-credientals ja Config -tiedostot (asetuksen app-nimisen profiilin alle)

Liikenneviraston API: 
http://digitraffic.liikennevirasto.fi/
Tiedot kartalla: https://liikennetilanne.liikennevirasto.fi/

#1 https://console.aws.amazon.com/lambda/home
#2 https://console.aws.amazon.com/ses/home