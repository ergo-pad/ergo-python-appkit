# ergo-python-appkit
This is a wrapper around Ergo's appkit, which is based on scala/java. Jpype is used to map to the JVM and the jar running within. That means that Java needs to be installed for this package to work.

## Installation
Installation can be done through pip. Currently the package is not available yet on PyPi so you need to refer directly to the github.
```
pip install git+https://github.com/ergo-pad/ergo-python-appkit.git
```

## Usage
The ergo appkit can be accessed by importing java classes AFTER importing the appkit, like this:
```python
import ergo_python_appkit.appkit
from org.ergoplatform.appkit import Address

myErgoAddress = Address.create("9gF2wmTWcEX2EZu5QY3dJwURep1HWsXjUZdVavVWESun4Sp8BYj")
#will print the ergotree belonging to the address
print(myErgoAddress.toErgoContract().getErgoTree())
```

There are also convenience methods created to allow for easier use from Python for appkit functionality that is used often.

An example of a simple intra wallet transaction send from the nodes wallet:
```python
from ergo_python_appkit.appkit import ErgoAppKit
from org.ergoplatform.appkit import Address

appKit = ErgoAppKit("http://myergonode:9053","mainnet","http://api.ergoplatform.org","nodeapikey")
myAddress = "9gF2wmTWcEX2EZu5QY3dJwURep1HWsXjUZdVavVWESun4Sp8BYj"

#collect boxes to spend 1 erg
inputs = appKit.boxesToSpend(address=myAddress,nergToSpend=int(1e9))

#Define output box
outputBox = appKit.buildOutBox(
                value=int(1e9),
                tokens=None,
                registers=None,
                contract=appKit.contractFromAddress(myAddress)
            )

#Build the unsigned transaction
unsignedTx = appKit.buildUnsignedTransaction(
                inputs=inputs,
                outputs=[outputBox],
                fee=int(1e6),
                sendChangeTo=Address.create(myAddress).getErgoAddress()
            )

#Sign the transaction with the node
signedTx = appKit.signTransactionWithNode(unsignedTx)

#Send the transaction
appKit.sendTransaction(signedTx)