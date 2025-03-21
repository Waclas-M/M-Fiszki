# M-Fiszki
<h3><a href="https://mfiszki.pl/" target="_blank">mfiszki.pl</a></h3>
</br>


## Krótko o stronie 

Na stronie można tworzyć zestawy pytań i odpowiedzi które poźniej wykorzystawne są w grach pomagających się uczyć.

Tworzenie zestawu:
- Za pomocą zdjęć
- Za pomocą pliku .txt
- Za pomocą dodawania manualnie pytań i odpowiedzi

Po przesłaniu zdjęcia OCR czyta plik a następnie skrypt dzieli przeczytany tekst na pytania i odpowiedzi.

Po przesłaniu pliku TXT skrypt czyta plik i dzieli słowa na pytania i odpowiedzi.

OCR --> googlevision API


Gry:
- Fiszki
- Wpisywanie ręczne

Wpisywanie ręczne polega na wpisaniu prawidłowej odpowiedzi w pole i uzbierania jak największej liczby punktów.

Fiszki są grą w której sam musisz sprawdzić czy odpowiedź którą podałeś jest prawidłowa.


</br>
</br>


## Krótko o technologiach

Backend strony jest napisany w Django, a wszytkie skryptu np do przetwarzania tego co zwrócił OCR są napisane w Python.

Frontend wykorzystuje BootStrap i jquery.

W pewnien sposób nawet udało mi się połączyć ajax z Django. Dzięki czemu aktualizuje dane zestawów bez odświeżania strony.

Również sam wydelepowałem aplikację django na server Linux.
