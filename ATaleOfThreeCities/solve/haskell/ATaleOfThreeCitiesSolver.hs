import System.Environment (getArgs)
import System.IO
import qualified TopCoder as TC
import qualified ATaleOfThreeCities (connect)

getVars :: TC.Parser ([Int], [Int], [Int], [Int], [Int], [Int])
getVars = do ax <- TC.spaces >> (TC.parseList TC.parseInt) ; TC.spaces >> TC.next
             ay <- TC.spaces >> (TC.parseList TC.parseInt) ; TC.spaces >> TC.next
             bx <- TC.spaces >> (TC.parseList TC.parseInt) ; TC.spaces >> TC.next
             by <- TC.spaces >> (TC.parseList TC.parseInt) ; TC.spaces >> TC.next
             cx <- TC.spaces >> (TC.parseList TC.parseInt) ; TC.spaces >> TC.next
             cy <- TC.spaces >> (TC.parseList TC.parseInt)
             return (ax, ay, bx, by, cx, cy)

main = do
    args <- getArgs
    hIn <- openFile (head args) ReadMode
    contents <- hGetContents hIn
    case (TC.parse getVars "parse variables" contents) of
        Left err -> print err
        Right (ax, ay, bx, by, cx, cy) -> do
            hOut <- openFile (head (tail args)) WriteMode
            hPutStr hOut $ show $ ATaleOfThreeCities.connect ax ay bx by cx cy
            hClose hOut
    hClose hIn
