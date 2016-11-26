import System.Environment (getArgs)
import System.IO
import qualified TopCoder as TC
import qualified SwappingParentheses (countValid)

getVars :: TC.Parser (String, [Int])
getVars = do s <- TC.spaces >> TC.parseString ; TC.spaces >> TC.next
             op <- TC.spaces >> (TC.parseList TC.parseInt)
             return (s, op)

main = do
    args <- getArgs
    hIn <- openFile (head args) ReadMode
    contents <- hGetContents hIn
    case (TC.parse getVars "parse variables" contents) of
        Left err -> print err
        Right (s, op) -> do
            hOut <- openFile (head (tail args)) WriteMode
            hPutStr hOut $ show $ SwappingParentheses.countValid s op
            hClose hOut
    hClose hIn
