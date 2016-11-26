import System.Environment (getArgs)
import System.IO
import qualified TopCoder as TC
import qualified ShopPositions (maxProfit)

getVars :: TC.Parser (Int, Int, [Int])
getVars = do n <- TC.spaces >> TC.parseInt ; TC.spaces >> TC.next
             m <- TC.spaces >> TC.parseInt ; TC.spaces >> TC.next
             c <- TC.spaces >> (TC.parseList TC.parseInt)
             return (n, m, c)

main = do
    args <- getArgs
    hIn <- openFile (head args) ReadMode
    contents <- hGetContents hIn
    case (TC.parse getVars "parse variables" contents) of
        Left err -> print err
        Right (n, m, c) -> do
            hOut <- openFile (head (tail args)) WriteMode
            hPutStr hOut $ show $ ShopPositions.maxProfit n m c
            hClose hOut
    hClose hIn
