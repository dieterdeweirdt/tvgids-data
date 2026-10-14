# tvgids-data

Dagelijkse datapijplijn voor de [tvOS tv-gids](https://github.com/dieterdeweirdt/appleTVguide). Een GitHub Action draait elke nacht om 03:15 UTC de grabber van [iptv-org/epg](https://github.com/iptv-org/epg) voor `pickx.be`, en publiceert het resultaat op GitHub Pages:

- https://dieterdeweirdt.github.io/tvgids-data/guide.xml.gz (deze URL gebruikt de app)
- https://dieterdeweirdt.github.io/tvgids-data/guide.xml
- https://dieterdeweirdt.github.io/tvgids-data/channels.json (taal en categorieën per zender, voor de filters in de app)

De gids bevat 3 dagen, tijden in UTC, voor de zenders in [`belgie.channels.xml`](belgie.channels.xml). De volgorde in dat bestand is de standaardvolgorde in de app.

## Werking

- Mislukt de grab of is het resultaat te klein (minder dan 20.000 programma's of minder dan 150 zenders met data; normaal ±28.000 op ±198), dan wordt niets gepubliceerd en blijft de gids van de vorige dag online.
- Pickx levert ongeveer een derde van de programma's dubbel (rond middernacht); [`scripts/dedupe-guide.py`](scripts/dedupe-guide.py) haalt die eruit voor publicatie.
- GitHub schakelt geplande workflows in publieke repo's uit na 60 dagen zonder activiteit. De eerste stap van de workflow zet zichzelf daarom bij elke run opnieuw aan via de API (geen dummy-commits nodig).
- Handmatig draaien: tab **Actions** › *grab-epg* › *Run workflow*, of `gh workflow run grab-epg`.
- `belgie.channels.xml` bevat alle zenders van Pickx (±209), gegenereerd met [`scripts/build-channels.py`](scripts/build-channels.py) (gebruiksaanwijzing bovenaan het script): één variant per zender (SD boven HD), volledige namen uit de [iptv-org-databank](https://iptv-org.github.io/api/channels.json), zonder testkanalen en erotische zenders. Volgorde: de 12 hoofdzenders, dan Nederlands-, Engels-, Duits- en Franstalig, alfabetisch. De app neemt nieuwe zenders automatisch op en verbergt zenders zonder programma's.

## Kanttekening

De data komt uit een niet-officiële Pickx-API en is enkel bedoeld voor persoonlijk gebruik. Wijzigt Pickx zijn site, dan werkt de grab niet meer tot iptv-org de grabber bijwerkt.
