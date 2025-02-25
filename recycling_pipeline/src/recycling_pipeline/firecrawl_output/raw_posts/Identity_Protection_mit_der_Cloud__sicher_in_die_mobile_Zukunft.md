![](https://25917640.fs1.hubspotusercontent-eu1.net/hub/25917640/hubfs/csm_iStock-648412962-min_bca7b6a118-600x400.webp?width=300&name=csm_iStock-648412962-min_bca7b6a118-600x400.webp)

[Michael Freuler](https://blog.dinotronic.ch/author/michael-freuler) Oct 24, 2017 7:30:00 AM4 min read

# Identity Protection mit der Cloud –sicher in die mobile Zukunft

[Vorherige](https://blog.dinotronic.ch/blog/cloud/hybride-cloud-vorteile-und-potenziale)

[Back Navigation](https://blog.dinotronic.ch/)

[Nächste](https://blog.dinotronic.ch/blog/digital-workplace/notizbloecke-waren-gestern-onenote-ist-heute)

## **Identitäts- und Zugriffsmanagement als zentrale Bausteine für Datensicherheit und Mobilität im Unternehmen**

Viele Mitarbeitende benötigen jederzeit Zugriff auf – auch sensitive – Unternehmensdaten. In der Vergangenheit war dies vorrangig nur möglich, wenn man im Unternehmen selbst anwesend war oder über eine VPN-Verbindung verfügte. Die Sicherheitsrichtlinien bildeten um das Unternehmen eine Grenze, machten aus ihm einen in sich geschlossenen, physischen Bereich.

Dass dem heute nicht mehr so sein muss, ist landläufig bekannt. Unternehmen öffnen sich, es kann von überall und über verschiedene, private wie geschäftliche, Geräte auf dessen Daten zugegriffen werden. Immer öfter wird auch Kunden und externen Partnern der Zugang zu Daten und Infrastruktur im eigenen Unternehmen gestattet. Hybride Umgebungen werden immer mehr zum Standard, da sie Bewährtes mit Neuem verknüpfen und den reibungslosen Übergang von einer IT-Landschaft in eine andere gewährleisten.

Um den Benutzern modernes Arbeiten zu ermöglichen und keine Schatten-IT entstehen zu lassen, müssen Unternehmen ihre Sicherheitsrichtlinien dem veränderten Arbeiten von überall, zu jeder Zeit und von unterschiedlichen Geräten aus anpassen. Der Endpunkt, von dem aus der Zugriff auf Unternehmensdaten erfolgt, ist variabel. Um das «Vertrauen» zu einem solchen Endpunkt, hinter dem jeweils ein Benutzer steht, herzustellen, muss folgende Frage beantwortet werden:

«In wie weit kann diesem Endpunkt in dieser Situation der Zugriff gewährt werden?»

## **Benutzeridentität wird zur Sicherheitsgrundlage**

Die Antwort auf die Frage liefert der Benutzer durch seine digitale Identität. Ein Zugang wird nur dem gewährt, der sich mittels seines Passwortes und einer weiteren Authentifizierung ausweisen kann, einer sogenannten Multifaktoren-Authentisierung (MFA). Nach der Passworteingabe folgt die zweite Identitätsüberprüfung wahlweise über eine SMS, einen Telefonanruf oder einen Code, welcher in einer mobilen App generiert wird und dann eingegeben werden muss. Die neueste Variante verlangt via mobiler App sogar nur noch eine Genehmigung. Wichtig ist hierbei, dass für die verschiedenen Schritte unterschiedliche Übermittlungskanäle genutzt werden. Dieses Vorgehen erhöht den Schutz vor «Man-in-the-Middle»-Attacken.

Die technische Voraussetzung hierfür schafft ein zentrales Verzeichnis wie das Microsoft Azure Active Directory, welches in hybriden Umgebungen mit dem lokalen Active Directory verbunden werden kann.

## **Gerätestandort beeinflusst die Zugriffsberechtigung**

Der Standort eines Endgerätes beim Zugriff bestimmt die Sicherheitsanforderungen. Befindet sich der Benutzer bspw. an einem Endgerät in einem Internetcafé, so sind andere Sicherheitsanforderungen und -prüfungen erforderlich, als wenn er sich innerhalb des Unternehmens an einem Firmengerät anmeldet. Diese Unterschiede werden im System als Bedingter Zugriff oder Conditional Access definiert. Die Sicherheitsanforderungen können sogar so weit gehen, dass der Zugriff auf bestimmte Anwendungen gesperrt ist oder dem Benutzer innerhalb einer Anwendung gewisse Funktionen nur dann zur Verfügung stehen – zum Beispiel das Kopieren von Dateien –, wenn er sich innerhalb des Firmennetzwerkes befindet.

Die Sicherheitsprüfungen können je Szenario definiert werden. Meldet sich ein Benutzer z.B. vom Ausland aus an, was über die IP-Adresse seines Endgeräts festgestellt werden kann, so erfordert die Multifaktor-Authentifizierung eine Verifizierung durch einen Telefonanruf. Erfolgt die Anmeldung hingegen aus der Schweiz, kann für die weitere Identifizierung nur ein Code aus einer mobilen App, zum Beispiel die Authenticator App von Microsoft, verlangt werden.

Das Identity Management erkennt und reagiert auch auf Anomalien beim Login. Angenommen, ein Benutzer meldet sich in Zürich an und fünf Minuten später nochmals von Hamburg aus, erkennt das System, dass dies aufgrund des Verhältnisses von Zeit und Entfernung nicht möglich ist. Abhängig von der definierten Sicherheitsrichtlinie wird dann beispielsweise der Zugriff blockiert und kann erst durch eine weitere Authentifizierung (beispielsweise ein Telefonat mit dem Servicedesk) wieder freigeschaltet werden.

Bedingter Zugriff bietet Kontrolle auf folgenden Ebenen

- Benutzer
- Standort
- Endgeräte
- Anwendung

und unterstützt alle Plattformen wie Windows, iOS, Android sowie neu auch macOS.

## **Mit Mobilgeräten sicher auf Unternehmensdaten zugreifen**

Durch die Integration eines Mobile-Device-Managements (MDM) können Unternehmensrichtlinien auf den Endgeräten der Benutzer, auch auf deren privaten Geräten, angewendet und durchgesetzt werden.

Die Datensicherheit kann mittels besonderer Anforderung zusätzlich erhöht werden. Beispielsweise gelingt der Zugriff auf Firmenmails oder -dokumente nur dann, wenn der Speicher des Endgeräts verschlüsselt wurde.

Microsoft Intune dient der cloudbasierten Verwaltung mobiler Anwendungen und Geräte im Unternehmen.

## **Einmal-Authentifizierung schafft Sicherheit und Effizienz**

Durch die Single Sign-on Funktion des Identity Management Systems erhält der Benutzer mit einem Login Zugriff auf all seine Anwendungen, unabhängig davon, ob diese im Firmenumfeld gehostet sind, sich in der Cloud oder auf anderen Plattformen (wie Salesforce, Twitter, Facebook, Google, Dropbox etc.) befinden. Neben Standardanwendungen können gleichzeitig auch eigene wie auch Mobil- und Web-Anwendungen des Unternehmens gesichert werden. Tausende von SaaS-Lösungen (Software-as-a-Service) können so geschützt und zentral angeboten werden, auch wenn die Anwendung an sich nicht MFA-fähig ist.

## **Passwortmanagement einfach und sicher gemacht**

Die hohe Anzahl von Anrufen zwecks Zurücksetzung des Passworts beschäftigen Servicedesks erfahrungsgemäss intensiv. Mit der Einrichtung eines Self-Service-Portals können Servicedesk-Mitarbeitende entlastet werden und die anfragenden Benutzer schneller zu einem neuen Passwort gelangen.

Mit dem sogenannten Self-Service-Password-Reset kann der Benutzer sein Passwort eigenständig zurücksetzen. Selbstverständlich greifen auch hier die Sicherheitsrichtlinien, so dass nur der berechtigte Benutzer sein Passwort zurücksetzen kann.

## **Cloud-Lösung generiert vielschichtigen Mehrwert**

Das Cloud Identity Management bringt folgenden Mehrwert:

⚿ Mehr Sicherheit

⛁ Geringere Kosten

⚒ Einfachere Inbetriebnahme

☺ Bessere Benutzererfahrung (User Experience)

✓ Gerüstet für die Zukunft

Cloud-first, mobile-first – immer mehr Unternehmen wählen diese IT-Strategie, denn heute wird vielerorts in hybriden, mobilen Umgebungen gearbeitet und entwickelt. Ein lokales Identity Management wäre nie so sicher, so günstig und so einfach zu betreiben wie ein cloudbasiertes.

Mittels Identity Management und Conditional Access von Microsoft Azure Active Directory & Enterprise Mobility + Security erhalten Sie die Kontrolle und Sicherheit, dass ihre Firmendaten geschützt sind, während Ihre Mitarbeitenden frei von jedem Gerät aus auf alle Anwendungen und Daten zugreifen können, unabhängig davon, ob sich diese in der Cloud oder in Ihrem Unternehmensnetzwerk befinden.

24\. Oktober 2017 \| Geschrieben von Udo Jetschmanegg

![avatar](https://25917640.fs1.hubspotusercontent-eu1.net/hub/25917640/hubfs/01_Visual%20Content/01_Mitarbeiter-Fotos/Michael%20Freuler%20klein.png?width=290&name=Michael%20Freuler%20klein.png)

[**Michael Freuler**](https://blog.dinotronic.ch/author/michael-freuler) Head of Solution Consulting and Marketing

## Abonnieren Sie unsere monatlichen Newsletter

Unsere Newsletter geben interessante Einblicke in neue Trends.

[JETZT ABONNIEREN](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/click?encryptedPayload=AVxigLJK7PFirT0cRWoVB%2FJCMiWNtA6kAaFWESe1oNnl4vy0r6aPG%2BNyl%2B4TYfWOuAIPb5lr2tNO7lHTGw%2FLql7VC1Lx44Lfee%2Bgv2%2BHZ5%2Fw58nDEOZQU%2FllHsVyM8FlZuO%2BdsGKIep9wUc8vvt%2B%2FAHwzALgjOhXF97KifK3xuP29eDwbLMYeVqJB5MDf7J%2F%2BjU%3D&portalId=25917640&webInteractiveContentId=114201044682&webInteractiveId=151726273754&containerType=EMBEDDED&pageUrl=https%3A%2F%2Fblog.dinotronic.ch%2Fblog%2Fcyber-security%2Fidentity-protection-mit-der-cloud-sicher-aufgestellt-fuer-die-mobile-zukunft&pageTitle=Identity+Protection+mit+der+Cloud+%E2%80%93sicher+in+die+mobile+Zukunft&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F132.0.0.0+Safari%2F537.36&hutk=&hssc=&hstc=&pageId=116865496252)

## Sie haben Fragen? Kommen Sie gernedirekt auf uns zu! Wir freuen uns vonIhnen zu hören

Kommen Sie gerne direkt auf uns zu!

Anrede

Bitte auswählenHerrFrau

Unternehmen

Vorname\*

Nachname\*

E-Mail\*

Telefon

Ihr Anliegen\*

- Ich habe die Datenschutzbestimmungen zur Kenntnis genommen und stimme ihnen zu.
\*

[Die Datenschutzerklärung finden sie hier.](https://dinotronic.ch/datenschutz)

## VERWANDTE ARTIKEL

[Michael Freuler28.05.2019, 20:30:004 min read\\
\\
**Viele Wege führen in die Cloud – mit Azure Schweiz einer mehr** \\
\\
Mit der zunehmenden Digitalisierung müssen Unternehmen ihre Produkte und Lösungen immer schneller überdenken und unmittelbar ...\\
\\
Mehr lesen](https://blog.dinotronic.ch/blog/azure/viele-wege-fuehren-in-die-cloud-mit-azure-schweiz-einer-mehr) [Michael Freuler02.03.2022, 20:30:004 min read\\
\\
**Microsoft SharePoint – Was Sie wissen müssen** \\
\\
In vielen Betrieben ist Microsoft SharePoint kaum mehr wegzudenken. Und dies zu Recht: Die Zusammenarbeit innerhalb von ...\\
\\
Mehr lesen](https://blog.dinotronic.ch/blog/digital-workplace/microsoft-sharepoint-was-sie-wissen-muessen) [Michael Freuler09.12.2021, 20:30:004 min read\\
\\
**Das steckt in unseren Managed Services** \\
\\
Die voranschreitende Digitalisierung führt zu einer steigenden Abhängigkeit von der IT. Die eigenen IT-Abteilungen haben ...\\
\\
Mehr lesen](https://blog.dinotronic.ch/blog/digital-workplace/das-steckt-in-unseren-managed-services)

Twitter Widget Iframe

Chat Widget