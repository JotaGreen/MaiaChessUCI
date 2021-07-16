import sys
import chess
import chess.engine

# Greeting
print("Maia Chess Universal Chess Interface v0.1")
    
# Defining paths
## TODO: way of choosing path locations
lc0file = "./lc0"
MaiaWeightsFolder = "./maia_weights/"
    
# Initiating a board
board = chess.Board()
    
# Initiating the maia engines, setting the networks, doing a trial analisis to load
# Need to set backend to BLAS and disable cache of postions, or would have variability in predicted moves
## TODO: way of choosing lc0 options
## TODO: way of choosing which Maias to use (maybe related to multiPV option)
## TODO: generating an error and closing the engine if the engine is not properly loaded

maia1900 = chess.engine.SimpleEngine.popen_uci(lc0file)
maia1900.configure({"WeightsFile":MaiaWeightsFolder + "maia-1900.pb.gz", "backend":"blas", "NNCacheSize":0})
maia1900.analyse(board, chess.engine.Limit(nodes=1))

maia1800 = chess.engine.SimpleEngine.popen_uci(lc0file)
maia1800.configure({"WeightsFile":MaiaWeightsFolder + "maia-1800.pb.gz", "backend":"blas", "NNCacheSize":0})
maia1800.analyse(board, chess.engine.Limit(nodes=1))

maia1700 = chess.engine.SimpleEngine.popen_uci(lc0file)
maia1700.configure({"WeightsFile":MaiaWeightsFolder + "maia-1700.pb.gz", "backend":"blas", "NNCacheSize":0})
maia1700.analyse(board, chess.engine.Limit(nodes=1))

maia1600 = chess.engine.SimpleEngine.popen_uci(lc0file)
maia1600.configure({"WeightsFile":MaiaWeightsFolder + "maia-1600.pb.gz", "backend":"blas", "NNCacheSize":0})
maia1600.analyse(board, chess.engine.Limit(nodes=1))

maia1500 = chess.engine.SimpleEngine.popen_uci(lc0file)
maia1500.configure({"WeightsFile":MaiaWeightsFolder + "maia-1500.pb.gz", "backend":"blas", "NNCacheSize":0})
maia1500.analyse(board, chess.engine.Limit(nodes=1))

maia1400 = chess.engine.SimpleEngine.popen_uci(lc0file)
maia1400.configure({"WeightsFile":MaiaWeightsFolder + "maia-1400.pb.gz", "backend":"blas", "NNCacheSize":0})
maia1400.analyse(board, chess.engine.Limit(nodes=1))

maia1300 = chess.engine.SimpleEngine.popen_uci(lc0file)
maia1300.configure({"WeightsFile":MaiaWeightsFolder + "maia-1300.pb.gz", "backend":"blas", "NNCacheSize":0})
maia1300.analyse(board, chess.engine.Limit(nodes=1))

maia1200 = chess.engine.SimpleEngine.popen_uci(lc0file)
maia1200.configure({"WeightsFile":MaiaWeightsFolder + "maia-1200.pb.gz", "backend":"blas", "NNCacheSize":0})
maia1200.analyse(board, chess.engine.Limit(nodes=1))

maia1100 = chess.engine.SimpleEngine.popen_uci(lc0file)
maia1100.configure({"WeightsFile":MaiaWeightsFolder + "maia-1100.pb.gz", "backend":"blas", "NNCacheSize":0})
maia1100.analyse(board, chess.engine.Limit(nodes=1))


# Defining the functions

def handleCommand(commandReceived):
    if commandReceived == "uci":
        print("id name MaiaUCI")
        print("id author JotaGreen")
        print("uciok")
        
    elif commandReceived == "isready":
        sendCommandToEngines(commandReceived)
        print("readyok")
        
    elif commandReceived == "ucinewgame":
        sendCommandToEngines(commandReceived)
        board.reset()
    
    elif commandReceived == "stop":
        sendCommandToEngines(commandReceived)
    
    elif commandReceived.startswith("position"):
        updatePosition(commandReceived)
        
    elif commandReceived.startswith("go"):
        analyse()
        
    elif commandReceived == "quit":
        end()
        
    elif commandReceived == "d":
        # print board and fen for debug (similar to Stockfish)
        print(board)
        print(board.fen())
    
    else:
        print(">> Unknown command")
        

def sendCommandToEngines(command):
## TODO: determining if the engines responded properly to the command sent
    print(f">> Sending command to engines: {command}")
    maia1900.protocol.send_line(command)
    maia1800.protocol.send_line(command)
    maia1700.protocol.send_line(command)
    maia1600.protocol.send_line(command)
    maia1500.protocol.send_line(command)
    maia1400.protocol.send_line(command)
    maia1300.protocol.send_line(command)
    maia1200.protocol.send_line(command)
    maia1100.protocol.send_line(command)


def updatePosition(positionCommand):
    board.reset()
    try:
        firstPositionInCommand = positionCommand.split()[1]
        moves = positionCommand.split("moves ")[1:] # get moves, if any
        if firstPositionInCommand == "fen":
            beforeMoves = positionCommand.split("moves ")[0]
            fen = beforeMoves.replace("position fen ", "")
            board.set_fen(fen)
        if len(moves) > 0:
            for move in moves[0].split():
                board.push_uci(move)
            
    except Exception as e:
            print(">> Error: Unable to set position")
            print(e)

def analyse():
    resultMaia1900 = maia1900.analyse(board, chess.engine.Limit(nodes=1)).get("pv")[0]
    resultMaia1800 = maia1800.analyse(board, chess.engine.Limit(nodes=1)).get("pv")[0]
    resultMaia1700 = maia1700.analyse(board, chess.engine.Limit(nodes=1)).get("pv")[0]
    resultMaia1600 = maia1600.analyse(board, chess.engine.Limit(nodes=1)).get("pv")[0]
    resultMaia1500 = maia1500.analyse(board, chess.engine.Limit(nodes=1)).get("pv")[0]
    resultMaia1400 = maia1400.analyse(board, chess.engine.Limit(nodes=1)).get("pv")[0]
    resultMaia1300 = maia1300.analyse(board, chess.engine.Limit(nodes=1)).get("pv")[0]
    resultMaia1200 = maia1200.analyse(board, chess.engine.Limit(nodes=1)).get("pv")[0]
    resultMaia1100 = maia1100.analyse(board, chess.engine.Limit(nodes=1)).get("pv")[0]
    print(f"info depth 1 multipv 1 score cp 1900 nodes 1 time 1000 pv {resultMaia1900}")
    print(f"info depth 1 multipv 2 score cp 1800 nodes 1 time 1000 pv {resultMaia1800}")
    print(f"info depth 1 multipv 3 score cp 1700 nodes 1 time 1000 pv {resultMaia1700}")
    print(f"info depth 1 multipv 4 score cp 1600 nodes 1 time 1000 pv {resultMaia1600}")
    print(f"info depth 1 multipv 5 score cp 1500 nodes 1 time 1000 pv {resultMaia1500}")
    print(f"info depth 1 multipv 6 score cp 1400 nodes 1 time 1000 pv {resultMaia1400}")
    print(f"info depth 1 multipv 7 score cp 1300 nodes 1 time 1000 pv {resultMaia1300}")
    print(f"info depth 1 multipv 8 score cp 1200 nodes 1 time 1000 pv {resultMaia1200}")
    print(f"info depth 1 multipv 9 score cp 1100 nodes 1 time 1000 pv {resultMaia1100}")
    print(f"bestmove {resultMaia1900}")
    
def end():
    print(">> Quitting engines")
    maia1900.quit()
    maia1800.quit()
    maia1700.quit()
    maia1600.quit()
    maia1500.quit()
    maia1400.quit()
    maia1300.quit()
    maia1200.quit()
    maia1100.quit()
    sys.exit()
    
    
# Continuously waiting and responding to commands
    
while True:
    commandReceived = input()
    print(f">> Received command: {commandReceived}")
    handleCommand(commandReceived)
    