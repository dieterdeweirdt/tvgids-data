# tvgids-data

Dagelijkse datapijplijn voor de [tvOS tv-gids](https://github.com/dieterdeweirdt/appleTVguide). Een GitHub Action draait elke nacht om 03:15 UTC de grabber van [iptv-org/epg](https://github.com/iptv-org/epg) voor `pickx.be`, en publiceert het resultaat op GitHub Pages:

- https://dieterdeweirdt.github.io/tvgids-data/guide.xml.gz (deze URL gebruikt de app)
- https://dieterdeweirdt.github.io/tvgids-data/guide.xml

De gids bevat 3 dagen, tijden in UTC, voor de zenders in [`belgie.channels.xml`](belgie.channels.xml). De volgorde in dat bestand is de standaardvolgorde in de app.

## Werking

- Mislukt de grab of is het resultaat te klein (minder dan 500 programma's of minder dan 10 zenders met data), dan wordt niets gepubliceerd en blijft de gids van de vorige dag online.
- GitHub schakelt geplande workflows in publieke repo's uit na 60 dagen zonder activiteit. De eerste stap van de workflow zet zichzelf daarom bij elke run opnieuw aan via de API (geen dummy-commits nodig).
- Handmatig draaien: tab **Actions** › *grab-epg* › *Run workflow*, of `gh workflow run grab-epg`.
- Zenders toevoegen: kopieer regels uit [`sites/pickx.be/pickx.be.channels.xml`](https://github.com/iptv-org/epg/blob/master/sites/pickx.be/pickx.be.channels.xml) naar `belgie.channels.xml`. De app neemt nieuwe zenders automatisch op.

## Kanttekening

De data komt uit een niet-officiële Pickx-API en is enkel bedoeld voor persoonlijk gebruik. Wijzigt Pickx zijn site, dan werkt de grab niet meer tot iptv-org de grabber bijwerkt.
