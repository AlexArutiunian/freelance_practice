# 1st job

In this work, it was necessary to collect data on 478 artscholls.
I automate the collection of TIN(ИНН) and geolocation.

I found [the ad](https://vk.com/moneymipt?w=wall-57876679_8598) in this group ['Клуб любителей денег'](https://vk.com/moneymipt)

### Geolacation
For parsing of geolacation in google maps I use selenium and web-driver chrome.
The instruction about this is on [the link](https://www.geeksforgeeks.org/how-to-scrape-data-from-google-maps-using-python/)

### TIN(ИНН)

This decision is based on the [discussion](https://stackoverflow.com/questions/22623798/google-search-with-python-requests-library) on the stakoverflow.

### Something about browsers...

Yandex is more closed to parse the request in comparison with Google,
so I used exactly google.

Also in some cases there was google recaptcha (after 100 requests).
I won it with vpn and changing wi-fi network. 

