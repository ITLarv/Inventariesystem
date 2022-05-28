# Stuff that is left to do

## New stuff (buttons for extra furniture)
### -1
* Should also add on the total number by 1

### Boka
* Decrease on the overall number
* Stop if there is no more
* Need to display how many there are left as well

## New stuff (show where gods should be)
* Use status for saying when just in system and not registered
* Registered should update status
* Autocompleaters should display where the gods should be
* Register should be able to create a new gods aswell

## More
* RED text for error messages in all guis


## Auto Completers
* Update autocompleter for the lokaler (This can change mid session)

## Relevant messages
* When trying to borrow palldragare that is already borrowed, it should not say successfull.
* When returning palldragare that does not exists, should not say successfull.
* When trying to add more extra furniture when not initialized
* When trying to borrow more extra furniture then allowed
* When trying to return extra furniture when already empty

## Stuff to make faster
* claim and return
* Search for companies and gods

## Mid priority
### Would be good if done before fair
* Colors for furniture
* Generealize extrafurniture GUI, this is now written specifically for only "ståbord" and "barstol"
* Change lineEdits to comboboxes to be able to use [suggestions before typing.](https://stackoverflow.com/questions/67891112/how-to-display-all-suggestions-before-typing-anything-in-pyqt5-tablewidget)
* GUI for lokal init
* Auto scaling of window [here](https://stackoverflow.com/questions/41331201/pyqt-5-and-4k-screen)
Problem with autoscaling is for the version of pyqt5? It gives a error that is mentioned in the comments of first answer

## Low priority
### Fix later stuff
* Make the code readable - some code splitting and rewriting
* Make the code run faster by removing stuff in the pyqt5 file (Starts faster)
* Make it possible to one-click the extra furniture part, so like adding to the list and then confirm with one button.
* right way of error handeling. All commands should return -1 if there was a error. It should also have specifik returns depending on the error. -1 is the general error. This should also include lexikon for all the error codes - in the docs. Or rais error idk
* Set new names on stuff, and use namingconventions right. All functions and variables should be names in the same way.
* Write docs for the code
* Remove all code that had with the update button to do, if any left
* Generalize the get all functions
* Storage should be generalized
* Initial display screen should be same layout as active display (search companies and gods)
* Palldragare is called storage right now? Something should be changed (buttons.py)
