
# Der Start-Befehl in der Batch-Programmierung

## Syntax

Der start-Befehl wird gemäß der folgenden Syntax ausgeführt:

	start "Titel" [/d Arbeitsverzeichnis] [Optionen]  "Befehl" [Argumente]

## Häufig genutzte Optionen

| Option | Bedeutung |
|---|---|
| `/B` | Erzeugt kein neues Fenster (Anwendung wird im selben Fenster gestartet). |
| `/W` oder `/WAIT` | Wartet auf das Ende der Anwendung, bevor forgefahren wird. |

## Beispiele

Einen Tomcat-Server starten:

	start "tomcat-server" ^
		/D D:\run\web\server\tomcat ^
		D:\app\apache\tomcat\v9.0.37\bin\startup.bat

Einen Apache-HTTPD-Server starten:

	start "apache-httpd-server"  ^
		/D D:\run\web\server\httpd  ^
		D:\app\apache\httpd\v2.4.41\bin\httpd.exe

## Referenz

[Der Start-Befehl auf ss64.com](https://ss64.com/nt/start.html){target="_blank"}

