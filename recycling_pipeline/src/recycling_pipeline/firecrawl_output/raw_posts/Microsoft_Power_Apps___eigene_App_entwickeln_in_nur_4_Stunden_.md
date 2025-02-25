![](https://25917640.fs1.hubspotusercontent-eu1.net/hub/25917640/hubfs/Power-Platform-1-600x375.webp?width=300&name=Power-Platform-1-600x375.webp)

[Michael Freuler](https://blog.dinotronic.ch/author/michael-freuler) Jul 27, 2022 7:30:00 AM6 min read

# Microsoft Power Apps – eigene App entwickeln in nur 4 Stunden?

[Vorherige](https://blog.dinotronic.ch/blog/digital-workplace/terminfindung-leicht-gemacht-dank-microsoft-bookings)

[Back Navigation](https://blog.dinotronic.ch/)

[Nächste](https://blog.dinotronic.ch/blog/cyber-security/cyber-security-awareness-trainings-warum-sie-so-essenziell-sind)

**Viele Unternehmen stehen vor einer Herausforderung, wenn es darum geht, Standard Anwendungen oder Services zu finden, die spezifische Aufgaben bewältigen können.**

**Software Entwickler sind Mangelware. Gerade für kleine und mittelständische Unternehmen ist es schwierig, Personal für die Entwicklung von Software zu finden. Es gibt jedoch bereits ein Konzept, das beim Ressourcenmangel in der Softwareentwicklung Abhilfe schaffen kann: Low-Coding (Programmieren mit niedriger Einstiegshürde) bspw. mit [Microsoft Power Apps](https://powerapps.microsoft.com/de-de/). Beim Low Coding werden Web- und mobile Anwendung mit Hilfe von Bausteinen und Drag & Drop von «Citizen Developer» (Nicht-Entwicklern) erstellt.**

Mit der Möglichkeit, Apps ohne Hilfe von Software-Spezialisten zu entwickeln, kann auch die Dauer der Entwicklungszeit reduziert werden. Der Grund dafür ist, dass Citizen Developer die Anforderungen an die Software besser verstehen als ein externer Entwickler, der zwar sehr gut programmieren kann, aber die Anforderungen zunächst verstehen muss. Zudem ist der Entwickler während der gesamten Dauer des Entwicklungsprozesses auf Feedback vom Auftraggeber angewiesen. Citizen Developer hingegen wissen genau, was die Anwendung können muss und wie sie aussehen soll. Diesen Vorteil hat auch Microsoft erkannt und hat mit der [Microsoft Power Platform](https://powerplatform.microsoft.com/de-de/) eine Basis für Low-Code Programmierung geschaffen.

## Microsoft Power Apps

Bei der Erstellung der Anwendungen kann man entweder auf Vorlagen von Microsoft zurückgreifen oder komplett bei null anfangen. Anwendungen, die mit Power Apps entwickelt werden, sind keine eigenständigen Applikationen, sondern werden über eine Container-App auf Mobilen Geräten wie Smartphones oder Tablets zu Verfügung gestellt. Benutzer laden sich die Microsoft Power Apps Mobile App für Android und iOS herunter ([Google Play](https://play.google.com/store/apps/details?id=com.microsoft.msapps&hl=de&gl=US) / [Apple Store](https://apps.apple.com/ch/app/power-apps/id1047318566)) und können anschliessend digital auf alle für sie freigegebenen Apps zugreifen. Diese lassen sich auch in MS Teams integrieren oder können bei Windows Geräten in der Startleiste angeheftet werden.

![MicrosoftTeams-image-600x1067](https://blog.dinotronic.ch/hs-fs/hubfs/MicrosoftTeams-image-600x1067.webp?width=300&height=534&name=MicrosoftTeams-image-600x1067.webp)

Bsp. Dinotronic Apps für Mitarbeitende in Power Apps

![Spesen-App-MS-Teams-neu](https://blog.dinotronic.ch/hs-fs/hubfs/Spesen-App-MS-Teams-neu.webp?width=413&height=534&name=Spesen-App-MS-Teams-neu.webp)

Bsp. Dinotronic Spesen App in MS Teams

Die Verwendung von Power Apps eignet sich besonders bei der Verwendung als Verbindungsstück zwischen verschiedenen Datenquellen (Office 365, Microsoft- und Drittanbieterprodukt) sowie bei der Entwicklung von Prototypen. Power Apps kann ausserdem genutzt werden, um Office 365 oder Dynamics 365 auf die eigenen Bedürfnisse anzupassen.

### **Canvas- oder Model-driven App?**

Bevor mit der Entwicklung der eigenen App gestartet werden kann, muss man sich überlegen was die App bewirken soll. Es gibt nämlich zwei Anwendungstypen, die mit der Power Apps Platform erstellt werden können: Canvas-Apps und Model-driven Apps.

Im Grunde unterscheiden sich die beiden Varianten nur marginal, schliesslich handelt es sich bei beiden um Geschäftsanwendungen, die von Nicht-Entwicklern erstellt werden und aus ähnlichen Komponenten bestehen. Die daraus resultierenden Applikationen unterscheiden sich oft nur geringfügig. Der wesentliche Unterschied liegt in den Anwendungsfällen und der Nutzersteuerung. Die einen Anwendungsszenarien eignen sich besser für Canvas-Apps, die anderen für Model-driven Apps.

#### Canvas-Apps

Canvas-Apps werden hauptsächlich für mobile Geräte verwendet. Es gibt nur zwei Layout-Optionen: Telefon oder Tablet (Portrait oder Landschaft). Die Canvas-App sieht zu Beginn aus wie eine leere PowerPoint Folie und hat daher auch ihren Namen «Canvas» (Deutsch: Leinwand). Auf die leere Leinwand können jetzt beliebige Elemente hinzugefügt werden (Kontrollen, Aktionen, Bilder, Objekte etc.). Canvas-Apps sind die wahren Low Coding Anwendungen. Dennoch ist es hilfreich zu verstehen, wie Excel Befehle funktionieren, da dies den Einstieg enorm erleichtert. Dieser Typ von Power App ist nicht auf eine bestimmte Datenquelle angewiesen und kann rund [200 Konnektoren](https://flow.microsoft.com/de-de/connectors/) nutzen, um bestehende Daten zu integrieren.

**Anwendungsbeispiele für Canvas Apps**

- Abbildung von Genehmigungsprozessen (Ferienantrag / Spesenantrag)
- Onboarding für neue Mitarbeitende
- Apps für Service Anfragen (Ticket System)

#### Model-driven Apps

Model-driven Apps folgen einem “Data first”-Ansatz. Sie können Datenmodelle generieren und eignen sich daher für komplexe Geschäftsanwendungen. Sie sind in der Erstellung anspruchsvoll und erfordern daher mehr technisches Knowhow als eine Canvas-App.

Die Grundlage von Model-driven Apps bildet immer das Datenmodell. Dieses kann bereits im Common Data Service (CMS) oder Dynamics 365 existieren oder neu erstellt werden.

Die daraus resultierenden Anwendungen werden vornehmlich von den eingegebenen Daten und Informationen gesteuert und weniger vom Benutzer. Die User haben daher weniger Kontrolle über die Funktionalität und das Layout im Gegensatz zur Canvas-App. Die Applikation passt sich den zugrundeliegenden Daten an und nicht umgekehrt (die eingegeben Daten bestimmen das Resultat).

## **Power Automate**

Mit [Power Automate](https://flow.microsoft.com/de-de/connectors/) (ehemals Microsoft Flow) können Sie Workflows zwischen Apps und Diensten erstellen und somit zeitaufwändige Aufgaben und Prozesse über verschiedene Anwendungen hinweg automatisieren.

Power Automate basiert wie Microsoft Power Apps auf der sogenannten Power Platform. Dadurch hat Power Automate auf dieselben Konnektoren Zugriff wie Power Apps. Damit können Cloud Lösungen angebunden werden, um auf Ereignisse zu reagieren oder Aktionen auszuführen. So kann beispielsweise darauf reagiert werden, wenn jemandem in [Microsoft Planner](https://www.dinotronic.ch/blog/digital-workplace/mit-dem-richtigen-werkzeug-gehts-einfacher-microsoft-planner/) eine Aufgabe zugewiesen wird. Wie bei Power Apps stehen den Benutzern bei Power Automate eine grosse Anzahl an Vorlagen zur Verfügung, die den Einstieg erleichtern und Anstoss zu neuen Ideen geben können.

**Anwendungsbeispiele für Power Automate**

- Automatische Benachrichtigung bei Eintreten eines bestimmten Ereignisses
- Abbildung von Genehmigungsprozessen
- Automatische Ablage von Daten in eine SharePoint Bibliothek

![Uebersicht-Flows-neu-1](https://blog.dinotronic.ch/hs-fs/hubfs/Uebersicht-Flows-neu-1.webp?width=900&height=533&name=Uebersicht-Flows-neu-1.webp)

Power Automate – Übersicht Flows-Vorlagen

![Flow-anpassen-neu](https://blog.dinotronic.ch/hs-fs/hubfs/Flow-anpassen-neu.webp?width=900&height=605&name=Flow-anpassen-neu.webp)

Einzelne Power Automate Flows lassen sich individuell anpassen

## Ist wirklich alles so einfach? Ein Selbstversuch.

Weil sich die Dinotronic vornehmlich nicht der Entwicklung von Software verschrieben hat, haben wir Power Apps und Power Automate lange Zeit wenig Beachtung geschenkt. Jedoch können auch wir nicht leugnen, dass die Möglichkeiten, die eine Low Coding Plattform bietet, sehr vielversprechend sind. Deshalb haben wir uns zum Ziel gesetzt, einige Applikationen für den Eigengebrauch zu entwickeln und damit Erfahrungen zu sammeln, um später auch unsere Kunden in diesem Bereich kompetent beraten zu können. Da wir als IT-Firma unsere Spesen Erfassung im Jahr 2020 noch nicht digitalisiert hatten, nahmen wir uns vor eine Spesen-App zu programmieren. Über die Mobile App können Speseneinträge für den laufenden Monat erfasst werden, jeweils Ende Monat werden die einzelnen Speseneinträge zusammengefasst und als Spesenantrag an den Vorgesetzten weitergeleitet. Der gesamte Genehmigungsprozess und die damit einhergehenden Änderungen an den Einträgen wurden mit Power Automate realisiert.

Hinsichtlich unseres Selbstversuches waren wir zu Beginn der Entwicklungsphase sehr euphorisch und machten gute Fortschritte. Je umfangreicher die App wurde, umso mehr Fehler schlichen sich ein. Zur einfachen Fehlerbehebung offerieren sowohl Power Automate wie auch Power Apps eine Fehleranalyse Funktion, um den Anwender schnell auf potenzielle Probleme hinzuweisen. Leider ist die Aussagekraft dieser Fehlerbehebungstipps zum aktuellen Zeitpunkt noch nicht ganz ausgereift und es bedarf in vielen Fällen einem “Try and Error”-Vorgehen, um der Ursache der Probleme auf den Grund zu gehen. Wir gingen anfänglich davon aus, dass wir die Applikation zu zweit an einem Nachmittag innert 4-5 Stunden fertigstellen können, was bei der Komplexität der Anforderungen aus unserer Sicht durchaus realistisch war. Jedoch haben wir den Aufwand unterschätzt, den es erfordert, um uns zunächst mit den Tools vertraut zu machen. Aber auch die Behebung von Fehlern deren Quelle nicht immer eindeutig zugeordnet werden konnte, hat uns mehr Ressourcen gekostet, als vermutet. Nach mehreren Anläufen konnten wir dennoch innert nützlicher Frist eine funktionierende Spesen-App bereitstellen, die unsere Mitarbeitenden bei der Erfassung der Berufs-Auslagen unterstützt.

### Unser Fazit:

Microsoft Power Apps und Microsoft Power Automate sind mächtige Werkzeuge der App-Entwicklung und besitzen enorm viel Potential, um Endanwender zu befähigen, eine eigene Applikation zu erstellen oder Prozesse zu digitalisieren. Die Einstiegshürde für Nicht-Entwickler ist in der aktuellen Ausführung ziemlich hoch, für manche vielleicht noch zu hoch. Es bedarf viel Aufwand und Disziplin, um sich in der Welt der Microsoft Power Platform zurecht zu finden und nicht jeder hat den Durchhaltewillen oder die Zeit, diesen Weg zu beschreiten. Die Tools werden jedoch kontinuierlich weiterentwickelt und wir sind zuversichtlich, dass es für Endanwender in den kommenden Jahren einfacher wird, eigene Apps zu entwickeln. Vielleicht unterschätzen wir aber auch die Fähigkeit potenzieller Nutzer.

Wir ermutigen alle, die Interesse daran haben, eine eigene App zu entwickeln, die ersten Gehversuche mit Power Apps zu machen. Benötigen Sie weitere Informationen oder Unterstützung von Experten? [Sprechen Sie mit uns darüber](https://www.dinotronic.ch/kontakt/), wir helfen Ihnen gerne weiter.

![avatar](https://25917640.fs1.hubspotusercontent-eu1.net/hub/25917640/hubfs/01_Visual%20Content/01_Mitarbeiter-Fotos/Michael%20Freuler%20klein.png?width=290&name=Michael%20Freuler%20klein.png)

[**Michael Freuler**](https://blog.dinotronic.ch/author/michael-freuler) Head of Solution Consulting and Marketing

## Abonnieren Sie unsere monatlichen Newsletter

Unsere Newsletter geben interessante Einblicke in neue Trends.

[JETZT ABONNIEREN](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/click?encryptedPayload=AVxigLLDeUTinalaEHzhVFxSN665Vfv1BEMieCwfnJ%2FoMLk180OmTmqwgnNUaRnnE5XvGr%2FKh%2B8GleaaDL6PtqWJ1mlQ3%2FN0QZxUc6NB1E65Bb3eHAEVA%2FakfnS05RWKr%2F2OfQfq6mpSt1w4meQKMIak214EuIcEnBlGAKsbhyrHJozdNOovxWvNoZ3m2KNkncE%3D&portalId=25917640&webInteractiveContentId=114201044682&webInteractiveId=151726273754&containerType=EMBEDDED&pageUrl=https%3A%2F%2Fblog.dinotronic.ch%2Fblog%2Fdigital-workplace%2Fmicrosoft-power-apps-eigene-app-entwickeln-in-nur-4-stunden&pageTitle=Microsoft+Power+Apps+%E2%80%93+eigene+App+entwickeln+in+nur+4+Stunden%3F&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F132.0.0.0+Safari%2F537.36&hutk=&hssc=&hstc=&pageId=116867826647)

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

[Michael Freuler06.02.2023, 20:30:009 min read\\
\\
**Digital Workplace Trends 2023** \\
\\
Digital Workplace, ein Begriff, mit dem sicher jedes Unternehmen in den letzten Jahren in Kontakt gekommen ist – egal ob aus ...\\
\\
Mehr lesen](https://blog.dinotronic.ch/blog/digital-workplace/digital-workplace-trends-2023) [Michael Freuler21.01.2025, 23:34:0912 min read\\
\\
**Künstliche Intelligenz mit Fokus auf Kunst, Kultur und Forschung** \\
\\
KI-Künstliche Intelligenz in Stiftungen mit Fokus auf Kunst, Kultur und Forschung: Effizienz trifft Inspiration\\
\\
Mehr lesen](https://blog.dinotronic.ch/k%C3%BCnstliche-intelligenz-mit-fokus-auf-kunst-kultur-und-forschung) [Michael Freuler22.06.2022, 20:30:004 min read\\
\\
**Cyber Security in Schweizer KMU – Und was Sie beachten müssen** \\
\\
Welche Sicherheitsmassnahmen ergreifen Sie zu Hause, wenn Sie in den Urlaub fahren? Vermutlich alle Türen und Fenster ...\\
\\
Mehr lesen](https://blog.dinotronic.ch/blog/cyber-security/cyber-security-in-schweizer-kmu-und-was-sie-beachten-muessen)

Twitter Widget Iframe

Chat Widget