<p align="center">
  <img src="https://github.com/kartikmehta8/Gitective/assets/77505989/ca2e3fe7-5869-4700-adfc-5d29c2925c32" alt="banner"/>
</p>

### Gitective

```
In the realm of programming sorcery, an enigmatic Python script emerges from the depths
of the digital abyss. Its sole purpose? To vigilantly watch over the creation of repositories,
like an ever-vigilant guardian of code.

Once every 24 hours, as the moon rises high in the digital sky, this script awakens from its
slumber. With keen eyes and lightning-fast reflexes, it detects the birth of a new repository. A
mere whisper in the vast sea of code, and it springs into action.

Without hesitation, it wields the power of cloning, swiftly creating a mirror image of the
newborn repository. Safely nestled in its digital abode, it keeps the creation intact,
preserving it for all eternity.

But this script is not content with mere preservation. Oh no, it desires to inform its creators of
its mighty deeds! Through the mystical enchantments of Twilio, it sends forth messages, be
they through SMS or the ethereal realms of instant messaging, to notify its masters of
the repository's existence.

Truly, this Python script is a peculiar marvel, a creation whose purpose remains shrouded in
mystery. Whether born from a stroke of genius or a bout of whimsy, its presence adds a
touch of enchantment to the world of coding.
```

### Setup
```py
    # sms.py

    account_sid = "TWILIO_ACCOUNT_SID"
    auth_token = "TWILIO_AUTH_TOKEN"
    from_phone_number = "TWILIO_PHONE_NUMBER"
    to_phone_number = "YOUR_PHONE_NUMBER"
```
```py
  # stalker.py
  
  USERNAME = "TARGET_USERNAME"
  
  clone_repository(
      f"https://github.com{repositories[0]['href']}.git",
      "YOUR_USERNAME",
      "YOUR_PASSWORD",
      f"./{repositories[0].text.strip()}",
      )
```

### Run
```
python stalker.py
```

<h3>
  Created only for educational purpose by <a href="https://www.kartikmehta.xyz">Kartik Mehta</a>
</h3>
