# Observer Pattern

## Description
The Observer pattern lets objects know when other objects change. It's based on a one-to-many relationship, where one object (the subject) notifies many other objects (the observers) of its changes, and the observers respond.

## Realization
The classes in the code let publishers tell subscribers about updates, like stock prices or exchange rates. Subscribers can choose whether to get notifications, and when the publisher updates the information, all subscribers get the update.

## Tests
Tests show that the subscription system is working. They show that subscribers are registered, on the list, removed from the list, and no longer on the list. They also show that subscribers get notifications from publishers when stock prices or exchange rates change.
