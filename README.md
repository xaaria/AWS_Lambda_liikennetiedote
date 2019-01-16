# AWS_Lambda_liikennetiedote

> Huom! Puhtaasi testimielessä tehty koodinpätkä! 
<img src="https://github.com/xaaria/AWS_Lambda_liikennetiedote/blob/master/2357920222.jpg" width="400" alt="foo">

AWS:n Lambda -palvelussa [1] pyörivä ajastettu yksinkertainen Python-scripti
(käytetty AWS:n _Boto3_-kirjastoa), joka tutkailee valtatie 9:n tiesensorin tietoja keskinopeudesta (viimeisin 5 min),
ja lähettää SES-palvelun avulla (_Simple Email Service_ [2]) sähköpostiin ilmoituksen alhaisista nopeuksista (raja esim. 50 km/h).

Toimiakseen scripti vaatii (sen lisäksi että se ladataan AWS Lambdaan):
- Ajastuksen
- SES:n asettamisen toimintakuntoon (mm. vahvistettu sähköposti lähettäjäksi)
Paikallisesti:
- AWS-credientals ja Config -tiedostot (asetuksen app-nimisen profiilin alle)


## Liikenneviraston API: 
- http://digitraffic.liikennevirasto.fi/
- Tiedot kartalla: https://liikennetilanne.liikennevirasto.fi/

### Viitteet
#1 https://console.aws.amazon.com/lambda/home
#2 https://console.aws.amazon.com/ses/home
