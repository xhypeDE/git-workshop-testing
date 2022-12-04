# Liebe Workshop Teilnehmer:innen,

für unseren Workshop am 02. Dezember mit dem Thema „Git“ bitten wir euch Git schon zu installieren und folgenden Link während des Workshops bereitzuhaben: https://github.com/xhypeDE/git-workshop.git

Die meisten von euch sollten Git schon haben. Wie genau ihr aber prüft, ob Git installiert ist und wie ihr Git installiert, falls ihr Git noch nicht installiert habt, erklären wir hier:

## Windows:
- Über die Tastenkombination Win+R öffnet sich ein Fenster, in dem ihr das Programm „Eingabeaufforderung“ starten könnt
- Anschließend gebt ihr `cmd.exe` ein und bestätigt das mit Enter
- Es öffnet sich jetzt das Fenster für die Eingabeaufforderung
- Um jetzt zu prüfen, ob Git installiert ist, kann man einfach eingeben `git --version`.
- Falls hier jetzt eine Rückmeldung wie `git version 2.33.0.windows.2` oder ähnlich, angezeigt wird, ist Git schon installiert und man braucht hier nichts Weiteres vorzunehmen.
- Falls jedoch der Befehl nicht gefunden wird, muss Git noch installiert werden
- Über folgenden Link kann der Git Installer für Windows heruntergeladen werden: https://git-scm.com/download/win hier den „Standalone Installer“ herunterladen und ausführen
- Nach Abschluss der Installation kann man wieder durch das Eingeben von `git --version` in der Eingabeaufforderung prüfen, ob Git erfolgreich installiert wurde.


## Mac:
- Im Applikationsordner muss das Programm „Terminal“ ausgeführt werden.
- Beim Ausführen öffnet sich eine Eingabeaufforderung, hier kann man jetzt durch die Eingabe des Befehls `git --version` prüfen, ob Git schon installiert ist.
- Falls hier die Rückmeldung ausgibt `git version 2.33.0` oder ähnliches ist Git schon installiert und es muss nicht weiteres vorgenommen werden
- Falls jedoch der Befehl nicht gefunden wird, ist Git noch nicht installiert
- Um Git beziehen zu können, muss erst Homebrew installiert werden. Dieses Programm ermöglicht die Installation von anderen Tools und Programmen über das Terminal
- Hierfür muss folgender Befehl ausgeführt werden:
     `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

- Nach der Installation von Homebrew kann man durch Ausführen des Befehls:
`brew install git` Git installieren.
- Nach Abschluss der Installation kann man wieder durch das Eingeben von `git --version` im Terminal prüfen, ob Git erfolgreich installiert wurde.

Bei Problemen könnt ihr uns gerne über E-Mail oder Webex kontaktieren.

Mit freundlichen Grüßen
Christian Tolu & Marwand Ayubi
