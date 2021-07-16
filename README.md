# MaiaChessUCI

UCI compatible interface to Maia Chess (https://github.com/CSSLab/maia-chess)

## Instructions

NOTE: Will add better instructions later.

### Setting up

* Create a folder for Maia (`Maia`)
* Download all maia networks (https://github.com/CSSLab/maia-chess/tree/master/maia_weights). To easily download a folder from Github can use third party tools (e.g., https://download-directory.github.io). Note that downloading manually from Github webpage may cause issues because the Maia UCI expects zipped files with names similar to `maia-1100.pb.gz`, but Github sometimes automatically unzips before downloading resulting in different filenames.
* Put all networks in a folder called `maia_weights`, inside the `Maia` folder.
* Install lc0 (instructions in https://lczero.org) and copy executable file `lc0` to `Maia` folder.

### Compiling Maia UCI

* Install python-chess (https://github.com/niklasf/python-chess) and pyinstaller (https://www.pyinstaller.org)
* Download the `MaiaChessUCI.py` file in the `Maia` folder.

Compile the Maia UCI, for example with the command
```
pyinstaller MaiaChessUCI.py --onefile --clean --distpath ./
```

### Using as a UCI engine

* The compiled executable file `MaiaChessUCI` can be used as a UCI engine, hopefully with any chess GUI. The `lc0` and `maia_weights` have to be in the same folder.
* When using the engine for analysis, choose to show 9 lines to see the prediction of the 9 Maia models (for each rating range). The evaluation is the model rating range.

#### Using on ChessX

* When configuring the engine in ChessX, need to set the `Directory` option to the `Maia` folder, and also check the option `Send history`


# References

* https://github.com/CSSLab/maia-chess
* https://github.com/LeelaChessZero/lc0
* https://github.com/niklasf/python-chess
* https://github.com/Isarhamster/chessx
* https://github.com/healeycodes/andoma
* https://github.com/feldi/py-goratschin

