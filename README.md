<h3> M-Fiszki <a href="https://mfiszki.pl/" target="_blank">mfiszki.pl</a></h3>
</br>


# Krótko o stronie 

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


# Krótko o technologiach

Backend strony jest napisany w Django, a wszytkie skryptu np do przetwarzania tego co zwrócił OCR są napisane w Python.

Frontend wykorzystuje BootStrap i jquery.

Udało mi się połączyć technologie ajax z Django. Dzięki czemu aktualizuje dane zestawów bez odświeżania strony.

Również sam wydelepowałem aplikację django na server Linux.

</br>



<h2>Przykład OCR | Zdjęcie wysłąne do OCR</h2>

</br>

![JUlkaTest](https://github.com/user-attachments/assets/80548ad3-449d-43cf-acda-899f521d65fb)

</br>

<h2>Wynik</h2>

</br>

![Wynik OCR](https://github.com/user-attachments/assets/7f1c5a11-d029-4d8e-96ff-c997c1770170)


</br>
</br>


<h2>Przykład .txt | Plik wysłany do aplikacji</h2>
</br>
Cat - Kot

Dog - Pies

Horse - Koń



</br>
<h2>Wynik</h2>
</br>

![Wynik txt](https://github.com/user-attachments/assets/fc9f8100-98f1-4db2-b083-eedeac5ba704)






